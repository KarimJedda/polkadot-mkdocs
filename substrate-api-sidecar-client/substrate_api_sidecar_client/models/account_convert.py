from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountConvert")


@_attrs_define
class AccountConvert:
    """
    Attributes:
        ss_58_prefix (Union[Unset, str]): SS58 prefix based on which the account ID or Public Key (hex) is converted to
            an SS58 address.
        network (Union[Unset, str]): The network based on which the returned address is encoded. It depends on the
            prefix that was given as a query param.
        address (Union[Unset, str]): The returned SS58 address which is the result of the conversion of the account ID
            or Public Key (hex).
        account_id (Union[Unset, str]): The given account ID or Public Key (hex) that is converted to an SS58 address.
        scheme (Union[Unset, str]): The cryptographic scheme/algorithm used to encode the given account ID or Public Key
            (hex).
        public_key (Union[Unset, bool]): Whether the given path parameter is a Public Key (hex) or not.
    """

    ss_58_prefix: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    scheme: Union[Unset, str] = UNSET
    public_key: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ss_58_prefix = self.ss_58_prefix

        network = self.network

        address = self.address

        account_id = self.account_id

        scheme = self.scheme

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ss_58_prefix is not UNSET:
            field_dict["ss58Prefix"] = ss_58_prefix
        if network is not UNSET:
            field_dict["network"] = network
        if address is not UNSET:
            field_dict["address"] = address
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ss_58_prefix = d.pop("ss58Prefix", UNSET)

        network = d.pop("network", UNSET)

        address = d.pop("address", UNSET)

        account_id = d.pop("accountId", UNSET)

        scheme = d.pop("scheme", UNSET)

        public_key = d.pop("publicKey", UNSET)

        account_convert = cls(
            ss_58_prefix=ss_58_prefix,
            network=network,
            address=address,
            account_id=account_id,
            scheme=scheme,
            public_key=public_key,
        )

        account_convert.additional_properties = d
        return account_convert

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
