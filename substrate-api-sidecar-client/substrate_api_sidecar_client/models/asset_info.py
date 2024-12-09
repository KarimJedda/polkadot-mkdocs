from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInfo")


@_attrs_define
class AssetInfo:
    """
    Attributes:
        owner (Union[Unset, str]): Owner of the assets privileges.
        issuer (Union[Unset, str]): The `AccountId` able to mint tokens.
        admin (Union[Unset, str]): The `AccountId` that can thaw tokens, force transfers and burn token from any
            account.
        freezer (Union[Unset, str]): The `AccountId` that can freeze tokens.
        supply (Union[Unset, str]): The total supply across accounts.
        deposit (Union[Unset, str]): The balance deposited for this. This pays for the data stored.
        min_balance (Union[Unset, str]): The ED for virtual accounts.
        is_sufficient (Union[Unset, bool]): If `true`, then any account with this asset is given a provider reference.
            Otherwise, it requires a consumer reference.
        accounts (Union[Unset, str]): The total number of accounts.
        sufficients (Union[Unset, str]): The total number of accounts for which is placed a self-sufficient reference.
        approvals (Union[Unset, str]): The total number of approvals.
        status (Union[Unset, str]): The status of the asset.
    """

    owner: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    admin: Union[Unset, str] = UNSET
    freezer: Union[Unset, str] = UNSET
    supply: Union[Unset, str] = UNSET
    deposit: Union[Unset, str] = UNSET
    min_balance: Union[Unset, str] = UNSET
    is_sufficient: Union[Unset, bool] = UNSET
    accounts: Union[Unset, str] = UNSET
    sufficients: Union[Unset, str] = UNSET
    approvals: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner

        issuer = self.issuer

        admin = self.admin

        freezer = self.freezer

        supply = self.supply

        deposit = self.deposit

        min_balance = self.min_balance

        is_sufficient = self.is_sufficient

        accounts = self.accounts

        sufficients = self.sufficients

        approvals = self.approvals

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner is not UNSET:
            field_dict["owner"] = owner
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if admin is not UNSET:
            field_dict["admin"] = admin
        if freezer is not UNSET:
            field_dict["freezer"] = freezer
        if supply is not UNSET:
            field_dict["supply"] = supply
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if min_balance is not UNSET:
            field_dict["minBalance"] = min_balance
        if is_sufficient is not UNSET:
            field_dict["isSufficient"] = is_sufficient
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if sufficients is not UNSET:
            field_dict["sufficients"] = sufficients
        if approvals is not UNSET:
            field_dict["approvals"] = approvals
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        owner = d.pop("owner", UNSET)

        issuer = d.pop("issuer", UNSET)

        admin = d.pop("admin", UNSET)

        freezer = d.pop("freezer", UNSET)

        supply = d.pop("supply", UNSET)

        deposit = d.pop("deposit", UNSET)

        min_balance = d.pop("minBalance", UNSET)

        is_sufficient = d.pop("isSufficient", UNSET)

        accounts = d.pop("accounts", UNSET)

        sufficients = d.pop("sufficients", UNSET)

        approvals = d.pop("approvals", UNSET)

        status = d.pop("status", UNSET)

        asset_info = cls(
            owner=owner,
            issuer=issuer,
            admin=admin,
            freezer=freezer,
            supply=supply,
            deposit=deposit,
            min_balance=min_balance,
            is_sufficient=is_sufficient,
            accounts=accounts,
            sufficients=sufficients,
            approvals=approvals,
            status=status,
        )

        asset_info.additional_properties = d
        return asset_info

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
