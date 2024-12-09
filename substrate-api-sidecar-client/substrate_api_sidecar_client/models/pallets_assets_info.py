from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_info import AssetInfo
    from ..models.asset_metadata import AssetMetadata
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="PalletsAssetsInfo")


@_attrs_define
class PalletsAssetsInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        asset_info (Union[Unset, AssetInfo]):
        asset_metadata (Union[Unset, AssetMetadata]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    asset_info: Union[Unset, "AssetInfo"] = UNSET
    asset_metadata: Union[Unset, "AssetMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        asset_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.asset_info, Unset):
            asset_info = self.asset_info.to_dict()

        asset_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.asset_metadata, Unset):
            asset_metadata = self.asset_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if asset_info is not UNSET:
            field_dict["assetInfo"] = asset_info
        if asset_metadata is not UNSET:
            field_dict["assetMetadata"] = asset_metadata

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

        _asset_info = d.pop("assetInfo", UNSET)
        asset_info: Union[Unset, AssetInfo]
        if isinstance(_asset_info, Unset):
            asset_info = UNSET
        else:
            asset_info = AssetInfo.from_dict(_asset_info)

        _asset_metadata = d.pop("assetMetadata", UNSET)
        asset_metadata: Union[Unset, AssetMetadata]
        if isinstance(_asset_metadata, Unset):
            asset_metadata = UNSET
        else:
            asset_metadata = AssetMetadata.from_dict(_asset_metadata)

        pallets_assets_info = cls(
            at=at,
            asset_info=asset_info,
            asset_metadata=asset_metadata,
        )

        pallets_assets_info.additional_properties = d
        return pallets_assets_info

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
