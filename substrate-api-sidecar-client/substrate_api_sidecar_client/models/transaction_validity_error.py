from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_validity_error_error_type import TransactionValidityErrorErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionValidityError")


@_attrs_define
class TransactionValidityError:
    """The error result from an invalid transaction submitted via the `dry-run` endpoint.

    Attributes:
        error_type (Union[Unset, TransactionValidityErrorErrorType]): The type of transaction error, either
            `Unimplemented` or `VersionedConversionFailed`.
    """

    error_type: Union[Unset, TransactionValidityErrorErrorType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type: Union[Unset, str] = UNSET
        if not isinstance(self.error_type, Unset):
            error_type = self.error_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_type is not UNSET:
            field_dict["errorType"] = error_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _error_type = d.pop("errorType", UNSET)
        error_type: Union[Unset, TransactionValidityErrorErrorType]
        if isinstance(_error_type, Unset):
            error_type = UNSET
        else:
            error_type = TransactionValidityErrorErrorType(_error_type)

        transaction_validity_error = cls(
            error_type=error_type,
        )

        transaction_validity_error.additional_properties = d
        return transaction_validity_error

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
