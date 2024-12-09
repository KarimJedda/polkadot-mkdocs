from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bonded_pool import BondedPool
    from ..models.reward_pool import RewardPool


T = TypeVar("T", bound="PalletsNominationPool")


@_attrs_define
class PalletsNominationPool:
    """
    Attributes:
        bonded_pool (Union[Unset, BondedPool]):
        reward_pool (Union[Unset, RewardPool]):
    """

    bonded_pool: Union[Unset, "BondedPool"] = UNSET
    reward_pool: Union[Unset, "RewardPool"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bonded_pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bonded_pool, Unset):
            bonded_pool = self.bonded_pool.to_dict()

        reward_pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reward_pool, Unset):
            reward_pool = self.reward_pool.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bonded_pool is not UNSET:
            field_dict["bondedPool"] = bonded_pool
        if reward_pool is not UNSET:
            field_dict["rewardPool"] = reward_pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bonded_pool import BondedPool
        from ..models.reward_pool import RewardPool

        d = src_dict.copy()
        _bonded_pool = d.pop("bondedPool", UNSET)
        bonded_pool: Union[Unset, BondedPool]
        if isinstance(_bonded_pool, Unset):
            bonded_pool = UNSET
        else:
            bonded_pool = BondedPool.from_dict(_bonded_pool)

        _reward_pool = d.pop("rewardPool", UNSET)
        reward_pool: Union[Unset, RewardPool]
        if isinstance(_reward_pool, Unset):
            reward_pool = UNSET
        else:
            reward_pool = RewardPool.from_dict(_reward_pool)

        pallets_nomination_pool = cls(
            bonded_pool=bonded_pool,
            reward_pool=reward_pool,
        )

        pallets_nomination_pool.additional_properties = d
        return pallets_nomination_pool

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
