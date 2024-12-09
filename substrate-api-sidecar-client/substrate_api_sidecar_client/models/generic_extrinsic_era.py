from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenericExtrinsicEra")


@_attrs_define
class GenericExtrinsicEra:
    """The return value for era can either be `mortalEra`, or `immortalEra` and is represented as an enum in substrate.
    `immortalEra` meaning
    the transaction is valid forever. `mortalEra` consists of a tuple containing a period and phase.
    ex: `"{"mortalEra": ["64", "11"]}"`. The Period is the period of validity from the block hash found in the signing
    material.
    The Phase is the period that this transaction's lifetime begins (and, importantly,
    implies which block hash is included in the signature material).

        Example:
            {"mortalEra":["64", "11"]}

        Attributes:
            mortal_era (Union[Unset, list[str]]): Tuple of a Phase, and Period. Each item in the array will be a string
                formatted as an integer.
            immortal_era (Union[Unset, str]): Hardcoded constant '0x00'.
    """

    mortal_era: Union[Unset, list[str]] = UNSET
    immortal_era: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mortal_era: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mortal_era, Unset):
            mortal_era = self.mortal_era

        immortal_era = self.immortal_era

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mortal_era is not UNSET:
            field_dict["mortalEra"] = mortal_era
        if immortal_era is not UNSET:
            field_dict["immortalEra"] = immortal_era

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        mortal_era = cast(list[str], d.pop("mortalEra", UNSET))

        immortal_era = d.pop("immortalEra", UNSET)

        generic_extrinsic_era = cls(
            mortal_era=mortal_era,
            immortal_era=immortal_era,
        )

        generic_extrinsic_era.additional_properties = d
        return generic_extrinsic_era

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
