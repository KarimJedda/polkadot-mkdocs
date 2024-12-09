from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountProxyInfoDelegatedAccountsItem")


@_attrs_define
class AccountProxyInfoDelegatedAccountsItem:
    """
    Attributes:
        delegate (Union[Unset, str]): Delegate address for the given proxy.
        delay (Union[Unset, str]): The announcement period required of the initial proxy. Will generally be zero.
        proxy_type (Union[Unset, str]): The permissions allowed for this proxy account.
    """

    delegate: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    proxy_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegate = self.delegate

        delay = self.delay

        proxy_type = self.proxy_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delegate is not UNSET:
            field_dict["delegate"] = delegate
        if delay is not UNSET:
            field_dict["delay"] = delay
        if proxy_type is not UNSET:
            field_dict["proxyType"] = proxy_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        delegate = d.pop("delegate", UNSET)

        delay = d.pop("delay", UNSET)

        proxy_type = d.pop("proxyType", UNSET)

        account_proxy_info_delegated_accounts_item = cls(
            delegate=delegate,
            delay=delay,
            proxy_type=proxy_type,
        )

        account_proxy_info_delegated_accounts_item.additional_properties = d
        return account_proxy_info_delegated_accounts_item

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
