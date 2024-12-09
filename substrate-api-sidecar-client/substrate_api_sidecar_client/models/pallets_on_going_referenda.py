from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.pallets_on_going_referenda_referenda_item import PalletsOnGoingReferendaReferendaItem


T = TypeVar("T", bound="PalletsOnGoingReferenda")


@_attrs_define
class PalletsOnGoingReferenda:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        referenda (Union[Unset, list['PalletsOnGoingReferendaReferendaItem']]): A list of ongoing referenda and their
            details.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    referenda: Union[Unset, list["PalletsOnGoingReferendaReferendaItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        referenda: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.referenda, Unset):
            referenda = []
            for referenda_item_data in self.referenda:
                referenda_item = referenda_item_data.to_dict()
                referenda.append(referenda_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if referenda is not UNSET:
            field_dict["referenda"] = referenda

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.pallets_on_going_referenda_referenda_item import PalletsOnGoingReferendaReferendaItem

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        referenda = []
        _referenda = d.pop("referenda", UNSET)
        for referenda_item_data in _referenda or []:
            referenda_item = PalletsOnGoingReferendaReferendaItem.from_dict(referenda_item_data)

            referenda.append(referenda_item)

        pallets_on_going_referenda = cls(
            at=at,
            referenda=referenda,
        )

        pallets_on_going_referenda.additional_properties = d
        return pallets_on_going_referenda

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
