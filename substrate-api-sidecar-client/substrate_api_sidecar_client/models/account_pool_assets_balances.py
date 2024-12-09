from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_balance import AssetsBalance
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="AccountPoolAssetsBalances")


@_attrs_define
class AccountPoolAssetsBalances:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        pool_assets (Union[Unset, list['AssetsBalance']]): An array of queried assets.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    pool_assets: Union[Unset, list["AssetsBalance"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        pool_assets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pool_assets, Unset):
            pool_assets = []
            for pool_assets_item_data in self.pool_assets:
                pool_assets_item = pool_assets_item_data.to_dict()
                pool_assets.append(pool_assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if pool_assets is not UNSET:
            field_dict["poolAssets"] = pool_assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.assets_balance import AssetsBalance
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        pool_assets = []
        _pool_assets = d.pop("poolAssets", UNSET)
        for pool_assets_item_data in _pool_assets or []:
            pool_assets_item = AssetsBalance.from_dict(pool_assets_item_data)

            pool_assets.append(pool_assets_item)

        account_pool_assets_balances = cls(
            at=at,
            pool_assets=pool_assets,
        )

        account_pool_assets_balances.additional_properties = d
        return account_pool_assets_balances

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
