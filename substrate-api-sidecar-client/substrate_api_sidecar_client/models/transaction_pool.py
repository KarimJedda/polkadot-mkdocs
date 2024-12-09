from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_pool_pool_item import TransactionPoolPoolItem


T = TypeVar("T", bound="TransactionPool")


@_attrs_define
class TransactionPool:
    """
    Attributes:
        pool (Union[Unset, list['TransactionPoolPoolItem']]):
    """

    pool: Union[Unset, list["TransactionPoolPoolItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pool: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = []
            for pool_item_data in self.pool:
                pool_item = pool_item_data.to_dict()
                pool.append(pool_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transaction_pool_pool_item import TransactionPoolPoolItem

        d = src_dict.copy()
        pool = []
        _pool = d.pop("pool", UNSET)
        for pool_item_data in _pool or []:
            pool_item = TransactionPoolPoolItem.from_dict(pool_item_data)

            pool.append(pool_item)

        transaction_pool = cls(
            pool=pool,
        )

        transaction_pool.additional_properties = d
        return transaction_pool

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
