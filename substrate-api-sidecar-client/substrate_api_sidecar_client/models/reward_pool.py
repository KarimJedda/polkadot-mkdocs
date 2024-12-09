from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RewardPool")


@_attrs_define
class RewardPool:
    """
    Attributes:
        last_recorded_reward_counter (Union[Unset, float]):
        last_recorded_total_payouts (Union[Unset, float]):
        total_rewards_claimed (Union[Unset, float]):
    """

    last_recorded_reward_counter: Union[Unset, float] = UNSET
    last_recorded_total_payouts: Union[Unset, float] = UNSET
    total_rewards_claimed: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_recorded_reward_counter = self.last_recorded_reward_counter

        last_recorded_total_payouts = self.last_recorded_total_payouts

        total_rewards_claimed = self.total_rewards_claimed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_recorded_reward_counter is not UNSET:
            field_dict["lastRecordedRewardCounter"] = last_recorded_reward_counter
        if last_recorded_total_payouts is not UNSET:
            field_dict["lastRecordedTotalPayouts"] = last_recorded_total_payouts
        if total_rewards_claimed is not UNSET:
            field_dict["totalRewardsClaimed"] = total_rewards_claimed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        last_recorded_reward_counter = d.pop("lastRecordedRewardCounter", UNSET)

        last_recorded_total_payouts = d.pop("lastRecordedTotalPayouts", UNSET)

        total_rewards_claimed = d.pop("totalRewardsClaimed", UNSET)

        reward_pool = cls(
            last_recorded_reward_counter=last_recorded_reward_counter,
            last_recorded_total_payouts=last_recorded_total_payouts,
            total_rewards_claimed=total_rewards_claimed,
        )

        reward_pool.additional_properties = d
        return reward_pool

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
