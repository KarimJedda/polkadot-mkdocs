from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.fund_info import FundInfo


T = TypeVar("T", bound="ParasCrowdloanInfo")


@_attrs_define
class ParasCrowdloanInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        fund_info (Union[Unset, FundInfo]):
        lease_periods (Union[Unset, list[str]]): Lease periods the crowdloan can bid on.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    fund_info: Union[Unset, "FundInfo"] = UNSET
    lease_periods: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        fund_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund_info, Unset):
            fund_info = self.fund_info.to_dict()

        lease_periods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lease_periods, Unset):
            lease_periods = self.lease_periods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if fund_info is not UNSET:
            field_dict["fundInfo"] = fund_info
        if lease_periods is not UNSET:
            field_dict["leasePeriods"] = lease_periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.fund_info import FundInfo

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _fund_info = d.pop("fundInfo", UNSET)
        fund_info: Union[Unset, FundInfo]
        if isinstance(_fund_info, Unset):
            fund_info = UNSET
        else:
            fund_info = FundInfo.from_dict(_fund_info)

        lease_periods = cast(list[str], d.pop("leasePeriods", UNSET))

        paras_crowdloan_info = cls(
            at=at,
            fund_info=fund_info,
            lease_periods=lease_periods,
        )

        paras_crowdloan_info.additional_properties = d
        return paras_crowdloan_info

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
