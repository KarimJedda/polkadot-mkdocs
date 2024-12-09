from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_event_data_string_values import TraceEventDataStringValues


T = TypeVar("T", bound="TraceEventData")


@_attrs_define
class TraceEventData:
    """
    Attributes:
        string_values (Union[Unset, TraceEventDataStringValues]): Note these exact values will only be present for
            storage events.
    """

    string_values: Union[Unset, "TraceEventDataStringValues"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_values: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.string_values, Unset):
            string_values = self.string_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_values is not UNSET:
            field_dict["stringValues"] = string_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.trace_event_data_string_values import TraceEventDataStringValues

        d = src_dict.copy()
        _string_values = d.pop("stringValues", UNSET)
        string_values: Union[Unset, TraceEventDataStringValues]
        if isinstance(_string_values, Unset):
            string_values = UNSET
        else:
            string_values = TraceEventDataStringValues.from_dict(_string_values)

        trace_event_data = cls(
            string_values=string_values,
        )

        trace_event_data.additional_properties = d
        return trace_event_data

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
