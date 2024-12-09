from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_dry_run_result_type import TransactionDryRunResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_dispatch_error import TransactionDispatchError
    from ..models.transaction_dispatch_outcome import TransactionDispatchOutcome
    from ..models.transaction_validity_error import TransactionValidityError


T = TypeVar("T", bound="TransactionDryRun")


@_attrs_define
class TransactionDryRun:
    """References:
    - `PostDispatchInfo`: https://docs.rs/frame-support/38.0.0/frame_support/dispatch/struct.PostDispatchInfo.html
    - `DispatchError`: https://docs.rs/sp-runtime/39.0.1/sp_runtime/enum.DispatchError.html
    - `Error Type`: https://paritytech.github.io/polkadot-sdk/master/xcm_runtime_apis/dry_run/enum.Error.html

      Attributes:
          result_type (Union[Unset, TransactionDryRunResultType]): The result will be either a `DispatchOutcome` if the
              transaction is valid, a `DispatchError` if the transaction failed, or a `TransactionValidityError` if the
              transaction is invalid.
          result (Union['TransactionDispatchError', 'TransactionDispatchOutcome', 'TransactionValidityError', Unset]):
    """

    result_type: Union[Unset, TransactionDryRunResultType] = UNSET
    result: Union["TransactionDispatchError", "TransactionDispatchOutcome", "TransactionValidityError", Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_dispatch_error import TransactionDispatchError
        from ..models.transaction_dispatch_outcome import TransactionDispatchOutcome

        result_type: Union[Unset, str] = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value

        result: Union[Unset, dict[str, Any]]
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, TransactionDispatchOutcome):
            result = self.result.to_dict()
        elif isinstance(self.result, TransactionDispatchError):
            result = self.result.to_dict()
        else:
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transaction_dispatch_error import TransactionDispatchError
        from ..models.transaction_dispatch_outcome import TransactionDispatchOutcome
        from ..models.transaction_validity_error import TransactionValidityError

        d = src_dict.copy()
        _result_type = d.pop("resultType", UNSET)
        result_type: Union[Unset, TransactionDryRunResultType]
        if isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = TransactionDryRunResultType(_result_type)

        def _parse_result(
            data: object,
        ) -> Union["TransactionDispatchError", "TransactionDispatchOutcome", "TransactionValidityError", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = TransactionDispatchOutcome.from_dict(data)

                return result_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_1 = TransactionDispatchError.from_dict(data)

                return result_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            result_type_2 = TransactionValidityError.from_dict(data)

            return result_type_2

        result = _parse_result(d.pop("result", UNSET))

        transaction_dry_run = cls(
            result_type=result_type,
            result=result,
        )

        transaction_dry_run.additional_properties = d
        return transaction_dry_run

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
