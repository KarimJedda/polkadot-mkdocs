from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_phase_variant import OperationPhaseVariant
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationPhase")


@_attrs_define
class OperationPhase:
    """
    Attributes:
        variant (Union[Unset, OperationPhaseVariant]): Phase of block execution pipeline.
        extrinsic_index (Union[Unset, str]): If phase variant is `applyExtrinsic` this will be the index of
            the extrinsic. Otherwise this field will not be present.
    """

    variant: Union[Unset, OperationPhaseVariant] = UNSET
    extrinsic_index: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value

        extrinsic_index = self.extrinsic_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant is not UNSET:
            field_dict["variant"] = variant
        if extrinsic_index is not UNSET:
            field_dict["extrinsicIndex"] = extrinsic_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, OperationPhaseVariant]
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = OperationPhaseVariant(_variant)

        extrinsic_index = d.pop("extrinsicIndex", UNSET)

        operation_phase = cls(
            variant=variant,
            extrinsic_index=extrinsic_index,
        )

        operation_phase.additional_properties = d
        return operation_phase

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
