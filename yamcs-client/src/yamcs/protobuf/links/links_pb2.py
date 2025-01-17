# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/links/links.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/links/links.proto',
  package='yamcs.protobuf.links',
  syntax='proto2',
  serialized_options=_b('\n\030org.yamcs.protobuf.linksB\021LinksServiceProtoP\001'),
  serialized_pb=_b('\n yamcs/protobuf/links/links.proto\x12\x14yamcs.protobuf.links\x1a\x1byamcs/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\"$\n\x10ListLinksRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\"B\n\x11ListLinksResponse\x12-\n\x05links\x18\x01 \x03(\x0b\x32\x1e.yamcs.protobuf.links.LinkInfo\"0\n\x0eGetLinkRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\"3\n\x11\x45nableLinkRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\"4\n\x12\x44isableLinkRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\":\n\x18ResetLinkCountersRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\"W\n\x0f\x45\x64itLinkRequest\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12\r\n\x05state\x18\x01 \x01(\t\x12\x15\n\rresetCounters\x18\x02 \x01(\x08\"l\n\x10RunActionRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12(\n\x07message\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xef\x01\n\tLinkEvent\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32$.yamcs.protobuf.links.LinkEvent.TypeB\x02\x18\x01\x12\x34\n\x08linkInfo\x18\x02 \x01(\x0b\x32\x1e.yamcs.protobuf.links.LinkInfoB\x02\x18\x01\x12-\n\x05links\x18\x03 \x03(\x0b\x32\x1e.yamcs.protobuf.links.LinkInfo\"E\n\x04Type\x12\x0e\n\nREGISTERED\x10\x01\x12\x10\n\x0cUNREGISTERED\x10\x02\x12\x0b\n\x07UPDATED\x10\x03\x12\x0e\n\nUPDATE_ALL\x10\x04\")\n\x15SubscribeLinksRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\"\xbe\x02\n\x08LinkInfo\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04spec\x18\x04 \x01(\t\x12\x10\n\x08\x64isabled\x18\x06 \x01(\x08\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x61taInCount\x18\n \x01(\x03\x12\x14\n\x0c\x64\x61taOutCount\x18\x0b \x01(\x03\x12\x16\n\x0e\x64\x65tailedStatus\x18\t \x01(\t\x12\x12\n\nparentName\x18\x0c \x01(\t\x12\x35\n\x07\x61\x63tions\x18\r \x03(\x0b\x32$.yamcs.protobuf.links.LinkActionInfo\x12&\n\x05\x65xtra\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nparameters\x18\x0f \x03(\tJ\x04\x08\x05\x10\x06J\x04\x08\x08\x10\t\"\\\n\x0eLinkActionInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\r\n\x05style\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0f\n\x07\x63hecked\x18\x05 \x01(\x08\x32\x8b\t\n\x08LinksApi\x12z\n\tListLinks\x12&.yamcs.protobuf.links.ListLinksRequest\x1a\'.yamcs.protobuf.links.ListLinksResponse\"\x1c\x8a\x92\x03\x18\n\x16/api/links/{instance?}\x12s\n\x07GetLink\x12$.yamcs.protobuf.links.GetLinkRequest\x1a\x1e.yamcs.protobuf.links.LinkInfo\"\"\x8a\x92\x03\x1e\n\x1c/api/links/{instance}/{link}\x12\x93\x01\n\nUpdateLink\x12%.yamcs.protobuf.links.EditLinkRequest\x1a\x1e.yamcs.protobuf.links.LinkInfo\">\x8a\x92\x03:*\x1c/api/links/{instance}/{link}0\x01:\x01*b\x15Link \'{link}\' updated\x12\x97\x01\n\nEnableLink\x12\'.yamcs.protobuf.links.EnableLinkRequest\x1a\x1e.yamcs.protobuf.links.LinkInfo\"@\x8a\x92\x03<\x1a#/api/links/{instance}/{link}:enableb\x15Link \'{link}\' enabled\x12\x9b\x01\n\x0b\x44isableLink\x12(.yamcs.protobuf.links.DisableLinkRequest\x1a\x1e.yamcs.protobuf.links.LinkInfo\"B\x8a\x92\x03>\x1a$/api/links/{instance}/{link}:disableb\x16Link \'{link}\' disabled\x12\x95\x01\n\x11ResetLinkCounters\x12..yamcs.protobuf.links.ResetLinkCountersRequest\x1a\x1e.yamcs.protobuf.links.LinkInfo\"0\x8a\x92\x03,\x1a*/api/links/{instance}/{link}:resetCounters\x12m\n\x0eSubscribeLinks\x12+.yamcs.protobuf.links.SubscribeLinksRequest\x1a\x1f.yamcs.protobuf.links.LinkEvent\"\x0b\xda\x92\x03\x07\n\x05links0\x01\x12\xb8\x01\n\tRunAction\x12&.yamcs.protobuf.links.RunActionRequest\x1a\x17.google.protobuf.Struct\"j\x8a\x92\x03\x66\x1a-/api/links/{instance}/{link}/actions/{action}:\x07messageb,Action \'{action}\' performed on link \'{link}\'B/\n\x18org.yamcs.protobuf.linksB\x11LinksServiceProtoP\x01')
  ,
  dependencies=[yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_LINKEVENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yamcs.protobuf.links.LinkEvent.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTERED', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTERED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATED', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_ALL', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=810,
  serialized_end=879,
)
_sym_db.RegisterEnumDescriptor(_LINKEVENT_TYPE)


_LISTLINKSREQUEST = _descriptor.Descriptor(
  name='ListLinksRequest',
  full_name='yamcs.protobuf.links.ListLinksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.ListLinksRequest.instance', index=0,
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
  serialized_start=117,
  serialized_end=153,
)


_LISTLINKSRESPONSE = _descriptor.Descriptor(
  name='ListLinksResponse',
  full_name='yamcs.protobuf.links.ListLinksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='yamcs.protobuf.links.ListLinksResponse.links', index=0,
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
  serialized_start=155,
  serialized_end=221,
)


_GETLINKREQUEST = _descriptor.Descriptor(
  name='GetLinkRequest',
  full_name='yamcs.protobuf.links.GetLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.GetLinkRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.GetLinkRequest.link', index=1,
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
  serialized_start=223,
  serialized_end=271,
)


_ENABLELINKREQUEST = _descriptor.Descriptor(
  name='EnableLinkRequest',
  full_name='yamcs.protobuf.links.EnableLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.EnableLinkRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.EnableLinkRequest.link', index=1,
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
  serialized_start=273,
  serialized_end=324,
)


_DISABLELINKREQUEST = _descriptor.Descriptor(
  name='DisableLinkRequest',
  full_name='yamcs.protobuf.links.DisableLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.DisableLinkRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.DisableLinkRequest.link', index=1,
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
  serialized_start=326,
  serialized_end=378,
)


_RESETLINKCOUNTERSREQUEST = _descriptor.Descriptor(
  name='ResetLinkCountersRequest',
  full_name='yamcs.protobuf.links.ResetLinkCountersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.ResetLinkCountersRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.ResetLinkCountersRequest.link', index=1,
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
  serialized_start=380,
  serialized_end=438,
)


_EDITLINKREQUEST = _descriptor.Descriptor(
  name='EditLinkRequest',
  full_name='yamcs.protobuf.links.EditLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.EditLinkRequest.instance', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.EditLinkRequest.link', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='yamcs.protobuf.links.EditLinkRequest.state', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resetCounters', full_name='yamcs.protobuf.links.EditLinkRequest.resetCounters', index=3,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=440,
  serialized_end=527,
)


_RUNACTIONREQUEST = _descriptor.Descriptor(
  name='RunActionRequest',
  full_name='yamcs.protobuf.links.RunActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.RunActionRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yamcs.protobuf.links.RunActionRequest.link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='yamcs.protobuf.links.RunActionRequest.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='yamcs.protobuf.links.RunActionRequest.message', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=529,
  serialized_end=637,
)


_LINKEVENT = _descriptor.Descriptor(
  name='LinkEvent',
  full_name='yamcs.protobuf.links.LinkEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.protobuf.links.LinkEvent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkInfo', full_name='yamcs.protobuf.links.LinkEvent.linkInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='yamcs.protobuf.links.LinkEvent.links', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LINKEVENT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=879,
)


_SUBSCRIBELINKSREQUEST = _descriptor.Descriptor(
  name='SubscribeLinksRequest',
  full_name='yamcs.protobuf.links.SubscribeLinksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.SubscribeLinksRequest.instance', index=0,
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
  serialized_start=881,
  serialized_end=922,
)


_LINKINFO = _descriptor.Descriptor(
  name='LinkInfo',
  full_name='yamcs.protobuf.links.LinkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.links.LinkInfo.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.links.LinkInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.protobuf.links.LinkInfo.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='yamcs.protobuf.links.LinkInfo.spec', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='yamcs.protobuf.links.LinkInfo.disabled', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yamcs.protobuf.links.LinkInfo.status', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataInCount', full_name='yamcs.protobuf.links.LinkInfo.dataInCount', index=6,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataOutCount', full_name='yamcs.protobuf.links.LinkInfo.dataOutCount', index=7,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detailedStatus', full_name='yamcs.protobuf.links.LinkInfo.detailedStatus', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentName', full_name='yamcs.protobuf.links.LinkInfo.parentName', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='yamcs.protobuf.links.LinkInfo.actions', index=10,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra', full_name='yamcs.protobuf.links.LinkInfo.extra', index=11,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='yamcs.protobuf.links.LinkInfo.parameters', index=12,
      number=15, type=9, cpp_type=9, label=3,
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
  serialized_start=925,
  serialized_end=1243,
)


_LINKACTIONINFO = _descriptor.Descriptor(
  name='LinkActionInfo',
  full_name='yamcs.protobuf.links.LinkActionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.links.LinkActionInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='yamcs.protobuf.links.LinkActionInfo.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='yamcs.protobuf.links.LinkActionInfo.style', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yamcs.protobuf.links.LinkActionInfo.enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checked', full_name='yamcs.protobuf.links.LinkActionInfo.checked', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=1245,
  serialized_end=1337,
)

_LISTLINKSRESPONSE.fields_by_name['links'].message_type = _LINKINFO
_RUNACTIONREQUEST.fields_by_name['message'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LINKEVENT.fields_by_name['type'].enum_type = _LINKEVENT_TYPE
_LINKEVENT.fields_by_name['linkInfo'].message_type = _LINKINFO
_LINKEVENT.fields_by_name['links'].message_type = _LINKINFO
_LINKEVENT_TYPE.containing_type = _LINKEVENT
_LINKINFO.fields_by_name['actions'].message_type = _LINKACTIONINFO
_LINKINFO.fields_by_name['extra'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ListLinksRequest'] = _LISTLINKSREQUEST
DESCRIPTOR.message_types_by_name['ListLinksResponse'] = _LISTLINKSRESPONSE
DESCRIPTOR.message_types_by_name['GetLinkRequest'] = _GETLINKREQUEST
DESCRIPTOR.message_types_by_name['EnableLinkRequest'] = _ENABLELINKREQUEST
DESCRIPTOR.message_types_by_name['DisableLinkRequest'] = _DISABLELINKREQUEST
DESCRIPTOR.message_types_by_name['ResetLinkCountersRequest'] = _RESETLINKCOUNTERSREQUEST
DESCRIPTOR.message_types_by_name['EditLinkRequest'] = _EDITLINKREQUEST
DESCRIPTOR.message_types_by_name['RunActionRequest'] = _RUNACTIONREQUEST
DESCRIPTOR.message_types_by_name['LinkEvent'] = _LINKEVENT
DESCRIPTOR.message_types_by_name['SubscribeLinksRequest'] = _SUBSCRIBELINKSREQUEST
DESCRIPTOR.message_types_by_name['LinkInfo'] = _LINKINFO
DESCRIPTOR.message_types_by_name['LinkActionInfo'] = _LINKACTIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListLinksRequest = _reflection.GeneratedProtocolMessageType('ListLinksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTLINKSREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.ListLinksRequest)
  ))
_sym_db.RegisterMessage(ListLinksRequest)

ListLinksResponse = _reflection.GeneratedProtocolMessageType('ListLinksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTLINKSRESPONSE,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.ListLinksResponse)
  ))
_sym_db.RegisterMessage(ListLinksResponse)

GetLinkRequest = _reflection.GeneratedProtocolMessageType('GetLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETLINKREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.GetLinkRequest)
  ))
_sym_db.RegisterMessage(GetLinkRequest)

EnableLinkRequest = _reflection.GeneratedProtocolMessageType('EnableLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENABLELINKREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.EnableLinkRequest)
  ))
_sym_db.RegisterMessage(EnableLinkRequest)

DisableLinkRequest = _reflection.GeneratedProtocolMessageType('DisableLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISABLELINKREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.DisableLinkRequest)
  ))
_sym_db.RegisterMessage(DisableLinkRequest)

ResetLinkCountersRequest = _reflection.GeneratedProtocolMessageType('ResetLinkCountersRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETLINKCOUNTERSREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.ResetLinkCountersRequest)
  ))
_sym_db.RegisterMessage(ResetLinkCountersRequest)

EditLinkRequest = _reflection.GeneratedProtocolMessageType('EditLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _EDITLINKREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.EditLinkRequest)
  ))
_sym_db.RegisterMessage(EditLinkRequest)

RunActionRequest = _reflection.GeneratedProtocolMessageType('RunActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _RUNACTIONREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.RunActionRequest)
  ))
_sym_db.RegisterMessage(RunActionRequest)

LinkEvent = _reflection.GeneratedProtocolMessageType('LinkEvent', (_message.Message,), dict(
  DESCRIPTOR = _LINKEVENT,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.LinkEvent)
  ))
_sym_db.RegisterMessage(LinkEvent)

SubscribeLinksRequest = _reflection.GeneratedProtocolMessageType('SubscribeLinksRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBELINKSREQUEST,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.SubscribeLinksRequest)
  ))
_sym_db.RegisterMessage(SubscribeLinksRequest)

LinkInfo = _reflection.GeneratedProtocolMessageType('LinkInfo', (_message.Message,), dict(
  DESCRIPTOR = _LINKINFO,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.LinkInfo)
  ))
_sym_db.RegisterMessage(LinkInfo)

LinkActionInfo = _reflection.GeneratedProtocolMessageType('LinkActionInfo', (_message.Message,), dict(
  DESCRIPTOR = _LINKACTIONINFO,
  __module__ = 'yamcs.protobuf.links.links_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.links.LinkActionInfo)
  ))
_sym_db.RegisterMessage(LinkActionInfo)


DESCRIPTOR._options = None
_LINKEVENT.fields_by_name['type']._options = None
_LINKEVENT.fields_by_name['linkInfo']._options = None

_LINKSAPI = _descriptor.ServiceDescriptor(
  name='LinksApi',
  full_name='yamcs.protobuf.links.LinksApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1340,
  serialized_end=2503,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListLinks',
    full_name='yamcs.protobuf.links.LinksApi.ListLinks',
    index=0,
    containing_service=None,
    input_type=_LISTLINKSREQUEST,
    output_type=_LISTLINKSRESPONSE,
    serialized_options=_b('\212\222\003\030\n\026/api/links/{instance?}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetLink',
    full_name='yamcs.protobuf.links.LinksApi.GetLink',
    index=1,
    containing_service=None,
    input_type=_GETLINKREQUEST,
    output_type=_LINKINFO,
    serialized_options=_b('\212\222\003\036\n\034/api/links/{instance}/{link}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateLink',
    full_name='yamcs.protobuf.links.LinksApi.UpdateLink',
    index=2,
    containing_service=None,
    input_type=_EDITLINKREQUEST,
    output_type=_LINKINFO,
    serialized_options=_b('\212\222\003:*\034/api/links/{instance}/{link}0\001:\001*b\025Link \'{link}\' updated'),
  ),
  _descriptor.MethodDescriptor(
    name='EnableLink',
    full_name='yamcs.protobuf.links.LinksApi.EnableLink',
    index=3,
    containing_service=None,
    input_type=_ENABLELINKREQUEST,
    output_type=_LINKINFO,
    serialized_options=_b('\212\222\003<\032#/api/links/{instance}/{link}:enableb\025Link \'{link}\' enabled'),
  ),
  _descriptor.MethodDescriptor(
    name='DisableLink',
    full_name='yamcs.protobuf.links.LinksApi.DisableLink',
    index=4,
    containing_service=None,
    input_type=_DISABLELINKREQUEST,
    output_type=_LINKINFO,
    serialized_options=_b('\212\222\003>\032$/api/links/{instance}/{link}:disableb\026Link \'{link}\' disabled'),
  ),
  _descriptor.MethodDescriptor(
    name='ResetLinkCounters',
    full_name='yamcs.protobuf.links.LinksApi.ResetLinkCounters',
    index=5,
    containing_service=None,
    input_type=_RESETLINKCOUNTERSREQUEST,
    output_type=_LINKINFO,
    serialized_options=_b('\212\222\003,\032*/api/links/{instance}/{link}:resetCounters'),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeLinks',
    full_name='yamcs.protobuf.links.LinksApi.SubscribeLinks',
    index=6,
    containing_service=None,
    input_type=_SUBSCRIBELINKSREQUEST,
    output_type=_LINKEVENT,
    serialized_options=_b('\332\222\003\007\n\005links'),
  ),
  _descriptor.MethodDescriptor(
    name='RunAction',
    full_name='yamcs.protobuf.links.LinksApi.RunAction',
    index=7,
    containing_service=None,
    input_type=_RUNACTIONREQUEST,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=_b('\212\222\003f\032-/api/links/{instance}/{link}/actions/{action}:\007messageb,Action \'{action}\' performed on link \'{link}\''),
  ),
])
_sym_db.RegisterServiceDescriptor(_LINKSAPI)

DESCRIPTOR.services_by_name['LinksApi'] = _LINKSAPI

# @@protoc_insertion_point(module_scope)
