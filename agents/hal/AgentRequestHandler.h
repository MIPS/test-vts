/*
 * Copyright 2016 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __VTS_AGENT_REQUEST_HANDLER_H__
#define __VTS_AGENT_REQUEST_HANDLER_H__

#include <string>
#include <vector>

#include <VtsDriverCommUtil.h>

#include "SocketClientToDriver.h"
#include "test/vts/proto/AndroidSystemControlMessage.pb.h"
#include "test/vts/proto/InterfaceSpecificationMessage.pb.h"


using namespace std;
using namespace google::protobuf;

namespace android {
namespace vts {

// Class which contains actual methods to handle the runner requests.
class AgentRequestHandler : public VtsDriverCommUtil {
 public:
  AgentRequestHandler(const char* spec_dir_path,
                      const char* hal_path32,
                      const char* hal_path64,
                      const char* shell_path32,
                      const char* shell_path64)
      : service_name_(),
        driver_client_(NULL),
        driver_hal_spec_dir_path_(spec_dir_path),
        driver_hal_binary32_(hal_path32),
        driver_hal_binary64_(hal_path64),
        driver_shell_binary32_(shell_path32),
        driver_shell_binary64_(shell_path64),
        VtsDriverCommUtil() {}

  // handles a new session.
  bool ProcessOneCommand();

 protected:

  // for the LIST_HAL command
  bool ListHals(
      const ::google::protobuf::RepeatedPtrField<::std::string>& base_paths);

  // for the SET_HOST_INFO command.
  bool SetHostInfo(const int callback_port);

  // for the CHECK_DRIVER_SERVICE command
  bool CheckDriverService(
      const string& service_name, bool* live);

  // for the LAUNCH_DRIVER_SERVICE command
  bool LaunchDriverService(
      int driver_type, const string& service_name, const string& file_path,
      int target_class, int target_type, float target_version,
      const string& module_name, int bits);

  // for the LIST_APIS command
  bool ListApis();

  // for the CALL_API command
  bool CallApi(const string& call_payload);

  // Returns a default response message.
  bool DefaultResponse();

 protected:
  // the currently opened, connected service name.
  string service_name_;
  // the port number of a host-side callback server.
  int callback_port_;
  // the socket client of a launched or connected driver.
  VtsDriverSocketClient* driver_client_;

  const string driver_hal_spec_dir_path_;
  const string driver_hal_binary32_;
  const string driver_hal_binary64_;
  const string driver_shell_binary32_;
  const string driver_shell_binary64_;
};

}  // namespace vts
}  // namespace android

#endif
