from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signature")


@_attrs_define
class Signature:
    """Object with `signature` and `signer`, or `null` if unsigned.

    Attributes:
        signature (Union[Unset, str]):
        signer (Union[Unset, str]):
    """

    signature: Union[Unset, str] = UNSET
    signer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signature = self.signature

        signer = self.signer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signature is not UNSET:
            field_dict["signature"] = signature
        if signer is not UNSET:
            field_dict["signer"] = signer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        signature = d.pop("signature", UNSET)

        signer = d.pop("signer", UNSET)

        signature = cls(
            signature=signature,
            signer=signer,
        )

        signature.additional_properties = d
        return signature

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
