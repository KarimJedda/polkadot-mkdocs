from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_staking_payouts_eras_payouts_item import AccountStakingPayoutsErasPayoutsItem
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="AccountStakingPayouts")


@_attrs_define
class AccountStakingPayouts:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        eras_payouts (Union[Unset, list['AccountStakingPayoutsErasPayoutsItem']]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    eras_payouts: Union[Unset, list["AccountStakingPayoutsErasPayoutsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        eras_payouts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.eras_payouts, Unset):
            eras_payouts = []
            for eras_payouts_item_data in self.eras_payouts:
                eras_payouts_item = eras_payouts_item_data.to_dict()
                eras_payouts.append(eras_payouts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if eras_payouts is not UNSET:
            field_dict["erasPayouts"] = eras_payouts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.account_staking_payouts_eras_payouts_item import AccountStakingPayoutsErasPayoutsItem
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        eras_payouts = []
        _eras_payouts = d.pop("erasPayouts", UNSET)
        for eras_payouts_item_data in _eras_payouts or []:
            eras_payouts_item = AccountStakingPayoutsErasPayoutsItem.from_dict(eras_payouts_item_data)

            eras_payouts.append(eras_payouts_item)

        account_staking_payouts = cls(
            at=at,
            eras_payouts=eras_payouts,
        )

        account_staking_payouts.additional_properties = d
        return account_staking_payouts

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
