from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="AccountAssetsApproval")


@_attrs_define
class AccountAssetsApproval:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        amount (Union[Unset, str]): The amount of funds approved for the balance transfer from the owner to some
            delegated target.
        deposit (Union[Unset, str]): The amount reserved on the owner's account to hold this item in storage.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    amount: Union[Unset, str] = UNSET
    deposit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        amount = self.amount

        deposit = self.deposit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if deposit is not UNSET:
            field_dict["deposit"] = deposit

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

        amount = d.pop("amount", UNSET)

        deposit = d.pop("deposit", UNSET)

        account_assets_approval = cls(
            at=at,
            amount=amount,
            deposit=deposit,
        )

        account_assets_approval.additional_properties = d
        return account_assets_approval

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
