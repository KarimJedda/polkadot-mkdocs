from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSpan")


@_attrs_define
class TraceSpan:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        target (Union[Unset, str]):
        wasm (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    wasm: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_id = self.parent_id

        target = self.target

        wasm = self.wasm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if target is not UNSET:
            field_dict["target"] = target
        if wasm is not UNSET:
            field_dict["wasm"] = wasm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_id = d.pop("parentId", UNSET)

        target = d.pop("target", UNSET)

        wasm = d.pop("wasm", UNSET)

        trace_span = cls(
            id=id,
            name=name,
            parent_id=parent_id,
            target=target,
            wasm=wasm,
        )

        trace_span.additional_properties = d
        return trace_span

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
