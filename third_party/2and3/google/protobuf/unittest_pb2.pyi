from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer,
)
from google.protobuf.internal.enum_type_wrapper import (
    EnumTypeWrapper,
)
from google.protobuf.message import (
    Message,
)
from google.protobuf.unittest_import_pb2 import (
    _ImportEnum,
    ImportMessage,
)
from google.protobuf.unittest_import_public_pb2 import (
    PublicImportMessage,
)
from typing import (
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Text,
    Tuple,
    cast,
    NewType,
)

_ForeignEnum = NewType('_ForeignEnum', int)
ForeignEnum: EnumTypeWrapper[_ForeignEnum]
FOREIGN_FOO: _ForeignEnum
FOREIGN_BAR: _ForeignEnum
FOREIGN_BAZ: _ForeignEnum

_TestEnumWithDupValue = NewType('_TestEnumWithDupValue', int)
TestEnumWithDupValue: EnumTypeWrapper[_TestEnumWithDupValue]
FOO1: _TestEnumWithDupValue
BAR1: _TestEnumWithDupValue
BAZ: _TestEnumWithDupValue
FOO2: _TestEnumWithDupValue
BAR2: _TestEnumWithDupValue

_TestSparseEnum = NewType('_TestSparseEnum', int)
TestSparseEnum: EnumTypeWrapper[_TestSparseEnum]
SPARSE_A: _TestSparseEnum
SPARSE_B: _TestSparseEnum
SPARSE_C: _TestSparseEnum
SPARSE_D: _TestSparseEnum
SPARSE_E: _TestSparseEnum
SPARSE_F: _TestSparseEnum
SPARSE_G: _TestSparseEnum

_TestAllTypes_NestedEnum = NewType('_TestAllTypes_NestedEnum', int)


class TestAllTypes(Message):
    NestedEnum: EnumTypeWrapper[_TestAllTypes_NestedEnum]
    FOO: _TestAllTypes_NestedEnum
    BAR: _TestAllTypes_NestedEnum
    BAZ: _TestAllTypes_NestedEnum
    NEG: _TestAllTypes_NestedEnum

    class NestedMessage(Message):
        bb = ...  # type: int

        def __init__(self,
                     bb: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestAllTypes.NestedMessage: ...

    class OptionalGroup(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestAllTypes.OptionalGroup: ...

    class RepeatedGroup(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestAllTypes.RepeatedGroup: ...
    optional_int32 = ...  # type: int
    optional_int64 = ...  # type: int
    optional_uint32 = ...  # type: int
    optional_uint64 = ...  # type: int
    optional_sint32 = ...  # type: int
    optional_sint64 = ...  # type: int
    optional_fixed32 = ...  # type: int
    optional_fixed64 = ...  # type: int
    optional_sfixed32 = ...  # type: int
    optional_sfixed64 = ...  # type: int
    optional_float = ...  # type: float
    optional_double = ...  # type: float
    optional_bool = ...  # type: bool
    optional_string = ...  # type: Text
    optional_bytes = ...  # type: bytes
    optional_nested_enum = ...  # type: _TestAllTypes_NestedEnum
    optional_foreign_enum = ...  # type: _ForeignEnum
    optional_import_enum = ...  # type: _ImportEnum
    optional_string_piece = ...  # type: Text
    optional_cord = ...  # type: Text
    repeated_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_int64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_uint32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_uint64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_sint32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_sint64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_fixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_fixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_sfixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_sfixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_float = ...  # type: RepeatedScalarFieldContainer[float]
    repeated_double = ...  # type: RepeatedScalarFieldContainer[float]
    repeated_bool = ...  # type: RepeatedScalarFieldContainer[bool]
    repeated_string = ...  # type: RepeatedScalarFieldContainer[Text]
    repeated_bytes = ...  # type: RepeatedScalarFieldContainer[bytes]
    repeated_nested_enum = ...  # type: RepeatedScalarFieldContainer[_TestAllTypes_NestedEnum]
    repeated_foreign_enum = ...  # type: RepeatedScalarFieldContainer[_ForeignEnum]
    repeated_import_enum = ...  # type: RepeatedScalarFieldContainer[_ImportEnum]
    repeated_string_piece = ...  # type: RepeatedScalarFieldContainer[Text]
    repeated_cord = ...  # type: RepeatedScalarFieldContainer[Text]
    default_int32 = ...  # type: int
    default_int64 = ...  # type: int
    default_uint32 = ...  # type: int
    default_uint64 = ...  # type: int
    default_sint32 = ...  # type: int
    default_sint64 = ...  # type: int
    default_fixed32 = ...  # type: int
    default_fixed64 = ...  # type: int
    default_sfixed32 = ...  # type: int
    default_sfixed64 = ...  # type: int
    default_float = ...  # type: float
    default_double = ...  # type: float
    default_bool = ...  # type: bool
    default_string = ...  # type: Text
    default_bytes = ...  # type: bytes
    default_nested_enum = ...  # type: _TestAllTypes_NestedEnum
    default_foreign_enum = ...  # type: _ForeignEnum
    default_import_enum = ...  # type: _ImportEnum
    default_string_piece = ...  # type: Text
    default_cord = ...  # type: Text
    oneof_uint32 = ...  # type: int
    oneof_string = ...  # type: Text
    oneof_bytes = ...  # type: bytes

    @property
    def optionalgroup(self) -> TestAllTypes.OptionalGroup: ...

    @property
    def optional_nested_message(self) -> TestAllTypes.NestedMessage: ...

    @property
    def optional_foreign_message(self) -> ForeignMessage: ...

    @property
    def optional_import_message(self) -> ImportMessage: ...

    @property
    def optional_public_import_message(self) -> PublicImportMessage: ...

    @property
    def optional_lazy_message(self) -> TestAllTypes.NestedMessage: ...

    @property
    def repeatedgroup(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.RepeatedGroup]: ...

    @property
    def repeated_nested_message(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]: ...

    @property
    def repeated_foreign_message(
        self) -> RepeatedCompositeFieldContainer[ForeignMessage]: ...

    @property
    def repeated_import_message(
        self) -> RepeatedCompositeFieldContainer[ImportMessage]: ...

    @property
    def repeated_lazy_message(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]: ...

    @property
    def oneof_nested_message(self) -> TestAllTypes.NestedMessage: ...

    def __init__(self,
                 optional_int32: Optional[int] = ...,
                 optional_int64: Optional[int] = ...,
                 optional_uint32: Optional[int] = ...,
                 optional_uint64: Optional[int] = ...,
                 optional_sint32: Optional[int] = ...,
                 optional_sint64: Optional[int] = ...,
                 optional_fixed32: Optional[int] = ...,
                 optional_fixed64: Optional[int] = ...,
                 optional_sfixed32: Optional[int] = ...,
                 optional_sfixed64: Optional[int] = ...,
                 optional_float: Optional[float] = ...,
                 optional_double: Optional[float] = ...,
                 optional_bool: Optional[bool] = ...,
                 optional_string: Optional[Text] = ...,
                 optional_bytes: Optional[bytes] = ...,
                 optionalgroup: Optional[TestAllTypes.OptionalGroup] = ...,
                 optional_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 optional_foreign_message: Optional[ForeignMessage] = ...,
                 optional_import_message: Optional[ImportMessage] = ...,
                 optional_nested_enum: Optional[_TestAllTypes_NestedEnum] = ...,
                 optional_foreign_enum: Optional[_ForeignEnum] = ...,
                 optional_import_enum: Optional[_ImportEnum] = ...,
                 optional_string_piece: Optional[Text] = ...,
                 optional_cord: Optional[Text] = ...,
                 optional_public_import_message: Optional[PublicImportMessage] = ...,
                 optional_lazy_message: Optional[TestAllTypes.NestedMessage] = ...,
                 repeated_int32: Optional[Iterable[int]] = ...,
                 repeated_int64: Optional[Iterable[int]] = ...,
                 repeated_uint32: Optional[Iterable[int]] = ...,
                 repeated_uint64: Optional[Iterable[int]] = ...,
                 repeated_sint32: Optional[Iterable[int]] = ...,
                 repeated_sint64: Optional[Iterable[int]] = ...,
                 repeated_fixed32: Optional[Iterable[int]] = ...,
                 repeated_fixed64: Optional[Iterable[int]] = ...,
                 repeated_sfixed32: Optional[Iterable[int]] = ...,
                 repeated_sfixed64: Optional[Iterable[int]] = ...,
                 repeated_float: Optional[Iterable[float]] = ...,
                 repeated_double: Optional[Iterable[float]] = ...,
                 repeated_bool: Optional[Iterable[bool]] = ...,
                 repeated_string: Optional[Iterable[Text]] = ...,
                 repeated_bytes: Optional[Iterable[bytes]] = ...,
                 repeatedgroup: Optional[Iterable[TestAllTypes.RepeatedGroup]] = ...,
                 repeated_nested_message: Optional[Iterable[TestAllTypes.NestedMessage]] = ...,
                 repeated_foreign_message: Optional[Iterable[ForeignMessage]] = ...,
                 repeated_import_message: Optional[Iterable[ImportMessage]] = ...,
                 repeated_nested_enum: Optional[Iterable[_TestAllTypes_NestedEnum]] = ...,
                 repeated_foreign_enum: Optional[Iterable[_ForeignEnum]] = ...,
                 repeated_import_enum: Optional[Iterable[_ImportEnum]] = ...,
                 repeated_string_piece: Optional[Iterable[Text]] = ...,
                 repeated_cord: Optional[Iterable[Text]] = ...,
                 repeated_lazy_message: Optional[Iterable[TestAllTypes.NestedMessage]] = ...,
                 default_int32: Optional[int] = ...,
                 default_int64: Optional[int] = ...,
                 default_uint32: Optional[int] = ...,
                 default_uint64: Optional[int] = ...,
                 default_sint32: Optional[int] = ...,
                 default_sint64: Optional[int] = ...,
                 default_fixed32: Optional[int] = ...,
                 default_fixed64: Optional[int] = ...,
                 default_sfixed32: Optional[int] = ...,
                 default_sfixed64: Optional[int] = ...,
                 default_float: Optional[float] = ...,
                 default_double: Optional[float] = ...,
                 default_bool: Optional[bool] = ...,
                 default_string: Optional[Text] = ...,
                 default_bytes: Optional[bytes] = ...,
                 default_nested_enum: Optional[_TestAllTypes_NestedEnum] = ...,
                 default_foreign_enum: Optional[_ForeignEnum] = ...,
                 default_import_enum: Optional[_ImportEnum] = ...,
                 default_string_piece: Optional[Text] = ...,
                 default_cord: Optional[Text] = ...,
                 oneof_uint32: Optional[int] = ...,
                 oneof_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 oneof_string: Optional[Text] = ...,
                 oneof_bytes: Optional[bytes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestAllTypes: ...


class NestedTestAllTypes(Message):

    @property
    def child(self) -> NestedTestAllTypes: ...

    @property
    def payload(self) -> TestAllTypes: ...

    @property
    def repeated_child(
        self) -> RepeatedCompositeFieldContainer[NestedTestAllTypes]: ...

    def __init__(self,
                 child: Optional[NestedTestAllTypes] = ...,
                 payload: Optional[TestAllTypes] = ...,
                 repeated_child: Optional[Iterable[NestedTestAllTypes]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> NestedTestAllTypes: ...


class TestDeprecatedFields(Message):
    deprecated_int32 = ...  # type: int
    deprecated_int32_in_oneof = ...  # type: int

    def __init__(self,
                 deprecated_int32: Optional[int] = ...,
                 deprecated_int32_in_oneof: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestDeprecatedFields: ...


class TestDeprecatedMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestDeprecatedMessage: ...


class ForeignMessage(Message):
    c = ...  # type: int
    d = ...  # type: int

    def __init__(self,
                 c: Optional[int] = ...,
                 d: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ForeignMessage: ...


class TestReservedFields(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestReservedFields: ...


class TestAllExtensions(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestAllExtensions: ...


class OptionalGroup_extension(Message):
    a = ...  # type: int

    def __init__(self,
                 a: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> OptionalGroup_extension: ...


class RepeatedGroup_extension(Message):
    a = ...  # type: int

    def __init__(self,
                 a: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> RepeatedGroup_extension: ...


class TestGroup(Message):
    class OptionalGroup(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestGroup.OptionalGroup: ...
    optional_foreign_enum = ...  # type: _ForeignEnum

    @property
    def optionalgroup(self) -> TestGroup.OptionalGroup: ...

    def __init__(self,
                 optionalgroup: Optional[TestGroup.OptionalGroup] = ...,
                 optional_foreign_enum: Optional[_ForeignEnum] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestGroup: ...


class TestGroupExtension(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestGroupExtension: ...


class TestNestedExtension(Message):
    class OptionalGroup_extension(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestNestedExtension.OptionalGroup_extension: ...

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestNestedExtension: ...


class TestRequired(Message):
    a = ...  # type: int
    dummy2 = ...  # type: int
    b = ...  # type: int
    dummy4 = ...  # type: int
    dummy5 = ...  # type: int
    dummy6 = ...  # type: int
    dummy7 = ...  # type: int
    dummy8 = ...  # type: int
    dummy9 = ...  # type: int
    dummy10 = ...  # type: int
    dummy11 = ...  # type: int
    dummy12 = ...  # type: int
    dummy13 = ...  # type: int
    dummy14 = ...  # type: int
    dummy15 = ...  # type: int
    dummy16 = ...  # type: int
    dummy17 = ...  # type: int
    dummy18 = ...  # type: int
    dummy19 = ...  # type: int
    dummy20 = ...  # type: int
    dummy21 = ...  # type: int
    dummy22 = ...  # type: int
    dummy23 = ...  # type: int
    dummy24 = ...  # type: int
    dummy25 = ...  # type: int
    dummy26 = ...  # type: int
    dummy27 = ...  # type: int
    dummy28 = ...  # type: int
    dummy29 = ...  # type: int
    dummy30 = ...  # type: int
    dummy31 = ...  # type: int
    dummy32 = ...  # type: int
    c = ...  # type: int

    def __init__(self,
                 a: int,
                 b: int,
                 c: int,
                 dummy2: Optional[int] = ...,
                 dummy4: Optional[int] = ...,
                 dummy5: Optional[int] = ...,
                 dummy6: Optional[int] = ...,
                 dummy7: Optional[int] = ...,
                 dummy8: Optional[int] = ...,
                 dummy9: Optional[int] = ...,
                 dummy10: Optional[int] = ...,
                 dummy11: Optional[int] = ...,
                 dummy12: Optional[int] = ...,
                 dummy13: Optional[int] = ...,
                 dummy14: Optional[int] = ...,
                 dummy15: Optional[int] = ...,
                 dummy16: Optional[int] = ...,
                 dummy17: Optional[int] = ...,
                 dummy18: Optional[int] = ...,
                 dummy19: Optional[int] = ...,
                 dummy20: Optional[int] = ...,
                 dummy21: Optional[int] = ...,
                 dummy22: Optional[int] = ...,
                 dummy23: Optional[int] = ...,
                 dummy24: Optional[int] = ...,
                 dummy25: Optional[int] = ...,
                 dummy26: Optional[int] = ...,
                 dummy27: Optional[int] = ...,
                 dummy28: Optional[int] = ...,
                 dummy29: Optional[int] = ...,
                 dummy30: Optional[int] = ...,
                 dummy31: Optional[int] = ...,
                 dummy32: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRequired: ...


class TestRequiredForeign(Message):
    dummy = ...  # type: int

    @property
    def optional_message(self) -> TestRequired: ...

    @property
    def repeated_message(
        self) -> RepeatedCompositeFieldContainer[TestRequired]: ...

    def __init__(self,
                 optional_message: Optional[TestRequired] = ...,
                 repeated_message: Optional[Iterable[TestRequired]] = ...,
                 dummy: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRequiredForeign: ...


class TestRequiredMessage(Message):

    @property
    def optional_message(self) -> TestRequired: ...

    @property
    def repeated_message(
        self) -> RepeatedCompositeFieldContainer[TestRequired]: ...

    @property
    def required_message(self) -> TestRequired: ...

    def __init__(self,
                 required_message: TestRequired,
                 optional_message: Optional[TestRequired] = ...,
                 repeated_message: Optional[Iterable[TestRequired]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRequiredMessage: ...


class TestForeignNested(Message):

    @property
    def foreign_nested(self) -> TestAllTypes.NestedMessage: ...

    def __init__(self,
                 foreign_nested: Optional[TestAllTypes.NestedMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestForeignNested: ...


class TestEmptyMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestEmptyMessage: ...


class TestEmptyMessageWithExtensions(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestEmptyMessageWithExtensions: ...


class TestMultipleExtensionRanges(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMultipleExtensionRanges: ...


class TestReallyLargeTagNumber(Message):
    a = ...  # type: int
    bb = ...  # type: int

    def __init__(self,
                 a: Optional[int] = ...,
                 bb: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestReallyLargeTagNumber: ...


class TestRecursiveMessage(Message):
    i = ...  # type: int

    @property
    def a(self) -> TestRecursiveMessage: ...

    def __init__(self,
                 a: Optional[TestRecursiveMessage] = ...,
                 i: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRecursiveMessage: ...


class TestMutualRecursionA(Message):
    class SubMessage(Message):

        @property
        def b(self) -> TestMutualRecursionB: ...

        def __init__(self,
                     b: Optional[TestMutualRecursionB] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestMutualRecursionA.SubMessage: ...

    class SubGroup(Message):

        @property
        def sub_message(self) -> TestMutualRecursionA.SubMessage: ...

        @property
        def not_in_this_scc(self) -> TestAllTypes: ...

        def __init__(self,
                     sub_message: Optional[TestMutualRecursionA.SubMessage] = ...,
                     not_in_this_scc: Optional[TestAllTypes] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestMutualRecursionA.SubGroup: ...

    @property
    def bb(self) -> TestMutualRecursionB: ...

    @property
    def subgroup(self) -> TestMutualRecursionA.SubGroup: ...

    def __init__(self,
                 bb: Optional[TestMutualRecursionB] = ...,
                 subgroup: Optional[TestMutualRecursionA.SubGroup] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMutualRecursionA: ...


class TestMutualRecursionB(Message):
    optional_int32 = ...  # type: int

    @property
    def a(self) -> TestMutualRecursionA: ...

    def __init__(self,
                 a: Optional[TestMutualRecursionA] = ...,
                 optional_int32: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMutualRecursionB: ...


class TestIsInitialized(Message):
    class SubMessage(Message):
        class SubGroup(Message):
            i = ...  # type: int

            def __init__(self,
                         i: int,
                         ) -> None: ...

            @classmethod
            def FromString(
                cls, s: bytes) -> TestIsInitialized.SubMessage.SubGroup: ...

        @property
        def subgroup(self) -> TestIsInitialized.SubMessage.SubGroup: ...

        def __init__(self,
                     subgroup: Optional[TestIsInitialized.SubMessage.SubGroup] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestIsInitialized.SubMessage: ...

    @property
    def sub_message(self) -> TestIsInitialized.SubMessage: ...

    def __init__(self,
                 sub_message: Optional[TestIsInitialized.SubMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestIsInitialized: ...


class TestDupFieldNumber(Message):
    class Foo(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestDupFieldNumber.Foo: ...

    class Bar(Message):
        a = ...  # type: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestDupFieldNumber.Bar: ...
    a = ...  # type: int

    @property
    def foo(self) -> TestDupFieldNumber.Foo: ...

    @property
    def bar(self) -> TestDupFieldNumber.Bar: ...

    def __init__(self,
                 a: Optional[int] = ...,
                 foo: Optional[TestDupFieldNumber.Foo] = ...,
                 bar: Optional[TestDupFieldNumber.Bar] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestDupFieldNumber: ...


class TestEagerMessage(Message):

    @property
    def sub_message(self) -> TestAllTypes: ...

    def __init__(self,
                 sub_message: Optional[TestAllTypes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestEagerMessage: ...


class TestLazyMessage(Message):

    @property
    def sub_message(self) -> TestAllTypes: ...

    def __init__(self,
                 sub_message: Optional[TestAllTypes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestLazyMessage: ...


class TestNestedMessageHasBits(Message):
    class NestedMessage(Message):
        nestedmessage_repeated_int32 = ...  # type: RepeatedScalarFieldContainer[int]

        @property
        def nestedmessage_repeated_foreignmessage(
            self) -> RepeatedCompositeFieldContainer[ForeignMessage]: ...

        def __init__(self,
                     nestedmessage_repeated_int32: Optional[Iterable[int]] = ...,
                     nestedmessage_repeated_foreignmessage: Optional[Iterable[ForeignMessage]] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestNestedMessageHasBits.NestedMessage: ...

    @property
    def optional_nested_message(
        self) -> TestNestedMessageHasBits.NestedMessage: ...

    def __init__(self,
                 optional_nested_message: Optional[TestNestedMessageHasBits.NestedMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestNestedMessageHasBits: ...


class TestCamelCaseFieldNames(Message):
    PrimitiveField = ...  # type: int
    StringField = ...  # type: Text
    EnumField = ...  # type: _ForeignEnum
    StringPieceField = ...  # type: Text
    CordField = ...  # type: Text
    RepeatedPrimitiveField = ...  # type: RepeatedScalarFieldContainer[int]
    RepeatedStringField = ...  # type: RepeatedScalarFieldContainer[Text]
    RepeatedEnumField = ...  # type: RepeatedScalarFieldContainer[_ForeignEnum]
    RepeatedStringPieceField = ...  # type: RepeatedScalarFieldContainer[Text]
    RepeatedCordField = ...  # type: RepeatedScalarFieldContainer[Text]

    @property
    def MessageField(self) -> ForeignMessage: ...

    @property
    def RepeatedMessageField(
        self) -> RepeatedCompositeFieldContainer[ForeignMessage]: ...

    def __init__(self,
                 PrimitiveField: Optional[int] = ...,
                 StringField: Optional[Text] = ...,
                 EnumField: Optional[_ForeignEnum] = ...,
                 MessageField: Optional[ForeignMessage] = ...,
                 StringPieceField: Optional[Text] = ...,
                 CordField: Optional[Text] = ...,
                 RepeatedPrimitiveField: Optional[Iterable[int]] = ...,
                 RepeatedStringField: Optional[Iterable[Text]] = ...,
                 RepeatedEnumField: Optional[Iterable[_ForeignEnum]] = ...,
                 RepeatedMessageField: Optional[Iterable[ForeignMessage]] = ...,
                 RepeatedStringPieceField: Optional[Iterable[Text]] = ...,
                 RepeatedCordField: Optional[Iterable[Text]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestCamelCaseFieldNames: ...


class TestFieldOrderings(Message):
    class NestedMessage(Message):
        oo = ...  # type: int
        bb = ...  # type: int

        def __init__(self,
                     oo: Optional[int] = ...,
                     bb: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestFieldOrderings.NestedMessage: ...
    my_string = ...  # type: Text
    my_int = ...  # type: int
    my_float = ...  # type: float

    @property
    def optional_nested_message(self) -> TestFieldOrderings.NestedMessage: ...

    def __init__(self,
                 my_string: Optional[Text] = ...,
                 my_int: Optional[int] = ...,
                 my_float: Optional[float] = ...,
                 optional_nested_message: Optional[TestFieldOrderings.NestedMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestFieldOrderings: ...


class TestExtensionOrderings1(Message):
    my_string = ...  # type: Text

    def __init__(self,
                 my_string: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestExtensionOrderings1: ...


class TestExtensionOrderings2(Message):
    class TestExtensionOrderings3(Message):
        my_string = ...  # type: Text

        def __init__(self,
                     my_string: Optional[Text] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestExtensionOrderings2.TestExtensionOrderings3: ...
    my_string = ...  # type: Text

    def __init__(self,
                 my_string: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestExtensionOrderings2: ...


class TestExtremeDefaultValues(Message):
    escaped_bytes = ...  # type: bytes
    large_uint32 = ...  # type: int
    large_uint64 = ...  # type: int
    small_int32 = ...  # type: int
    small_int64 = ...  # type: int
    really_small_int32 = ...  # type: int
    really_small_int64 = ...  # type: int
    utf8_string = ...  # type: Text
    zero_float = ...  # type: float
    one_float = ...  # type: float
    small_float = ...  # type: float
    negative_one_float = ...  # type: float
    negative_float = ...  # type: float
    large_float = ...  # type: float
    small_negative_float = ...  # type: float
    inf_double = ...  # type: float
    neg_inf_double = ...  # type: float
    nan_double = ...  # type: float
    inf_float = ...  # type: float
    neg_inf_float = ...  # type: float
    nan_float = ...  # type: float
    cpp_trigraph = ...  # type: Text
    string_with_zero = ...  # type: Text
    bytes_with_zero = ...  # type: bytes
    string_piece_with_zero = ...  # type: Text
    cord_with_zero = ...  # type: Text
    replacement_string = ...  # type: Text

    def __init__(self,
                 escaped_bytes: Optional[bytes] = ...,
                 large_uint32: Optional[int] = ...,
                 large_uint64: Optional[int] = ...,
                 small_int32: Optional[int] = ...,
                 small_int64: Optional[int] = ...,
                 really_small_int32: Optional[int] = ...,
                 really_small_int64: Optional[int] = ...,
                 utf8_string: Optional[Text] = ...,
                 zero_float: Optional[float] = ...,
                 one_float: Optional[float] = ...,
                 small_float: Optional[float] = ...,
                 negative_one_float: Optional[float] = ...,
                 negative_float: Optional[float] = ...,
                 large_float: Optional[float] = ...,
                 small_negative_float: Optional[float] = ...,
                 inf_double: Optional[float] = ...,
                 neg_inf_double: Optional[float] = ...,
                 nan_double: Optional[float] = ...,
                 inf_float: Optional[float] = ...,
                 neg_inf_float: Optional[float] = ...,
                 nan_float: Optional[float] = ...,
                 cpp_trigraph: Optional[Text] = ...,
                 string_with_zero: Optional[Text] = ...,
                 bytes_with_zero: Optional[bytes] = ...,
                 string_piece_with_zero: Optional[Text] = ...,
                 cord_with_zero: Optional[Text] = ...,
                 replacement_string: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestExtremeDefaultValues: ...


class SparseEnumMessage(Message):
    sparse_enum = ...  # type: _TestSparseEnum

    def __init__(self,
                 sparse_enum: Optional[_TestSparseEnum] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> SparseEnumMessage: ...


class OneString(Message):
    data = ...  # type: Text

    def __init__(self,
                 data: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> OneString: ...


class MoreString(Message):
    data = ...  # type: RepeatedScalarFieldContainer[Text]

    def __init__(self,
                 data: Optional[Iterable[Text]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> MoreString: ...


class OneBytes(Message):
    data = ...  # type: bytes

    def __init__(self,
                 data: Optional[bytes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> OneBytes: ...


class MoreBytes(Message):
    data = ...  # type: RepeatedScalarFieldContainer[bytes]

    def __init__(self,
                 data: Optional[Iterable[bytes]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> MoreBytes: ...


class Int32Message(Message):
    data = ...  # type: int

    def __init__(self,
                 data: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Int32Message: ...


class Uint32Message(Message):
    data = ...  # type: int

    def __init__(self,
                 data: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Uint32Message: ...


class Int64Message(Message):
    data = ...  # type: int

    def __init__(self,
                 data: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Int64Message: ...


class Uint64Message(Message):
    data = ...  # type: int

    def __init__(self,
                 data: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Uint64Message: ...


class BoolMessage(Message):
    data = ...  # type: bool

    def __init__(self,
                 data: Optional[bool] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> BoolMessage: ...


class TestOneof(Message):
    class FooGroup(Message):
        a = ...  # type: int
        b = ...  # type: Text

        def __init__(self,
                     a: Optional[int] = ...,
                     b: Optional[Text] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestOneof.FooGroup: ...
    foo_int = ...  # type: int
    foo_string = ...  # type: Text

    @property
    def foo_message(self) -> TestAllTypes: ...

    @property
    def foogroup(self) -> TestOneof.FooGroup: ...

    def __init__(self,
                 foo_int: Optional[int] = ...,
                 foo_string: Optional[Text] = ...,
                 foo_message: Optional[TestAllTypes] = ...,
                 foogroup: Optional[TestOneof.FooGroup] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestOneof: ...


class TestOneofBackwardsCompatible(Message):
    class FooGroup(Message):
        a = ...  # type: int
        b = ...  # type: Text

        def __init__(self,
                     a: Optional[int] = ...,
                     b: Optional[Text] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestOneofBackwardsCompatible.FooGroup: ...
    foo_int = ...  # type: int
    foo_string = ...  # type: Text

    @property
    def foo_message(self) -> TestAllTypes: ...

    @property
    def foogroup(self) -> TestOneofBackwardsCompatible.FooGroup: ...

    def __init__(self,
                 foo_int: Optional[int] = ...,
                 foo_string: Optional[Text] = ...,
                 foo_message: Optional[TestAllTypes] = ...,
                 foogroup: Optional[TestOneofBackwardsCompatible.FooGroup] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestOneofBackwardsCompatible: ...


_TestOneof2_NestedEnum = NewType('_TestOneof2_NestedEnum', int)


class TestOneof2(Message):
    NestedEnum: EnumTypeWrapper[_TestOneof2_NestedEnum]
    FOO: _TestOneof2_NestedEnum
    BAR: _TestOneof2_NestedEnum
    BAZ: _TestOneof2_NestedEnum

    class FooGroup(Message):
        a = ...  # type: int
        b = ...  # type: Text

        def __init__(self,
                     a: Optional[int] = ...,
                     b: Optional[Text] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestOneof2.FooGroup: ...

    class NestedMessage(Message):
        qux_int = ...  # type: int
        corge_int = ...  # type: RepeatedScalarFieldContainer[int]

        def __init__(self,
                     qux_int: Optional[int] = ...,
                     corge_int: Optional[Iterable[int]] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestOneof2.NestedMessage: ...
    foo_int = ...  # type: int
    foo_string = ...  # type: Text
    foo_cord = ...  # type: Text
    foo_string_piece = ...  # type: Text
    foo_bytes = ...  # type: bytes
    foo_enum = ...  # type: _TestOneof2_NestedEnum
    bar_int = ...  # type: int
    bar_string = ...  # type: Text
    bar_cord = ...  # type: Text
    bar_string_piece = ...  # type: Text
    bar_bytes = ...  # type: bytes
    bar_enum = ...  # type: _TestOneof2_NestedEnum
    baz_int = ...  # type: int
    baz_string = ...  # type: Text

    @property
    def foo_message(self) -> TestOneof2.NestedMessage: ...

    @property
    def foogroup(self) -> TestOneof2.FooGroup: ...

    @property
    def foo_lazy_message(self) -> TestOneof2.NestedMessage: ...

    def __init__(self,
                 foo_int: Optional[int] = ...,
                 foo_string: Optional[Text] = ...,
                 foo_cord: Optional[Text] = ...,
                 foo_string_piece: Optional[Text] = ...,
                 foo_bytes: Optional[bytes] = ...,
                 foo_enum: Optional[_TestOneof2_NestedEnum] = ...,
                 foo_message: Optional[TestOneof2.NestedMessage] = ...,
                 foogroup: Optional[TestOneof2.FooGroup] = ...,
                 foo_lazy_message: Optional[TestOneof2.NestedMessage] = ...,
                 bar_int: Optional[int] = ...,
                 bar_string: Optional[Text] = ...,
                 bar_cord: Optional[Text] = ...,
                 bar_string_piece: Optional[Text] = ...,
                 bar_bytes: Optional[bytes] = ...,
                 bar_enum: Optional[_TestOneof2_NestedEnum] = ...,
                 baz_int: Optional[int] = ...,
                 baz_string: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestOneof2: ...


class TestRequiredOneof(Message):
    class NestedMessage(Message):
        required_double = ...  # type: float

        def __init__(self,
                     required_double: float,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestRequiredOneof.NestedMessage: ...
    foo_int = ...  # type: int
    foo_string = ...  # type: Text

    @property
    def foo_message(self) -> TestRequiredOneof.NestedMessage: ...

    def __init__(self,
                 foo_int: Optional[int] = ...,
                 foo_string: Optional[Text] = ...,
                 foo_message: Optional[TestRequiredOneof.NestedMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRequiredOneof: ...


class TestPackedTypes(Message):
    packed_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_int64 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_uint32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_uint64 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_sint32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_sint64 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_fixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_fixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_sfixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_sfixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_float = ...  # type: RepeatedScalarFieldContainer[float]
    packed_double = ...  # type: RepeatedScalarFieldContainer[float]
    packed_bool = ...  # type: RepeatedScalarFieldContainer[bool]
    packed_enum = ...  # type: RepeatedScalarFieldContainer[_ForeignEnum]

    def __init__(self,
                 packed_int32: Optional[Iterable[int]] = ...,
                 packed_int64: Optional[Iterable[int]] = ...,
                 packed_uint32: Optional[Iterable[int]] = ...,
                 packed_uint64: Optional[Iterable[int]] = ...,
                 packed_sint32: Optional[Iterable[int]] = ...,
                 packed_sint64: Optional[Iterable[int]] = ...,
                 packed_fixed32: Optional[Iterable[int]] = ...,
                 packed_fixed64: Optional[Iterable[int]] = ...,
                 packed_sfixed32: Optional[Iterable[int]] = ...,
                 packed_sfixed64: Optional[Iterable[int]] = ...,
                 packed_float: Optional[Iterable[float]] = ...,
                 packed_double: Optional[Iterable[float]] = ...,
                 packed_bool: Optional[Iterable[bool]] = ...,
                 packed_enum: Optional[Iterable[_ForeignEnum]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestPackedTypes: ...


class TestUnpackedTypes(Message):
    unpacked_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_int64 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_uint32 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_uint64 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_sint32 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_sint64 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_fixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_fixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_sfixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_sfixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    unpacked_float = ...  # type: RepeatedScalarFieldContainer[float]
    unpacked_double = ...  # type: RepeatedScalarFieldContainer[float]
    unpacked_bool = ...  # type: RepeatedScalarFieldContainer[bool]
    unpacked_enum = ...  # type: RepeatedScalarFieldContainer[_ForeignEnum]

    def __init__(self,
                 unpacked_int32: Optional[Iterable[int]] = ...,
                 unpacked_int64: Optional[Iterable[int]] = ...,
                 unpacked_uint32: Optional[Iterable[int]] = ...,
                 unpacked_uint64: Optional[Iterable[int]] = ...,
                 unpacked_sint32: Optional[Iterable[int]] = ...,
                 unpacked_sint64: Optional[Iterable[int]] = ...,
                 unpacked_fixed32: Optional[Iterable[int]] = ...,
                 unpacked_fixed64: Optional[Iterable[int]] = ...,
                 unpacked_sfixed32: Optional[Iterable[int]] = ...,
                 unpacked_sfixed64: Optional[Iterable[int]] = ...,
                 unpacked_float: Optional[Iterable[float]] = ...,
                 unpacked_double: Optional[Iterable[float]] = ...,
                 unpacked_bool: Optional[Iterable[bool]] = ...,
                 unpacked_enum: Optional[Iterable[_ForeignEnum]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestUnpackedTypes: ...


class TestPackedExtensions(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestPackedExtensions: ...


class TestUnpackedExtensions(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestUnpackedExtensions: ...


_TestDynamicExtensions_DynamicEnumType = NewType('_TestDynamicExtensions_DynamicEnumType', int)


class TestDynamicExtensions(Message):
    DynamicEnumType: EnumTypeWrapper[_TestDynamicExtensions_DynamicEnumType]
    DYNAMIC_FOO: _TestDynamicExtensions_DynamicEnumType
    DYNAMIC_BAR: _TestDynamicExtensions_DynamicEnumType
    DYNAMIC_BAZ: _TestDynamicExtensions_DynamicEnumType

    class DynamicMessageType(Message):
        dynamic_field = ...  # type: int

        def __init__(self,
                     dynamic_field: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestDynamicExtensions.DynamicMessageType: ...
    scalar_extension = ...  # type: int
    enum_extension = ...  # type: _ForeignEnum
    dynamic_enum_extension = ...  # type: _TestDynamicExtensions_DynamicEnumType
    repeated_extension = ...  # type: RepeatedScalarFieldContainer[Text]
    packed_extension = ...  # type: RepeatedScalarFieldContainer[int]

    @property
    def message_extension(self) -> ForeignMessage: ...

    @property
    def dynamic_message_extension(
        self) -> TestDynamicExtensions.DynamicMessageType: ...

    def __init__(self,
                 scalar_extension: Optional[int] = ...,
                 enum_extension: Optional[_ForeignEnum] = ...,
                 dynamic_enum_extension: Optional[_TestDynamicExtensions_DynamicEnumType] = ...,
                 message_extension: Optional[ForeignMessage] = ...,
                 dynamic_message_extension: Optional[TestDynamicExtensions.DynamicMessageType] = ...,
                 repeated_extension: Optional[Iterable[Text]] = ...,
                 packed_extension: Optional[Iterable[int]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestDynamicExtensions: ...


class TestRepeatedScalarDifferentTagSizes(Message):
    repeated_fixed32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_fixed64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_int64 = ...  # type: RepeatedScalarFieldContainer[int]
    repeated_float = ...  # type: RepeatedScalarFieldContainer[float]
    repeated_uint64 = ...  # type: RepeatedScalarFieldContainer[int]

    def __init__(self,
                 repeated_fixed32: Optional[Iterable[int]] = ...,
                 repeated_int32: Optional[Iterable[int]] = ...,
                 repeated_fixed64: Optional[Iterable[int]] = ...,
                 repeated_int64: Optional[Iterable[int]] = ...,
                 repeated_float: Optional[Iterable[float]] = ...,
                 repeated_uint64: Optional[Iterable[int]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestRepeatedScalarDifferentTagSizes: ...


class TestParsingMerge(Message):
    class RepeatedFieldsGenerator(Message):
        class Group1(Message):

            @property
            def field1(self) -> TestAllTypes: ...

            def __init__(self,
                         field1: Optional[TestAllTypes] = ...,
                         ) -> None: ...

            @classmethod
            def FromString(
                cls, s: bytes) -> TestParsingMerge.RepeatedFieldsGenerator.Group1: ...

        class Group2(Message):

            @property
            def field1(self) -> TestAllTypes: ...

            def __init__(self,
                         field1: Optional[TestAllTypes] = ...,
                         ) -> None: ...

            @classmethod
            def FromString(
                cls, s: bytes) -> TestParsingMerge.RepeatedFieldsGenerator.Group2: ...

        @property
        def field1(self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

        @property
        def field2(self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

        @property
        def field3(self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

        @property
        def group1(
            self) -> RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedFieldsGenerator.Group1]: ...

        @property
        def group2(
            self) -> RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedFieldsGenerator.Group2]: ...

        @property
        def ext1(self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

        @property
        def ext2(self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

        def __init__(self,
                     field1: Optional[Iterable[TestAllTypes]] = ...,
                     field2: Optional[Iterable[TestAllTypes]] = ...,
                     field3: Optional[Iterable[TestAllTypes]] = ...,
                     group1: Optional[Iterable[TestParsingMerge.RepeatedFieldsGenerator.Group1]] = ...,
                     group2: Optional[Iterable[TestParsingMerge.RepeatedFieldsGenerator.Group2]] = ...,
                     ext1: Optional[Iterable[TestAllTypes]] = ...,
                     ext2: Optional[Iterable[TestAllTypes]] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestParsingMerge.RepeatedFieldsGenerator: ...

    class OptionalGroup(Message):

        @property
        def optional_group_all_types(self) -> TestAllTypes: ...

        def __init__(self,
                     optional_group_all_types: Optional[TestAllTypes] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestParsingMerge.OptionalGroup: ...

    class RepeatedGroup(Message):

        @property
        def repeated_group_all_types(self) -> TestAllTypes: ...

        def __init__(self,
                     repeated_group_all_types: Optional[TestAllTypes] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestParsingMerge.RepeatedGroup: ...

    @property
    def required_all_types(self) -> TestAllTypes: ...

    @property
    def optional_all_types(self) -> TestAllTypes: ...

    @property
    def repeated_all_types(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes]: ...

    @property
    def optionalgroup(self) -> TestParsingMerge.OptionalGroup: ...

    @property
    def repeatedgroup(
        self) -> RepeatedCompositeFieldContainer[TestParsingMerge.RepeatedGroup]: ...

    def __init__(self,
                 required_all_types: TestAllTypes,
                 optional_all_types: Optional[TestAllTypes] = ...,
                 repeated_all_types: Optional[Iterable[TestAllTypes]] = ...,
                 optionalgroup: Optional[TestParsingMerge.OptionalGroup] = ...,
                 repeatedgroup: Optional[Iterable[TestParsingMerge.RepeatedGroup]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestParsingMerge: ...


class TestCommentInjectionMessage(Message):
    a = ...  # type: Text

    def __init__(self,
                 a: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestCommentInjectionMessage: ...


class FooRequest(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> FooRequest: ...


class FooResponse(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> FooResponse: ...


class FooClientMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> FooClientMessage: ...


class FooServerMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> FooServerMessage: ...


class BarRequest(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> BarRequest: ...


class BarResponse(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> BarResponse: ...


class TestJsonName(Message):
    field_name1 = ...  # type: int
    fieldName2 = ...  # type: int
    FieldName3 = ...  # type: int
    _field_name4 = ...  # type: int
    FIELD_NAME5 = ...  # type: int
    field_name6 = ...  # type: int

    def __init__(self,
                 field_name1: Optional[int] = ...,
                 fieldName2: Optional[int] = ...,
                 FieldName3: Optional[int] = ...,
                 _field_name4: Optional[int] = ...,
                 FIELD_NAME5: Optional[int] = ...,
                 field_name6: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestJsonName: ...


class TestHugeFieldNumbers(Message):
    class OptionalGroup(Message):
        group_a = ...  # type: int

        def __init__(self,
                     group_a: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> TestHugeFieldNumbers.OptionalGroup: ...

    class StringStringMapEntry(Message):
        key = ...  # type: Text
        value = ...  # type: Text

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[Text] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> TestHugeFieldNumbers.StringStringMapEntry: ...
    optional_int32 = ...  # type: int
    fixed_32 = ...  # type: int
    repeated_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    packed_int32 = ...  # type: RepeatedScalarFieldContainer[int]
    optional_enum = ...  # type: _ForeignEnum
    optional_string = ...  # type: Text
    optional_bytes = ...  # type: bytes
    oneof_uint32 = ...  # type: int
    oneof_string = ...  # type: Text
    oneof_bytes = ...  # type: bytes

    @property
    def optional_message(self) -> ForeignMessage: ...

    @property
    def optionalgroup(self) -> TestHugeFieldNumbers.OptionalGroup: ...

    @property
    def string_string_map(self) -> MutableMapping[Text, Text]: ...

    @property
    def oneof_test_all_types(self) -> TestAllTypes: ...

    def __init__(self,
                 optional_int32: Optional[int] = ...,
                 fixed_32: Optional[int] = ...,
                 repeated_int32: Optional[Iterable[int]] = ...,
                 packed_int32: Optional[Iterable[int]] = ...,
                 optional_enum: Optional[_ForeignEnum] = ...,
                 optional_string: Optional[Text] = ...,
                 optional_bytes: Optional[bytes] = ...,
                 optional_message: Optional[ForeignMessage] = ...,
                 optionalgroup: Optional[TestHugeFieldNumbers.OptionalGroup] = ...,
                 string_string_map: Optional[Mapping[Text, Text]] = ...,
                 oneof_uint32: Optional[int] = ...,
                 oneof_test_all_types: Optional[TestAllTypes] = ...,
                 oneof_string: Optional[Text] = ...,
                 oneof_bytes: Optional[bytes] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestHugeFieldNumbers: ...


class TestExtensionInsideTable(Message):
    field1 = ...  # type: int
    field2 = ...  # type: int
    field3 = ...  # type: int
    field4 = ...  # type: int
    field6 = ...  # type: int
    field7 = ...  # type: int
    field8 = ...  # type: int
    field9 = ...  # type: int
    field10 = ...  # type: int

    def __init__(self,
                 field1: Optional[int] = ...,
                 field2: Optional[int] = ...,
                 field3: Optional[int] = ...,
                 field4: Optional[int] = ...,
                 field6: Optional[int] = ...,
                 field7: Optional[int] = ...,
                 field8: Optional[int] = ...,
                 field9: Optional[int] = ...,
                 field10: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestExtensionInsideTable: ...
