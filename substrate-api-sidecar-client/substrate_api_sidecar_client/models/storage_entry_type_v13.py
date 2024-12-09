from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageEntryTypeV13")


@_attrs_define
class StorageEntryTypeV13:
    """
    Attributes:
        hasher (Union[Unset, str]): Returns a string deonting the storage hasher.
        key (Union[Unset, str]): Key of the queried pallet storageId.
        value (Union[Unset, str]): Value of the queried pallet storageId.
        linked (Union[Unset, bool]):
    """

    hasher: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    linked: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hasher = self.hasher

        key = self.key

        value = self.value

        linked = self.linked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hasher is not UNSET:
            field_dict["hasher"] = hasher
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if linked is not UNSET:
            field_dict["linked"] = linked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hasher = d.pop("hasher", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        linked = d.pop("linked", UNSET)

        storage_entry_type_v13 = cls(
            hasher=hasher,
            key=key,
            value=value,
            linked=linked,
        )

        storage_entry_type_v13.additional_properties = d
        return storage_entry_type_v13

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
