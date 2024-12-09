from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.pallet_storage_item_metadata import PalletStorageItemMetadata
    from ..models.pallet_storage_item_value import PalletStorageItemValue


T = TypeVar("T", bound="PalletStorageItem")


@_attrs_define
class PalletStorageItem:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        pallet (Union[Unset, str]): Name of the pallet. Example: democracy.
        pallet_index (Union[Unset, str]): Index of the pallet for looking up storage. Example: 15.
        storage_item (Union[Unset, str]): Name of the storage item. Example: referendumInfoOf.
        keys (Union[Unset, list[str]]): N Storage keys passed in as the `keys` query param. Example: ['0x00', '0x01'].
        value (Union[Unset, PalletStorageItemValue]): Value returned by this storage query. Example: {'Ongoing': {'end':
            '1612800', 'proposalHash': '0x7de70fc8be782076d0b5772be77153d172a5381c72dd56d3385e25f62abf507e', 'threshold':
            'Supermajorityapproval', 'delay': '403200', 'tally': {'ayes': '41925212461400000', 'nays': '214535586500000',
            'turnout': '34485320658000000'}}}.
        metadata (Union[Unset, PalletStorageItemMetadata]): Metadata of a storage item from a FRAME pallet.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    pallet: Union[Unset, str] = UNSET
    pallet_index: Union[Unset, str] = UNSET
    storage_item: Union[Unset, str] = UNSET
    keys: Union[Unset, list[str]] = UNSET
    value: Union[Unset, "PalletStorageItemValue"] = UNSET
    metadata: Union[Unset, "PalletStorageItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        pallet = self.pallet

        pallet_index = self.pallet_index

        storage_item = self.storage_item

        keys: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if pallet_index is not UNSET:
            field_dict["palletIndex"] = pallet_index
        if storage_item is not UNSET:
            field_dict["storageItem"] = storage_item
        if keys is not UNSET:
            field_dict["keys"] = keys
        if value is not UNSET:
            field_dict["value"] = value
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.pallet_storage_item_metadata import PalletStorageItemMetadata
        from ..models.pallet_storage_item_value import PalletStorageItemValue

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        pallet = d.pop("pallet", UNSET)

        pallet_index = d.pop("palletIndex", UNSET)

        storage_item = d.pop("storageItem", UNSET)

        keys = cast(list[str], d.pop("keys", UNSET))

        _value = d.pop("value", UNSET)
        value: Union[Unset, PalletStorageItemValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PalletStorageItemValue.from_dict(_value)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PalletStorageItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PalletStorageItemMetadata.from_dict(_metadata)

        pallet_storage_item = cls(
            at=at,
            pallet=pallet,
            pallet_index=pallet_index,
            storage_item=storage_item,
            keys=keys,
            value=value,
            metadata=metadata,
        )

        pallet_storage_item.additional_properties = d
        return pallet_storage_item

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
