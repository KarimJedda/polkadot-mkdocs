from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.staking_progress_force_era import StakingProgressForceEra
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.election_status import ElectionStatus
    from ..models.unapplied_slash import UnappliedSlash


T = TypeVar("T", bound="StakingProgress")


@_attrs_define
class StakingProgress:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        active_era (Union[Unset, str]): `EraIndex` of the era being rewarded.
        force_era (Union[Unset, StakingProgressForceEra]): Current status of era forcing.
        next_active_era_estimate (Union[Unset, str]): Upper bound estimate of the block height at which the next active
            era will start. Not included in response when `forceEra.isForceNone`.
        next_session_estimate (Union[Unset, str]): Upper bound estimate of the block height at which the next session
            will start.
        unapplied_slashes (Union[Unset, list['UnappliedSlash']]): Array of upcoming `UnappliedSlash` indexed by era.
        election_status (Union[Unset, ElectionStatus]): Information about the off-chain election. Not included in
            response when `forceEra.isForceNone`.
        ideal_validator_count (Union[Unset, str]): Upper bound of validator set size; considered the ideal size. Not
            included in response when `forceEra.isForceNone`.
        validator_set (Union[Unset, list[str]]): Stash account IDs of the validators for the current session. Not
            included in response when `forceEra.isForceNone`.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    active_era: Union[Unset, str] = UNSET
    force_era: Union[Unset, StakingProgressForceEra] = UNSET
    next_active_era_estimate: Union[Unset, str] = UNSET
    next_session_estimate: Union[Unset, str] = UNSET
    unapplied_slashes: Union[Unset, list["UnappliedSlash"]] = UNSET
    election_status: Union[Unset, "ElectionStatus"] = UNSET
    ideal_validator_count: Union[Unset, str] = UNSET
    validator_set: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        active_era = self.active_era

        force_era: Union[Unset, str] = UNSET
        if not isinstance(self.force_era, Unset):
            force_era = self.force_era.value

        next_active_era_estimate = self.next_active_era_estimate

        next_session_estimate = self.next_session_estimate

        unapplied_slashes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.unapplied_slashes, Unset):
            unapplied_slashes = []
            for unapplied_slashes_item_data in self.unapplied_slashes:
                unapplied_slashes_item = unapplied_slashes_item_data.to_dict()
                unapplied_slashes.append(unapplied_slashes_item)

        election_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.election_status, Unset):
            election_status = self.election_status.to_dict()

        ideal_validator_count = self.ideal_validator_count

        validator_set: Union[Unset, list[str]] = UNSET
        if not isinstance(self.validator_set, Unset):
            validator_set = self.validator_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if active_era is not UNSET:
            field_dict["activeEra"] = active_era
        if force_era is not UNSET:
            field_dict["forceEra"] = force_era
        if next_active_era_estimate is not UNSET:
            field_dict["nextActiveEraEstimate"] = next_active_era_estimate
        if next_session_estimate is not UNSET:
            field_dict["nextSessionEstimate"] = next_session_estimate
        if unapplied_slashes is not UNSET:
            field_dict["unappliedSlashes"] = unapplied_slashes
        if election_status is not UNSET:
            field_dict["electionStatus"] = election_status
        if ideal_validator_count is not UNSET:
            field_dict["idealValidatorCount"] = ideal_validator_count
        if validator_set is not UNSET:
            field_dict["validatorSet"] = validator_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.election_status import ElectionStatus
        from ..models.unapplied_slash import UnappliedSlash

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        active_era = d.pop("activeEra", UNSET)

        _force_era = d.pop("forceEra", UNSET)
        force_era: Union[Unset, StakingProgressForceEra]
        if isinstance(_force_era, Unset):
            force_era = UNSET
        else:
            force_era = StakingProgressForceEra(_force_era)

        next_active_era_estimate = d.pop("nextActiveEraEstimate", UNSET)

        next_session_estimate = d.pop("nextSessionEstimate", UNSET)

        unapplied_slashes = []
        _unapplied_slashes = d.pop("unappliedSlashes", UNSET)
        for unapplied_slashes_item_data in _unapplied_slashes or []:
            unapplied_slashes_item = UnappliedSlash.from_dict(unapplied_slashes_item_data)

            unapplied_slashes.append(unapplied_slashes_item)

        _election_status = d.pop("electionStatus", UNSET)
        election_status: Union[Unset, ElectionStatus]
        if isinstance(_election_status, Unset):
            election_status = UNSET
        else:
            election_status = ElectionStatus.from_dict(_election_status)

        ideal_validator_count = d.pop("idealValidatorCount", UNSET)

        validator_set = cast(list[str], d.pop("validatorSet", UNSET))

        staking_progress = cls(
            at=at,
            active_era=active_era,
            force_era=force_era,
            next_active_era_estimate=next_active_era_estimate,
            next_session_estimate=next_session_estimate,
            unapplied_slashes=unapplied_slashes,
            election_status=election_status,
            ideal_validator_count=ideal_validator_count,
            validator_set=validator_set,
        )

        staking_progress.additional_properties = d
        return staking_progress

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
