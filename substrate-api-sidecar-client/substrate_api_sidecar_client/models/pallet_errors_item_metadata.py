from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PalletErrorsItemMetadata")


@_attrs_define
class PalletErrorsItemMetadata:
    """Metadata of an error item from a FRAME pallet.

    Attributes:
        name (Union[Unset, str]): The error item's name (which is the same as the error item's ID). Example:
            InsufficientFunds.
        fields (Union[Unset, list[str]]):
        index (Union[Unset, str]): The index of the error item in the lists of pallet errors Example: 0.
        docs (Union[Unset, str]):  Example:  Information concerning any given error.

             TWOX-NOTE: SAFE as indexes are not under an attacker’s control..
        args (Union[Unset, list[str]]):
    """

    name: Union[Unset, str] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    index: Union[Unset, str] = UNSET
    docs: Union[Unset, str] = UNSET
    args: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        index = self.index

        docs = self.docs

        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields
        if index is not UNSET:
            field_dict["index"] = index
        if docs is not UNSET:
            field_dict["docs"] = docs
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        fields = cast(list[str], d.pop("fields", UNSET))

        index = d.pop("index", UNSET)

        docs = d.pop("docs", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        pallet_errors_item_metadata = cls(
            name=name,
            fields=fields,
            index=index,
            docs=docs,
            args=args,
        )

        pallet_errors_item_metadata.additional_properties = d
        return pallet_errors_item_metadata

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
