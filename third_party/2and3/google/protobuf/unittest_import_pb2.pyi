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

_ImportEnum = NewType('_ImportEnum', int)
ImportEnum: EnumTypeWrapper[_ImportEnum]
IMPORT_FOO: _ImportEnum
IMPORT_BAR: _ImportEnum
IMPORT_BAZ: _ImportEnum

_ImportEnumForMap = NewType('_ImportEnumForMap', int)
ImportEnumForMap: EnumTypeWrapper[_ImportEnumForMap]
UNKNOWN: _ImportEnumForMap
FOO: _ImportEnumForMap
BAR: _ImportEnumForMap


class ImportMessage(Message):
    d = ...  # type: int

    def __init__(self,
                 d: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ImportMessage: ...
