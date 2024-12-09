from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PalletsOnGoingReferendaReferendaItemDecisionDeposit")


@_attrs_define
class PalletsOnGoingReferendaReferendaItemDecisionDeposit:
    """A deposit which is required for a referendum to progress to the decision phase.

    Attributes:
        who (Union[Unset, str]): The account who placed the referendum's decision deposit.
        amount (Union[Unset, str]): The amount of the decision deposit.
    """

    who: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        who = self.who

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if who is not UNSET:
            field_dict["who"] = who
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        who = d.pop("who", UNSET)

        amount = d.pop("amount", UNSET)

        pallets_on_going_referenda_referenda_item_decision_deposit = cls(
            who=who,
            amount=amount,
        )

        pallets_on_going_referenda_referenda_item_decision_deposit.additional_properties = d
        return pallets_on_going_referenda_referenda_item_decision_deposit

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
