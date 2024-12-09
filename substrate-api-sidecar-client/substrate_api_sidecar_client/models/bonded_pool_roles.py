from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BondedPoolRoles")


@_attrs_define
class BondedPoolRoles:
    """
    Attributes:
        depositor (Union[Unset, str]):
        root (Union[Unset, str]):
        nominator (Union[Unset, str]):
        state_toggler (Union[Unset, str]):
    """

    depositor: Union[Unset, str] = UNSET
    root: Union[Unset, str] = UNSET
    nominator: Union[Unset, str] = UNSET
    state_toggler: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depositor = self.depositor

        root = self.root

        nominator = self.nominator

        state_toggler = self.state_toggler

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if depositor is not UNSET:
            field_dict["depositor"] = depositor
        if root is not UNSET:
            field_dict["root"] = root
        if nominator is not UNSET:
            field_dict["nominator"] = nominator
        if state_toggler is not UNSET:
            field_dict["stateToggler"] = state_toggler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        depositor = d.pop("depositor", UNSET)

        root = d.pop("root", UNSET)

        nominator = d.pop("nominator", UNSET)

        state_toggler = d.pop("stateToggler", UNSET)

        bonded_pool_roles = cls(
            depositor=depositor,
            root=root,
            nominator=nominator,
            state_toggler=state_toggler,
        )

        bonded_pool_roles.additional_properties = d
        return bonded_pool_roles

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
