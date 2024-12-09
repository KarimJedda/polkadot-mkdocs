from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pallet_storage_item_metadata import PalletStorageItemMetadata


T = TypeVar("T", bound="PalletStorage")


@_attrs_define
class PalletStorage:
    """
    Attributes:
        pallet (Union[Unset, str]): Name of the pallet. Example: democracy.
        pallet_index (Union[Unset, str]): Index of the pallet for looking up storage. Example: 15.
        items (Union[Unset, list['PalletStorageItemMetadata']]): Array containing metadata for each storage entry of the
            pallet.
    """

    pallet: Union[Unset, str] = UNSET
    pallet_index: Union[Unset, str] = UNSET
    items: Union[Unset, list["PalletStorageItemMetadata"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet = self.pallet

        pallet_index = self.pallet_index

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if pallet_index is not UNSET:
            field_dict["palletIndex"] = pallet_index
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pallet_storage_item_metadata import PalletStorageItemMetadata

        d = src_dict.copy()
        pallet = d.pop("pallet", UNSET)

        pallet_index = d.pop("palletIndex", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = PalletStorageItemMetadata.from_dict(items_item_data)

            items.append(items_item)

        pallet_storage = cls(
            pallet=pallet,
            pallet_index=pallet_index,
            items=items,
        )

        pallet_storage.additional_properties = d
        return pallet_storage

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
