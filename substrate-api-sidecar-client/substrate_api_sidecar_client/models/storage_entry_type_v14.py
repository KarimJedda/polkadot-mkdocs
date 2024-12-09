from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageEntryTypeV14")


@_attrs_define
class StorageEntryTypeV14:
    """
    Attributes:
        hasher (Union[Unset, list[str]]): Returns a string denoting the storage hasher inside of an array.
        key (Union[Unset, str]): The SiLookupTypeId to identify the type.
        value (Union[Unset, str]): The SiLookupTypeId to identify the type.
    """

    hasher: Union[Unset, list[str]] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hasher: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hasher, Unset):
            hasher = self.hasher

        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hasher is not UNSET:
            field_dict["hasher"] = hasher
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hasher = cast(list[str], d.pop("hasher", UNSET))

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        storage_entry_type_v14 = cls(
            hasher=hasher,
            key=key,
            value=value,
        )

        storage_entry_type_v14.additional_properties = d
        return storage_entry_type_v14

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
