# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/cfdp/cfdp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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
  name='yamcs/protobuf/cfdp/cfdp.proto',
  package='yamcs.protobuf.cfdp',
  syntax='proto2',
  serialized_options=b'\n\022org.yamcs.protobufB\tCfdpProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eyamcs/protobuf/cfdp/cfdp.proto\x12\x13yamcs.protobuf.cfdp\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1byamcs/api/annotations.proto\"@\n\rTransactionId\x12\x16\n\x0esequenceNumber\x18\x01 \x01(\r\x12\x17\n\x0finitiatorEntity\x18\x02 \x01(\x04\"\xff\x02\n\x0cTransferInfo\x12\n\n\x02id\x18\x01 \x01(\r\x12-\n\tstartTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\".yamcs.protobuf.cfdp.TransferState\x12\x0e\n\x06\x62ucket\x18\x04 \x01(\t\x12\x12\n\nobjectName\x18\x05 \x01(\t\x12\x12\n\nremotePath\x18\x06 \x01(\t\x12\x39\n\tdirection\x18\x07 \x01(\x0e\x32&.yamcs.protobuf.cfdp.TransferDirection\x12\x11\n\ttotalSize\x18\x08 \x01(\x04\x12\x17\n\x0fsizeTransferred\x18\t \x01(\x04\x12\x10\n\x08reliable\x18\n \x01(\x08\x12\x15\n\rfailureReason\x18\x0b \x01(\t\x12\x39\n\rtransactionId\x18\x0c \x01(\x0b\x32\".yamcs.protobuf.cfdp.TransactionId\"\x9f\x03\n\x15\x43reateTransferRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x39\n\tdirection\x18\x02 \x01(\x0e\x32&.yamcs.protobuf.cfdp.TransferDirection\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\x12\x12\n\nobjectName\x18\x04 \x01(\t\x12\x12\n\nremotePath\x18\x05 \x01(\t\x12S\n\x0f\x64ownloadOptions\x18\x06 \x01(\x0b\x32:.yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions\x12O\n\ruploadOptions\x18\x07 \x01(\x0b\x32\x38.yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions\x1aH\n\rUploadOptions\x12\x11\n\toverwrite\x18\x01 \x01(\x08\x12\x12\n\ncreatePath\x18\x02 \x01(\x08\x12\x10\n\x08reliable\x18\x03 \x01(\x08\x1a\x11\n\x0f\x44ownloadOptions\"4\n\x14PauseTransferRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"5\n\x15\x43\x61ncelTransferRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"5\n\x15ResumeTransferRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"(\n\x14ListTransfersRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\"2\n\x12GetTransferRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"M\n\x15ListTransfersResponse\x12\x34\n\ttransfers\x18\x01 \x03(\x0b\x32!.yamcs.protobuf.cfdp.TransferInfo\"-\n\x19SubscribeTransfersRequest\x12\x10\n\x08instance\x18\x01 \x01(\t*-\n\x11TransferDirection\x12\n\n\x06UPLOAD\x10\x01\x12\x0c\n\x08\x44OWNLOAD\x10\x02*C\n\rTransferState\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\r\n\tCOMPLETED\x10\x04\x32\xc3\x07\n\x07\x43\x66\x64pApi\x12\x8c\x01\n\rListTransfers\x12).yamcs.protobuf.cfdp.ListTransfersRequest\x1a*.yamcs.protobuf.cfdp.ListTransfersResponse\"$\x8a\x92\x03 \n\x1e/api/cfdp/{instance}/transfers\x12\x84\x01\n\x0bGetTransfer\x12\'.yamcs.protobuf.cfdp.GetTransferRequest\x1a!.yamcs.protobuf.cfdp.TransferInfo\")\x8a\x92\x03%\n#/api/cfdp/{instance}/transfers/{id}\x12\x88\x01\n\x0e\x43reateTransfer\x12*.yamcs.protobuf.cfdp.CreateTransferRequest\x1a!.yamcs.protobuf.cfdp.TransferInfo\"\'\x8a\x92\x03#\x1a\x1e/api/cfdp/{instance}/transfers:\x01*\x12\x83\x01\n\rPauseTransfer\x12).yamcs.protobuf.cfdp.PauseTransferRequest\x1a\x16.google.protobuf.Empty\"/\x8a\x92\x03+\x1a)/api/cfdp/{instance}/transfers/{id}:pause\x12\x86\x01\n\x0e\x43\x61ncelTransfer\x12*.yamcs.protobuf.cfdp.CancelTransferRequest\x1a\x16.google.protobuf.Empty\"0\x8a\x92\x03,\x1a*/api/cfdp/{instance}/transfers/{id}:cancel\x12\x86\x01\n\x0eResumeTransfer\x12*.yamcs.protobuf.cfdp.ResumeTransferRequest\x1a\x16.google.protobuf.Empty\"0\x8a\x92\x03,\x1a*/api/cfdp/{instance}/transfers/{id}:resume\x12\x7f\n\x12SubscribeTransfers\x12..yamcs.protobuf.cfdp.SubscribeTransfersRequest\x1a!.yamcs.protobuf.cfdp.TransferInfo\"\x14\xda\x92\x03\x10\n\x0e\x63\x66\x64p-transfers0\x01\x42!\n\x12org.yamcs.protobufB\tCfdpProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_TRANSFERDIRECTION = _descriptor.EnumDescriptor(
  name='TransferDirection',
  full_name='yamcs.protobuf.cfdp.TransferDirection',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPLOAD', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1400,
  serialized_end=1445,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERDIRECTION)

TransferDirection = enum_type_wrapper.EnumTypeWrapper(_TRANSFERDIRECTION)
_TRANSFERSTATE = _descriptor.EnumDescriptor(
  name='TransferState',
  full_name='yamcs.protobuf.cfdp.TransferState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1447,
  serialized_end=1514,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERSTATE)

TransferState = enum_type_wrapper.EnumTypeWrapper(_TRANSFERSTATE)
UPLOAD = 1
DOWNLOAD = 2
RUNNING = 1
PAUSED = 2
FAILED = 3
COMPLETED = 4



_TRANSACTIONID = _descriptor.Descriptor(
  name='TransactionId',
  full_name='yamcs.protobuf.cfdp.TransactionId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequenceNumber', full_name='yamcs.protobuf.cfdp.TransactionId.sequenceNumber', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initiatorEntity', full_name='yamcs.protobuf.cfdp.TransactionId.initiatorEntity', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=146,
  serialized_end=210,
)


_TRANSFERINFO = _descriptor.Descriptor(
  name='TransferInfo',
  full_name='yamcs.protobuf.cfdp.TransferInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.cfdp.TransferInfo.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='yamcs.protobuf.cfdp.TransferInfo.startTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='yamcs.protobuf.cfdp.TransferInfo.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yamcs.protobuf.cfdp.TransferInfo.bucket', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.cfdp.TransferInfo.objectName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remotePath', full_name='yamcs.protobuf.cfdp.TransferInfo.remotePath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='yamcs.protobuf.cfdp.TransferInfo.direction', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalSize', full_name='yamcs.protobuf.cfdp.TransferInfo.totalSize', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sizeTransferred', full_name='yamcs.protobuf.cfdp.TransferInfo.sizeTransferred', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reliable', full_name='yamcs.protobuf.cfdp.TransferInfo.reliable', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failureReason', full_name='yamcs.protobuf.cfdp.TransferInfo.failureReason', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='yamcs.protobuf.cfdp.TransferInfo.transactionId', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=596,
)


_CREATETRANSFERREQUEST_UPLOADOPTIONS = _descriptor.Descriptor(
  name='UploadOptions',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.overwrite', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createPath', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.createPath', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reliable', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.reliable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=923,
  serialized_end=995,
)

_CREATETRANSFERREQUEST_DOWNLOADOPTIONS = _descriptor.Descriptor(
  name='DownloadOptions',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=997,
  serialized_end=1014,
)

_CREATETRANSFERREQUEST = _descriptor.Descriptor(
  name='CreateTransferRequest',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.objectName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remotePath', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.remotePath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloadOptions', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.downloadOptions', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uploadOptions', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.uploadOptions', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CREATETRANSFERREQUEST_UPLOADOPTIONS, _CREATETRANSFERREQUEST_DOWNLOADOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=1014,
)


_PAUSETRANSFERREQUEST = _descriptor.Descriptor(
  name='PauseTransferRequest',
  full_name='yamcs.protobuf.cfdp.PauseTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.PauseTransferRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.cfdp.PauseTransferRequest.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1016,
  serialized_end=1068,
)


_CANCELTRANSFERREQUEST = _descriptor.Descriptor(
  name='CancelTransferRequest',
  full_name='yamcs.protobuf.cfdp.CancelTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.CancelTransferRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.cfdp.CancelTransferRequest.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1070,
  serialized_end=1123,
)


_RESUMETRANSFERREQUEST = _descriptor.Descriptor(
  name='ResumeTransferRequest',
  full_name='yamcs.protobuf.cfdp.ResumeTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.ResumeTransferRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.cfdp.ResumeTransferRequest.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1125,
  serialized_end=1178,
)


_LISTTRANSFERSREQUEST = _descriptor.Descriptor(
  name='ListTransfersRequest',
  full_name='yamcs.protobuf.cfdp.ListTransfersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.ListTransfersRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1180,
  serialized_end=1220,
)


_GETTRANSFERREQUEST = _descriptor.Descriptor(
  name='GetTransferRequest',
  full_name='yamcs.protobuf.cfdp.GetTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.GetTransferRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.cfdp.GetTransferRequest.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1222,
  serialized_end=1272,
)


_LISTTRANSFERSRESPONSE = _descriptor.Descriptor(
  name='ListTransfersResponse',
  full_name='yamcs.protobuf.cfdp.ListTransfersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transfers', full_name='yamcs.protobuf.cfdp.ListTransfersResponse.transfers', index=0,
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
  serialized_start=1274,
  serialized_end=1351,
)


_SUBSCRIBETRANSFERSREQUEST = _descriptor.Descriptor(
  name='SubscribeTransfersRequest',
  full_name='yamcs.protobuf.cfdp.SubscribeTransfersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.cfdp.SubscribeTransfersRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1353,
  serialized_end=1398,
)

_TRANSFERINFO.fields_by_name['startTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSFERINFO.fields_by_name['state'].enum_type = _TRANSFERSTATE
_TRANSFERINFO.fields_by_name['direction'].enum_type = _TRANSFERDIRECTION
_TRANSFERINFO.fields_by_name['transactionId'].message_type = _TRANSACTIONID
_CREATETRANSFERREQUEST_UPLOADOPTIONS.containing_type = _CREATETRANSFERREQUEST
_CREATETRANSFERREQUEST_DOWNLOADOPTIONS.containing_type = _CREATETRANSFERREQUEST
_CREATETRANSFERREQUEST.fields_by_name['direction'].enum_type = _TRANSFERDIRECTION
_CREATETRANSFERREQUEST.fields_by_name['downloadOptions'].message_type = _CREATETRANSFERREQUEST_DOWNLOADOPTIONS
_CREATETRANSFERREQUEST.fields_by_name['uploadOptions'].message_type = _CREATETRANSFERREQUEST_UPLOADOPTIONS
_LISTTRANSFERSRESPONSE.fields_by_name['transfers'].message_type = _TRANSFERINFO
DESCRIPTOR.message_types_by_name['TransactionId'] = _TRANSACTIONID
DESCRIPTOR.message_types_by_name['TransferInfo'] = _TRANSFERINFO
DESCRIPTOR.message_types_by_name['CreateTransferRequest'] = _CREATETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['PauseTransferRequest'] = _PAUSETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['CancelTransferRequest'] = _CANCELTRANSFERREQUEST
DESCRIPTOR.message_types_by_name['ResumeTransferRequest'] = _RESUMETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['ListTransfersRequest'] = _LISTTRANSFERSREQUEST
DESCRIPTOR.message_types_by_name['GetTransferRequest'] = _GETTRANSFERREQUEST
DESCRIPTOR.message_types_by_name['ListTransfersResponse'] = _LISTTRANSFERSRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeTransfersRequest'] = _SUBSCRIBETRANSFERSREQUEST
DESCRIPTOR.enum_types_by_name['TransferDirection'] = _TRANSFERDIRECTION
DESCRIPTOR.enum_types_by_name['TransferState'] = _TRANSFERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionId = _reflection.GeneratedProtocolMessageType('TransactionId', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONID,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.TransactionId)
  })
_sym_db.RegisterMessage(TransactionId)

TransferInfo = _reflection.GeneratedProtocolMessageType('TransferInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERINFO,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.TransferInfo)
  })
_sym_db.RegisterMessage(TransferInfo)

CreateTransferRequest = _reflection.GeneratedProtocolMessageType('CreateTransferRequest', (_message.Message,), {

  'UploadOptions' : _reflection.GeneratedProtocolMessageType('UploadOptions', (_message.Message,), {
    'DESCRIPTOR' : _CREATETRANSFERREQUEST_UPLOADOPTIONS,
    '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
    # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions)
    })
  ,

  'DownloadOptions' : _reflection.GeneratedProtocolMessageType('DownloadOptions', (_message.Message,), {
    'DESCRIPTOR' : _CREATETRANSFERREQUEST_DOWNLOADOPTIONS,
    '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
    # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions)
    })
  ,
  'DESCRIPTOR' : _CREATETRANSFERREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest)
  })
_sym_db.RegisterMessage(CreateTransferRequest)
_sym_db.RegisterMessage(CreateTransferRequest.UploadOptions)
_sym_db.RegisterMessage(CreateTransferRequest.DownloadOptions)

PauseTransferRequest = _reflection.GeneratedProtocolMessageType('PauseTransferRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSETRANSFERREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.PauseTransferRequest)
  })
_sym_db.RegisterMessage(PauseTransferRequest)

CancelTransferRequest = _reflection.GeneratedProtocolMessageType('CancelTransferRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELTRANSFERREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CancelTransferRequest)
  })
_sym_db.RegisterMessage(CancelTransferRequest)

ResumeTransferRequest = _reflection.GeneratedProtocolMessageType('ResumeTransferRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMETRANSFERREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.ResumeTransferRequest)
  })
_sym_db.RegisterMessage(ResumeTransferRequest)

ListTransfersRequest = _reflection.GeneratedProtocolMessageType('ListTransfersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSFERSREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.ListTransfersRequest)
  })
_sym_db.RegisterMessage(ListTransfersRequest)

GetTransferRequest = _reflection.GeneratedProtocolMessageType('GetTransferRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSFERREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.GetTransferRequest)
  })
_sym_db.RegisterMessage(GetTransferRequest)

ListTransfersResponse = _reflection.GeneratedProtocolMessageType('ListTransfersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSFERSRESPONSE,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.ListTransfersResponse)
  })
_sym_db.RegisterMessage(ListTransfersResponse)

SubscribeTransfersRequest = _reflection.GeneratedProtocolMessageType('SubscribeTransfersRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETRANSFERSREQUEST,
  '__module__' : 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.SubscribeTransfersRequest)
  })
_sym_db.RegisterMessage(SubscribeTransfersRequest)


DESCRIPTOR._options = None

_CFDPAPI = _descriptor.ServiceDescriptor(
  name='CfdpApi',
  full_name='yamcs.protobuf.cfdp.CfdpApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1517,
  serialized_end=2480,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTransfers',
    full_name='yamcs.protobuf.cfdp.CfdpApi.ListTransfers',
    index=0,
    containing_service=None,
    input_type=_LISTTRANSFERSREQUEST,
    output_type=_LISTTRANSFERSRESPONSE,
    serialized_options=b'\212\222\003 \n\036/api/cfdp/{instance}/transfers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransfer',
    full_name='yamcs.protobuf.cfdp.CfdpApi.GetTransfer',
    index=1,
    containing_service=None,
    input_type=_GETTRANSFERREQUEST,
    output_type=_TRANSFERINFO,
    serialized_options=b'\212\222\003%\n#/api/cfdp/{instance}/transfers/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTransfer',
    full_name='yamcs.protobuf.cfdp.CfdpApi.CreateTransfer',
    index=2,
    containing_service=None,
    input_type=_CREATETRANSFERREQUEST,
    output_type=_TRANSFERINFO,
    serialized_options=b'\212\222\003#\032\036/api/cfdp/{instance}/transfers:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PauseTransfer',
    full_name='yamcs.protobuf.cfdp.CfdpApi.PauseTransfer',
    index=3,
    containing_service=None,
    input_type=_PAUSETRANSFERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003+\032)/api/cfdp/{instance}/transfers/{id}:pause',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CancelTransfer',
    full_name='yamcs.protobuf.cfdp.CfdpApi.CancelTransfer',
    index=4,
    containing_service=None,
    input_type=_CANCELTRANSFERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003,\032*/api/cfdp/{instance}/transfers/{id}:cancel',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResumeTransfer',
    full_name='yamcs.protobuf.cfdp.CfdpApi.ResumeTransfer',
    index=5,
    containing_service=None,
    input_type=_RESUMETRANSFERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\212\222\003,\032*/api/cfdp/{instance}/transfers/{id}:resume',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeTransfers',
    full_name='yamcs.protobuf.cfdp.CfdpApi.SubscribeTransfers',
    index=6,
    containing_service=None,
    input_type=_SUBSCRIBETRANSFERSREQUEST,
    output_type=_TRANSFERINFO,
    serialized_options=b'\332\222\003\020\n\016cfdp-transfers',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CFDPAPI)

DESCRIPTOR.services_by_name['CfdpApi'] = _CFDPAPI

# @@protoc_insertion_point(module_scope)
