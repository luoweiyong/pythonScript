# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServerRoleService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ServerCommonMessage_pb2 as ServerCommonMessage__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from google.protobuf.timestamp_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServerRoleService.proto',
  package='platformserver',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17ServerRoleService.proto\x12\x0eplatformserver\x1a\x19ServerCommonMessage.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"-\n\x0fRoleSaveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\"-\n\x11RoleUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1f\n\x11RoleDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x11RoleSearchRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\"#\n\x13\x46indAllRolesRequest\x12\x0c\n\x04type\x18\x01 \x01(\x05\"\xdc\x01\n\x12\x46indAllRolesResult\x12\x35\n\x04role\x18\x01 \x03(\x0b\x32\'.platformserver.FindAllRolesResult.Role\x1a\x8e\x01\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12.\n\ncreateTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdateTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"B\n\x1b\x41ssociationPrivilegeRequest\x12\x13\n\x0bprivilegeId\x18\x01 \x01(\t\x12\x0e\n\x06roleId\x18\x02 \x01(\t\"+\n\x1dUnAssociationPrivilegeRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xbc\x04\n\x11ServerRoleService\x12\x41\n\x04save\x12\x1f.platformserver.RoleSaveRequest\x1a\x18.platformserver.Response\x12\x45\n\x06update\x12!.platformserver.RoleUpdateRequest\x1a\x18.platformserver.Response\x12\x45\n\x06\x64\x65lete\x12!.platformserver.RoleDeleteRequest\x1a\x18.platformserver.Response\x12\x45\n\x06search\x12!.platformserver.RoleSearchRequest\x1a\x18.platformserver.Response\x12]\n\x14\x61ssociationPrivilege\x12+.platformserver.AssociationPrivilegeRequest\x1a\x18.platformserver.Response\x12\x61\n\x16unAssociationPrivilege\x12-.platformserver.UnAssociationPrivilegeRequest\x1a\x18.platformserver.Response\x12M\n\x0c\x66indAllRoles\x12#.platformserver.FindAllRolesRequest\x1a\x18.platformserver.ResponseP\x01\x62\x06proto3')
  ,
  dependencies=[ServerCommonMessage__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,],
  public_dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ROLESAVEREQUEST = _descriptor.Descriptor(
  name='RoleSaveRequest',
  full_name='platformserver.RoleSaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.RoleSaveRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.RoleSaveRequest.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=148,
)


_ROLEUPDATEREQUEST = _descriptor.Descriptor(
  name='RoleUpdateRequest',
  full_name='platformserver.RoleUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.RoleUpdateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.RoleUpdateRequest.name', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=195,
)


_ROLEDELETEREQUEST = _descriptor.Descriptor(
  name='RoleDeleteRequest',
  full_name='platformserver.RoleDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.RoleDeleteRequest.id', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=228,
)


_ROLESEARCHREQUEST = _descriptor.Descriptor(
  name='RoleSearchRequest',
  full_name='platformserver.RoleSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.RoleSearchRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.RoleSearchRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.RoleSearchRequest.type', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=289,
)


_FINDALLROLESREQUEST = _descriptor.Descriptor(
  name='FindAllRolesRequest',
  full_name='platformserver.FindAllRolesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindAllRolesRequest.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=326,
)


_FINDALLROLESRESULT_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='platformserver.FindAllRolesResult.Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.FindAllRolesResult.Role.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.FindAllRolesResult.Role.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.FindAllRolesResult.Role.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='platformserver.FindAllRolesResult.Role.createTime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='platformserver.FindAllRolesResult.Role.updateTime', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=549,
)

_FINDALLROLESRESULT = _descriptor.Descriptor(
  name='FindAllRolesResult',
  full_name='platformserver.FindAllRolesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='platformserver.FindAllRolesResult.role', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDALLROLESRESULT_ROLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=549,
)


_ASSOCIATIONPRIVILEGEREQUEST = _descriptor.Descriptor(
  name='AssociationPrivilegeRequest',
  full_name='platformserver.AssociationPrivilegeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='privilegeId', full_name='platformserver.AssociationPrivilegeRequest.privilegeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleId', full_name='platformserver.AssociationPrivilegeRequest.roleId', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=617,
)


_UNASSOCIATIONPRIVILEGEREQUEST = _descriptor.Descriptor(
  name='UnAssociationPrivilegeRequest',
  full_name='platformserver.UnAssociationPrivilegeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.UnAssociationPrivilegeRequest.id', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=662,
)

_FINDALLROLESRESULT_ROLE.fields_by_name['createTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDALLROLESRESULT_ROLE.fields_by_name['updateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FINDALLROLESRESULT_ROLE.containing_type = _FINDALLROLESRESULT
_FINDALLROLESRESULT.fields_by_name['role'].message_type = _FINDALLROLESRESULT_ROLE
DESCRIPTOR.message_types_by_name['RoleSaveRequest'] = _ROLESAVEREQUEST
DESCRIPTOR.message_types_by_name['RoleUpdateRequest'] = _ROLEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['RoleDeleteRequest'] = _ROLEDELETEREQUEST
DESCRIPTOR.message_types_by_name['RoleSearchRequest'] = _ROLESEARCHREQUEST
DESCRIPTOR.message_types_by_name['FindAllRolesRequest'] = _FINDALLROLESREQUEST
DESCRIPTOR.message_types_by_name['FindAllRolesResult'] = _FINDALLROLESRESULT
DESCRIPTOR.message_types_by_name['AssociationPrivilegeRequest'] = _ASSOCIATIONPRIVILEGEREQUEST
DESCRIPTOR.message_types_by_name['UnAssociationPrivilegeRequest'] = _UNASSOCIATIONPRIVILEGEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleSaveRequest = _reflection.GeneratedProtocolMessageType('RoleSaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROLESAVEREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.RoleSaveRequest)
  ))
_sym_db.RegisterMessage(RoleSaveRequest)

RoleUpdateRequest = _reflection.GeneratedProtocolMessageType('RoleUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROLEUPDATEREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.RoleUpdateRequest)
  ))
_sym_db.RegisterMessage(RoleUpdateRequest)

RoleDeleteRequest = _reflection.GeneratedProtocolMessageType('RoleDeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROLEDELETEREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.RoleDeleteRequest)
  ))
_sym_db.RegisterMessage(RoleDeleteRequest)

RoleSearchRequest = _reflection.GeneratedProtocolMessageType('RoleSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROLESEARCHREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.RoleSearchRequest)
  ))
_sym_db.RegisterMessage(RoleSearchRequest)

FindAllRolesRequest = _reflection.GeneratedProtocolMessageType('FindAllRolesRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDALLROLESREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindAllRolesRequest)
  ))
_sym_db.RegisterMessage(FindAllRolesRequest)

FindAllRolesResult = _reflection.GeneratedProtocolMessageType('FindAllRolesResult', (_message.Message,), dict(

  Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), dict(
    DESCRIPTOR = _FINDALLROLESRESULT_ROLE,
    __module__ = 'ServerRoleService_pb2'
    # @@protoc_insertion_point(class_scope:platformserver.FindAllRolesResult.Role)
    ))
  ,
  DESCRIPTOR = _FINDALLROLESRESULT,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.FindAllRolesResult)
  ))
_sym_db.RegisterMessage(FindAllRolesResult)
_sym_db.RegisterMessage(FindAllRolesResult.Role)

AssociationPrivilegeRequest = _reflection.GeneratedProtocolMessageType('AssociationPrivilegeRequest', (_message.Message,), dict(
  DESCRIPTOR = _ASSOCIATIONPRIVILEGEREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.AssociationPrivilegeRequest)
  ))
_sym_db.RegisterMessage(AssociationPrivilegeRequest)

UnAssociationPrivilegeRequest = _reflection.GeneratedProtocolMessageType('UnAssociationPrivilegeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNASSOCIATIONPRIVILEGEREQUEST,
  __module__ = 'ServerRoleService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.UnAssociationPrivilegeRequest)
  ))
_sym_db.RegisterMessage(UnAssociationPrivilegeRequest)



_SERVERROLESERVICE = _descriptor.ServiceDescriptor(
  name='ServerRoleService',
  full_name='platformserver.ServerRoleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=665,
  serialized_end=1237,
  methods=[
  _descriptor.MethodDescriptor(
    name='save',
    full_name='platformserver.ServerRoleService.save',
    index=0,
    containing_service=None,
    input_type=_ROLESAVEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='platformserver.ServerRoleService.update',
    index=1,
    containing_service=None,
    input_type=_ROLEUPDATEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='platformserver.ServerRoleService.delete',
    index=2,
    containing_service=None,
    input_type=_ROLEDELETEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='search',
    full_name='platformserver.ServerRoleService.search',
    index=3,
    containing_service=None,
    input_type=_ROLESEARCHREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='associationPrivilege',
    full_name='platformserver.ServerRoleService.associationPrivilege',
    index=4,
    containing_service=None,
    input_type=_ASSOCIATIONPRIVILEGEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unAssociationPrivilege',
    full_name='platformserver.ServerRoleService.unAssociationPrivilege',
    index=5,
    containing_service=None,
    input_type=_UNASSOCIATIONPRIVILEGEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='findAllRoles',
    full_name='platformserver.ServerRoleService.findAllRoles',
    index=6,
    containing_service=None,
    input_type=_FINDALLROLESREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERROLESERVICE)

DESCRIPTOR.services_by_name['ServerRoleService'] = _SERVERROLESERVICE

# @@protoc_insertion_point(module_scope)