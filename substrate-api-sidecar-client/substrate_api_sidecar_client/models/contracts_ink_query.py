from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contracts_ink_query_result import ContractsInkQueryResult
    from ..models.contracts_ink_query_storage_deposit import ContractsInkQueryStorageDeposit


T = TypeVar("T", bound="ContractsInkQuery")


@_attrs_define
class ContractsInkQuery:
    """Result from calling a query to a Ink contract.

    Attributes:
        debug_message (Union[Unset, str]):
        gas_consumed (Union[Unset, str]):
        gas_required (Union[Unset, str]):
        output (Union[Unset, bool]):
        result (Union[Unset, ContractsInkQueryResult]): Will result in an Ok or Err object depending on the result of
            the query.
        storage_deposit (Union[Unset, ContractsInkQueryStorageDeposit]):
    """

    debug_message: Union[Unset, str] = UNSET
    gas_consumed: Union[Unset, str] = UNSET
    gas_required: Union[Unset, str] = UNSET
    output: Union[Unset, bool] = UNSET
    result: Union[Unset, "ContractsInkQueryResult"] = UNSET
    storage_deposit: Union[Unset, "ContractsInkQueryStorageDeposit"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debug_message = self.debug_message

        gas_consumed = self.gas_consumed

        gas_required = self.gas_required

        output = self.output

        result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        storage_deposit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.storage_deposit, Unset):
            storage_deposit = self.storage_deposit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debug_message is not UNSET:
            field_dict["debugMessage"] = debug_message
        if gas_consumed is not UNSET:
            field_dict["gasConsumed"] = gas_consumed
        if gas_required is not UNSET:
            field_dict["gasRequired"] = gas_required
        if output is not UNSET:
            field_dict["output"] = output
        if result is not UNSET:
            field_dict["result"] = result
        if storage_deposit is not UNSET:
            field_dict["storageDeposit"] = storage_deposit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.contracts_ink_query_result import ContractsInkQueryResult
        from ..models.contracts_ink_query_storage_deposit import ContractsInkQueryStorageDeposit

        d = src_dict.copy()
        debug_message = d.pop("debugMessage", UNSET)

        gas_consumed = d.pop("gasConsumed", UNSET)

        gas_required = d.pop("gasRequired", UNSET)

        output = d.pop("output", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, ContractsInkQueryResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ContractsInkQueryResult.from_dict(_result)

        _storage_deposit = d.pop("storageDeposit", UNSET)
        storage_deposit: Union[Unset, ContractsInkQueryStorageDeposit]
        if isinstance(_storage_deposit, Unset):
            storage_deposit = UNSET
        else:
            storage_deposit = ContractsInkQueryStorageDeposit.from_dict(_storage_deposit)

        contracts_ink_query = cls(
            debug_message=debug_message,
            gas_consumed=gas_consumed,
            gas_required=gas_required,
            output=output,
            result=result,
            storage_deposit=storage_deposit,
        )

        contracts_ink_query.additional_properties = d
        return contracts_ink_query

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
