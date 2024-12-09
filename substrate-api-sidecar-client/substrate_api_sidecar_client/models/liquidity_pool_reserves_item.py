from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidity_pool_reserves_item_interior import LiquidityPoolReservesItemInterior


T = TypeVar("T", bound="LiquidityPoolReservesItem")


@_attrs_define
class LiquidityPoolReservesItem:
    """
    Attributes:
        parents (Union[Unset, str]):
        interior (Union[Unset, LiquidityPoolReservesItemInterior]):
    """

    parents: Union[Unset, str] = UNSET
    interior: Union[Unset, "LiquidityPoolReservesItemInterior"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parents = self.parents

        interior: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interior, Unset):
            interior = self.interior.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parents is not UNSET:
            field_dict["parents"] = parents
        if interior is not UNSET:
            field_dict["interior"] = interior

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.liquidity_pool_reserves_item_interior import LiquidityPoolReservesItemInterior

        d = src_dict.copy()
        parents = d.pop("parents", UNSET)

        _interior = d.pop("interior", UNSET)
        interior: Union[Unset, LiquidityPoolReservesItemInterior]
        if isinstance(_interior, Unset):
            interior = UNSET
        else:
            interior = LiquidityPoolReservesItemInterior.from_dict(_interior)

        liquidity_pool_reserves_item = cls(
            parents=parents,
            interior=interior,
        )

        liquidity_pool_reserves_item.additional_properties = d
        return liquidity_pool_reserves_item

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
