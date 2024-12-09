from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_info import AssetInfo
    from ..models.asset_metadata import AssetMetadata
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="PalletsPoolAssetsInfo")


@_attrs_define
class PalletsPoolAssetsInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        pool_asset_info (Union[Unset, AssetInfo]):
        pool_asset_metadata (Union[Unset, AssetMetadata]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    pool_asset_info: Union[Unset, "AssetInfo"] = UNSET
    pool_asset_metadata: Union[Unset, "AssetMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        pool_asset_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool_asset_info, Unset):
            pool_asset_info = self.pool_asset_info.to_dict()

        pool_asset_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool_asset_metadata, Unset):
            pool_asset_metadata = self.pool_asset_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if pool_asset_info is not UNSET:
            field_dict["poolAssetInfo"] = pool_asset_info
        if pool_asset_metadata is not UNSET:
            field_dict["poolAssetMetadata"] = pool_asset_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.asset_info import AssetInfo
        from ..models.asset_metadata import AssetMetadata
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _pool_asset_info = d.pop("poolAssetInfo", UNSET)
        pool_asset_info: Union[Unset, AssetInfo]
        if isinstance(_pool_asset_info, Unset):
            pool_asset_info = UNSET
        else:
            pool_asset_info = AssetInfo.from_dict(_pool_asset_info)

        _pool_asset_metadata = d.pop("poolAssetMetadata", UNSET)
        pool_asset_metadata: Union[Unset, AssetMetadata]
        if isinstance(_pool_asset_metadata, Unset):
            pool_asset_metadata = UNSET
        else:
            pool_asset_metadata = AssetMetadata.from_dict(_pool_asset_metadata)

        pallets_pool_assets_info = cls(
            at=at,
            pool_asset_info=pool_asset_info,
            pool_asset_metadata=pool_asset_metadata,
        )

        pallets_pool_assets_info.additional_properties = d
        return pallets_pool_assets_info

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
