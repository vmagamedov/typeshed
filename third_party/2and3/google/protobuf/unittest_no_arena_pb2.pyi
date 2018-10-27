from google.protobuf.internal.enum_type_wrapper import (
    EnumTypeWrapper,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer,
)
from google.protobuf.message import (
    Message,
)
from google.protobuf.unittest_arena_pb2 import (
    ArenaMessage,
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
    def optional_message(self) -> TestAllTypes.NestedMessage: ...

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

    @property
    def lazy_oneof_nested_message(self) -> TestAllTypes.NestedMessage: ...

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
                 optional_message: Optional[TestAllTypes.NestedMessage] = ...,
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
                 lazy_oneof_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestAllTypes: ...


class ForeignMessage(Message):
    c = ...  # type: int

    def __init__(self,
                 c: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ForeignMessage: ...


class TestNoArenaMessage(Message):

    @property
    def arena_message(self) -> ArenaMessage: ...

    def __init__(self,
                 arena_message: Optional[ArenaMessage] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestNoArenaMessage: ...
