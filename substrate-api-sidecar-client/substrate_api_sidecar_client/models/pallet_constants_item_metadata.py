from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PalletConstantsItemMetadata")


@_attrs_define
class PalletConstantsItemMetadata:
    """Metadata of an constant item from a FRAME pallet.

    Attributes:
        name (Union[Unset, str]): The constant item's name (which is the same as the constant item's ID). Example:
            VotingPeriod.
        type_ (Union[Unset, str]):  Example: 4.
        value (Union[Unset, str]): The hex value of the constant Example: 0x00270600.
        docs (Union[Unset, str]):  Example: Information concerning any given constant.

             TWOX-NOTE: SAFE as indexes are not under an attacker’s control..
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    docs: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        value = self.value

        docs = self.docs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if docs is not UNSET:
            field_dict["docs"] = docs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        docs = d.pop("docs", UNSET)

        pallet_constants_item_metadata = cls(
            name=name,
            type_=type_,
            value=value,
            docs=docs,
        )

        pallet_constants_item_metadata.additional_properties = d
        return pallet_constants_item_metadata

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
