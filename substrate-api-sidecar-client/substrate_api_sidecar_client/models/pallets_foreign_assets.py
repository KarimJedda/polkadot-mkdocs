from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.pallets_foreign_assets_info import PalletsForeignAssetsInfo


T = TypeVar("T", bound="PalletsForeignAssets")


@_attrs_define
class PalletsForeignAssets:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        items (Union[Unset, list['PalletsForeignAssetsInfo']]): Array containing the `AssetDetails` and `AssetMetadata`
            of every foreign asset.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    items: Union[Unset, list["PalletsForeignAssetsInfo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

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
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.pallets_foreign_assets_info import PalletsForeignAssetsInfo

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = PalletsForeignAssetsInfo.from_dict(items_item_data)

            items.append(items_item)

        pallets_foreign_assets = cls(
            at=at,
            items=items,
        )

        pallets_foreign_assets.additional_properties = d
        return pallets_foreign_assets

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
