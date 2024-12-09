from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceEventDataStringValues")


@_attrs_define
class TraceEventDataStringValues:
    """Note these exact values will only be present for storage events.

    Attributes:
        key (Union[Unset, str]): The complete storage key for the entry.
        method (Union[Unset, str]): Normally one of Put or Get.
        result (Union[Unset, str]): Hex scale encoded storage value.
    """

    key: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        method = self.method

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if method is not UNSET:
            field_dict["method"] = method
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        method = d.pop("method", UNSET)

        result = d.pop("result", UNSET)

        trace_event_data_string_values = cls(
            key=key,
            method=method,
            result=result,
        )

        trace_event_data_string_values.additional_properties = d
        return trace_event_data_string_values

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
