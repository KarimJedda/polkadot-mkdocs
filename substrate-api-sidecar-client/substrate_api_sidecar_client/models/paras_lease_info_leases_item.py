from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParasLeaseInfoLeasesItem")


@_attrs_define
class ParasLeaseInfoLeasesItem:
    """
    Attributes:
        lease_period_index (Union[Unset, str]):
        account (Union[Unset, str]):
        deposit (Union[Unset, str]):
    """

    lease_period_index: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    deposit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lease_period_index = self.lease_period_index

        account = self.account

        deposit = self.deposit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lease_period_index is not UNSET:
            field_dict["leasePeriodIndex"] = lease_period_index
        if account is not UNSET:
            field_dict["account"] = account
        if deposit is not UNSET:
            field_dict["deposit"] = deposit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lease_period_index = d.pop("leasePeriodIndex", UNSET)

        account = d.pop("account", UNSET)

        deposit = d.pop("deposit", UNSET)

        paras_lease_info_leases_item = cls(
            lease_period_index=lease_period_index,
            account=account,
            deposit=deposit,
        )

        paras_lease_info_leases_item.additional_properties = d
        return paras_lease_info_leases_item

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
