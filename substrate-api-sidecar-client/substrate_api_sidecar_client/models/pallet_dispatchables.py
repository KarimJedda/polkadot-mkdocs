from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.pallet_dispatchables_item_metadata import PalletDispatchablesItemMetadata


T = TypeVar("T", bound="PalletDispatchables")


@_attrs_define
class PalletDispatchables:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        pallet (Union[Unset, str]): Name of the pallet. Example: democracy.
        pallet_index (Union[Unset, str]): Index of the pallet for looking up dispatchables. Example: 14.
        items (Union[Unset, list['PalletDispatchablesItemMetadata']]): Array containing metadata for each dispatchable
            entry of the pallet.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    pallet: Union[Unset, str] = UNSET
    pallet_index: Union[Unset, str] = UNSET
    items: Union[Unset, list["PalletDispatchablesItemMetadata"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

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
        if at is not UNSET:
            field_dict["at"] = at
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if pallet_index is not UNSET:
            field_dict["palletIndex"] = pallet_index
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.pallet_dispatchables_item_metadata import PalletDispatchablesItemMetadata

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        pallet = d.pop("pallet", UNSET)

        pallet_index = d.pop("palletIndex", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = PalletDispatchablesItemMetadata.from_dict(items_item_data)

            items.append(items_item)

        pallet_dispatchables = cls(
            at=at,
            pallet=pallet,
            pallet_index=pallet_index,
            items=items,
        )

        pallet_dispatchables.additional_properties = d
        return pallet_dispatchables

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
