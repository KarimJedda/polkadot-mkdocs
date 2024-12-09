from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pallet_events_item_metadata import PalletEventsItemMetadata


T = TypeVar("T", bound="PalletEventsItem")


@_attrs_define
class PalletEventsItem:
    """
    Attributes:
        pallet (Union[Unset, str]): Name of the pallet. Example: democracy.
        pallet_index (Union[Unset, str]): Index of the pallet for looking up events. Example: 14.
        event_item (Union[Unset, str]): Name of the events item. Example: Proposed.
        metadata (Union[Unset, PalletEventsItemMetadata]): Metadata of an event item from a FRAME pallet.
    """

    pallet: Union[Unset, str] = UNSET
    pallet_index: Union[Unset, str] = UNSET
    event_item: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PalletEventsItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet = self.pallet

        pallet_index = self.pallet_index

        event_item = self.event_item

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if pallet_index is not UNSET:
            field_dict["palletIndex"] = pallet_index
        if event_item is not UNSET:
            field_dict["eventItem"] = event_item
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pallet_events_item_metadata import PalletEventsItemMetadata

        d = src_dict.copy()
        pallet = d.pop("pallet", UNSET)

        pallet_index = d.pop("palletIndex", UNSET)

        event_item = d.pop("eventItem", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PalletEventsItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PalletEventsItemMetadata.from_dict(_metadata)

        pallet_events_item = cls(
            pallet=pallet,
            pallet_index=pallet_index,
            event_item=event_item,
            metadata=metadata,
        )

        pallet_events_item.additional_properties = d
        return pallet_events_item

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
