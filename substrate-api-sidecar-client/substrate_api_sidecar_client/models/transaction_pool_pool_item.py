from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionPoolPoolItem")


@_attrs_define
class TransactionPoolPoolItem:
    """
    Attributes:
        hash_ (Union[Unset, str]): H256 hash of the extrinsic.
        encoded_extrinsic (Union[Unset, str]): Scale encoded extrinsic.
        tip (Union[Unset, str]): The tip included in the extrinsic. Only included if the query param `includeFee` is set
            to true.
        priority (Union[Unset, str]): Computed priority of an extrinsic. Only included if the query param `includeFee`
            is set to true.
        partial_fee (Union[Unset, str]): Provided `partialFee` of an extrinsic. Only included if the query param
            `includeFee` is set to true.
    """

    hash_: Union[Unset, str] = UNSET
    encoded_extrinsic: Union[Unset, str] = UNSET
    tip: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    partial_fee: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        encoded_extrinsic = self.encoded_extrinsic

        tip = self.tip

        priority = self.priority

        partial_fee = self.partial_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if encoded_extrinsic is not UNSET:
            field_dict["encodedExtrinsic"] = encoded_extrinsic
        if tip is not UNSET:
            field_dict["tip"] = tip
        if priority is not UNSET:
            field_dict["priority"] = priority
        if partial_fee is not UNSET:
            field_dict["partialFee"] = partial_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_ = d.pop("hash", UNSET)

        encoded_extrinsic = d.pop("encodedExtrinsic", UNSET)

        tip = d.pop("tip", UNSET)

        priority = d.pop("priority", UNSET)

        partial_fee = d.pop("partialFee", UNSET)

        transaction_pool_pool_item = cls(
            hash_=hash_,
            encoded_extrinsic=encoded_extrinsic,
            tip=tip,
            priority=priority,
            partial_fee=partial_fee,
        )

        transaction_pool_pool_item.additional_properties = d
        return transaction_pool_pool_item

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
