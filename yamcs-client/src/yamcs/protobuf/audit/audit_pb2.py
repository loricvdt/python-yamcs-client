# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/audit/audit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/audit/audit.proto',
  package='yamcs.protobuf.audit',
  syntax='proto2',
  serialized_options=_b('\n\030org.yamcs.protobuf.auditB\021AuditServiceProtoP\001'),
  serialized_pb=_b('\n yamcs/protobuf/audit/audit.proto\x12\x14yamcs.protobuf.audit\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\"\xb9\x01\n\x17ListAuditRecordsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0c\n\x04next\x18\x03 \x01(\t\x12)\n\x05start\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\t\n\x01q\x18\x06 \x01(\t\x12\x0f\n\x07service\x18\x07 \x01(\t\"i\n\x18ListAuditRecordsResponse\x12\x32\n\x07records\x18\x01 \x03(\x0b\x32!.yamcs.protobuf.audit.AuditRecord\x12\x19\n\x11\x63ontinuationToken\x18\x02 \x01(\t\"\xa1\x01\n\x0b\x41uditRecord\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x0f\n\x07summary\x18\x05 \x01(\t\x12(\n\x07request\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct2\xa3\x01\n\x08\x41uditApi\x12\x96\x01\n\x10ListAuditRecords\x12-.yamcs.protobuf.audit.ListAuditRecordsRequest\x1a..yamcs.protobuf.audit.ListAuditRecordsResponse\"#\x8a\x92\x03\x1f\n\x1d/api/audit/records/{instance}B/\n\x18org.yamcs.protobuf.auditB\x11\x41uditServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LISTAUDITRECORDSREQUEST = _descriptor.Descriptor(
  name='ListAuditRecordsRequest',
  full_name='yamcs.protobuf.audit.ListAuditRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.next', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.start', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.stop', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.q', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='yamcs.protobuf.audit.ListAuditRecordsRequest.service', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=151,
  serialized_end=336,
)


_LISTAUDITRECORDSRESPONSE = _descriptor.Descriptor(
  name='ListAuditRecordsResponse',
  full_name='yamcs.protobuf.audit.ListAuditRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='yamcs.protobuf.audit.ListAuditRecordsResponse.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='continuationToken', full_name='yamcs.protobuf.audit.ListAuditRecordsResponse.continuationToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=338,
  serialized_end=443,
)


_AUDITRECORD = _descriptor.Descriptor(
  name='AuditRecord',
  full_name='yamcs.protobuf.audit.AuditRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='yamcs.protobuf.audit.AuditRecord.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='yamcs.protobuf.audit.AuditRecord.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='yamcs.protobuf.audit.AuditRecord.method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='yamcs.protobuf.audit.AuditRecord.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='yamcs.protobuf.audit.AuditRecord.summary', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='yamcs.protobuf.audit.AuditRecord.request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=446,
  serialized_end=607,
)

_LISTAUDITRECORDSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTAUDITRECORDSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTAUDITRECORDSRESPONSE.fields_by_name['records'].message_type = _AUDITRECORD
_AUDITRECORD.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AUDITRECORD.fields_by_name['request'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ListAuditRecordsRequest'] = _LISTAUDITRECORDSREQUEST
DESCRIPTOR.message_types_by_name['ListAuditRecordsResponse'] = _LISTAUDITRECORDSRESPONSE
DESCRIPTOR.message_types_by_name['AuditRecord'] = _AUDITRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAuditRecordsRequest = _reflection.GeneratedProtocolMessageType('ListAuditRecordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTAUDITRECORDSREQUEST,
  __module__ = 'yamcs.protobuf.audit.audit_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.audit.ListAuditRecordsRequest)
  ))
_sym_db.RegisterMessage(ListAuditRecordsRequest)

ListAuditRecordsResponse = _reflection.GeneratedProtocolMessageType('ListAuditRecordsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTAUDITRECORDSRESPONSE,
  __module__ = 'yamcs.protobuf.audit.audit_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.audit.ListAuditRecordsResponse)
  ))
_sym_db.RegisterMessage(ListAuditRecordsResponse)

AuditRecord = _reflection.GeneratedProtocolMessageType('AuditRecord', (_message.Message,), dict(
  DESCRIPTOR = _AUDITRECORD,
  __module__ = 'yamcs.protobuf.audit.audit_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.audit.AuditRecord)
  ))
_sym_db.RegisterMessage(AuditRecord)


DESCRIPTOR._options = None

_AUDITAPI = _descriptor.ServiceDescriptor(
  name='AuditApi',
  full_name='yamcs.protobuf.audit.AuditApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=610,
  serialized_end=773,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAuditRecords',
    full_name='yamcs.protobuf.audit.AuditApi.ListAuditRecords',
    index=0,
    containing_service=None,
    input_type=_LISTAUDITRECORDSREQUEST,
    output_type=_LISTAUDITRECORDSRESPONSE,
    serialized_options=_b('\212\222\003\037\n\035/api/audit/records/{instance}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDITAPI)

DESCRIPTOR.services_by_name['AuditApi'] = _AUDITAPI

# @@protoc_insertion_point(module_scope)