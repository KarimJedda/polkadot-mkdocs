from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Nominations")


@_attrs_define
class Nominations:
    """
    Attributes:
        targets (Union[Unset, list[str]]): The targets of the nomination.
        submitted_in (Union[Unset, str]): The era the nominations were submitted. (Except for initial nominations which
            are considered submitted at era 0.)
        suppressed (Union[Unset, bool]): Whether the nominations have been suppressed.
    """

    targets: Union[Unset, list[str]] = UNSET
    submitted_in: Union[Unset, str] = UNSET
    suppressed: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        targets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = self.targets

        submitted_in = self.submitted_in

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if targets is not UNSET:
            field_dict["targets"] = targets
        if submitted_in is not UNSET:
            field_dict["submittedIn"] = submitted_in
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        targets = cast(list[str], d.pop("targets", UNSET))

        submitted_in = d.pop("submittedIn", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        nominations = cls(
            targets=targets,
            submitted_in=submitted_in,
            suppressed=suppressed,
        )

        nominations.additional_properties = d
        return nominations

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
