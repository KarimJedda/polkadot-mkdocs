from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StakingLedger")


@_attrs_define
class StakingLedger:
    """The staking ledger.

    Attributes:
        stash (Union[Unset, str]): The _Stash_ account whose balance is actually locked and at stake.
        total (Union[Unset, str]): The total amount of the _Stash_'s balance that we are currently accounting for.
            Simply `active + unlocking`.
        active (Union[Unset, str]): The total amount of the _Stash_'s balance that will be at stake in any forthcoming
            eras.
        unlocking (Union[Unset, str]): Any balance that is becoming free, which may eventually be transferred out of the
            _Stash_ (assuming it doesn't get slashed first). Represented as an array of objects, each with an `era` at which
            `value` will be unlocked.
        claimed_rewards (Union[Unset, list[str]]): Array of eras for which the stakers behind a validator have claimed
            rewards. Only updated for _validators._
    """

    stash: Union[Unset, str] = UNSET
    total: Union[Unset, str] = UNSET
    active: Union[Unset, str] = UNSET
    unlocking: Union[Unset, str] = UNSET
    claimed_rewards: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stash = self.stash

        total = self.total

        active = self.active

        unlocking = self.unlocking

        claimed_rewards: Union[Unset, list[str]] = UNSET
        if not isinstance(self.claimed_rewards, Unset):
            claimed_rewards = self.claimed_rewards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stash is not UNSET:
            field_dict["stash"] = stash
        if total is not UNSET:
            field_dict["total"] = total
        if active is not UNSET:
            field_dict["active"] = active
        if unlocking is not UNSET:
            field_dict["unlocking"] = unlocking
        if claimed_rewards is not UNSET:
            field_dict["claimedRewards"] = claimed_rewards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        stash = d.pop("stash", UNSET)

        total = d.pop("total", UNSET)

        active = d.pop("active", UNSET)

        unlocking = d.pop("unlocking", UNSET)

        claimed_rewards = cast(list[str], d.pop("claimedRewards", UNSET))

        staking_ledger = cls(
            stash=stash,
            total=total,
            active=active,
            unlocking=unlocking,
            claimed_rewards=claimed_rewards,
        )

        staking_ledger.additional_properties = d
        return staking_ledger

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
