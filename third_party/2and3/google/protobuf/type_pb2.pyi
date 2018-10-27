from google.protobuf.any_pb2 import (
    Any,
)
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
from google.protobuf.source_context_pb2 import (
    SourceContext,
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

_Syntax = NewType('_Syntax', int)
Syntax: EnumTypeWrapper[_Syntax]
SYNTAX_PROTO2: _Syntax
SYNTAX_PROTO3: _Syntax


class Type(Message):
    name = ...  # type: Text
    oneofs = ...  # type: RepeatedScalarFieldContainer[Text]
    syntax = ...  # type: _Syntax

    @property
    def fields(self) -> RepeatedCompositeFieldContainer[Field]: ...

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    @property
    def source_context(self) -> SourceContext: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 fields: Optional[Iterable[Field]] = ...,
                 oneofs: Optional[Iterable[Text]] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 source_context: Optional[SourceContext] = ...,
                 syntax: Optional[_Syntax] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Type: ...


_Field_Kind = NewType('_Field_Kind', int)
_Field_Cardinality = NewType('_Field_Cardinality', int)


class Field(Message):
    Kind: EnumTypeWrapper[_Field_Kind]
    TYPE_UNKNOWN: _Field_Kind
    TYPE_DOUBLE: _Field_Kind
    TYPE_FLOAT: _Field_Kind
    TYPE_INT64: _Field_Kind
    TYPE_UINT64: _Field_Kind
    TYPE_INT32: _Field_Kind
    TYPE_FIXED64: _Field_Kind
    TYPE_FIXED32: _Field_Kind
    TYPE_BOOL: _Field_Kind
    TYPE_STRING: _Field_Kind
    TYPE_GROUP: _Field_Kind
    TYPE_MESSAGE: _Field_Kind
    TYPE_BYTES: _Field_Kind
    TYPE_UINT32: _Field_Kind
    TYPE_ENUM: _Field_Kind
    TYPE_SFIXED32: _Field_Kind
    TYPE_SFIXED64: _Field_Kind
    TYPE_SINT32: _Field_Kind
    TYPE_SINT64: _Field_Kind
    Cardinality: EnumTypeWrapper[_Field_Cardinality]
    CARDINALITY_UNKNOWN: _Field_Cardinality
    CARDINALITY_OPTIONAL: _Field_Cardinality
    CARDINALITY_REQUIRED: _Field_Cardinality
    CARDINALITY_REPEATED: _Field_Cardinality
    kind = ...  # type: _Field_Kind
    cardinality = ...  # type: _Field_Cardinality
    number = ...  # type: int
    name = ...  # type: Text
    type_url = ...  # type: Text
    oneof_index = ...  # type: int
    packed = ...  # type: bool
    json_name = ...  # type: Text
    default_value = ...  # type: Text

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
                 kind: Optional[_Field_Kind] = ...,
                 cardinality: Optional[_Field_Cardinality] = ...,
                 number: Optional[int] = ...,
                 name: Optional[Text] = ...,
                 type_url: Optional[Text] = ...,
                 oneof_index: Optional[int] = ...,
                 packed: Optional[bool] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 json_name: Optional[Text] = ...,
                 default_value: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Field: ...


class Enum(Message):
    name = ...  # type: Text
    syntax = ...  # type: _Syntax

    @property
    def enumvalue(self) -> RepeatedCompositeFieldContainer[EnumValue]: ...

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    @property
    def source_context(self) -> SourceContext: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 enumvalue: Optional[Iterable[EnumValue]] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 source_context: Optional[SourceContext] = ...,
                 syntax: Optional[_Syntax] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Enum: ...


class EnumValue(Message):
    name = ...  # type: Text
    number = ...  # type: int

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 number: Optional[int] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> EnumValue: ...


class Option(Message):
    name = ...  # type: Text

    @property
    def value(self) -> Any: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 value: Optional[Any] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Option: ...
