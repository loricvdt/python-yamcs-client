# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/packets/packets_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.api import httpbody_pb2 as yamcs_dot_api_dot_httpbody__pb2
from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/packets/packets_service.proto',
  package='yamcs.protobuf.packets',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\023PacketsServiceProtoP\001'),
  serialized_pb=_b('\n,yamcs/protobuf/packets/packets_service.proto\x12\x16yamcs.protobuf.packets\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a\x18yamcs/api/httpbody.proto\x1a\x1ayamcs/protobuf/yamcs.proto\"*\n\x16ListPacketNamesRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\"\'\n\x17ListPacketNamesResponse\x12\x0c\n\x04name\x18\x01 \x03(\t\"\xc2\x01\n\x12ListPacketsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\x03\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\r\n\x05order\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x03(\t\x12\x0c\n\x04next\x18\x06 \x01(\t\x12)\n\x05start\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"^\n\x13ListPacketsResponse\x12,\n\x06packet\x18\x01 \x03(\x0b\x32\x1c.yamcs.protobuf.TmPacketData\x12\x19\n\x11\x63ontinuationToken\x18\x02 \x01(\t\"a\n\x10GetPacketRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12+\n\x07gentime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06seqnum\x18\x03 \x01(\x05\"\x8b\x01\n\x14StreamPacketsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x03(\t\"d\n\x13\x45xportPacketRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12+\n\x07gentime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06seqnum\x18\x03 \x01(\x05\"\x8b\x01\n\x14\x45xportPacketsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x03(\t\"N\n\x17SubscribePacketsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x11\n\tprocessor\x18\x03 \x01(\t\"P\n\x1aSubscribeContainersRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x11\n\tprocessor\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\t\"\x94\x01\n\rContainerData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x0egenerationTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rreceptionTime\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x62inary\x18\x04 \x01(\x0c\x32\xf7\x08\n\nPacketsApi\x12\x9e\x01\n\x0fListPacketNames\x12..yamcs.protobuf.packets.ListPacketNamesRequest\x1a/.yamcs.protobuf.packets.ListPacketNamesResponse\"*\x8a\x92\x03&\n$/api/archive/{instance}/packet-names\x12\x8d\x01\n\x0bListPackets\x12*.yamcs.protobuf.packets.ListPacketsRequest\x1a+.yamcs.protobuf.packets.ListPacketsResponse\"%\x8a\x92\x03!\n\x1f/api/archive/{instance}/packets\x12\x8d\x01\n\tGetPacket\x12(.yamcs.protobuf.packets.GetPacketRequest\x1a\x1c.yamcs.protobuf.TmPacketData\"8\x8a\x92\x03\x34\n2/api/archive/{instance}/packets/{gentime}/{seqnum}\x12\x94\x01\n\rStreamPackets\x12,.yamcs.protobuf.packets.StreamPacketsRequest\x1a\x1c.yamcs.protobuf.TmPacketData\"5\x8a\x92\x03\x31\x1a,/api/stream-archive/{instance}:streamPackets:\x01*0\x01\x12\x91\x01\n\x0c\x45xportPacket\x12+.yamcs.protobuf.packets.ExportPacketRequest\x1a\x13.yamcs.api.HttpBody\"?\x8a\x92\x03;\n9/api/archive/{instance}/packets/{gentime}/{seqnum}:export\x12\x81\x01\n\rExportPackets\x12,.yamcs.protobuf.packets.ExportPacketsRequest\x1a\x13.yamcs.api.HttpBody\"+\x8a\x92\x03\'\n%/api/archive/{instance}:exportPackets0\x01\x12r\n\x10SubscribePackets\x12/.yamcs.protobuf.packets.SubscribePacketsRequest\x1a\x1c.yamcs.protobuf.TmPacketData\"\r\xda\x92\x03\t\n\x07packets0\x01\x12\x84\x01\n\x13SubscribeContainers\x12\x32.yamcs.protobuf.packets.SubscribeContainersRequest\x1a%.yamcs.protobuf.packets.ContainerData\"\x10\xda\x92\x03\x0c\n\ncontainers0\x01\x42+\n\x12org.yamcs.protobufB\x13PacketsServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_api_dot_httpbody__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,])




_LISTPACKETNAMESREQUEST = _descriptor.Descriptor(
  name='ListPacketNamesRequest',
  full_name='yamcs.protobuf.packets.ListPacketNamesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.ListPacketNamesRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=188,
  serialized_end=230,
)


_LISTPACKETNAMESRESPONSE = _descriptor.Descriptor(
  name='ListPacketNamesResponse',
  full_name='yamcs.protobuf.packets.ListPacketNamesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.packets.ListPacketNamesResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=232,
  serialized_end=271,
)


_LISTPACKETSREQUEST = _descriptor.Descriptor(
  name='ListPacketsRequest',
  full_name='yamcs.protobuf.packets.ListPacketsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.ListPacketsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='yamcs.protobuf.packets.ListPacketsRequest.pos', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='yamcs.protobuf.packets.ListPacketsRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='yamcs.protobuf.packets.ListPacketsRequest.order', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.packets.ListPacketsRequest.name', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='yamcs.protobuf.packets.ListPacketsRequest.next', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.packets.ListPacketsRequest.start', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.packets.ListPacketsRequest.stop', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=274,
  serialized_end=468,
)


_LISTPACKETSRESPONSE = _descriptor.Descriptor(
  name='ListPacketsResponse',
  full_name='yamcs.protobuf.packets.ListPacketsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet', full_name='yamcs.protobuf.packets.ListPacketsResponse.packet', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='continuationToken', full_name='yamcs.protobuf.packets.ListPacketsResponse.continuationToken', index=1,
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
  serialized_start=470,
  serialized_end=564,
)


_GETPACKETREQUEST = _descriptor.Descriptor(
  name='GetPacketRequest',
  full_name='yamcs.protobuf.packets.GetPacketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.GetPacketRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gentime', full_name='yamcs.protobuf.packets.GetPacketRequest.gentime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='yamcs.protobuf.packets.GetPacketRequest.seqnum', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=566,
  serialized_end=663,
)


_STREAMPACKETSREQUEST = _descriptor.Descriptor(
  name='StreamPacketsRequest',
  full_name='yamcs.protobuf.packets.StreamPacketsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.StreamPacketsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.packets.StreamPacketsRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.packets.StreamPacketsRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.packets.StreamPacketsRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=666,
  serialized_end=805,
)


_EXPORTPACKETREQUEST = _descriptor.Descriptor(
  name='ExportPacketRequest',
  full_name='yamcs.protobuf.packets.ExportPacketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.ExportPacketRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gentime', full_name='yamcs.protobuf.packets.ExportPacketRequest.gentime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='yamcs.protobuf.packets.ExportPacketRequest.seqnum', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=807,
  serialized_end=907,
)


_EXPORTPACKETSREQUEST = _descriptor.Descriptor(
  name='ExportPacketsRequest',
  full_name='yamcs.protobuf.packets.ExportPacketsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.ExportPacketsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.packets.ExportPacketsRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.packets.ExportPacketsRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.packets.ExportPacketsRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=910,
  serialized_end=1049,
)


_SUBSCRIBEPACKETSREQUEST = _descriptor.Descriptor(
  name='SubscribePacketsRequest',
  full_name='yamcs.protobuf.packets.SubscribePacketsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.SubscribePacketsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='yamcs.protobuf.packets.SubscribePacketsRequest.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.packets.SubscribePacketsRequest.processor', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1051,
  serialized_end=1129,
)


_SUBSCRIBECONTAINERSREQUEST = _descriptor.Descriptor(
  name='SubscribeContainersRequest',
  full_name='yamcs.protobuf.packets.SubscribeContainersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.packets.SubscribeContainersRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.packets.SubscribeContainersRequest.processor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='yamcs.protobuf.packets.SubscribeContainersRequest.names', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=1131,
  serialized_end=1211,
)


_CONTAINERDATA = _descriptor.Descriptor(
  name='ContainerData',
  full_name='yamcs.protobuf.packets.ContainerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.packets.ContainerData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generationTime', full_name='yamcs.protobuf.packets.ContainerData.generationTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receptionTime', full_name='yamcs.protobuf.packets.ContainerData.receptionTime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary', full_name='yamcs.protobuf.packets.ContainerData.binary', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1214,
  serialized_end=1362,
)

_LISTPACKETSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTPACKETSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTPACKETSRESPONSE.fields_by_name['packet'].message_type = yamcs_dot_protobuf_dot_yamcs__pb2._TMPACKETDATA
_GETPACKETREQUEST.fields_by_name['gentime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMPACKETSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STREAMPACKETSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPORTPACKETREQUEST.fields_by_name['gentime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPORTPACKETSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPORTPACKETSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINERDATA.fields_by_name['generationTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINERDATA.fields_by_name['receptionTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['ListPacketNamesRequest'] = _LISTPACKETNAMESREQUEST
DESCRIPTOR.message_types_by_name['ListPacketNamesResponse'] = _LISTPACKETNAMESRESPONSE
DESCRIPTOR.message_types_by_name['ListPacketsRequest'] = _LISTPACKETSREQUEST
DESCRIPTOR.message_types_by_name['ListPacketsResponse'] = _LISTPACKETSRESPONSE
DESCRIPTOR.message_types_by_name['GetPacketRequest'] = _GETPACKETREQUEST
DESCRIPTOR.message_types_by_name['StreamPacketsRequest'] = _STREAMPACKETSREQUEST
DESCRIPTOR.message_types_by_name['ExportPacketRequest'] = _EXPORTPACKETREQUEST
DESCRIPTOR.message_types_by_name['ExportPacketsRequest'] = _EXPORTPACKETSREQUEST
DESCRIPTOR.message_types_by_name['SubscribePacketsRequest'] = _SUBSCRIBEPACKETSREQUEST
DESCRIPTOR.message_types_by_name['SubscribeContainersRequest'] = _SUBSCRIBECONTAINERSREQUEST
DESCRIPTOR.message_types_by_name['ContainerData'] = _CONTAINERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPacketNamesRequest = _reflection.GeneratedProtocolMessageType('ListPacketNamesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKETNAMESREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ListPacketNamesRequest)
  ))
_sym_db.RegisterMessage(ListPacketNamesRequest)

ListPacketNamesResponse = _reflection.GeneratedProtocolMessageType('ListPacketNamesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKETNAMESRESPONSE,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ListPacketNamesResponse)
  ))
_sym_db.RegisterMessage(ListPacketNamesResponse)

ListPacketsRequest = _reflection.GeneratedProtocolMessageType('ListPacketsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKETSREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ListPacketsRequest)
  ))
_sym_db.RegisterMessage(ListPacketsRequest)

ListPacketsResponse = _reflection.GeneratedProtocolMessageType('ListPacketsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPACKETSRESPONSE,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ListPacketsResponse)
  ))
_sym_db.RegisterMessage(ListPacketsResponse)

GetPacketRequest = _reflection.GeneratedProtocolMessageType('GetPacketRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPACKETREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.GetPacketRequest)
  ))
_sym_db.RegisterMessage(GetPacketRequest)

StreamPacketsRequest = _reflection.GeneratedProtocolMessageType('StreamPacketsRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMPACKETSREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.StreamPacketsRequest)
  ))
_sym_db.RegisterMessage(StreamPacketsRequest)

ExportPacketRequest = _reflection.GeneratedProtocolMessageType('ExportPacketRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTPACKETREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ExportPacketRequest)
  ))
_sym_db.RegisterMessage(ExportPacketRequest)

ExportPacketsRequest = _reflection.GeneratedProtocolMessageType('ExportPacketsRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTPACKETSREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ExportPacketsRequest)
  ))
_sym_db.RegisterMessage(ExportPacketsRequest)

SubscribePacketsRequest = _reflection.GeneratedProtocolMessageType('SubscribePacketsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEPACKETSREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.SubscribePacketsRequest)
  ))
_sym_db.RegisterMessage(SubscribePacketsRequest)

SubscribeContainersRequest = _reflection.GeneratedProtocolMessageType('SubscribeContainersRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBECONTAINERSREQUEST,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.SubscribeContainersRequest)
  ))
_sym_db.RegisterMessage(SubscribeContainersRequest)

ContainerData = _reflection.GeneratedProtocolMessageType('ContainerData', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERDATA,
  __module__ = 'yamcs.protobuf.packets.packets_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.packets.ContainerData)
  ))
_sym_db.RegisterMessage(ContainerData)


DESCRIPTOR._options = None

_PACKETSAPI = _descriptor.ServiceDescriptor(
  name='PacketsApi',
  full_name='yamcs.protobuf.packets.PacketsApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1365,
  serialized_end=2508,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListPacketNames',
    full_name='yamcs.protobuf.packets.PacketsApi.ListPacketNames',
    index=0,
    containing_service=None,
    input_type=_LISTPACKETNAMESREQUEST,
    output_type=_LISTPACKETNAMESRESPONSE,
    serialized_options=_b('\212\222\003&\n$/api/archive/{instance}/packet-names'),
  ),
  _descriptor.MethodDescriptor(
    name='ListPackets',
    full_name='yamcs.protobuf.packets.PacketsApi.ListPackets',
    index=1,
    containing_service=None,
    input_type=_LISTPACKETSREQUEST,
    output_type=_LISTPACKETSRESPONSE,
    serialized_options=_b('\212\222\003!\n\037/api/archive/{instance}/packets'),
  ),
  _descriptor.MethodDescriptor(
    name='GetPacket',
    full_name='yamcs.protobuf.packets.PacketsApi.GetPacket',
    index=2,
    containing_service=None,
    input_type=_GETPACKETREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._TMPACKETDATA,
    serialized_options=_b('\212\222\0034\n2/api/archive/{instance}/packets/{gentime}/{seqnum}'),
  ),
  _descriptor.MethodDescriptor(
    name='StreamPackets',
    full_name='yamcs.protobuf.packets.PacketsApi.StreamPackets',
    index=3,
    containing_service=None,
    input_type=_STREAMPACKETSREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._TMPACKETDATA,
    serialized_options=_b('\212\222\0031\032,/api/stream-archive/{instance}:streamPackets:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ExportPacket',
    full_name='yamcs.protobuf.packets.PacketsApi.ExportPacket',
    index=4,
    containing_service=None,
    input_type=_EXPORTPACKETREQUEST,
    output_type=yamcs_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=_b('\212\222\003;\n9/api/archive/{instance}/packets/{gentime}/{seqnum}:export'),
  ),
  _descriptor.MethodDescriptor(
    name='ExportPackets',
    full_name='yamcs.protobuf.packets.PacketsApi.ExportPackets',
    index=5,
    containing_service=None,
    input_type=_EXPORTPACKETSREQUEST,
    output_type=yamcs_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=_b('\212\222\003\'\n%/api/archive/{instance}:exportPackets'),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribePackets',
    full_name='yamcs.protobuf.packets.PacketsApi.SubscribePackets',
    index=6,
    containing_service=None,
    input_type=_SUBSCRIBEPACKETSREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._TMPACKETDATA,
    serialized_options=_b('\332\222\003\t\n\007packets'),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeContainers',
    full_name='yamcs.protobuf.packets.PacketsApi.SubscribeContainers',
    index=7,
    containing_service=None,
    input_type=_SUBSCRIBECONTAINERSREQUEST,
    output_type=_CONTAINERDATA,
    serialized_options=_b('\332\222\003\014\n\ncontainers'),
  ),
])
_sym_db.RegisterServiceDescriptor(_PACKETSAPI)

DESCRIPTOR.services_by_name['PacketsApi'] = _PACKETSAPI

# @@protoc_insertion_point(module_scope)