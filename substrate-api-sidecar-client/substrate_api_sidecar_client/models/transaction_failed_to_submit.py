from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionFailedToSubmit")


@_attrs_define
class TransactionFailedToSubmit:
    """Error message when the node rejects the submitted transaction.

    Attributes:
        code (Union[Unset, float]):
        error (Union[Unset, str]): Failed to submit transaction.
        transaction (Union[Unset, str]):
        cause (Union[Unset, str]):
        stack (Union[Unset, str]):
    """

    code: Union[Unset, float] = UNSET
    error: Union[Unset, str] = UNSET
    transaction: Union[Unset, str] = UNSET
    cause: Union[Unset, str] = UNSET
    stack: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        error = self.error

        transaction = self.transaction

        cause = self.cause

        stack = self.stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if cause is not UNSET:
            field_dict["cause"] = cause
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        transaction = d.pop("transaction", UNSET)

        cause = d.pop("cause", UNSET)

        stack = d.pop("stack", UNSET)

        transaction_failed_to_submit = cls(
            code=code,
            error=error,
            transaction=transaction,
            cause=cause,
            stack=stack,
        )

        transaction_failed_to_submit.additional_properties = d
        return transaction_failed_to_submit

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
