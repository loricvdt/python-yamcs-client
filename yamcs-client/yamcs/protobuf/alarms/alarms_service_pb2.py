# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/alarms/alarms_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.protobuf.alarms import alarms_pb2 as yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/alarms/alarms_service.proto',
  package='yamcs.protobuf.alarms',
  syntax='proto2',
  serialized_options=b'\n\031org.yamcs.protobuf.alarmsB\022AlarmsServiceProtoP\001',
  serialized_pb=b'\n*yamcs/protobuf/alarms/alarms_service.proto\x12\x15yamcs.protobuf.alarms\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a\"yamcs/protobuf/alarms/alarms.proto\"\xa5\x01\n\x11ListAlarmsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\x03\x12\r\n\x05limit\x18\x03 \x01(\x05\x12)\n\x05start\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05order\x18\x06 \x01(\t\"F\n\x12ListAlarmsResponse\x12\x30\n\x06\x61larms\x18\x01 \x03(\x0b\x32 .yamcs.protobuf.alarms.AlarmData\"\xd1\x01\n\x1aListParameterAlarmsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tparameter\x18\x02 \x01(\t\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\r\n\x05limit\x18\x04 \x01(\x05\x12)\n\x05start\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05order\x18\x07 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x08 \x01(\x08\"O\n\x1bListParameterAlarmsResponse\x12\x30\n\x06\x61larms\x18\x01 \x03(\x0b\x32 .yamcs.protobuf.alarms.AlarmData\"A\n\x1aListProcessorAlarmsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\"O\n\x1bListProcessorAlarmsResponse\x12\x30\n\x06\x61larms\x18\x01 \x03(\x0b\x32 .yamcs.protobuf.alarms.AlarmData\"=\n\x16SubscribeAlarmsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\"\x8d\x01\n\x10\x45\x64itAlarmRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06seqnum\x18\x04 \x01(\r\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x12\x16\n\x0eshelveDuration\x18\x07 \x01(\x04\"C\n\x1cSubscribeGlobalStatusRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\"\xb2\x01\n\x11GlobalAlarmStatus\x12\x1b\n\x13unacknowledgedCount\x18\x01 \x01(\x05\x12\x1c\n\x14unacknowledgedActive\x18\x02 \x01(\x08\x12\x19\n\x11\x61\x63knowledgedCount\x18\x03 \x01(\x05\x12\x1a\n\x12\x61\x63knowledgedActive\x18\x04 \x01(\x08\x12\x14\n\x0cshelvedCount\x18\x05 \x01(\x05\x12\x15\n\rshelvedActive\x18\x06 \x01(\x08\x32\x9d\x07\n\tAlarmsApi\x12\x87\x01\n\nListAlarms\x12(.yamcs.protobuf.alarms.ListAlarmsRequest\x1a).yamcs.protobuf.alarms.ListAlarmsResponse\"$\x8a\x92\x03 \n\x1e/api/archive/{instance}/alarms\x12\xaf\x01\n\x13ListParameterAlarms\x12\x31.yamcs.protobuf.alarms.ListParameterAlarmsRequest\x1a\x32.yamcs.protobuf.alarms.ListParameterAlarmsResponse\"1\x8a\x92\x03-\n+/api/archive/{instance}/alarms/{parameter*}\x12\xb1\x01\n\x13ListProcessorAlarms\x12\x31.yamcs.protobuf.alarms.ListProcessorAlarmsRequest\x1a\x32.yamcs.protobuf.alarms.ListProcessorAlarmsResponse\"3\x8a\x92\x03/\n-/api/processors/{instance}/{processor}/alarms\x12\x95\x01\n\tEditAlarm\x12\'.yamcs.protobuf.alarms.EditAlarmRequest\x1a\x16.google.protobuf.Empty\"G\x8a\x92\x03\x43*>/api/processors/{instance}/{processor}/alarms/{name*}/{seqnum}:\x01*\x12\x93\x01\n\x15SubscribeGlobalStatus\x12\x33.yamcs.protobuf.alarms.SubscribeGlobalStatusRequest\x1a(.yamcs.protobuf.alarms.GlobalAlarmStatus\"\x19\xda\x92\x03\x15\n\x13global-alarm-status0\x01\x12r\n\x0fSubscribeAlarms\x12-.yamcs.protobuf.alarms.SubscribeAlarmsRequest\x1a .yamcs.protobuf.alarms.AlarmData\"\x0c\xda\x92\x03\x08\n\x06\x61larms0\x01\x42\x31\n\x19org.yamcs.protobuf.alarmsB\x12\x41larmsServiceProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2.DESCRIPTOR,])




_LISTALARMSREQUEST = _descriptor.Descriptor(
  name='ListAlarmsRequest',
  full_name='yamcs.protobuf.alarms.ListAlarmsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.pos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.start', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.stop', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='yamcs.protobuf.alarms.ListAlarmsRequest.order', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=362,
)


_LISTALARMSRESPONSE = _descriptor.Descriptor(
  name='ListAlarmsResponse',
  full_name='yamcs.protobuf.alarms.ListAlarmsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alarms', full_name='yamcs.protobuf.alarms.ListAlarmsResponse.alarms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=434,
)


_LISTPARAMETERALARMSREQUEST = _descriptor.Descriptor(
  name='ListParameterAlarmsRequest',
  full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.parameter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.pos', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.start', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.stop', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.order', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='yamcs.protobuf.alarms.ListParameterAlarmsRequest.detail', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=646,
)


_LISTPARAMETERALARMSRESPONSE = _descriptor.Descriptor(
  name='ListParameterAlarmsResponse',
  full_name='yamcs.protobuf.alarms.ListParameterAlarmsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alarms', full_name='yamcs.protobuf.alarms.ListParameterAlarmsResponse.alarms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=648,
  serialized_end=727,
)


_LISTPROCESSORALARMSREQUEST = _descriptor.Descriptor(
  name='ListProcessorAlarmsRequest',
  full_name='yamcs.protobuf.alarms.ListProcessorAlarmsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.ListProcessorAlarmsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.alarms.ListProcessorAlarmsRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=794,
)


_LISTPROCESSORALARMSRESPONSE = _descriptor.Descriptor(
  name='ListProcessorAlarmsResponse',
  full_name='yamcs.protobuf.alarms.ListProcessorAlarmsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alarms', full_name='yamcs.protobuf.alarms.ListProcessorAlarmsResponse.alarms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=875,
)


_SUBSCRIBEALARMSREQUEST = _descriptor.Descriptor(
  name='SubscribeAlarmsRequest',
  full_name='yamcs.protobuf.alarms.SubscribeAlarmsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.SubscribeAlarmsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.alarms.SubscribeAlarmsRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=877,
  serialized_end=938,
)


_EDITALARMREQUEST = _descriptor.Descriptor(
  name='EditAlarmRequest',
  full_name='yamcs.protobuf.alarms.EditAlarmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.EditAlarmRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.alarms.EditAlarmRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.alarms.EditAlarmRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='yamcs.protobuf.alarms.EditAlarmRequest.seqnum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='yamcs.protobuf.alarms.EditAlarmRequest.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='yamcs.protobuf.alarms.EditAlarmRequest.comment', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelveDuration', full_name='yamcs.protobuf.alarms.EditAlarmRequest.shelveDuration', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=1082,
)


_SUBSCRIBEGLOBALSTATUSREQUEST = _descriptor.Descriptor(
  name='SubscribeGlobalStatusRequest',
  full_name='yamcs.protobuf.alarms.SubscribeGlobalStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.alarms.SubscribeGlobalStatusRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.alarms.SubscribeGlobalStatusRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1084,
  serialized_end=1151,
)


_GLOBALALARMSTATUS = _descriptor.Descriptor(
  name='GlobalAlarmStatus',
  full_name='yamcs.protobuf.alarms.GlobalAlarmStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unacknowledgedCount', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.unacknowledgedCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unacknowledgedActive', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.unacknowledgedActive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledgedCount', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.acknowledgedCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acknowledgedActive', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.acknowledgedActive', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelvedCount', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.shelvedCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shelvedActive', full_name='yamcs.protobuf.alarms.GlobalAlarmStatus.shelvedActive', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1154,
  serialized_end=1332,
)

_LISTALARMSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTALARMSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTALARMSRESPONSE.fields_by_name['alarms'].message_type = yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2._ALARMDATA
_LISTPARAMETERALARMSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTPARAMETERALARMSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTPARAMETERALARMSRESPONSE.fields_by_name['alarms'].message_type = yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2._ALARMDATA
_LISTPROCESSORALARMSRESPONSE.fields_by_name['alarms'].message_type = yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2._ALARMDATA
DESCRIPTOR.message_types_by_name['ListAlarmsRequest'] = _LISTALARMSREQUEST
DESCRIPTOR.message_types_by_name['ListAlarmsResponse'] = _LISTALARMSRESPONSE
DESCRIPTOR.message_types_by_name['ListParameterAlarmsRequest'] = _LISTPARAMETERALARMSREQUEST
DESCRIPTOR.message_types_by_name['ListParameterAlarmsResponse'] = _LISTPARAMETERALARMSRESPONSE
DESCRIPTOR.message_types_by_name['ListProcessorAlarmsRequest'] = _LISTPROCESSORALARMSREQUEST
DESCRIPTOR.message_types_by_name['ListProcessorAlarmsResponse'] = _LISTPROCESSORALARMSRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeAlarmsRequest'] = _SUBSCRIBEALARMSREQUEST
DESCRIPTOR.message_types_by_name['EditAlarmRequest'] = _EDITALARMREQUEST
DESCRIPTOR.message_types_by_name['SubscribeGlobalStatusRequest'] = _SUBSCRIBEGLOBALSTATUSREQUEST
DESCRIPTOR.message_types_by_name['GlobalAlarmStatus'] = _GLOBALALARMSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAlarmsRequest = _reflection.GeneratedProtocolMessageType('ListAlarmsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALARMSREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListAlarmsRequest)
  })
_sym_db.RegisterMessage(ListAlarmsRequest)

ListAlarmsResponse = _reflection.GeneratedProtocolMessageType('ListAlarmsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTALARMSRESPONSE,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListAlarmsResponse)
  })
_sym_db.RegisterMessage(ListAlarmsResponse)

ListParameterAlarmsRequest = _reflection.GeneratedProtocolMessageType('ListParameterAlarmsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPARAMETERALARMSREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListParameterAlarmsRequest)
  })
_sym_db.RegisterMessage(ListParameterAlarmsRequest)

ListParameterAlarmsResponse = _reflection.GeneratedProtocolMessageType('ListParameterAlarmsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPARAMETERALARMSRESPONSE,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListParameterAlarmsResponse)
  })
_sym_db.RegisterMessage(ListParameterAlarmsResponse)

ListProcessorAlarmsRequest = _reflection.GeneratedProtocolMessageType('ListProcessorAlarmsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSORALARMSREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListProcessorAlarmsRequest)
  })
_sym_db.RegisterMessage(ListProcessorAlarmsRequest)

ListProcessorAlarmsResponse = _reflection.GeneratedProtocolMessageType('ListProcessorAlarmsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSORALARMSRESPONSE,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.ListProcessorAlarmsResponse)
  })
_sym_db.RegisterMessage(ListProcessorAlarmsResponse)

SubscribeAlarmsRequest = _reflection.GeneratedProtocolMessageType('SubscribeAlarmsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEALARMSREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.SubscribeAlarmsRequest)
  })
_sym_db.RegisterMessage(SubscribeAlarmsRequest)

EditAlarmRequest = _reflection.GeneratedProtocolMessageType('EditAlarmRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITALARMREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.EditAlarmRequest)
  })
_sym_db.RegisterMessage(EditAlarmRequest)

SubscribeGlobalStatusRequest = _reflection.GeneratedProtocolMessageType('SubscribeGlobalStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEGLOBALSTATUSREQUEST,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.SubscribeGlobalStatusRequest)
  })
_sym_db.RegisterMessage(SubscribeGlobalStatusRequest)

GlobalAlarmStatus = _reflection.GeneratedProtocolMessageType('GlobalAlarmStatus', (_message.Message,), {
  'DESCRIPTOR' : _GLOBALALARMSTATUS,
  '__module__' : 'yamcs.protobuf.alarms.alarms_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.alarms.GlobalAlarmStatus)
  })
_sym_db.RegisterMessage(GlobalAlarmStatus)


DESCRIPTOR._options = None

_ALARMSAPI = _descriptor.ServiceDescriptor(
  name='AlarmsApi',
  full_name='yamcs.protobuf.alarms.AlarmsApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1335,
  serialized_end=2260,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAlarms',
    full_name='yamcs.protobuf.alarms.AlarmsApi.ListAlarms',
    index=0,
    containing_service=None,
    input_type=_LISTALARMSREQUEST,
    output_type=_LISTALARMSRESPONSE,
    serialized_options=b'\212\222\003 \n\036/api/archive/{instance}/alarms',
  ),
  _descriptor.MethodDescriptor(
    name='ListParameterAlarms',
    full_name='yamcs.protobuf.alarms.AlarmsApi.ListParameterAlarms',
    index=1,
    containing_service=None,
    input_type=_LISTPARAMETERALARMSREQUEST,
    output_type=_LISTPARAMETERALARMSRESPONSE,
    serialized_options=b'\212\222\003-\n+/api/archive/{instance}/alarms/{parameter*}',
  ),
  _descriptor.MethodDescriptor(
    name='ListProcessorAlarms',
    full_name='yamcs.protobuf.alarms.AlarmsApi.ListProcessorAlarms',
    index=2,
    containing_service=None,
    input_type=_LISTPROCESSORALARMSREQUEST,
    output_type=_LISTPROCESSORALARMSRESPONSE,
    serialized_options=b'\212\222\003/\n-/api/processors/{instance}/{processor}/alarms',
  ),
  _descriptor.MethodDescriptor(
    name='EditAlarm',
    full_name='yamcs.protobuf.alarms.AlarmsApi.EditAlarm',
    index=3,
    containing_service=None,
    input_type=_EDITALARMREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003C*>/api/processors/{instance}/{processor}/alarms/{name*}/{seqnum}:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeGlobalStatus',
    full_name='yamcs.protobuf.alarms.AlarmsApi.SubscribeGlobalStatus',
    index=4,
    containing_service=None,
    input_type=_SUBSCRIBEGLOBALSTATUSREQUEST,
    output_type=_GLOBALALARMSTATUS,
    serialized_options=b'\332\222\003\025\n\023global-alarm-status',
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeAlarms',
    full_name='yamcs.protobuf.alarms.AlarmsApi.SubscribeAlarms',
    index=5,
    containing_service=None,
    input_type=_SUBSCRIBEALARMSREQUEST,
    output_type=yamcs_dot_protobuf_dot_alarms_dot_alarms__pb2._ALARMDATA,
    serialized_options=b'\332\222\003\010\n\006alarms',
  ),
])
_sym_db.RegisterServiceDescriptor(_ALARMSAPI)

DESCRIPTOR.services_by_name['AlarmsApi'] = _ALARMSAPI

# @@protoc_insertion_point(module_scope)
