from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionDispatchOutcome")


@_attrs_define
class TransactionDispatchOutcome:
    """The result of a valid transaction submitted via the `dry-run` endpoint.

    Attributes:
        actual_weight (Union[Unset, str]): The actual weight of the transaction.
        pays_fee (Union[Unset, str]): Whether the transaction pays a fee.
    """

    actual_weight: Union[Unset, str] = UNSET
    pays_fee: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_weight = self.actual_weight

        pays_fee = self.pays_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_weight is not UNSET:
            field_dict["actualWeight"] = actual_weight
        if pays_fee is not UNSET:
            field_dict["paysFee"] = pays_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        actual_weight = d.pop("actualWeight", UNSET)

        pays_fee = d.pop("paysFee", UNSET)

        transaction_dispatch_outcome = cls(
            actual_weight=actual_weight,
            pays_fee=pays_fee,
        )

        transaction_dispatch_outcome.additional_properties = d
        return transaction_dispatch_outcome

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
