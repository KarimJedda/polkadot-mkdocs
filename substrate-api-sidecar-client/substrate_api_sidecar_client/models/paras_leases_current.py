from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="ParasLeasesCurrent")


@_attrs_define
class ParasLeasesCurrent:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        lease_period_index (Union[Unset, str]): Current lease period index. This value may be null when the current
            block now, substracted by the leaseOffset is less then zero.
        end_of_lease_period (Union[Unset, str]): Last block (number) of the current lease period. This value may be null
            when `leasePeriodIndex` is null.
        current_lease_holders (Union[Unset, list[str]]): List of `paraId`s that currently hold a lease.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    lease_period_index: Union[Unset, str] = UNSET
    end_of_lease_period: Union[Unset, str] = UNSET
    current_lease_holders: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        lease_period_index = self.lease_period_index

        end_of_lease_period = self.end_of_lease_period

        current_lease_holders: Union[Unset, list[str]] = UNSET
        if not isinstance(self.current_lease_holders, Unset):
            current_lease_holders = self.current_lease_holders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if lease_period_index is not UNSET:
            field_dict["leasePeriodIndex"] = lease_period_index
        if end_of_lease_period is not UNSET:
            field_dict["endOfLeasePeriod"] = end_of_lease_period
        if current_lease_holders is not UNSET:
            field_dict["currentLeaseHolders"] = current_lease_holders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        lease_period_index = d.pop("leasePeriodIndex", UNSET)

        end_of_lease_period = d.pop("endOfLeasePeriod", UNSET)

        current_lease_holders = cast(list[str], d.pop("currentLeaseHolders", UNSET))

        paras_leases_current = cls(
            at=at,
            lease_period_index=lease_period_index,
            end_of_lease_period=end_of_lease_period,
            current_lease_holders=current_lease_holders,
        )

        paras_leases_current.additional_properties = d
        return paras_leases_current

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
