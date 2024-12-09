from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PalletsOnGoingReferendaReferendaItemDeciding")


@_attrs_define
class PalletsOnGoingReferendaReferendaItemDeciding:
    """
    Attributes:
        since (Union[Unset, str]): The block number at which the referendum started being `decided`.
        confirming (Union[Unset, str]): The block number at which the referendum's confirmation stage will end at as
            long as it doesn't lose its approval in the meantime.
    """

    since: Union[Unset, str] = UNSET
    confirming: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        since = self.since

        confirming = self.confirming

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if since is not UNSET:
            field_dict["since"] = since
        if confirming is not UNSET:
            field_dict["confirming"] = confirming

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        since = d.pop("since", UNSET)

        confirming = d.pop("confirming", UNSET)

        pallets_on_going_referenda_referenda_item_deciding = cls(
            since=since,
            confirming=confirming,
        )

        pallets_on_going_referenda_referenda_item_deciding.additional_properties = d
        return pallets_on_going_referenda_referenda_item_deciding

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
