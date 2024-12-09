from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.onboarding_as import OnboardingAs
from ..models.para_lifecycle import ParaLifecycle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.paras_lease_info_leases_item import ParasLeaseInfoLeasesItem


T = TypeVar("T", bound="ParasLeaseInfo")


@_attrs_define
class ParasLeaseInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        para_lifecycle (Union[Unset, ParaLifecycle]): The possible states of a para, to take into account delayed
            lifecycle
            changes.
        onboarding_as (Union[Unset, OnboardingAs]): This property only shows up when `paraLifecycle=onboarding`. It
            describes if a particular para is onboarding as a `parachain` or a
            `parathread`.
        leases (Union[Unset, list['ParasLeaseInfoLeasesItem']]): List of lease periods for which the `paraId` holds a
            lease along with
            the deposit held and the associated `accountId`.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    para_lifecycle: Union[Unset, ParaLifecycle] = UNSET
    onboarding_as: Union[Unset, OnboardingAs] = UNSET
    leases: Union[Unset, list["ParasLeaseInfoLeasesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        para_lifecycle: Union[Unset, str] = UNSET
        if not isinstance(self.para_lifecycle, Unset):
            para_lifecycle = self.para_lifecycle.value

        onboarding_as: Union[Unset, str] = UNSET
        if not isinstance(self.onboarding_as, Unset):
            onboarding_as = self.onboarding_as.value

        leases: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leases, Unset):
            leases = []
            for leases_item_data in self.leases:
                leases_item = leases_item_data.to_dict()
                leases.append(leases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if para_lifecycle is not UNSET:
            field_dict["paraLifecycle"] = para_lifecycle
        if onboarding_as is not UNSET:
            field_dict["onboardingAs"] = onboarding_as
        if leases is not UNSET:
            field_dict["leases"] = leases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.paras_lease_info_leases_item import ParasLeaseInfoLeasesItem

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _para_lifecycle = d.pop("paraLifecycle", UNSET)
        para_lifecycle: Union[Unset, ParaLifecycle]
        if isinstance(_para_lifecycle, Unset):
            para_lifecycle = UNSET
        else:
            para_lifecycle = ParaLifecycle(_para_lifecycle)

        _onboarding_as = d.pop("onboardingAs", UNSET)
        onboarding_as: Union[Unset, OnboardingAs]
        if isinstance(_onboarding_as, Unset):
            onboarding_as = UNSET
        else:
            onboarding_as = OnboardingAs(_onboarding_as)

        leases = []
        _leases = d.pop("leases", UNSET)
        for leases_item_data in _leases or []:
            leases_item = ParasLeaseInfoLeasesItem.from_dict(leases_item_data)

            leases.append(leases_item)

        paras_lease_info = cls(
            at=at,
            para_lifecycle=para_lifecycle,
            onboarding_as=onboarding_as,
            leases=leases,
        )

        paras_lease_info.additional_properties = d
        return paras_lease_info

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
