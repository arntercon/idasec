# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instruction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='instruction.proto',
  package='instruction_pol',
  syntax='proto2',
  serialized_pb=_b('\n\x11instruction.proto\x12\x0finstruction_pol\x1a\x0c\x63ommon.proto\"\x82\x01\n\tinstr_pol\x12+\n\x05ident\x18\x01 \x02(\x0e\x32\x1c.instruction_pol.instr_ident\x12\x0e\n\x06opcode\x18\x02 \x02(\t\x12+\n\x05\x63puid\x18\x03 \x01(\x0b\x32\x1a.instruction_pol.cpuid_polH\x00\x42\x0b\n\tinstr_cnt\"\xa3\x01\n\tcpuid_pol\x12$\n\x03\x65\x61x\x18\x01 \x01(\x0e\x32\x0e.common.action:\x07\x44\x45\x46\x41ULT\x12$\n\x03\x65\x62x\x18\x02 \x01(\x0e\x32\x0e.common.action:\x07\x44\x45\x46\x41ULT\x12$\n\x03\x65\x63x\x18\x03 \x01(\x0e\x32\x0e.common.action:\x07\x44\x45\x46\x41ULT\x12$\n\x03\x65\x64x\x18\x04 \x01(\x0e\x32\x0e.common.action:\x07\x44\x45\x46\x41ULT**\n\x0binstr_ident\x12\x10\n\x0cINVALID_INST\x10\x00\x12\t\n\x05\x43PUID\x10\x01')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INSTR_IDENT = _descriptor.EnumDescriptor(
  name='instr_ident',
  full_name='instruction_pol.instr_ident',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_INST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPUID', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=351,
  serialized_end=393,
)
_sym_db.RegisterEnumDescriptor(_INSTR_IDENT)

instr_ident = enum_type_wrapper.EnumTypeWrapper(_INSTR_IDENT)
INVALID_INST = 0
CPUID = 1



_INSTR_POL = _descriptor.Descriptor(
  name='instr_pol',
  full_name='instruction_pol.instr_pol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ident', full_name='instruction_pol.instr_pol.ident', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opcode', full_name='instruction_pol.instr_pol.opcode', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpuid', full_name='instruction_pol.instr_pol.cpuid', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='instr_cnt', full_name='instruction_pol.instr_pol.instr_cnt',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=53,
  serialized_end=183,
)


_CPUID_POL = _descriptor.Descriptor(
  name='cpuid_pol',
  full_name='instruction_pol.cpuid_pol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eax', full_name='instruction_pol.cpuid_pol.eax', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ebx', full_name='instruction_pol.cpuid_pol.ebx', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ecx', full_name='instruction_pol.cpuid_pol.ecx', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edx', full_name='instruction_pol.cpuid_pol.edx', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=349,
)

_INSTR_POL.fields_by_name['ident'].enum_type = _INSTR_IDENT
_INSTR_POL.fields_by_name['cpuid'].message_type = _CPUID_POL
_INSTR_POL.oneofs_by_name['instr_cnt'].fields.append(
  _INSTR_POL.fields_by_name['cpuid'])
_INSTR_POL.fields_by_name['cpuid'].containing_oneof = _INSTR_POL.oneofs_by_name['instr_cnt']
_CPUID_POL.fields_by_name['eax'].enum_type = common__pb2._ACTION
_CPUID_POL.fields_by_name['ebx'].enum_type = common__pb2._ACTION
_CPUID_POL.fields_by_name['ecx'].enum_type = common__pb2._ACTION
_CPUID_POL.fields_by_name['edx'].enum_type = common__pb2._ACTION
DESCRIPTOR.message_types_by_name['instr_pol'] = _INSTR_POL
DESCRIPTOR.message_types_by_name['cpuid_pol'] = _CPUID_POL
DESCRIPTOR.enum_types_by_name['instr_ident'] = _INSTR_IDENT

instr_pol = _reflection.GeneratedProtocolMessageType('instr_pol', (_message.Message,), dict(
  DESCRIPTOR = _INSTR_POL,
  __module__ = 'instruction_pb2'
  # @@protoc_insertion_point(class_scope:instruction_pol.instr_pol)
  ))
_sym_db.RegisterMessage(instr_pol)

cpuid_pol = _reflection.GeneratedProtocolMessageType('cpuid_pol', (_message.Message,), dict(
  DESCRIPTOR = _CPUID_POL,
  __module__ = 'instruction_pb2'
  # @@protoc_insertion_point(class_scope:instruction_pol.cpuid_pol)
  ))
_sym_db.RegisterMessage(cpuid_pol)


# @@protoc_insertion_point(module_scope)
