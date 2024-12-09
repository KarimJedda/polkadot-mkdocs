from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pallet_errors_item_metadata import PalletErrorsItemMetadata


T = TypeVar("T", bound="PalletErrorsItem")


@_attrs_define
class PalletErrorsItem:
    """
    Attributes:
        pallet (Union[Unset, str]): Name of the pallet. Example: democracy.
        pallet_index (Union[Unset, str]): Index of the pallet for looking up errors. Example: 14.
        error_item (Union[Unset, str]): Name of the error item. Example: ValueLow.
        metadata (Union[Unset, PalletErrorsItemMetadata]): Metadata of an error item from a FRAME pallet.
    """

    pallet: Union[Unset, str] = UNSET
    pallet_index: Union[Unset, str] = UNSET
    error_item: Union[Unset, str] = UNSET
    metadata: Union[Unset, "PalletErrorsItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet = self.pallet

        pallet_index = self.pallet_index

        error_item = self.error_item

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
        if error_item is not UNSET:
            field_dict["errorItem"] = error_item
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pallet_errors_item_metadata import PalletErrorsItemMetadata

        d = src_dict.copy()
        pallet = d.pop("pallet", UNSET)

        pallet_index = d.pop("palletIndex", UNSET)

        error_item = d.pop("errorItem", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PalletErrorsItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PalletErrorsItemMetadata.from_dict(_metadata)

        pallet_errors_item = cls(
            pallet=pallet,
            pallet_index=pallet_index,
            error_item=error_item,
            metadata=metadata,
        )

        pallet_errors_item.additional_properties = d
        return pallet_errors_item

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
