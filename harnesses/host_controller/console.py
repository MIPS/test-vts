#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import cmd
import sys

from vts.harnesses.host_controller.tfc import request
from vts.harnesses.host_controller.build import build_flasher

# The default Partner Android Build (PAB) public account.
# To obtain access permission, please reach out to Android partner engineering
# department of Google LLC.
_DEFAULT_ACCOUNT_ID = '543365459'


class ConsoleArgumentError(Exception):
    """Raised when the console fails to parse commands."""
    pass


class ConsoleArgumentParser(argparse.ArgumentParser):
    """The argument parser for a console command."""

    def __init__(self, command_name, description):
        """Initializes the ArgumentParser without --help option.

        Args:
            command_name: A string, the first argument of the command.
            description: The help message about the command.
        """
        super(ConsoleArgumentParser, self).__init__(prog=command_name,
                                                    description=description,
                                                    add_help=False)

    def ParseLine(self, line):
        """Parses a command line.

        Args:
            line: A string, the command line.

        Returns:
            An argparse.Namespace object.
        """
        return self.parse_args(line.split())

    # @Override
    def error(self, message):
        """Raises an exception when failing to parse the command.

        Args:
            message: The error message.

        Raises:
            ConsoleArgumentError.
        """
        raise ConsoleArgumentError(message)


class Console(cmd.Cmd):
    """The console for host controllers.

    Attributes:
        _pab_client: The PartnerAndroidBuildClient used to download artifacts
        _tfc_client: The TfcClient that the host controllers connect to.
        _hosts: A list of HostController objects.
        _in_file: The input file object.
        _out_file: The output file object.
        prompt: The prompt string at the beginning of each command line.
        _fetch_parser: The parser for fetch command
        _flash_parser: The parser for flash command
        _lease_parser: The parser for lease command.
        _list_parser: The parser for list command.
        _request_parser: The parser for request command.
    """

    def __init__(self, tfc, pab, host_controllers,
                 in_file=sys.stdin, out_file=sys.stdout):
        """Initializes the attributes and the parsers."""
        # cmd.Cmd is old-style class.
        cmd.Cmd.__init__(self, stdin=in_file, stdout=out_file)
        self._pab_client = pab
        self._tfc_client = tfc
        self._hosts = host_controllers
        self._in_file = in_file
        self._out_file = out_file
        self.prompt = "> "

        self._InitFetchParser()
        self._InitFlashParser()
        self._InitLeaseParser()
        self._InitListParser()
        self._InitRequestParser()

    def _InitRequestParser(self):
        """Initializes the parser for request command."""
        self._request_parser = ConsoleArgumentParser(
                "request", "Send TFC a request to execute a command.")
        self._request_parser.add_argument(
                "--cluster", required=True,
                help="The cluster to which the request is submitted.")
        self._request_parser.add_argument(
                "--run-target", required=True,
                help="The target device to run the command.")
        self._request_parser.add_argument(
                "--user", required=True,
                help="The name of the user submitting the request.")
        self._request_parser.add_argument(
                "command", metavar="COMMAND", nargs="+",
                help='The command to be executed. If the command contains '
                     'arguments starting with "-", place the command after '
                     '"--" at end of line.')

    def do_request(self, line):
        """Sends TFC a request to execute a command."""
        args = self._request_parser.ParseLine(line)
        req = request.Request(cluster=args.cluster,
                              command_line=" ".join(args.command),
                              run_target=args.run_target,
                              user=args.user)
        self._tfc_client.NewRequest(req)

    def help_request(self):
        """Prints help message for request command."""
        self._request_parser.print_help(self._out_file)

    def _InitListParser(self):
        """Initializes the parser for list command."""
        self._list_parser = ConsoleArgumentParser(
                "list", "Show information about the hosts.")
        self._list_parser.add_argument("--host", type=int,
                                       help="The index of the host.")
        self._list_parser.add_argument("type",
                                       choices=("hosts", "devices"),
                                       help="The type of the shown objects.")

    def _Print(self, string):
        """Prints a string and a new line character.

        Args:
            string: The string to be printed.
        """
        self._out_file.write(string + "\n")

    def do_list(self, line):
        """Shows information about the hosts."""
        args = self._list_parser.ParseLine(line)
        if args.host is None:
            hosts = enumerate(self._hosts)
        else:
            hosts = [(args.host, self._hosts[args.host])]
        if args.type == "hosts":
            self._PrintHosts(self._hosts)
        elif args.type == "devices":
            for ind, host in hosts:
                devices = host.ListDevices()
                self._Print("[%3d]  %s" % (ind, host.hostname))
                self._PrintDevices(devices)

    def help_list(self):
        """Prints help message for list command."""
        self._list_parser.print_help(self._out_file)

    def _PrintHosts(self, hosts):
        """Shows a list of host controllers.

        Args:
            hosts: A list of HostController objects.
        """
        self._Print("index  name")
        for ind, host in enumerate(hosts):
            self._Print("[%3d]  %s" % (ind, host.hostname))

    def _PrintDevices(self, devices):
        """Shows a list of devices.

        Args:
            devices: A list of DeviceInfo objects.
        """
        attr_names = ("device_serial", "state", "run_target", "build_id",
                      "sdk_version", "stub")
        self._PrintObjects(devices, attr_names)

    def _PrintObjects(self, objects, attr_names):
        """Shows objects as a table.

        Args:
            object: The objects to be shown, one object in a row.
            attr_names: The attributes to be shown, one attribute in a column.
        """
        width = [len(name) for name in attr_names]
        rows = [attr_names]
        for dev_info in objects:
            attrs = [_ToPrintString(getattr(dev_info, name, ""))
                     for name in attr_names]
            rows.append(attrs)
            for index, attr in enumerate(attrs):
                width[index] = max(width[index], len(attr))

        for row in rows:
            self._Print("  ".join(attr.ljust(width[index])
                                  for index, attr in enumerate(row)))

    def _InitLeaseParser(self):
        """Initializes the parser for lease command."""
        self._lease_parser = ConsoleArgumentParser(
                "lease", "Make a host lease command tasks from TFC.")
        self._lease_parser.add_argument("--host", type=int,
                                        help="The index of the host.")

    def do_lease(self, line):
        """Makes a host lease command tasks from TFC."""
        args = self._lease_parser.ParseLine(line)
        if args.host is None:
            if len(self._hosts) > 1:
                raise ConsoleArgumentError("More than one hosts.")
            args.host = 0
        tasks = self._hosts[args.host].LeaseCommandTasks()
        self._PrintTasks(tasks)

    def help_lease(self):
        """Prints help message for lease command."""
        self._lease_parser.print_help(self._out_file)

    def _InitFetchParser(self):
        """Initializes the parser for fetch command."""
        self._fetch_parser = ConsoleArgumentParser("fetch",
                                                   "Fetch a build artifact.")
        self._fetch_parser.add_argument(
            '--method',
            default='GET',
            choices=('GET', 'POST'),
            help='Method for fetching')
        self._fetch_parser.add_argument(
            "--branch",
            required=True,
            help="Branch to grab the artifact from.")
        self._fetch_parser.add_argument(
            "--target",
            required=True,
            help="Target product to grab the artifact from.")
        # TODO(lejonathan): find a way to not specify this?
        self._fetch_parser.add_argument(
            "--account_id",
            default=_DEFAULT_ACCOUNT_ID,
            help="Partner Android Build account_id to use.")
        self._fetch_parser.add_argument(
            '--build_id',
            default='latest',
            help='Build ID to use default latest.')
        self._fetch_parser.add_argument(
            "--artifact_name",
            required=True,
            help=
            "Name of the artifact to be fetched. {id} replaced with build id.")
        self._fetch_parser.add_argument(
            "--userinfo_file",
            help=
            "Location of file containing email and password, if using POST.")

    def do_fetch(self, line):
        """Makes the host download a build artifact from PAB."""
        args = self._fetch_parser.ParseLine(line)
        # do we want this somewhere else? No harm in doing multiple times
        self._pab_client.Authenticate(args.userinfo_file)
        filename = self._pab_client.GetArtifact(
            account_id=args.account_id,
            branch=args.branch,
            target=args.target,
            artifact_name=args.artifact_name,
            build_id=args.build_id,
            method=args.method)
        print("Filename: %s" % filename)

    def help_fetch(self):
        """Prints help message for fetch command."""
        self._fetch_parser.print_help(self._out_file)

    def _InitFlashParser(self):
        """Initializes the parser for flash command."""
        self._flash_parser = ConsoleArgumentParser("flash",
                                                   "Flash images to a device.")
        self._flash_parser.add_argument(
            "--serial",
            default="",
            help="Serial number for device.")
        self._flash_parser.add_argument(
            "--build_dir",
            help="Directory containing build images to be flashed.")
        self._flash_parser.add_argument(
            "--gsi",
            help="Path to generic system image")
        self._flash_parser.add_argument(
            "--vbmeta",
            help="Path to vbmeta image")

    def do_flash(self, line):
        """Flash GSI or build images to a device connected with ADB."""
        args = self._flash_parser.ParseLine(line)
        if args.gsi is None and args.build_dir is None:
            self._flash_parser.error(
                "Nothing requested: specify --gsi or --build_dir")

        flasher = build_flasher.BuildFlasher(args.serial)
        if args.build_dir is not None:
            flasher.Flashall(args.build_dir)
        if args.gsi is not None:
            flasher.FlashGSI(args.gsi, args.vbmeta)

    def help_flash(self):
        """Prints help message for flash command."""
        self._flash_parser.print_help(self._out_file)

    def _PrintTasks(self, tasks):
        """Shows a list of command tasks.

        Args:
            devices: A list of DeviceInfo objects.
        """
        attr_names = ("request_id", "command_id", "task_id", "device_serials",
                      "command_line")
        self._PrintObjects(tasks, attr_names)

    def do_exit(self, line):
        """Terminates the console.

        Returns:
            True, which stops the cmdloop.
        """
        return True

    def help_exit(self):
        """Prints help message for exit command."""
        self._Print("Terminate the console.")

    # @Override
    def onecmd(self, line):
        """Executes a command and prints any exception."""
        try:
            return cmd.Cmd.onecmd(self, line)
        except Exception as e:
            self._Print("%s: %s" % (type(e).__name__, e))
            return None

    # @Override
    def emptyline(self):
        """Ignores empty lines."""
        pass

    # @Override
    def default(self, line):
        """Handles unrecognized commands.

        Returns:
            True if receives EOF; otherwise delegates to default handler.
        """
        if line == "EOF":
            return self.do_exit(line)
        return cmd.Cmd.default(self, line)


def _ToPrintString(obj):
    """Converts an object to printable string on console.

    Args:
        obj: The object to be printed.
    """
    if isinstance(obj, (list, tuple, set)):
        return ",".join(str(x) for x in obj)
    return str(obj)