from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DryRunBody")


@_attrs_define
class DryRunBody:
    """
    Attributes:
        at (Union[Unset, str]):
        tx (Union[Unset, str]):
        sender_address (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    tx: Union[Unset, str] = UNSET
    sender_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at

        tx = self.tx

        sender_address = self.sender_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if tx is not UNSET:
            field_dict["tx"] = tx
        if sender_address is not UNSET:
            field_dict["senderAddress"] = sender_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        tx = d.pop("tx", UNSET)

        sender_address = d.pop("senderAddress", UNSET)

        dry_run_body = cls(
            at=at,
            tx=tx,
            sender_address=sender_address,
        )

        dry_run_body.additional_properties = d
        return dry_run_body

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
