from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.balance_lock_reasons import BalanceLockReasons
from ..types import UNSET, Unset

T = TypeVar("T", bound="BalanceLock")


@_attrs_define
class BalanceLock:
    """
    Attributes:
        id (Union[Unset, str]): An identifier for this lock. Only one lock may be in existence for each identifier.
        amount (Union[Unset, str]): The amount below which the free balance may not drop with this lock in effect.
        reasons (Union[Unset, BalanceLockReasons]): Reasons for withdrawing balance.
    """

    id: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    reasons: Union[Unset, BalanceLockReasons] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        reasons: Union[Unset, str] = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: Union[Unset, BalanceLockReasons]
        if isinstance(_reasons, Unset):
            reasons = UNSET
        else:
            reasons = BalanceLockReasons(_reasons)

        balance_lock = cls(
            id=id,
            amount=amount,
            reasons=reasons,
        )

        balance_lock.additional_properties = d
        return balance_lock

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
