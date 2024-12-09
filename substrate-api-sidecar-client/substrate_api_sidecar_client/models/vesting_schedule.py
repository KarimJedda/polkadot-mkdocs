from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VestingSchedule")


@_attrs_define
class VestingSchedule:
    """Vesting schedule for an account.

    Attributes:
        locked (Union[Unset, str]): Number of tokens locked at start.
        per_block (Union[Unset, str]): Number of tokens that gets unlocked every block after `startingBlock`.
        starting_block (Union[Unset, str]): Starting block for unlocking (vesting).
    """

    locked: Union[Unset, str] = UNSET
    per_block: Union[Unset, str] = UNSET
    starting_block: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locked = self.locked

        per_block = self.per_block

        starting_block = self.starting_block

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locked is not UNSET:
            field_dict["locked"] = locked
        if per_block is not UNSET:
            field_dict["perBlock"] = per_block
        if starting_block is not UNSET:
            field_dict["startingBlock"] = starting_block

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        locked = d.pop("locked", UNSET)

        per_block = d.pop("perBlock", UNSET)

        starting_block = d.pop("startingBlock", UNSET)

        vesting_schedule = cls(
            locked=locked,
            per_block=per_block,
            starting_block=starting_block,
        )

        vesting_schedule.additional_properties = d
        return vesting_schedule

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
