from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_fee_estimate_failure_at import TransactionFeeEstimateFailureAt


T = TypeVar("T", bound="TransactionFeeEstimateFailure")


@_attrs_define
class TransactionFeeEstimateFailure:
    """
    Attributes:
        code (Union[Unset, float]):
        at (Union[Unset, TransactionFeeEstimateFailureAt]):
        error (Union[Unset, str]): Error description.
        transaction (Union[Unset, str]):
        block (Union[Unset, str]): Block hash of the block fee estimation was attempted at.
        cause (Union[Unset, str]): Error message from the client.
        stack (Union[Unset, str]):
    """

    code: Union[Unset, float] = UNSET
    at: Union[Unset, "TransactionFeeEstimateFailureAt"] = UNSET
    error: Union[Unset, str] = UNSET
    transaction: Union[Unset, str] = UNSET
    block: Union[Unset, str] = UNSET
    cause: Union[Unset, str] = UNSET
    stack: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        error = self.error

        transaction = self.transaction

        block = self.block

        cause = self.cause

        stack = self.stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if at is not UNSET:
            field_dict["at"] = at
        if error is not UNSET:
            field_dict["error"] = error
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if block is not UNSET:
            field_dict["block"] = block
        if cause is not UNSET:
            field_dict["cause"] = cause
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transaction_fee_estimate_failure_at import TransactionFeeEstimateFailureAt

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        _at = d.pop("at", UNSET)
        at: Union[Unset, TransactionFeeEstimateFailureAt]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = TransactionFeeEstimateFailureAt.from_dict(_at)

        error = d.pop("error", UNSET)

        transaction = d.pop("transaction", UNSET)

        block = d.pop("block", UNSET)

        cause = d.pop("cause", UNSET)

        stack = d.pop("stack", UNSET)

        transaction_fee_estimate_failure = cls(
            code=code,
            at=at,
            error=error,
            transaction=transaction,
            block=block,
            cause=cause,
            stack=stack,
        )

        transaction_fee_estimate_failure.additional_properties = d
        return transaction_fee_estimate_failure

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
