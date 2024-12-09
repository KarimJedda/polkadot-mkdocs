from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_amount_currency import OperationAmountCurrency


T = TypeVar("T", bound="OperationAmount")


@_attrs_define
class OperationAmount:
    """
    Attributes:
        values (Union[Unset, str]):
        currency (Union[Unset, OperationAmountCurrency]):
    """

    values: Union[Unset, str] = UNSET
    currency: Union[Unset, "OperationAmountCurrency"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.operation_amount_currency import OperationAmountCurrency

        d = src_dict.copy()
        values = d.pop("values", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, OperationAmountCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = OperationAmountCurrency.from_dict(_currency)

        operation_amount = cls(
            values=values,
            currency=currency,
        )

        operation_amount.additional_properties = d
        return operation_amount

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
