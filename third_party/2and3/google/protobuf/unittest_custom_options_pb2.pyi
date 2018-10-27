from google.protobuf.descriptor_pb2 import (
    FileOptions,
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
from typing import (
    Iterable,
    List,
    Optional,
    Text,
    Tuple,
    cast,
    NewType,
)


_MethodOpt1 = NewType('_MethodOpt1', int)
MethodOpt1: EnumTypeWrapper[_MethodOpt1]
METHODOPT1_VAL1: _MethodOpt1
METHODOPT1_VAL2: _MethodOpt1

_AggregateEnum = NewType('_AggregateEnum', int)
AggregateEnum: EnumTypeWrapper[_AggregateEnum]
VALUE: _AggregateEnum

_TestMessageWithCustomOptions_AnEnum = NewType('_TestMessageWithCustomOptions_AnEnum', int)


class TestMessageWithCustomOptions(Message):
    AnEnum: EnumTypeWrapper[_TestMessageWithCustomOptions_AnEnum]
    ANENUM_VAL1: _TestMessageWithCustomOptions_AnEnum
    ANENUM_VAL2: _TestMessageWithCustomOptions_AnEnum
    field1 = ...  # type: Text
    oneof_field = ...  # type: int

    def __init__(self,
                 field1: Optional[Text] = ...,
                 oneof_field: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMessageWithCustomOptions: ...


class CustomOptionFooRequest(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionFooRequest: ...


class CustomOptionFooResponse(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionFooResponse: ...


class CustomOptionFooClientMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionFooClientMessage: ...


class CustomOptionFooServerMessage(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionFooServerMessage: ...


_DummyMessageContainingEnum_TestEnumType = NewType('_DummyMessageContainingEnum_TestEnumType', int)


class DummyMessageContainingEnum(Message):
    TestEnumType: EnumTypeWrapper[_DummyMessageContainingEnum_TestEnumType]
    TEST_OPTION_ENUM_TYPE1: _DummyMessageContainingEnum_TestEnumType
    TEST_OPTION_ENUM_TYPE2: _DummyMessageContainingEnum_TestEnumType

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> DummyMessageContainingEnum: ...


class DummyMessageInvalidAsOptionType(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> DummyMessageInvalidAsOptionType: ...


class CustomOptionMinIntegerValues(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionMinIntegerValues: ...


class CustomOptionMaxIntegerValues(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionMaxIntegerValues: ...


class CustomOptionOtherValues(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> CustomOptionOtherValues: ...


class SettingRealsFromPositiveInts(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> SettingRealsFromPositiveInts: ...


class SettingRealsFromNegativeInts(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> SettingRealsFromNegativeInts: ...


class ComplexOptionType1(Message):
    foo = ...  # type: int
    foo2 = ...  # type: int
    foo3 = ...  # type: int
    foo4 = ...  # type: RepeatedScalarFieldContainer[int]

    def __init__(self,
                 foo: Optional[int] = ...,
                 foo2: Optional[int] = ...,
                 foo3: Optional[int] = ...,
                 foo4: Optional[Iterable[int]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ComplexOptionType1: ...


class ComplexOptionType2(Message):

    class ComplexOptionType4(Message):
        waldo = ...  # type: int

        def __init__(self,
                     waldo: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> ComplexOptionType2.ComplexOptionType4: ...
    baz = ...  # type: int

    @property
    def bar(self) -> ComplexOptionType1: ...

    @property
    def fred(self) -> ComplexOptionType2.ComplexOptionType4: ...

    @property
    def barney(
        self) -> RepeatedCompositeFieldContainer[ComplexOptionType2.ComplexOptionType4]: ...

    def __init__(self,
                 bar: Optional[ComplexOptionType1] = ...,
                 baz: Optional[int] = ...,
                 fred: Optional[ComplexOptionType2.ComplexOptionType4] = ...,
                 barney: Optional[Iterable[ComplexOptionType2.ComplexOptionType4]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ComplexOptionType2: ...


class ComplexOptionType3(Message):

    class ComplexOptionType5(Message):
        plugh = ...  # type: int

        def __init__(self,
                     plugh: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(
            cls, s: bytes) -> ComplexOptionType3.ComplexOptionType5: ...
    qux = ...  # type: int

    @property
    def complexoptiontype5(self) -> ComplexOptionType3.ComplexOptionType5: ...

    def __init__(self,
                 qux: Optional[int] = ...,
                 complexoptiontype5: Optional[ComplexOptionType3.ComplexOptionType5] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ComplexOptionType3: ...


class ComplexOpt6(Message):
    xyzzy = ...  # type: int

    def __init__(self,
                 xyzzy: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> ComplexOpt6: ...


class VariousComplexOptions(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> VariousComplexOptions: ...


class AggregateMessageSet(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> AggregateMessageSet: ...


class AggregateMessageSetElement(Message):
    s = ...  # type: Text

    def __init__(self,
                 s: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> AggregateMessageSetElement: ...


class Aggregate(Message):
    i = ...  # type: int
    s = ...  # type: Text

    @property
    def sub(self) -> Aggregate: ...

    @property
    def file(self) -> FileOptions: ...

    @property
    def mset(self) -> AggregateMessageSet: ...

    def __init__(self,
                 i: Optional[int] = ...,
                 s: Optional[Text] = ...,
                 sub: Optional[Aggregate] = ...,
                 file: Optional[FileOptions] = ...,
                 mset: Optional[AggregateMessageSet] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Aggregate: ...


class AggregateMessage(Message):
    fieldname = ...  # type: int

    def __init__(self,
                 fieldname: Optional[int] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> AggregateMessage: ...


_NestedOptionType_NestedEnum = NewType('_NestedOptionType_NestedEnum', int)


class NestedOptionType(Message):
    NestedEnum: EnumTypeWrapper[_NestedOptionType_NestedEnum]
    NESTED_ENUM_VALUE: _NestedOptionType_NestedEnum

    class NestedMessage(Message):
        nested_field = ...  # type: int

        def __init__(self,
                     nested_field: Optional[int] = ...,
                     ) -> None: ...

        @classmethod
        def FromString(cls, s: bytes) -> NestedOptionType.NestedMessage: ...

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> NestedOptionType: ...


_OldOptionType_TestEnum = NewType('_OldOptionType_TestEnum', int)


class OldOptionType(Message):
    TestEnum: EnumTypeWrapper[_OldOptionType_TestEnum]
    OLD_VALUE: _OldOptionType_TestEnum
    value = ...  # type: _OldOptionType_TestEnum

    def __init__(self,
                 value: _OldOptionType_TestEnum,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> OldOptionType: ...


_NewOptionType_TestEnum = NewType('_NewOptionType_TestEnum', int)


class NewOptionType(Message):
    TestEnum: EnumTypeWrapper[_NewOptionType_TestEnum]
    OLD_VALUE: _NewOptionType_TestEnum
    NEW_VALUE: _NewOptionType_TestEnum
    value = ...  # type: _NewOptionType_TestEnum

    def __init__(self,
                 value: _NewOptionType_TestEnum,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> NewOptionType: ...


class TestMessageWithRequiredEnumOption(Message):

    def __init__(self,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> TestMessageWithRequiredEnumOption: ...
