# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RCCoursewareService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RCCommon_pb2 as RCCommon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RCCoursewareService.proto',
  package='resourcecenter',
  syntax='proto3',
  serialized_options=_b('\n!com.szwdcloud.resource.coursewareB\030RCCoursewareServiceProtoP\001'),
  serialized_pb=_b('\n\x19RCCoursewareService.proto\x12\x0eresourcecenter\x1a\x0eRCCommon.proto\"o\n\x10\x43oursewarePageVo\x12\x14\n\x0c\x63oursewareId\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tcontentId\x18\x03 \x01(\t\x12\x13\n\x0b\x63ontentType\x18\x04 \x01(\x05\x12\x0f\n\x07pageNum\x18\x05 \x01(\x05\"\x83\x01\n\x13ReqInsertCourseware\x12\x11\n\tteacherId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ncustomerId\x18\x03 \x01(\x03\x12\x11\n\teditionId\x18\x04 \x01(\x05\x12\x12\n\nchapterIds\x18\x05 \x03(\x05\x12\x10\n\x08pointIds\x18\x06 \x03(\x05\"\x9c\x01\n\x0c\x43oursewareVo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tteacherId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\ncustomerId\x18\x04 \x01(\x03\x12\x11\n\tsubjectId\x18\x05 \x01(\x05\x12\x11\n\teditionId\x18\x06 \x01(\x05\x12\x12\n\nisBoutique\x18\x07 \x01(\x05\x12\x11\n\tpageCount\x18\x08 \x01(\x05\".\n\x13ReqCoursewareIsJing\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\x05\"\xcd\x01\n\x11ReqCoursewareList\x12\x12\n\nisBoutique\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tsubjectId\x18\x03 \x01(\x05\x12\x18\n\x10\x65\x64itionVersionId\x18\x04 \x01(\x05\x12\x0f\n\x07stageId\x18\x05 \x01(\x05\x12\x0f\n\x07gradeId\x18\x06 \x01(\x05\x12\x12\n\nfascicleId\x18\x07 \x01(\x05\x12\x11\n\torderType\x18\x08 \x01(\x05\x12\x0e\n\x06pageNo\x18\t \x01(\x05\x12\x10\n\x08pageSize\x18\n \x01(\x05\"\xbf\x02\n\x10\x43oursewareItemVo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpageCount\x18\x02 \x01(\x05\x12\x12\n\nisBoutique\x18\x03 \x01(\x05\x12\x1a\n\x12\x65\x64itionVersionName\x18\x04 \x01(\t\x12\x11\n\tgradeName\x18\x05 \x01(\t\x12\x13\n\x0bsubjectName\x18\x06 \x01(\t\x12\x16\n\x0e\x63oursewareName\x18\x07 \x01(\t\x12\r\n\x05stage\x18\x08 \x01(\t\x12\x10\n\x08\x66\x61scicle\x18\t \x01(\t\x12\x13\n\x0b\x63hapterName\x18\n \x03(\t\x12\x11\n\tpointName\x18\x0b \x03(\t\x12\x12\n\nupdateTime\x18\x0c \x01(\t\x12\x16\n\x0ereferenceCount\x18\r \x01(\x05\x12\x12\n\nschoolName\x18\x0e \x01(\t\x12\x13\n\x0bteacherName\x18\x0f \x01(\t\"\xa4\x01\n\x16ResponseCoursewareList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05total\x18\x03 \x01(\x03\x12\r\n\x05pages\x18\x04 \x01(\x05\x12\x0e\n\x06pageNo\x18\x05 \x01(\x05\x12\x10\n\x08pageSize\x18\x06 \x01(\x05\x12/\n\x05\x64\x61tas\x18\x07 \x03(\x0b\x32 .resourcecenter.CoursewareItemVo2\xa5\x04\n\x13RCCoursewareService\x12T\n\x10insertCourseware\x12#.resourcecenter.ReqInsertCourseware\x1a\x19.resourcecenter.EmptyResp\"\x00\x12T\n\x10isJingCourseware\x12#.resourcecenter.ReqCoursewareIsJing\x1a\x19.resourcecenter.EmptyResp\"\x00\x12U\n\x14insertCoursewarePage\x12 .resourcecenter.CoursewarePageVo\x1a\x19.resourcecenter.EmptyResp\"\x00\x12U\n\x14updateCoursewarePage\x12 .resourcecenter.CoursewarePageVo\x1a\x19.resourcecenter.EmptyResp\"\x00\x12U\n\x14\x64\x65leteCoursewarePage\x12 .resourcecenter.CoursewarePageVo\x1a\x19.resourcecenter.EmptyResp\"\x00\x12]\n\x0elistCourseware\x12!.resourcecenter.ReqCoursewareList\x1a&.resourcecenter.ResponseCoursewareList\"\x00\x42?\n!com.szwdcloud.resource.coursewareB\x18RCCoursewareServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[RCCommon__pb2.DESCRIPTOR,])




_COURSEWAREPAGEVO = _descriptor.Descriptor(
  name='CoursewarePageVo',
  full_name='resourcecenter.CoursewarePageVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coursewareId', full_name='resourcecenter.CoursewarePageVo.coursewareId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='resourcecenter.CoursewarePageVo.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentId', full_name='resourcecenter.CoursewarePageVo.contentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentType', full_name='resourcecenter.CoursewarePageVo.contentType', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNum', full_name='resourcecenter.CoursewarePageVo.pageNum', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=61,
  serialized_end=172,
)


_REQINSERTCOURSEWARE = _descriptor.Descriptor(
  name='ReqInsertCourseware',
  full_name='resourcecenter.ReqInsertCourseware',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teacherId', full_name='resourcecenter.ReqInsertCourseware.teacherId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='resourcecenter.ReqInsertCourseware.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customerId', full_name='resourcecenter.ReqInsertCourseware.customerId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editionId', full_name='resourcecenter.ReqInsertCourseware.editionId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapterIds', full_name='resourcecenter.ReqInsertCourseware.chapterIds', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointIds', full_name='resourcecenter.ReqInsertCourseware.pointIds', index=5,
      number=6, type=5, cpp_type=1, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=306,
)


_COURSEWAREVO = _descriptor.Descriptor(
  name='CoursewareVo',
  full_name='resourcecenter.CoursewareVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resourcecenter.CoursewareVo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teacherId', full_name='resourcecenter.CoursewareVo.teacherId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='resourcecenter.CoursewareVo.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customerId', full_name='resourcecenter.CoursewareVo.customerId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectId', full_name='resourcecenter.CoursewareVo.subjectId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editionId', full_name='resourcecenter.CoursewareVo.editionId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isBoutique', full_name='resourcecenter.CoursewareVo.isBoutique', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageCount', full_name='resourcecenter.CoursewareVo.pageCount', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=309,
  serialized_end=465,
)


_REQCOURSEWAREISJING = _descriptor.Descriptor(
  name='ReqCoursewareIsJing',
  full_name='resourcecenter.ReqCoursewareIsJing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resourcecenter.ReqCoursewareIsJing.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='resourcecenter.ReqCoursewareIsJing.tag', index=1,
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
  serialized_start=467,
  serialized_end=513,
)


_REQCOURSEWARELIST = _descriptor.Descriptor(
  name='ReqCoursewareList',
  full_name='resourcecenter.ReqCoursewareList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isBoutique', full_name='resourcecenter.ReqCoursewareList.isBoutique', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='resourcecenter.ReqCoursewareList.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectId', full_name='resourcecenter.ReqCoursewareList.subjectId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editionVersionId', full_name='resourcecenter.ReqCoursewareList.editionVersionId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stageId', full_name='resourcecenter.ReqCoursewareList.stageId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeId', full_name='resourcecenter.ReqCoursewareList.gradeId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fascicleId', full_name='resourcecenter.ReqCoursewareList.fascicleId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderType', full_name='resourcecenter.ReqCoursewareList.orderType', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='resourcecenter.ReqCoursewareList.pageNo', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='resourcecenter.ReqCoursewareList.pageSize', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=516,
  serialized_end=721,
)


_COURSEWAREITEMVO = _descriptor.Descriptor(
  name='CoursewareItemVo',
  full_name='resourcecenter.CoursewareItemVo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resourcecenter.CoursewareItemVo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageCount', full_name='resourcecenter.CoursewareItemVo.pageCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isBoutique', full_name='resourcecenter.CoursewareItemVo.isBoutique', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editionVersionName', full_name='resourcecenter.CoursewareItemVo.editionVersionName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gradeName', full_name='resourcecenter.CoursewareItemVo.gradeName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subjectName', full_name='resourcecenter.CoursewareItemVo.subjectName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coursewareName', full_name='resourcecenter.CoursewareItemVo.coursewareName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='resourcecenter.CoursewareItemVo.stage', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fascicle', full_name='resourcecenter.CoursewareItemVo.fascicle', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chapterName', full_name='resourcecenter.CoursewareItemVo.chapterName', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pointName', full_name='resourcecenter.CoursewareItemVo.pointName', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='resourcecenter.CoursewareItemVo.updateTime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceCount', full_name='resourcecenter.CoursewareItemVo.referenceCount', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolName', full_name='resourcecenter.CoursewareItemVo.schoolName', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teacherName', full_name='resourcecenter.CoursewareItemVo.teacherName', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=724,
  serialized_end=1043,
)


_RESPONSECOURSEWARELIST = _descriptor.Descriptor(
  name='ResponseCoursewareList',
  full_name='resourcecenter.ResponseCoursewareList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='resourcecenter.ResponseCoursewareList.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='resourcecenter.ResponseCoursewareList.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='resourcecenter.ResponseCoursewareList.total', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pages', full_name='resourcecenter.ResponseCoursewareList.pages', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='resourcecenter.ResponseCoursewareList.pageNo', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='resourcecenter.ResponseCoursewareList.pageSize', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datas', full_name='resourcecenter.ResponseCoursewareList.datas', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1046,
  serialized_end=1210,
)

_RESPONSECOURSEWARELIST.fields_by_name['datas'].message_type = _COURSEWAREITEMVO
DESCRIPTOR.message_types_by_name['CoursewarePageVo'] = _COURSEWAREPAGEVO
DESCRIPTOR.message_types_by_name['ReqInsertCourseware'] = _REQINSERTCOURSEWARE
DESCRIPTOR.message_types_by_name['CoursewareVo'] = _COURSEWAREVO
DESCRIPTOR.message_types_by_name['ReqCoursewareIsJing'] = _REQCOURSEWAREISJING
DESCRIPTOR.message_types_by_name['ReqCoursewareList'] = _REQCOURSEWARELIST
DESCRIPTOR.message_types_by_name['CoursewareItemVo'] = _COURSEWAREITEMVO
DESCRIPTOR.message_types_by_name['ResponseCoursewareList'] = _RESPONSECOURSEWARELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoursewarePageVo = _reflection.GeneratedProtocolMessageType('CoursewarePageVo', (_message.Message,), dict(
  DESCRIPTOR = _COURSEWAREPAGEVO,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.CoursewarePageVo)
  ))
_sym_db.RegisterMessage(CoursewarePageVo)

ReqInsertCourseware = _reflection.GeneratedProtocolMessageType('ReqInsertCourseware', (_message.Message,), dict(
  DESCRIPTOR = _REQINSERTCOURSEWARE,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.ReqInsertCourseware)
  ))
_sym_db.RegisterMessage(ReqInsertCourseware)

CoursewareVo = _reflection.GeneratedProtocolMessageType('CoursewareVo', (_message.Message,), dict(
  DESCRIPTOR = _COURSEWAREVO,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.CoursewareVo)
  ))
_sym_db.RegisterMessage(CoursewareVo)

ReqCoursewareIsJing = _reflection.GeneratedProtocolMessageType('ReqCoursewareIsJing', (_message.Message,), dict(
  DESCRIPTOR = _REQCOURSEWAREISJING,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.ReqCoursewareIsJing)
  ))
_sym_db.RegisterMessage(ReqCoursewareIsJing)

ReqCoursewareList = _reflection.GeneratedProtocolMessageType('ReqCoursewareList', (_message.Message,), dict(
  DESCRIPTOR = _REQCOURSEWARELIST,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.ReqCoursewareList)
  ))
_sym_db.RegisterMessage(ReqCoursewareList)

CoursewareItemVo = _reflection.GeneratedProtocolMessageType('CoursewareItemVo', (_message.Message,), dict(
  DESCRIPTOR = _COURSEWAREITEMVO,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.CoursewareItemVo)
  ))
_sym_db.RegisterMessage(CoursewareItemVo)

ResponseCoursewareList = _reflection.GeneratedProtocolMessageType('ResponseCoursewareList', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSECOURSEWARELIST,
  __module__ = 'RCCoursewareService_pb2'
  # @@protoc_insertion_point(class_scope:resourcecenter.ResponseCoursewareList)
  ))
_sym_db.RegisterMessage(ResponseCoursewareList)


DESCRIPTOR._options = None

_RCCOURSEWARESERVICE = _descriptor.ServiceDescriptor(
  name='RCCoursewareService',
  full_name='resourcecenter.RCCoursewareService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1213,
  serialized_end=1762,
  methods=[
  _descriptor.MethodDescriptor(
    name='insertCourseware',
    full_name='resourcecenter.RCCoursewareService.insertCourseware',
    index=0,
    containing_service=None,
    input_type=_REQINSERTCOURSEWARE,
    output_type=RCCommon__pb2._EMPTYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='isJingCourseware',
    full_name='resourcecenter.RCCoursewareService.isJingCourseware',
    index=1,
    containing_service=None,
    input_type=_REQCOURSEWAREISJING,
    output_type=RCCommon__pb2._EMPTYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='insertCoursewarePage',
    full_name='resourcecenter.RCCoursewareService.insertCoursewarePage',
    index=2,
    containing_service=None,
    input_type=_COURSEWAREPAGEVO,
    output_type=RCCommon__pb2._EMPTYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='updateCoursewarePage',
    full_name='resourcecenter.RCCoursewareService.updateCoursewarePage',
    index=3,
    containing_service=None,
    input_type=_COURSEWAREPAGEVO,
    output_type=RCCommon__pb2._EMPTYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='deleteCoursewarePage',
    full_name='resourcecenter.RCCoursewareService.deleteCoursewarePage',
    index=4,
    containing_service=None,
    input_type=_COURSEWAREPAGEVO,
    output_type=RCCommon__pb2._EMPTYRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listCourseware',
    full_name='resourcecenter.RCCoursewareService.listCourseware',
    index=5,
    containing_service=None,
    input_type=_REQCOURSEWARELIST,
    output_type=_RESPONSECOURSEWARELIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RCCOURSEWARESERVICE)

DESCRIPTOR.services_by_name['RCCoursewareService'] = _RCCOURSEWARESERVICE

# @@protoc_insertion_point(module_scope)