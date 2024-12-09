from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_staking_info_reward_destination import AccountStakingInfoRewardDestination
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.nominations import Nominations
    from ..models.staking_ledger import StakingLedger


T = TypeVar("T", bound="AccountStakingInfo")


@_attrs_define
class AccountStakingInfo:
    """Note: Runtime versions of Kusama less than 1062 will either have `lastReward` in place of `claimedRewards`, or no
    field at all. This is related to changes in reward distribution. See: [Lazy
    Payouts](https://github.com/paritytech/substrate/pull/4474), [Simple
    Payouts](https://github.com/paritytech/substrate/pull/5406)

        Attributes:
            at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
            reward_destination (Union[Unset, AccountStakingInfoRewardDestination]): The account to which rewards will be
                paid. Can be 'Staked' (Stash account, adding to the amount at stake), 'Stash' (Stash address, not adding to the
                amount at stake), or 'Controller' (Controller address).
            controller (Union[Unset, str]): Controller address for the given Stash.
            num_slashing_spans (Union[Unset, str]): Number of slashing spans on Stash account; `null` if provided address is
                not a Controller.
            nominations (Union[Unset, Nominations]):
            staking_ledger (Union[Unset, StakingLedger]): The staking ledger.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    reward_destination: Union[Unset, AccountStakingInfoRewardDestination] = UNSET
    controller: Union[Unset, str] = UNSET
    num_slashing_spans: Union[Unset, str] = UNSET
    nominations: Union[Unset, "Nominations"] = UNSET
    staking_ledger: Union[Unset, "StakingLedger"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        reward_destination: Union[Unset, str] = UNSET
        if not isinstance(self.reward_destination, Unset):
            reward_destination = self.reward_destination.value

        controller = self.controller

        num_slashing_spans = self.num_slashing_spans

        nominations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nominations, Unset):
            nominations = self.nominations.to_dict()

        staking_ledger: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.staking_ledger, Unset):
            staking_ledger = self.staking_ledger.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if reward_destination is not UNSET:
            field_dict["rewardDestination"] = reward_destination
        if controller is not UNSET:
            field_dict["controller"] = controller
        if num_slashing_spans is not UNSET:
            field_dict["numSlashingSpans"] = num_slashing_spans
        if nominations is not UNSET:
            field_dict["nominations"] = nominations
        if staking_ledger is not UNSET:
            field_dict["stakingLedger"] = staking_ledger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.nominations import Nominations
        from ..models.staking_ledger import StakingLedger

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _reward_destination = d.pop("rewardDestination", UNSET)
        reward_destination: Union[Unset, AccountStakingInfoRewardDestination]
        if isinstance(_reward_destination, Unset):
            reward_destination = UNSET
        else:
            reward_destination = AccountStakingInfoRewardDestination(_reward_destination)

        controller = d.pop("controller", UNSET)

        num_slashing_spans = d.pop("numSlashingSpans", UNSET)

        _nominations = d.pop("nominations", UNSET)
        nominations: Union[Unset, Nominations]
        if isinstance(_nominations, Unset):
            nominations = UNSET
        else:
            nominations = Nominations.from_dict(_nominations)

        _staking_ledger = d.pop("stakingLedger", UNSET)
        staking_ledger: Union[Unset, StakingLedger]
        if isinstance(_staking_ledger, Unset):
            staking_ledger = UNSET
        else:
            staking_ledger = StakingLedger.from_dict(_staking_ledger)

        account_staking_info = cls(
            at=at,
            reward_destination=reward_destination,
            controller=controller,
            num_slashing_spans=num_slashing_spans,
            nominations=nominations,
            staking_ledger=staking_ledger,
        )

        account_staking_info.additional_properties = d
        return account_staking_info

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
