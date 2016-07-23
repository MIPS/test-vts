# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VtsReportMessage.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VtsReportMessage.proto',
  package='android.vts',
  serialized_pb='\n\x16VtsReportMessage.proto\x12\x0b\x61ndroid.vts\"_\n\x18\x41ndroidDeviceInfoMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x12\n\nbuild_type\x18\x02 \x01(\x0c\x12\x0e\n\x06\x62ranch\x18\x03 \x01(\x0c\x12\x11\n\tapi_level\x18\x04 \x01(\r\"P\n\x10\x41ndroidBuildInfo\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x0b \x01(\x0c\x12\x12\n\nbuild_type\x18\x0c \x01(\x0c\x12\x0e\n\x06\x62ranch\x18\r \x01(\x0c\"\x87\x01\n\x15TestCaseReportMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x30\n\x0btest_result\x18\x0b \x01(\x0e\x32\x1b.android.vts.TestCaseResult\x12\x17\n\x0fstart_timestamp\x18\x15 \x01(\x03\x12\x15\n\rend_timestamp\x18\x16 \x01(\x03\"V\n\x16ProfilingReportMessage\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x17\n\x0fstart_timestamp\x18\x0b \x01(\x03\x12\x15\n\rend_timestamp\x18\x0c \x01(\x03\"\xf0\x02\n\x11TestReportMessage\x12\x12\n\ntest_suite\x18\x01 \x01(\x0c\x12\x0c\n\x04test\x18\x02 \x01(\x0c\x12+\n\ttest_type\x18\x03 \x01(\x0e\x32\x18.android.vts.VtsTestType\x12:\n\x0b\x64\x65vice_info\x18\x04 \x03(\x0b\x32%.android.vts.AndroidDeviceInfoMessage\x12\x31\n\nbuild_info\x18\x05 \x01(\x0b\x32\x1d.android.vts.AndroidBuildInfo\x12\x35\n\ttest_case\x18\x0b \x03(\x0b\x32\".android.vts.TestCaseReportMessage\x12\x36\n\tprofiling\x18\x15 \x03(\x0b\x32#.android.vts.ProfilingReportMessage\x12\x17\n\x0fstart_timestamp\x18\x65 \x01(\x03\x12\x15\n\rend_timestamp\x18\x66 \x01(\x03*\xb3\x01\n\x0eTestCaseResult\x12\x12\n\x0eUNKNOWN_RESULT\x10\x00\x12\x19\n\x15TEST_CASE_RESULT_PASS\x10\x01\x12\x19\n\x15TEST_CASE_RESULT_FAIL\x10\x02\x12\x19\n\x15TEST_CASE_RESULT_SKIP\x10\x03\x12\x1e\n\x1aTEST_CASE_RESULT_EXCEPTION\x10\x04\x12\x1c\n\x18TEST_CASE_RESULT_TIMEOUT\x10\x05*\x9c\x01\n\x0bVtsTestType\x12\x18\n\x14UNKNOWN_VTS_TESTTYPE\x10\x00\x12\x1e\n\x1aVTS_HOST_DRIVEN_STRUCTURAL\x10\x01\x12\x1b\n\x17VTS_HOST_DRIVEN_FUZZING\x10\x02\x12\x19\n\x15VTS_TARGET_SIDE_GTEST\x10\x03\x12\x1b\n\x17VTS_TARGET_SIDE_FUZZING\x10\x04')

_TESTCASERESULT = _descriptor.EnumDescriptor(
  name='TestCaseResult',
  full_name='android.vts.TestCaseResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_RESULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_PASS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_FAIL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_SKIP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_EXCEPTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_CASE_RESULT_TIMEOUT', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=816,
  serialized_end=995,
)

TestCaseResult = enum_type_wrapper.EnumTypeWrapper(_TESTCASERESULT)
_VTSTESTTYPE = _descriptor.EnumDescriptor(
  name='VtsTestType',
  full_name='android.vts.VtsTestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VTS_TESTTYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_HOST_DRIVEN_STRUCTURAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_HOST_DRIVEN_FUZZING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_TARGET_SIDE_GTEST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTS_TARGET_SIDE_FUZZING', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=998,
  serialized_end=1154,
)

VtsTestType = enum_type_wrapper.EnumTypeWrapper(_VTSTESTTYPE)
UNKNOWN_RESULT = 0
TEST_CASE_RESULT_PASS = 1
TEST_CASE_RESULT_FAIL = 2
TEST_CASE_RESULT_SKIP = 3
TEST_CASE_RESULT_EXCEPTION = 4
TEST_CASE_RESULT_TIMEOUT = 5
UNKNOWN_VTS_TESTTYPE = 0
VTS_HOST_DRIVEN_STRUCTURAL = 1
VTS_HOST_DRIVEN_FUZZING = 2
VTS_TARGET_SIDE_GTEST = 3
VTS_TARGET_SIDE_FUZZING = 4



_ANDROIDDEVICEINFOMESSAGE = _descriptor.Descriptor(
  name='AndroidDeviceInfoMessage',
  full_name='android.vts.AndroidDeviceInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.AndroidDeviceInfoMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_type', full_name='android.vts.AndroidDeviceInfoMessage.build_type', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='android.vts.AndroidDeviceInfoMessage.branch', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_level', full_name='android.vts.AndroidDeviceInfoMessage.api_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=39,
  serialized_end=134,
)


_ANDROIDBUILDINFO = _descriptor.Descriptor(
  name='AndroidBuildInfo',
  full_name='android.vts.AndroidBuildInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='android.vts.AndroidBuildInfo.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.AndroidBuildInfo.name', index=1,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_type', full_name='android.vts.AndroidBuildInfo.build_type', index=2,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='android.vts.AndroidBuildInfo.branch', index=3,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=136,
  serialized_end=216,
)


_TESTCASEREPORTMESSAGE = _descriptor.Descriptor(
  name='TestCaseReportMessage',
  full_name='android.vts.TestCaseReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.TestCaseReportMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_result', full_name='android.vts.TestCaseReportMessage.test_result', index=1,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.TestCaseReportMessage.start_timestamp', index=2,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.TestCaseReportMessage.end_timestamp', index=3,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=219,
  serialized_end=354,
)


_PROFILINGREPORTMESSAGE = _descriptor.Descriptor(
  name='ProfilingReportMessage',
  full_name='android.vts.ProfilingReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.ProfilingReportMessage.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.ProfilingReportMessage.start_timestamp', index=1,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.ProfilingReportMessage.end_timestamp', index=2,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=356,
  serialized_end=442,
)


_TESTREPORTMESSAGE = _descriptor.Descriptor(
  name='TestReportMessage',
  full_name='android.vts.TestReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_suite', full_name='android.vts.TestReportMessage.test_suite', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test', full_name='android.vts.TestReportMessage.test', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_type', full_name='android.vts.TestReportMessage.test_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='android.vts.TestReportMessage.device_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_info', full_name='android.vts.TestReportMessage.build_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_case', full_name='android.vts.TestReportMessage.test_case', index=5,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profiling', full_name='android.vts.TestReportMessage.profiling', index=6,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='android.vts.TestReportMessage.start_timestamp', index=7,
      number=101, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='android.vts.TestReportMessage.end_timestamp', index=8,
      number=102, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=445,
  serialized_end=813,
)

_TESTCASEREPORTMESSAGE.fields_by_name['test_result'].enum_type = _TESTCASERESULT
_TESTREPORTMESSAGE.fields_by_name['test_type'].enum_type = _VTSTESTTYPE
_TESTREPORTMESSAGE.fields_by_name['device_info'].message_type = _ANDROIDDEVICEINFOMESSAGE
_TESTREPORTMESSAGE.fields_by_name['build_info'].message_type = _ANDROIDBUILDINFO
_TESTREPORTMESSAGE.fields_by_name['test_case'].message_type = _TESTCASEREPORTMESSAGE
_TESTREPORTMESSAGE.fields_by_name['profiling'].message_type = _PROFILINGREPORTMESSAGE
DESCRIPTOR.message_types_by_name['AndroidDeviceInfoMessage'] = _ANDROIDDEVICEINFOMESSAGE
DESCRIPTOR.message_types_by_name['AndroidBuildInfo'] = _ANDROIDBUILDINFO
DESCRIPTOR.message_types_by_name['TestCaseReportMessage'] = _TESTCASEREPORTMESSAGE
DESCRIPTOR.message_types_by_name['ProfilingReportMessage'] = _PROFILINGREPORTMESSAGE
DESCRIPTOR.message_types_by_name['TestReportMessage'] = _TESTREPORTMESSAGE

class AndroidDeviceInfoMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANDROIDDEVICEINFOMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.AndroidDeviceInfoMessage)

class AndroidBuildInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ANDROIDBUILDINFO

  # @@protoc_insertion_point(class_scope:android.vts.AndroidBuildInfo)

class TestCaseReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTCASEREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.TestCaseReportMessage)

class ProfilingReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROFILINGREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.ProfilingReportMessage)

class TestReportMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTREPORTMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.TestReportMessage)


# @@protoc_insertion_point(module_scope)
