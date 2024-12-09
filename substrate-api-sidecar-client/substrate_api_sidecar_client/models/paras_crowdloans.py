from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.paras_crowdloans_funds_item import ParasCrowdloansFundsItem


T = TypeVar("T", bound="ParasCrowdloans")


@_attrs_define
class ParasCrowdloans:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        funds (Union[Unset, list['ParasCrowdloansFundsItem']]): List of paras that have crowdloans.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    funds: Union[Unset, list["ParasCrowdloansFundsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        funds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.funds, Unset):
            funds = []
            for funds_item_data in self.funds:
                funds_item = funds_item_data.to_dict()
                funds.append(funds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if funds is not UNSET:
            field_dict["funds"] = funds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.paras_crowdloans_funds_item import ParasCrowdloansFundsItem

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        funds = []
        _funds = d.pop("funds", UNSET)
        for funds_item_data in _funds or []:
            funds_item = ParasCrowdloansFundsItem.from_dict(funds_item_data)

            funds.append(funds_item)

        paras_crowdloans = cls(
            at=at,
            funds=funds,
        )

        paras_crowdloans.additional_properties = d
        return paras_crowdloans

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
