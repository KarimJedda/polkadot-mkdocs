from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.onboarding_as import OnboardingAs
from ..models.para_lifecycle import ParaLifecycle
from ..types import UNSET, Unset

T = TypeVar("T", bound="Para")


@_attrs_define
class Para:
    """
    Attributes:
        para_id (Union[Unset, str]):
        para_lifecycle (Union[Unset, ParaLifecycle]): The possible states of a para, to take into account delayed
            lifecycle
            changes.
        onboarding_as (Union[Unset, OnboardingAs]): This property only shows up when `paraLifecycle=onboarding`. It
            describes if a particular para is onboarding as a `parachain` or a
            `parathread`.
    """

    para_id: Union[Unset, str] = UNSET
    para_lifecycle: Union[Unset, ParaLifecycle] = UNSET
    onboarding_as: Union[Unset, OnboardingAs] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        para_id = self.para_id

        para_lifecycle: Union[Unset, str] = UNSET
        if not isinstance(self.para_lifecycle, Unset):
            para_lifecycle = self.para_lifecycle.value

        onboarding_as: Union[Unset, str] = UNSET
        if not isinstance(self.onboarding_as, Unset):
            onboarding_as = self.onboarding_as.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if para_id is not UNSET:
            field_dict["paraId"] = para_id
        if para_lifecycle is not UNSET:
            field_dict["paraLifecycle"] = para_lifecycle
        if onboarding_as is not UNSET:
            field_dict["onboardingAs"] = onboarding_as

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        para_id = d.pop("paraId", UNSET)

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

        para = cls(
            para_id=para_id,
            para_lifecycle=para_lifecycle,
            onboarding_as=onboarding_as,
        )

        para.additional_properties = d
        return para

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
