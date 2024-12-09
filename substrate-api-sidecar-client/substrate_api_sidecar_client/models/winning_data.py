from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.winning_data_bid import WinningDataBid


T = TypeVar("T", bound="WinningData")


@_attrs_define
class WinningData:
    """A currently winning bid and the set of lease periods the bid is for. The
    `amount` of the bid is per lease period. The `bid` property will be `null`
    if no bid has been made for the corresponding `leaseSet`.

        Attributes:
            bid (Union[Unset, WinningDataBid]):
            lease_set (Union[Unset, list[str]]):
    """

    bid: Union[Unset, "WinningDataBid"] = UNSET
    lease_set: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bid, Unset):
            bid = self.bid.to_dict()

        lease_set: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lease_set, Unset):
            lease_set = self.lease_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bid is not UNSET:
            field_dict["bid"] = bid
        if lease_set is not UNSET:
            field_dict["leaseSet"] = lease_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.winning_data_bid import WinningDataBid

        d = src_dict.copy()
        _bid = d.pop("bid", UNSET)
        bid: Union[Unset, WinningDataBid]
        if isinstance(_bid, Unset):
            bid = UNSET
        else:
            bid = WinningDataBid.from_dict(_bid)

        lease_set = cast(list[str], d.pop("leaseSet", UNSET))

        winning_data = cls(
            bid=bid,
            lease_set=lease_set,
        )

        winning_data.additional_properties = d
        return winning_data

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
