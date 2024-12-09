from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.liquidity_pool import LiquidityPool


T = TypeVar("T", bound="LiquidityPools")


@_attrs_define
class LiquidityPools:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        pools (Union[Unset, list['LiquidityPool']]): Array containing existent liquidity pool's token id. Example:
            [{"reserves":[{"parents":"1","interior":{"here": null}},{"parents":"0","interior":{"x2":[{"palletInstance":
            "50"},{"generalIndex":"2"}]}}],"lpToken":{"lpToken":"1"} },{"lpToken":{"lpToken":"0"}}].
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    pools: Union[Unset, list["LiquidityPool"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        pools: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pools, Unset):
            pools = []
            for pools_item_data in self.pools:
                pools_item = pools_item_data.to_dict()
                pools.append(pools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if pools is not UNSET:
            field_dict["pools"] = pools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.liquidity_pool import LiquidityPool

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        pools = []
        _pools = d.pop("pools", UNSET)
        for pools_item_data in _pools or []:
            pools_item = LiquidityPool.from_dict(pools_item_data)

            pools.append(pools_item)

        liquidity_pools = cls(
            at=at,
            pools=pools,
        )

        liquidity_pools.additional_properties = d
        return liquidity_pools

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
