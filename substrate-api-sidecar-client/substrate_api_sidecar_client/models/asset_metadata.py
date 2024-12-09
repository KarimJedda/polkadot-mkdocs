from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetMetadata")


@_attrs_define
class AssetMetadata:
    """
    Attributes:
        deposit (Union[Unset, str]): The balance deposited for this metadata. This pays for the data stored in this
            struct.
        name (Union[Unset, str]): The user friendly name of this asset.
        symbol (Union[Unset, str]): The ticker symbol for this asset.
        decimals (Union[Unset, str]): The number of decimals this asset uses to represent one unit.
        is_frozen (Union[Unset, bool]): Whether the asset metadata may be changed by a non Force origin. Note, that some
            runtimes may not have support for isFrozen and if so the following will be returned `isFrozen does not exist for
            this runtime`
    """

    deposit: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    decimals: Union[Unset, str] = UNSET
    is_frozen: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deposit = self.deposit

        name = self.name

        symbol = self.symbol

        decimals = self.decimals

        is_frozen = self.is_frozen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        deposit = d.pop("deposit", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        decimals = d.pop("decimals", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        asset_metadata = cls(
            deposit=deposit,
            name=name,
            symbol=symbol,
            decimals=decimals,
            is_frozen=is_frozen,
        )

        asset_metadata.additional_properties = d
        return asset_metadata

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
