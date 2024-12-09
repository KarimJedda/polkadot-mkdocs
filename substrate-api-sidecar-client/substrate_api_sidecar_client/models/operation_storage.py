from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationStorage")


@_attrs_define
class OperationStorage:
    """
    Attributes:
        pallet (Union[Unset, str]):
        item (Union[Unset, str]):
        field1 (Union[Unset, str]): A field of the storage item. (i.e `system::Account::get(address).data`)
        field2 (Union[Unset, str]): A field of the struct described by field1 (i.e
            `system::Account::get(address).data.free`)
    """

    pallet: Union[Unset, str] = UNSET
    item: Union[Unset, str] = UNSET
    field1: Union[Unset, str] = UNSET
    field2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet = self.pallet

        item = self.item

        field1 = self.field1

        field2 = self.field2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if item is not UNSET:
            field_dict["item"] = item
        if field1 is not UNSET:
            field_dict["field1"] = field1
        if field2 is not UNSET:
            field_dict["field2"] = field2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pallet = d.pop("pallet", UNSET)

        item = d.pop("item", UNSET)

        field1 = d.pop("field1", UNSET)

        field2 = d.pop("field2", UNSET)

        operation_storage = cls(
            pallet=pallet,
            item=item,
            field1=field1,
            field2=field2,
        )

        operation_storage.additional_properties = d
        return operation_storage

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
