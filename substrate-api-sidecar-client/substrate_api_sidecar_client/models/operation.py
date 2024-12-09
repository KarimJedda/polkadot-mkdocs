from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_amount import OperationAmount
    from ..models.operation_phase import OperationPhase
    from ..models.operation_storage import OperationStorage
    from ..models.span_id import SpanId


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        phase (Union[Unset, OperationPhase]):
        parent_span_id (Union[Unset, SpanId]):
        primary_span_id (Union[Unset, SpanId]):
        event_index (Union[Unset, str]): Index of the underlying trace event.
        address (Union[Unset, str]): Account this operation affects. Note - this will be an object like
            `{ id: address }` if the network uses `MultiAddress`
        storage (Union[Unset, OperationStorage]):
        amount (Union[Unset, OperationAmount]):
    """

    phase: Union[Unset, "OperationPhase"] = UNSET
    parent_span_id: Union[Unset, "SpanId"] = UNSET
    primary_span_id: Union[Unset, "SpanId"] = UNSET
    event_index: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    storage: Union[Unset, "OperationStorage"] = UNSET
    amount: Union[Unset, "OperationAmount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.to_dict()

        parent_span_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_span_id, Unset):
            parent_span_id = self.parent_span_id.to_dict()

        primary_span_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_span_id, Unset):
            primary_span_id = self.primary_span_id.to_dict()

        event_index = self.event_index

        address = self.address

        storage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.to_dict()

        amount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if primary_span_id is not UNSET:
            field_dict["primarySpanId"] = primary_span_id
        if event_index is not UNSET:
            field_dict["eventIndex"] = event_index
        if address is not UNSET:
            field_dict["address"] = address
        if storage is not UNSET:
            field_dict["storage"] = storage
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.operation_amount import OperationAmount
        from ..models.operation_phase import OperationPhase
        from ..models.operation_storage import OperationStorage
        from ..models.span_id import SpanId

        d = src_dict.copy()
        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, OperationPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = OperationPhase.from_dict(_phase)

        _parent_span_id = d.pop("parentSpanId", UNSET)
        parent_span_id: Union[Unset, SpanId]
        if isinstance(_parent_span_id, Unset):
            parent_span_id = UNSET
        else:
            parent_span_id = SpanId.from_dict(_parent_span_id)

        _primary_span_id = d.pop("primarySpanId", UNSET)
        primary_span_id: Union[Unset, SpanId]
        if isinstance(_primary_span_id, Unset):
            primary_span_id = UNSET
        else:
            primary_span_id = SpanId.from_dict(_primary_span_id)

        event_index = d.pop("eventIndex", UNSET)

        address = d.pop("address", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: Union[Unset, OperationStorage]
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = OperationStorage.from_dict(_storage)

        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, OperationAmount]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = OperationAmount.from_dict(_amount)

        operation = cls(
            phase=phase,
            parent_span_id=parent_span_id,
            primary_span_id=primary_span_id,
            event_index=event_index,
            address=address,
            storage=storage,
            amount=amount,
        )

        operation.additional_properties = d
        return operation

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
