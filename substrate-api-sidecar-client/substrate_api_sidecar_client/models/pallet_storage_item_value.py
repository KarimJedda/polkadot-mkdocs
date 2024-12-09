from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PalletStorageItemValue")


@_attrs_define
class PalletStorageItemValue:
    """Value returned by this storage query.

    Example:
        {'Ongoing': {'end': '1612800', 'proposalHash':
            '0x7de70fc8be782076d0b5772be77153d172a5381c72dd56d3385e25f62abf507e', 'threshold': 'Supermajorityapproval',
            'delay': '403200', 'tally': {'ayes': '41925212461400000', 'nays': '214535586500000', 'turnout':
            '34485320658000000'}}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pallet_storage_item_value = cls()

        pallet_storage_item_value.additional_properties = d
        return pallet_storage_item_value

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
