from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsBalance")


@_attrs_define
class AssetsBalance:
    """
    Attributes:
        asset_id (Union[Unset, str]): The identifier of the asset.
        balance (Union[Unset, str]): The balance of the asset.
        is_frozen (Union[Unset, bool]): Whether the asset is frozen for non-admin transfers. Note, that some runtimes
            may not have support for isFrozen and if so the following will be returned `isFrozen does not exist for this
            runtime`
        is_sufficient (Union[Unset, bool]): Whether a non-zero balance of this asset is a deposit of sufficient value to
            account for the state bloat associated with its balance storage. If set to `true`, then non-zero balances may be
            stored without a `consumer` reference (and thus an ED in the Balances pallet or whatever else is used to control
            user-account state growth).
    """

    asset_id: Union[Unset, str] = UNSET
    balance: Union[Unset, str] = UNSET
    is_frozen: Union[Unset, bool] = UNSET
    is_sufficient: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        balance = self.balance

        is_frozen = self.is_frozen

        is_sufficient = self.is_sufficient

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if balance is not UNSET:
            field_dict["balance"] = balance
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen
        if is_sufficient is not UNSET:
            field_dict["isSufficient"] = is_sufficient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_id = d.pop("assetId", UNSET)

        balance = d.pop("balance", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        is_sufficient = d.pop("isSufficient", UNSET)

        assets_balance = cls(
            asset_id=asset_id,
            balance=balance,
            is_frozen=is_frozen,
            is_sufficient=is_sufficient,
        )

        assets_balance.additional_properties = d
        return assets_balance

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
