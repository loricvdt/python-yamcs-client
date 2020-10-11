# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/clients/clients.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/clients/clients.proto',
  package='yamcs.protobuf.clients',
  syntax='proto2',
  serialized_options=b'\n\022org.yamcs.protobufB\014ClientsProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$yamcs/protobuf/clients/clients.proto\x12\x16yamcs.protobuf.clients\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1byamcs/api/annotations.proto\"J\n\x13ListClientsResponse\x12\x33\n\x07\x63lients\x18\x01 \x03(\x0b\x32\".yamcs.protobuf.clients.ClientInfo\"\x1e\n\x10GetClientRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"D\n\x11\x45\x64itClientRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x11\n\tprocessor\x18\x03 \x01(\t\"\xa7\x02\n\nClientInfo\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x17\n\x0f\x61pplicationName\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\n \x01(\t\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x15\n\rprocessorName\x18\x05 \x01(\t\x12=\n\x05state\x18\x06 \x01(\x0e\x32..yamcs.protobuf.clients.ClientInfo.ClientState\x12-\n\tloginTime\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\".\n\x0b\x43lientState\x12\r\n\tCONNECTED\x10\x00\x12\x10\n\x0c\x44ISCONNECTED\x10\x01J\x04\x08\x08\x10\tJ\x04\x08\t\x10\n2\xd7\x02\n\nClientsApi\x12\x66\n\x0bListClients\x12\x16.google.protobuf.Empty\x1a+.yamcs.protobuf.clients.ListClientsResponse\"\x12\x8a\x92\x03\x0e\n\x0c/api/clients\x12r\n\tGetClient\x12(.yamcs.protobuf.clients.GetClientRequest\x1a\".yamcs.protobuf.clients.ClientInfo\"\x17\x8a\x92\x03\x13\n\x11/api/clients/{id}\x12m\n\x0cUpdateClient\x12).yamcs.protobuf.clients.EditClientRequest\x1a\x16.google.protobuf.Empty\"\x1a\x8a\x92\x03\x16*\x11/api/clients/{id}:\x01*B$\n\x12org.yamcs.protobufB\x0c\x43lientsProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CLIENTINFO_CLIENTSTATE = _descriptor.EnumDescriptor(
  name='ClientState',
  full_name='yamcs.protobuf.clients.ClientInfo.ClientState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=571,
  serialized_end=617,
)
_sym_db.RegisterEnumDescriptor(_CLIENTINFO_CLIENTSTATE)


_LISTCLIENTSRESPONSE = _descriptor.Descriptor(
  name='ListClientsResponse',
  full_name='yamcs.protobuf.clients.ListClientsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients', full_name='yamcs.protobuf.clients.ListClientsResponse.clients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=155,
  serialized_end=229,
)


_GETCLIENTREQUEST = _descriptor.Descriptor(
  name='GetClientRequest',
  full_name='yamcs.protobuf.clients.GetClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.clients.GetClientRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=231,
  serialized_end=261,
)


_EDITCLIENTREQUEST = _descriptor.Descriptor(
  name='EditClientRequest',
  full_name='yamcs.protobuf.clients.EditClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.clients.EditClientRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.clients.EditClientRequest.instance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processor', full_name='yamcs.protobuf.clients.EditClientRequest.processor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=263,
  serialized_end=331,
)


_CLIENTINFO = _descriptor.Descriptor(
  name='ClientInfo',
  full_name='yamcs.protobuf.clients.ClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.clients.ClientInfo.id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='yamcs.protobuf.clients.ClientInfo.username', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='applicationName', full_name='yamcs.protobuf.clients.ClientInfo.applicationName', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='yamcs.protobuf.clients.ClientInfo.address', index=3,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.clients.ClientInfo.instance', index=4,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processorName', full_name='yamcs.protobuf.clients.ClientInfo.processorName', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='yamcs.protobuf.clients.ClientInfo.state', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loginTime', full_name='yamcs.protobuf.clients.ClientInfo.loginTime', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTINFO_CLIENTSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=629,
)

_LISTCLIENTSRESPONSE.fields_by_name['clients'].message_type = _CLIENTINFO
_CLIENTINFO.fields_by_name['state'].enum_type = _CLIENTINFO_CLIENTSTATE
_CLIENTINFO.fields_by_name['loginTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLIENTINFO_CLIENTSTATE.containing_type = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ListClientsResponse'] = _LISTCLIENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetClientRequest'] = _GETCLIENTREQUEST
DESCRIPTOR.message_types_by_name['EditClientRequest'] = _EDITCLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListClientsResponse = _reflection.GeneratedProtocolMessageType('ListClientsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCLIENTSRESPONSE,
  '__module__' : 'yamcs.protobuf.clients.clients_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.clients.ListClientsResponse)
  })
_sym_db.RegisterMessage(ListClientsResponse)

GetClientRequest = _reflection.GeneratedProtocolMessageType('GetClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTREQUEST,
  '__module__' : 'yamcs.protobuf.clients.clients_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.clients.GetClientRequest)
  })
_sym_db.RegisterMessage(GetClientRequest)

EditClientRequest = _reflection.GeneratedProtocolMessageType('EditClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITCLIENTREQUEST,
  '__module__' : 'yamcs.protobuf.clients.clients_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.clients.EditClientRequest)
  })
_sym_db.RegisterMessage(EditClientRequest)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTINFO,
  '__module__' : 'yamcs.protobuf.clients.clients_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.clients.ClientInfo)
  })
_sym_db.RegisterMessage(ClientInfo)


DESCRIPTOR._options = None

_CLIENTSAPI = _descriptor.ServiceDescriptor(
  name='ClientsApi',
  full_name='yamcs.protobuf.clients.ClientsApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=632,
  serialized_end=975,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListClients',
    full_name='yamcs.protobuf.clients.ClientsApi.ListClients',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTCLIENTSRESPONSE,
    serialized_options=b'\212\222\003\016\n\014/api/clients',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetClient',
    full_name='yamcs.protobuf.clients.ClientsApi.GetClient',
    index=1,
    containing_service=None,
    input_type=_GETCLIENTREQUEST,
    output_type=_CLIENTINFO,
    serialized_options=b'\212\222\003\023\n\021/api/clients/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateClient',
    full_name='yamcs.protobuf.clients.ClientsApi.UpdateClient',
    index=2,
    containing_service=None,
    input_type=_EDITCLIENTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003\026*\021/api/clients/{id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTSAPI)

DESCRIPTOR.services_by_name['ClientsApi'] = _CLIENTSAPI

# @@protoc_insertion_point(module_scope)
