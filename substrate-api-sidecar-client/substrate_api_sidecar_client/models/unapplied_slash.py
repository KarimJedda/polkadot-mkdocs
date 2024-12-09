from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnappliedSlash")


@_attrs_define
class UnappliedSlash:
    """
    Attributes:
        validator (Union[Unset, str]): Stash account ID of the offending validator.
        own (Union[Unset, str]): The amount the validator will be slashed.
        others (Union[Unset, list[str]]): Array of tuples(`[accountId, amount]`) representing all the stashes of other
            slashed stakers and the amount they will be slashed.
        reporters (Union[Unset, list[str]]): Array of account IDs of the reporters of the offense.
        payout (Union[Unset, str]): Amount of bounty payout to reporters.
    """

    validator: Union[Unset, str] = UNSET
    own: Union[Unset, str] = UNSET
    others: Union[Unset, list[str]] = UNSET
    reporters: Union[Unset, list[str]] = UNSET
    payout: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        validator = self.validator

        own = self.own

        others: Union[Unset, list[str]] = UNSET
        if not isinstance(self.others, Unset):
            others = self.others

        reporters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reporters, Unset):
            reporters = self.reporters

        payout = self.payout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validator is not UNSET:
            field_dict["validator"] = validator
        if own is not UNSET:
            field_dict["own"] = own
        if others is not UNSET:
            field_dict["others"] = others
        if reporters is not UNSET:
            field_dict["reporters"] = reporters
        if payout is not UNSET:
            field_dict["payout"] = payout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        validator = d.pop("validator", UNSET)

        own = d.pop("own", UNSET)

        others = cast(list[str], d.pop("others", UNSET))

        reporters = cast(list[str], d.pop("reporters", UNSET))

        payout = d.pop("payout", UNSET)

        unapplied_slash = cls(
            validator=validator,
            own=own,
            others=others,
            reporters=reporters,
            payout=payout,
        )

        unapplied_slash.additional_properties = d
        return unapplied_slash

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
