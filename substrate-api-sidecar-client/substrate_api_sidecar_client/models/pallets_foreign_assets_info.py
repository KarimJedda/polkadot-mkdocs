from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_info import AssetInfo
    from ..models.asset_metadata import AssetMetadata


T = TypeVar("T", bound="PalletsForeignAssetsInfo")


@_attrs_define
class PalletsForeignAssetsInfo:
    """
    Attributes:
        foreign_asset_info (Union[Unset, AssetInfo]):
        foreign_asset_metadata (Union[Unset, AssetMetadata]):
    """

    foreign_asset_info: Union[Unset, "AssetInfo"] = UNSET
    foreign_asset_metadata: Union[Unset, "AssetMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        foreign_asset_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.foreign_asset_info, Unset):
            foreign_asset_info = self.foreign_asset_info.to_dict()

        foreign_asset_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.foreign_asset_metadata, Unset):
            foreign_asset_metadata = self.foreign_asset_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if foreign_asset_info is not UNSET:
            field_dict["foreignAssetInfo"] = foreign_asset_info
        if foreign_asset_metadata is not UNSET:
            field_dict["foreignAssetMetadata"] = foreign_asset_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.asset_info import AssetInfo
        from ..models.asset_metadata import AssetMetadata

        d = src_dict.copy()
        _foreign_asset_info = d.pop("foreignAssetInfo", UNSET)
        foreign_asset_info: Union[Unset, AssetInfo]
        if isinstance(_foreign_asset_info, Unset):
            foreign_asset_info = UNSET
        else:
            foreign_asset_info = AssetInfo.from_dict(_foreign_asset_info)

        _foreign_asset_metadata = d.pop("foreignAssetMetadata", UNSET)
        foreign_asset_metadata: Union[Unset, AssetMetadata]
        if isinstance(_foreign_asset_metadata, Unset):
            foreign_asset_metadata = UNSET
        else:
            foreign_asset_metadata = AssetMetadata.from_dict(_foreign_asset_metadata)

        pallets_foreign_assets_info = cls(
            foreign_asset_info=foreign_asset_info,
            foreign_asset_metadata=foreign_asset_metadata,
        )

        pallets_foreign_assets_info.additional_properties = d
        return pallets_foreign_assets_info

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
