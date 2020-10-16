# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/archive/tag_service.proto

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
from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/archive/tag_service.proto',
  package='yamcs.protobuf.web',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\017TagServiceProtoP\001'),
  serialized_pb=_b('\n(yamcs/protobuf/archive/tag_service.proto\x12\x12yamcs.protobuf.web\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a\x1ayamcs/protobuf/yamcs.proto\"x\n\x0fListTagsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04stop\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\x10ListTagsResponse\x12\'\n\x03tag\x18\x01 \x03(\x0b\x32\x1a.yamcs.protobuf.ArchiveTag\"A\n\rGetTagRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07tagTime\x18\x02 \x01(\x03\x12\r\n\x05tagId\x18\x03 \x01(\x05\"s\n\x10\x43reateTagRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\t\x12\x0c\n\x04stop\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\r\n\x05\x63olor\x18\x06 \x01(\t\"\x91\x01\n\x0e\x45\x64itTagRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07tagTime\x18\x02 \x01(\x03\x12\r\n\x05tagId\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\t\x12\x0c\n\x04stop\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\r\n\x05\x63olor\x18\x08 \x01(\t\"D\n\x10\x44\x65leteTagRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07tagTime\x18\x02 \x01(\x03\x12\r\n\x05tagId\x18\x03 \x01(\x05\x32\xba\x05\n\x06TagApi\x12y\n\x08ListTags\x12#.yamcs.protobuf.web.ListTagsRequest\x1a$.yamcs.protobuf.web.ListTagsResponse\"\"\x8a\x92\x03\x1e\n\x1c/api/archive/{instance}/tags\x12}\n\x06GetTag\x12!.yamcs.protobuf.web.GetTagRequest\x1a\x1a.yamcs.protobuf.ArchiveTag\"4\x8a\x92\x03\x30\n./api/archive/{instance}/tags/{tagTime}/{tagId}\x12t\n\tCreateTag\x12$.yamcs.protobuf.web.CreateTagRequest\x1a\x1a.yamcs.protobuf.ArchiveTag\"%\x8a\x92\x03!\x1a\x1c/api/archive/{instance}/tags:\x01*\x12\xb9\x01\n\tUpdateTag\x12\".yamcs.protobuf.web.EditTagRequest\x1a\x1a.yamcs.protobuf.ArchiveTag\"l\x8a\x92\x03h*./api/archive/{instance}/tags/{tagTime}/{tagId}:\x01*Z3\x12./api/archive/{instance}/tags/{tagTime}/{tagId}:\x01*\x12\x83\x01\n\tDeleteTag\x12$.yamcs.protobuf.web.DeleteTagRequest\x1a\x1a.yamcs.protobuf.ArchiveTag\"4\x8a\x92\x03\x30\"./api/archive/{instance}/tags/{tagTime}/{tagId}B\'\n\x12org.yamcs.protobufB\x0fTagServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,])




_LISTTAGSREQUEST = _descriptor.Descriptor(
  name='ListTagsRequest',
  full_name='yamcs.protobuf.web.ListTagsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.web.ListTagsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.web.ListTagsRequest.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.web.ListTagsRequest.stop', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=154,
  serialized_end=274,
)


_LISTTAGSRESPONSE = _descriptor.Descriptor(
  name='ListTagsResponse',
  full_name='yamcs.protobuf.web.ListTagsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='yamcs.protobuf.web.ListTagsResponse.tag', index=0,
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
  serialized_start=276,
  serialized_end=335,
)


_GETTAGREQUEST = _descriptor.Descriptor(
  name='GetTagRequest',
  full_name='yamcs.protobuf.web.GetTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.web.GetTagRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagTime', full_name='yamcs.protobuf.web.GetTagRequest.tagTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagId', full_name='yamcs.protobuf.web.GetTagRequest.tagId', index=2,
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
  serialized_start=337,
  serialized_end=402,
)


_CREATETAGREQUEST = _descriptor.Descriptor(
  name='CreateTagRequest',
  full_name='yamcs.protobuf.web.CreateTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.web.CreateTagRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.web.CreateTagRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.web.CreateTagRequest.start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.web.CreateTagRequest.stop', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yamcs.protobuf.web.CreateTagRequest.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='yamcs.protobuf.web.CreateTagRequest.color', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=404,
  serialized_end=519,
)


_EDITTAGREQUEST = _descriptor.Descriptor(
  name='EditTagRequest',
  full_name='yamcs.protobuf.web.EditTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.web.EditTagRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagTime', full_name='yamcs.protobuf.web.EditTagRequest.tagTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagId', full_name='yamcs.protobuf.web.EditTagRequest.tagId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.web.EditTagRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='yamcs.protobuf.web.EditTagRequest.start', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='yamcs.protobuf.web.EditTagRequest.stop', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yamcs.protobuf.web.EditTagRequest.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='yamcs.protobuf.web.EditTagRequest.color', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=522,
  serialized_end=667,
)


_DELETETAGREQUEST = _descriptor.Descriptor(
  name='DeleteTagRequest',
  full_name='yamcs.protobuf.web.DeleteTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.web.DeleteTagRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagTime', full_name='yamcs.protobuf.web.DeleteTagRequest.tagTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagId', full_name='yamcs.protobuf.web.DeleteTagRequest.tagId', index=2,
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
  serialized_start=669,
  serialized_end=737,
)

_LISTTAGSREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTAGSREQUEST.fields_by_name['stop'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTAGSRESPONSE.fields_by_name['tag'].message_type = yamcs_dot_protobuf_dot_yamcs__pb2._ARCHIVETAG
DESCRIPTOR.message_types_by_name['ListTagsRequest'] = _LISTTAGSREQUEST
DESCRIPTOR.message_types_by_name['ListTagsResponse'] = _LISTTAGSRESPONSE
DESCRIPTOR.message_types_by_name['GetTagRequest'] = _GETTAGREQUEST
DESCRIPTOR.message_types_by_name['CreateTagRequest'] = _CREATETAGREQUEST
DESCRIPTOR.message_types_by_name['EditTagRequest'] = _EDITTAGREQUEST
DESCRIPTOR.message_types_by_name['DeleteTagRequest'] = _DELETETAGREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTagsRequest = _reflection.GeneratedProtocolMessageType('ListTagsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTAGSREQUEST,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.ListTagsRequest)
  ))
_sym_db.RegisterMessage(ListTagsRequest)

ListTagsResponse = _reflection.GeneratedProtocolMessageType('ListTagsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTAGSRESPONSE,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.ListTagsResponse)
  ))
_sym_db.RegisterMessage(ListTagsResponse)

GetTagRequest = _reflection.GeneratedProtocolMessageType('GetTagRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTAGREQUEST,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.GetTagRequest)
  ))
_sym_db.RegisterMessage(GetTagRequest)

CreateTagRequest = _reflection.GeneratedProtocolMessageType('CreateTagRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATETAGREQUEST,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.CreateTagRequest)
  ))
_sym_db.RegisterMessage(CreateTagRequest)

EditTagRequest = _reflection.GeneratedProtocolMessageType('EditTagRequest', (_message.Message,), dict(
  DESCRIPTOR = _EDITTAGREQUEST,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.EditTagRequest)
  ))
_sym_db.RegisterMessage(EditTagRequest)

DeleteTagRequest = _reflection.GeneratedProtocolMessageType('DeleteTagRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETETAGREQUEST,
  __module__ = 'yamcs.protobuf.archive.tag_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.DeleteTagRequest)
  ))
_sym_db.RegisterMessage(DeleteTagRequest)


DESCRIPTOR._options = None

_TAGAPI = _descriptor.ServiceDescriptor(
  name='TagApi',
  full_name='yamcs.protobuf.web.TagApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=740,
  serialized_end=1438,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListTags',
    full_name='yamcs.protobuf.web.TagApi.ListTags',
    index=0,
    containing_service=None,
    input_type=_LISTTAGSREQUEST,
    output_type=_LISTTAGSRESPONSE,
    serialized_options=_b('\212\222\003\036\n\034/api/archive/{instance}/tags'),
  ),
  _descriptor.MethodDescriptor(
    name='GetTag',
    full_name='yamcs.protobuf.web.TagApi.GetTag',
    index=1,
    containing_service=None,
    input_type=_GETTAGREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._ARCHIVETAG,
    serialized_options=_b('\212\222\0030\n./api/archive/{instance}/tags/{tagTime}/{tagId}'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateTag',
    full_name='yamcs.protobuf.web.TagApi.CreateTag',
    index=2,
    containing_service=None,
    input_type=_CREATETAGREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._ARCHIVETAG,
    serialized_options=_b('\212\222\003!\032\034/api/archive/{instance}/tags:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTag',
    full_name='yamcs.protobuf.web.TagApi.UpdateTag',
    index=3,
    containing_service=None,
    input_type=_EDITTAGREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._ARCHIVETAG,
    serialized_options=_b('\212\222\003h*./api/archive/{instance}/tags/{tagTime}/{tagId}:\001*Z3\022./api/archive/{instance}/tags/{tagTime}/{tagId}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTag',
    full_name='yamcs.protobuf.web.TagApi.DeleteTag',
    index=4,
    containing_service=None,
    input_type=_DELETETAGREQUEST,
    output_type=yamcs_dot_protobuf_dot_yamcs__pb2._ARCHIVETAG,
    serialized_options=_b('\212\222\0030\"./api/archive/{instance}/tags/{tagTime}/{tagId}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_TAGAPI)

DESCRIPTOR.services_by_name['TagApi'] = _TAGAPI

# @@protoc_insertion_point(module_scope)
