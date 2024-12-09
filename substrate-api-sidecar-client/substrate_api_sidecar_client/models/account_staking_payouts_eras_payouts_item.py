from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payouts_item import PayoutsItem


T = TypeVar("T", bound="AccountStakingPayoutsErasPayoutsItem")


@_attrs_define
class AccountStakingPayoutsErasPayoutsItem:
    """
    Attributes:
        era (Union[Unset, str]): Era this information is associated with.
        total_era_reward_points (Union[Unset, str]): Total reward points for the era. Equals the sum of reward points
            for all the validators in the set.
        total_era_payout (Union[Unset, str]): Total payout for the era. Validators split the payout based on the portion
            of `totalEraRewardPoints` they have.
        payouts (Union[Unset, list['PayoutsItem']]):
    """

    era: Union[Unset, str] = UNSET
    total_era_reward_points: Union[Unset, str] = UNSET
    total_era_payout: Union[Unset, str] = UNSET
    payouts: Union[Unset, list["PayoutsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        era = self.era

        total_era_reward_points = self.total_era_reward_points

        total_era_payout = self.total_era_payout

        payouts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.payouts, Unset):
            payouts = []
            for componentsschemas_payouts_item_data in self.payouts:
                componentsschemas_payouts_item = componentsschemas_payouts_item_data.to_dict()
                payouts.append(componentsschemas_payouts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if era is not UNSET:
            field_dict["era"] = era
        if total_era_reward_points is not UNSET:
            field_dict["totalEraRewardPoints"] = total_era_reward_points
        if total_era_payout is not UNSET:
            field_dict["totalEraPayout"] = total_era_payout
        if payouts is not UNSET:
            field_dict["payouts"] = payouts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.payouts_item import PayoutsItem

        d = src_dict.copy()
        era = d.pop("era", UNSET)

        total_era_reward_points = d.pop("totalEraRewardPoints", UNSET)

        total_era_payout = d.pop("totalEraPayout", UNSET)

        payouts = []
        _payouts = d.pop("payouts", UNSET)
        for componentsschemas_payouts_item_data in _payouts or []:
            componentsschemas_payouts_item = PayoutsItem.from_dict(componentsschemas_payouts_item_data)

            payouts.append(componentsschemas_payouts_item)

        account_staking_payouts_eras_payouts_item = cls(
            era=era,
            total_era_reward_points=total_era_reward_points,
            total_era_payout=total_era_payout,
            payouts=payouts,
        )

        account_staking_payouts_eras_payouts_item.additional_properties = d
        return account_staking_payouts_eras_payouts_item

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
