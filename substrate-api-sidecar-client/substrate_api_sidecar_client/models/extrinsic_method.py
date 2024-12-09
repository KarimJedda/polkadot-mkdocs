from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtrinsicMethod")


@_attrs_define
class ExtrinsicMethod:
    """Extrinsic method

    Attributes:
        pallet (Union[Unset, str]):
        method (Union[Unset, str]):
    """

    pallet: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet = self.pallet

        method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallet is not UNSET:
            field_dict["pallet"] = pallet
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pallet = d.pop("pallet", UNSET)

        method = d.pop("method", UNSET)

        extrinsic_method = cls(
            pallet=pallet,
            method=method,
        )

        extrinsic_method.additional_properties = d
        return extrinsic_method

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
