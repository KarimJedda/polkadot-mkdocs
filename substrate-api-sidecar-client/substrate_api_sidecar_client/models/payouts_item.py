from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutsItem")


@_attrs_define
class PayoutsItem:
    """Payout for a nominating _Stash_ address and information about the validator they were nominating.

    Attributes:
        validator_id (Union[Unset, str]): AccountId of the validator the payout is coming from.
        nominator_staking_payout (Union[Unset, str]): Payout for the reward destination associated with the accountId
            the query was made for.
        claimed (Union[Unset, bool]): Whether or not the reward has been claimed.
        total_validator_reward_points (Union[Unset, str]): Number of reward points earned by the validator.
        validator_commission (Union[Unset, str]): The percentage of the total payout that the validator takes as
            commission, expressed as a Perbill.
        total_validator_exposure (Union[Unset, str]): The sum of the validator's and its nominators' stake.
        nominator_exposure (Union[Unset, str]): The amount of stake the nominator has behind the validator.
    """

    validator_id: Union[Unset, str] = UNSET
    nominator_staking_payout: Union[Unset, str] = UNSET
    claimed: Union[Unset, bool] = UNSET
    total_validator_reward_points: Union[Unset, str] = UNSET
    validator_commission: Union[Unset, str] = UNSET
    total_validator_exposure: Union[Unset, str] = UNSET
    nominator_exposure: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        validator_id = self.validator_id

        nominator_staking_payout = self.nominator_staking_payout

        claimed = self.claimed

        total_validator_reward_points = self.total_validator_reward_points

        validator_commission = self.validator_commission

        total_validator_exposure = self.total_validator_exposure

        nominator_exposure = self.nominator_exposure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validator_id is not UNSET:
            field_dict["validatorId"] = validator_id
        if nominator_staking_payout is not UNSET:
            field_dict["nominatorStakingPayout"] = nominator_staking_payout
        if claimed is not UNSET:
            field_dict["claimed"] = claimed
        if total_validator_reward_points is not UNSET:
            field_dict["totalValidatorRewardPoints"] = total_validator_reward_points
        if validator_commission is not UNSET:
            field_dict["validatorCommission"] = validator_commission
        if total_validator_exposure is not UNSET:
            field_dict["totalValidatorExposure"] = total_validator_exposure
        if nominator_exposure is not UNSET:
            field_dict["nominatorExposure"] = nominator_exposure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        validator_id = d.pop("validatorId", UNSET)

        nominator_staking_payout = d.pop("nominatorStakingPayout", UNSET)

        claimed = d.pop("claimed", UNSET)

        total_validator_reward_points = d.pop("totalValidatorRewardPoints", UNSET)

        validator_commission = d.pop("validatorCommission", UNSET)

        total_validator_exposure = d.pop("totalValidatorExposure", UNSET)

        nominator_exposure = d.pop("nominatorExposure", UNSET)

        payouts_item = cls(
            validator_id=validator_id,
            nominator_staking_payout=nominator_staking_payout,
            claimed=claimed,
            total_validator_reward_points=total_validator_reward_points,
            validator_commission=validator_commission,
            total_validator_exposure=total_validator_exposure,
            nominator_exposure=nominator_exposure,
        )

        payouts_item.additional_properties = d
        return payouts_item

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
