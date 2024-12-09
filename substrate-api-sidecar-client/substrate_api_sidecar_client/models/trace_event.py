from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_event_data import TraceEventData


T = TypeVar("T", bound="TraceEvent")


@_attrs_define
class TraceEvent:
    """
    Attributes:
        data (Union[Unset, TraceEventData]):
        parent_id (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    data: Union[Unset, "TraceEventData"] = UNSET
    parent_id: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        parent_id = self.parent_id

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.trace_event_data import TraceEventData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, TraceEventData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TraceEventData.from_dict(_data)

        parent_id = d.pop("parentId", UNSET)

        target = d.pop("target", UNSET)

        trace_event = cls(
            data=data,
            parent_id=parent_id,
            target=target,
        )

        trace_event.additional_properties = d
        return trace_event

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
