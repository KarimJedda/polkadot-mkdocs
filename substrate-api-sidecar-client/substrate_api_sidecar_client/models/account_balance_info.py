from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.balance_lock import BalanceLock
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="AccountBalanceInfo")


@_attrs_define
class AccountBalanceInfo:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        nonce (Union[Unset, str]): Account nonce.
        token_symbol (Union[Unset, str]): Token symbol of the balances displayed in this response.
        free (Union[Unset, str]): Free balance of the account. Not equivalent to _spendable_ balance. This is the only
            balance that matters in terms of most operations on tokens.
        reserved (Union[Unset, str]): Reserved balance of the account.
        misc_frozen (Union[Unset, str]): The amount that `free` may not drop below when withdrawing for anything except
            transaction fee payment. Note, that some runtimes may not have support for miscFrozen and if so the following
            will be returned `miscFrozen does not exist for this runtime`
        fee_frozen (Union[Unset, str]): The amount that `free` may not drop below when withdrawing specifically for
            transaction fee payment. Note, that some runtimes may not have support for feeFrozen and if so the following
            will be returned `feeFrozen does not exist for this runtime`
        frozen (Union[Unset, str]): The amount that `free` may not drop below when reducing the balance, except for
            actions where the account owner cannot reasonably benefit from the balance reduction, such as slashing. Note,
            that some runtimes may not have support for frozen and if so the following will be returned `frozen does not
            exist for this runtime`
        locks (Union[Unset, list['BalanceLock']]): Array of locks on a balance. There can be many of these on an account
            and they "overlap", so the same balance is frozen by multiple locks
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    nonce: Union[Unset, str] = UNSET
    token_symbol: Union[Unset, str] = UNSET
    free: Union[Unset, str] = UNSET
    reserved: Union[Unset, str] = UNSET
    misc_frozen: Union[Unset, str] = UNSET
    fee_frozen: Union[Unset, str] = UNSET
    frozen: Union[Unset, str] = UNSET
    locks: Union[Unset, list["BalanceLock"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        nonce = self.nonce

        token_symbol = self.token_symbol

        free = self.free

        reserved = self.reserved

        misc_frozen = self.misc_frozen

        fee_frozen = self.fee_frozen

        frozen = self.frozen

        locks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locks, Unset):
            locks = []
            for locks_item_data in self.locks:
                locks_item = locks_item_data.to_dict()
                locks.append(locks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if token_symbol is not UNSET:
            field_dict["tokenSymbol"] = token_symbol
        if free is not UNSET:
            field_dict["free"] = free
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if misc_frozen is not UNSET:
            field_dict["miscFrozen"] = misc_frozen
        if fee_frozen is not UNSET:
            field_dict["feeFrozen"] = fee_frozen
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if locks is not UNSET:
            field_dict["locks"] = locks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.balance_lock import BalanceLock
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        nonce = d.pop("nonce", UNSET)

        token_symbol = d.pop("tokenSymbol", UNSET)

        free = d.pop("free", UNSET)

        reserved = d.pop("reserved", UNSET)

        misc_frozen = d.pop("miscFrozen", UNSET)

        fee_frozen = d.pop("feeFrozen", UNSET)

        frozen = d.pop("frozen", UNSET)

        locks = []
        _locks = d.pop("locks", UNSET)
        for locks_item_data in _locks or []:
            locks_item = BalanceLock.from_dict(locks_item_data)

            locks.append(locks_item)

        account_balance_info = cls(
            at=at,
            nonce=nonce,
            token_symbol=token_symbol,
            free=free,
            reserved=reserved,
            misc_frozen=misc_frozen,
            fee_frozen=fee_frozen,
            frozen=frozen,
            locks=locks,
        )

        account_balance_info.additional_properties = d
        return account_balance_info

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
