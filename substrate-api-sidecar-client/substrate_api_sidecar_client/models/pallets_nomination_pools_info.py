from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="PalletsNominationPoolsInfo")


@_attrs_define
class PalletsNominationPoolsInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        counter_for_bonded_pools (Union[Unset, float]):
        counter_for_metadata (Union[Unset, float]):
        counter_for_pool_members (Union[Unset, float]):
        counter_for_reverse_pool_id_lookup (Union[Unset, float]):
        counter_for_reward_pools (Union[Unset, float]):
        counter_for_sub_pools_storage (Union[Unset, float]):
        last_pool_id (Union[Unset, float]):
        max_pool_members (Union[Unset, float]):
        max_pool_members_per_pool (Union[None, Unset, float]):
        max_pools (Union[Unset, float]):
        min_create_bond (Union[Unset, float]):
        min_join_bond (Union[Unset, float]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    counter_for_bonded_pools: Union[Unset, float] = UNSET
    counter_for_metadata: Union[Unset, float] = UNSET
    counter_for_pool_members: Union[Unset, float] = UNSET
    counter_for_reverse_pool_id_lookup: Union[Unset, float] = UNSET
    counter_for_reward_pools: Union[Unset, float] = UNSET
    counter_for_sub_pools_storage: Union[Unset, float] = UNSET
    last_pool_id: Union[Unset, float] = UNSET
    max_pool_members: Union[Unset, float] = UNSET
    max_pool_members_per_pool: Union[None, Unset, float] = UNSET
    max_pools: Union[Unset, float] = UNSET
    min_create_bond: Union[Unset, float] = UNSET
    min_join_bond: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        counter_for_bonded_pools = self.counter_for_bonded_pools

        counter_for_metadata = self.counter_for_metadata

        counter_for_pool_members = self.counter_for_pool_members

        counter_for_reverse_pool_id_lookup = self.counter_for_reverse_pool_id_lookup

        counter_for_reward_pools = self.counter_for_reward_pools

        counter_for_sub_pools_storage = self.counter_for_sub_pools_storage

        last_pool_id = self.last_pool_id

        max_pool_members = self.max_pool_members

        max_pool_members_per_pool: Union[None, Unset, float]
        if isinstance(self.max_pool_members_per_pool, Unset):
            max_pool_members_per_pool = UNSET
        else:
            max_pool_members_per_pool = self.max_pool_members_per_pool

        max_pools = self.max_pools

        min_create_bond = self.min_create_bond

        min_join_bond = self.min_join_bond

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if counter_for_bonded_pools is not UNSET:
            field_dict["counterForBondedPools"] = counter_for_bonded_pools
        if counter_for_metadata is not UNSET:
            field_dict["counterForMetadata"] = counter_for_metadata
        if counter_for_pool_members is not UNSET:
            field_dict["counterForPoolMembers"] = counter_for_pool_members
        if counter_for_reverse_pool_id_lookup is not UNSET:
            field_dict["counterForReversePoolIdLookup"] = counter_for_reverse_pool_id_lookup
        if counter_for_reward_pools is not UNSET:
            field_dict["counterForRewardPools"] = counter_for_reward_pools
        if counter_for_sub_pools_storage is not UNSET:
            field_dict["counterForSubPoolsStorage"] = counter_for_sub_pools_storage
        if last_pool_id is not UNSET:
            field_dict["lastPoolId"] = last_pool_id
        if max_pool_members is not UNSET:
            field_dict["maxPoolMembers"] = max_pool_members
        if max_pool_members_per_pool is not UNSET:
            field_dict["maxPoolMembersPerPool"] = max_pool_members_per_pool
        if max_pools is not UNSET:
            field_dict["maxPools"] = max_pools
        if min_create_bond is not UNSET:
            field_dict["minCreateBond"] = min_create_bond
        if min_join_bond is not UNSET:
            field_dict["minJoinBond"] = min_join_bond

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        counter_for_bonded_pools = d.pop("counterForBondedPools", UNSET)

        counter_for_metadata = d.pop("counterForMetadata", UNSET)

        counter_for_pool_members = d.pop("counterForPoolMembers", UNSET)

        counter_for_reverse_pool_id_lookup = d.pop("counterForReversePoolIdLookup", UNSET)

        counter_for_reward_pools = d.pop("counterForRewardPools", UNSET)

        counter_for_sub_pools_storage = d.pop("counterForSubPoolsStorage", UNSET)

        last_pool_id = d.pop("lastPoolId", UNSET)

        max_pool_members = d.pop("maxPoolMembers", UNSET)

        def _parse_max_pool_members_per_pool(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_pool_members_per_pool = _parse_max_pool_members_per_pool(d.pop("maxPoolMembersPerPool", UNSET))

        max_pools = d.pop("maxPools", UNSET)

        min_create_bond = d.pop("minCreateBond", UNSET)

        min_join_bond = d.pop("minJoinBond", UNSET)

        pallets_nomination_pools_info = cls(
            at=at,
            counter_for_bonded_pools=counter_for_bonded_pools,
            counter_for_metadata=counter_for_metadata,
            counter_for_pool_members=counter_for_pool_members,
            counter_for_reverse_pool_id_lookup=counter_for_reverse_pool_id_lookup,
            counter_for_reward_pools=counter_for_reward_pools,
            counter_for_sub_pools_storage=counter_for_sub_pools_storage,
            last_pool_id=last_pool_id,
            max_pool_members=max_pool_members,
            max_pool_members_per_pool=max_pool_members_per_pool,
            max_pools=max_pools,
            min_create_bond=min_create_bond,
            min_join_bond=min_join_bond,
        )

        pallets_nomination_pools_info.additional_properties = d
        return pallets_nomination_pools_info

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
