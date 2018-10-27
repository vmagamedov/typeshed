from google.protobuf.internal.enum_type_wrapper import (
    EnumTypeWrapper,
)
from google.protobuf.message import (
    Message,
)
from typing import (
    List,
    Optional,
    Tuple,
    cast,
    NewType,
)

_TestEnum = NewType('_TestEnum', int)
TestEnum: EnumTypeWrapper[_TestEnum]
FOO: _TestEnum


class TestMessage(Message):
    a = ...  # type: int

    def __init__(self,
                 a: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMessage: ...
