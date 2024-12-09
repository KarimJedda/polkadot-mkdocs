from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pallet_storage_type import PalletStorageType


T = TypeVar("T", bound="PalletStorageItemMetadata")


@_attrs_define
class PalletStorageItemMetadata:
    """Metadata of a storage item from a FRAME pallet.

    Attributes:
        name (Union[Unset, str]): The storage item's name (which is the same as the storage item's ID). Example:
            ReferendumInfoOf.
        modifier (Union[Unset, str]):  Example: Optional.
        type_ (Union[Unset, PalletStorageType]): This is going to be formatted to the type of StorageEntryTypeV14.
        fallback (Union[Unset, str]):  Example: 0x00.
        docs (Union[Unset, str]):  Example:  Information concerning any given referendum.

             TWOX-NOTE: SAFE as indexes are not under an attacker’s control..
    """

    name: Union[Unset, str] = UNSET
    modifier: Union[Unset, str] = UNSET
    type_: Union[Unset, "PalletStorageType"] = UNSET
    fallback: Union[Unset, str] = UNSET
    docs: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        modifier = self.modifier

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        fallback = self.fallback

        docs = self.docs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if modifier is not UNSET:
            field_dict["modifier"] = modifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if docs is not UNSET:
            field_dict["docs"] = docs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pallet_storage_type import PalletStorageType

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        modifier = d.pop("modifier", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PalletStorageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PalletStorageType.from_dict(_type_)

        fallback = d.pop("fallback", UNSET)

        docs = d.pop("docs", UNSET)

        pallet_storage_item_metadata = cls(
            name=name,
            modifier=modifier,
            type_=type_,
            fallback=fallback,
            docs=docs,
        )

        pallet_storage_item_metadata.additional_properties = d
        return pallet_storage_item_metadata

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
