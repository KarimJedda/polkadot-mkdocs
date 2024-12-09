from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_fee_estimate_class import TransactionFeeEstimateClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weights_v2 import WeightsV2


T = TypeVar("T", bound="TransactionFeeEstimate")


@_attrs_define
class TransactionFeeEstimate:
    """Note: `partialFee` does not include any tips that you may add to increase a transaction's priority. See
    [compute_fee](https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.compute_fee).

        Attributes:
            weight (Union[Unset, WeightsV2]):
            class_ (Union[Unset, TransactionFeeEstimateClass]): Extrinsic class.
            partial_fee (Union[Unset, str]): Expected inclusion fee for the transaction. Note that the fee rate changes up
                to 30% in a 24 hour period and this will not be the exact fee.
    """

    weight: Union[Unset, "WeightsV2"] = UNSET
    class_: Union[Unset, TransactionFeeEstimateClass] = UNSET
    partial_fee: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        class_: Union[Unset, str] = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        partial_fee = self.partial_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if class_ is not UNSET:
            field_dict["class"] = class_
        if partial_fee is not UNSET:
            field_dict["partialFee"] = partial_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.weights_v2 import WeightsV2

        d = src_dict.copy()
        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, WeightsV2]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = WeightsV2.from_dict(_weight)

        _class_ = d.pop("class", UNSET)
        class_: Union[Unset, TransactionFeeEstimateClass]
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = TransactionFeeEstimateClass(_class_)

        partial_fee = d.pop("partialFee", UNSET)

        transaction_fee_estimate = cls(
            weight=weight,
            class_=class_,
            partial_fee=partial_fee,
        )

        transaction_fee_estimate.additional_properties = d
        return transaction_fee_estimate

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
