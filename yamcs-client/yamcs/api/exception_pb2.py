# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/api/exception.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/api/exception.proto',
  package='yamcs.api',
  syntax='proto3',
  serialized_options=b'\n\rorg.yamcs.apiB\016ExceptionProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19yamcs/api/exception.proto\x12\tyamcs.api\x1a\x19google/protobuf/any.proto\"a\n\x10\x45xceptionMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12$\n\x06\x64\x65tail\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyB!\n\rorg.yamcs.apiB\x0e\x45xceptionProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_EXCEPTIONMESSAGE = _descriptor.Descriptor(
  name='ExceptionMessage',
  full_name='yamcs.api.ExceptionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='yamcs.api.ExceptionMessage.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.api.ExceptionMessage.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='yamcs.api.ExceptionMessage.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='yamcs.api.ExceptionMessage.detail', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=164,
)

_EXCEPTIONMESSAGE.fields_by_name['detail'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['ExceptionMessage'] = _EXCEPTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExceptionMessage = _reflection.GeneratedProtocolMessageType('ExceptionMessage', (_message.Message,), {
  'DESCRIPTOR' : _EXCEPTIONMESSAGE,
  '__module__' : 'yamcs.api.exception_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.api.ExceptionMessage)
  })
_sym_db.RegisterMessage(ExceptionMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
