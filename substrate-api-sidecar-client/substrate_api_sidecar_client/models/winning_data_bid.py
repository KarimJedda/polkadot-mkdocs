from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WinningDataBid")


@_attrs_define
class WinningDataBid:
    """
    Attributes:
        account_id (Union[Unset, str]):
        para_id (Union[Unset, str]):
        amount (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    para_id: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        para_id = self.para_id

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if para_id is not UNSET:
            field_dict["paraId"] = para_id
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        para_id = d.pop("paraId", UNSET)

        amount = d.pop("amount", UNSET)

        winning_data_bid = cls(
            account_id=account_id,
            para_id=para_id,
            amount=amount,
        )

        winning_data_bid.additional_properties = d
        return winning_data_bid

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
