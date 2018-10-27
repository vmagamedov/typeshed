from google.protobuf.internal.enum_type_wrapper import (
    EnumTypeWrapper,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
)
from google.protobuf.internal import well_known_types

from google.protobuf.message import (
    Message,
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


_NullValue = NewType('_NullValue', int)
NullValue: EnumTypeWrapper[_NullValue]
NULL_VALUE: _NullValue


class Struct(Message, well_known_types.Struct):
    class FieldsEntry(Message):
        key = ...  # type: Text

        @property
        def value(self) -> Value: ...

        def __init__(self,
                     key: Optional[Text] = ...,
                     value: Optional[Value] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> Struct.FieldsEntry: ...

    @property
    def fields(self) -> MutableMapping[Text, Value]: ...

    def __init__(self,
                 fields: Optional[Mapping[Text, Value]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Struct: ...


class _Value(Message):
    null_value = ...  # type: _NullValue
    number_value = ...  # type: float
    string_value = ...  # type: Text
    bool_value = ...  # type: bool

    @property
    def struct_value(self) -> Struct: ...

    @property
    def list_value(self) -> ListValue: ...

    def __init__(self,
                 null_value: Optional[_NullValue] = ...,
                 number_value: Optional[float] = ...,
                 string_value: Optional[Text] = ...,
                 bool_value: Optional[bool] = ...,
                 struct_value: Optional[Struct] = ...,
                 list_value: Optional[ListValue] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> _Value: ...


Value = _Value


class ListValue(Message, well_known_types.ListValue):

    @property
    def values(self) -> RepeatedCompositeFieldContainer[Value]: ...

    def __init__(self,
                 values: Optional[Iterable[Value]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ListValue: ...
