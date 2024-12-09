from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeightsV2")


@_attrs_define
class WeightsV2:
    """
    Attributes:
        ref_time (Union[Unset, str]): The weight of computational time used based on some reference hardware.
        proof_size (Union[Unset, str]): The weight of storage space used by proof of validity.
    """

    ref_time: Union[Unset, str] = UNSET
    proof_size: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref_time = self.ref_time

        proof_size = self.proof_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref_time is not UNSET:
            field_dict["refTime"] = ref_time
        if proof_size is not UNSET:
            field_dict["proofSize"] = proof_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ref_time = d.pop("refTime", UNSET)

        proof_size = d.pop("proofSize", UNSET)

        weights_v2 = cls(
            ref_time=ref_time,
            proof_size=proof_size,
        )

        weights_v2.additional_properties = d
        return weights_v2

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
