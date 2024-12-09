from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bonded_pool_roles import BondedPoolRoles


T = TypeVar("T", bound="BondedPool")


@_attrs_define
class BondedPool:
    """
    Attributes:
        points (Union[Unset, float]):
        state (Union[Unset, str]):
        member_counter (Union[Unset, float]):
        roles (Union[Unset, BondedPoolRoles]):
    """

    points: Union[Unset, float] = UNSET
    state: Union[Unset, str] = UNSET
    member_counter: Union[Unset, float] = UNSET
    roles: Union[Unset, "BondedPoolRoles"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points

        state = self.state

        member_counter = self.member_counter

        roles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points is not UNSET:
            field_dict["points"] = points
        if state is not UNSET:
            field_dict["state"] = state
        if member_counter is not UNSET:
            field_dict["memberCounter"] = member_counter
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bonded_pool_roles import BondedPoolRoles

        d = src_dict.copy()
        points = d.pop("points", UNSET)

        state = d.pop("state", UNSET)

        member_counter = d.pop("memberCounter", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: Union[Unset, BondedPoolRoles]
        if isinstance(_roles, Unset):
            roles = UNSET
        else:
            roles = BondedPoolRoles.from_dict(_roles)

        bonded_pool = cls(
            points=points,
            state=state,
            member_counter=member_counter,
            roles=roles,
        )

        bonded_pool.additional_properties = d
        return bonded_pool

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
