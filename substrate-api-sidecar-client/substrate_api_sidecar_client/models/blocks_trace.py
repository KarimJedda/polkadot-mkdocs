from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.trace_event import TraceEvent
    from ..models.trace_span import TraceSpan


T = TypeVar("T", bound="BlocksTrace")


@_attrs_define
class BlocksTrace:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        block_hash (Union[Unset, str]):
        events (Union[Unset, list['TraceEvent']]):
        parent_hash (Union[Unset, str]):
        spans (Union[Unset, list['TraceSpan']]):
        storage_keys (Union[Unset, str]): Hex encoded storage keys used to filter events.
        tracing_targets (Union[Unset, str]): Targets used to filter spans and events.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    block_hash: Union[Unset, str] = UNSET
    events: Union[Unset, list["TraceEvent"]] = UNSET
    parent_hash: Union[Unset, str] = UNSET
    spans: Union[Unset, list["TraceSpan"]] = UNSET
    storage_keys: Union[Unset, str] = UNSET
    tracing_targets: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        block_hash = self.block_hash

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        parent_hash = self.parent_hash

        spans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.spans, Unset):
            spans = []
            for spans_item_data in self.spans:
                spans_item = spans_item_data.to_dict()
                spans.append(spans_item)

        storage_keys = self.storage_keys

        tracing_targets = self.tracing_targets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if block_hash is not UNSET:
            field_dict["blockHash"] = block_hash
        if events is not UNSET:
            field_dict["events"] = events
        if parent_hash is not UNSET:
            field_dict["parentHash"] = parent_hash
        if spans is not UNSET:
            field_dict["spans"] = spans
        if storage_keys is not UNSET:
            field_dict["storageKeys"] = storage_keys
        if tracing_targets is not UNSET:
            field_dict["tracingTargets"] = tracing_targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.trace_event import TraceEvent
        from ..models.trace_span import TraceSpan

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        block_hash = d.pop("blockHash", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = TraceEvent.from_dict(events_item_data)

            events.append(events_item)

        parent_hash = d.pop("parentHash", UNSET)

        spans = []
        _spans = d.pop("spans", UNSET)
        for spans_item_data in _spans or []:
            spans_item = TraceSpan.from_dict(spans_item_data)

            spans.append(spans_item)

        storage_keys = d.pop("storageKeys", UNSET)

        tracing_targets = d.pop("tracingTargets", UNSET)

        blocks_trace = cls(
            at=at,
            block_hash=block_hash,
            events=events,
            parent_hash=parent_hash,
            spans=spans,
            storage_keys=storage_keys,
            tracing_targets=tracing_targets,
        )

        blocks_trace.additional_properties = d
        return blocks_trace

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
