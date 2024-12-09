from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DigestItem")


@_attrs_define
class DigestItem:
    """
    Attributes:
        type_ (Union[Unset, str]):
        index (Union[Unset, str]):
        value (Union[Unset, list[str]]):
    """

    type_: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    value: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        index = self.index

        value: Union[Unset, list[str]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if index is not UNSET:
            field_dict["index"] = index
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type", UNSET)

        index = d.pop("index", UNSET)

        value = cast(list[str], d.pop("value", UNSET))

        digest_item = cls(
            type_=type_,
            index=index,
            value=value,
        )

        digest_item.additional_properties = d
        return digest_item

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
