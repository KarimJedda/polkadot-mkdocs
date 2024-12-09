from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountValidation")


@_attrs_define
class AccountValidation:
    """
    Attributes:
        is_valid (Union[Unset, bool]): Whether the given address is valid ss58 formatted.
        ss_58_prefix (Union[Unset, str]): SS58 prefix of the given address. If the address is a valid base58 format, but
            incorrect ss58, a prefix for the given address will still be returned.
        network (Union[Unset, str]): The network based on which the given address is encoded.
        account_id (Union[Unset, str]): The account id of the given address.
    """

    is_valid: Union[Unset, bool] = UNSET
    ss_58_prefix: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        ss_58_prefix = self.ss_58_prefix

        network = self.network

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if ss_58_prefix is not UNSET:
            field_dict["ss58Prefix"] = ss_58_prefix
        if network is not UNSET:
            field_dict["network"] = network
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_valid = d.pop("isValid", UNSET)

        ss_58_prefix = d.pop("ss58Prefix", UNSET)

        network = d.pop("network", UNSET)

        account_id = d.pop("accountId", UNSET)

        account_validation = cls(
            is_valid=is_valid,
            ss_58_prefix=ss_58_prefix,
            network=network,
            account_id=account_id,
        )

        account_validation.additional_properties = d
        return account_validation

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
