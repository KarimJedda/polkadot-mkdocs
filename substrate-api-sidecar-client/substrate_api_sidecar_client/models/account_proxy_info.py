from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_proxy_info_delegated_accounts_item import AccountProxyInfoDelegatedAccountsItem
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="AccountProxyInfo")


@_attrs_define
class AccountProxyInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        delegated_accounts (Union[Unset, list['AccountProxyInfoDelegatedAccountsItem']]):
        deposit_held (Union[Unset, str]): The held deposit.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    delegated_accounts: Union[Unset, list["AccountProxyInfoDelegatedAccountsItem"]] = UNSET
    deposit_held: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        delegated_accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delegated_accounts, Unset):
            delegated_accounts = []
            for delegated_accounts_item_data in self.delegated_accounts:
                delegated_accounts_item = delegated_accounts_item_data.to_dict()
                delegated_accounts.append(delegated_accounts_item)

        deposit_held = self.deposit_held

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if delegated_accounts is not UNSET:
            field_dict["delegatedAccounts"] = delegated_accounts
        if deposit_held is not UNSET:
            field_dict["depositHeld"] = deposit_held

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.account_proxy_info_delegated_accounts_item import AccountProxyInfoDelegatedAccountsItem
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        delegated_accounts = []
        _delegated_accounts = d.pop("delegatedAccounts", UNSET)
        for delegated_accounts_item_data in _delegated_accounts or []:
            delegated_accounts_item = AccountProxyInfoDelegatedAccountsItem.from_dict(delegated_accounts_item_data)

            delegated_accounts.append(delegated_accounts_item)

        deposit_held = d.pop("depositHeld", UNSET)

        account_proxy_info = cls(
            at=at,
            delegated_accounts=delegated_accounts,
            deposit_held=deposit_held,
        )

        account_proxy_info.additional_properties = d
        return account_proxy_info

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
