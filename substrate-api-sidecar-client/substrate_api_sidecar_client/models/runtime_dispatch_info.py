from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.runtime_dispatch_info_class import RuntimeDispatchInfoClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weights_v2 import WeightsV2


T = TypeVar("T", bound="RuntimeDispatchInfo")


@_attrs_define
class RuntimeDispatchInfo:
    """RuntimeDispatchInfo for the transaction. Includes the `partialFee`.

    Attributes:
        weight (Union[Unset, WeightsV2]):
        class_ (Union[Unset, RuntimeDispatchInfoClass]): Extrinsic class.
        partial_fee (Union[Unset, str]): The _inclusion fee_ of a transaction, i.e. the minimum fee required for a
            transaction. Includes weight and encoded length fees, but does not have access to any signed extensions, e.g.
            the `tip`.
        kind (Union[Unset, str]): Information on the partialFee that is collected. Can be either `preDispatch`,
            `postDispatch` or `fromEvent`. `preDispatch` means the information used to collect the fee was from
            `payment_queryInfo`, `postDispatch` means the information used to calculate the fee was from finalized weights
            for the extrinsic, and `fromEvent` means that the partialFee was abstracted from the
            `TransactionPayment::TransactionPaidFee` event.
    """

    weight: Union[Unset, "WeightsV2"] = UNSET
    class_: Union[Unset, RuntimeDispatchInfoClass] = UNSET
    partial_fee: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        class_: Union[Unset, str] = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        partial_fee = self.partial_fee

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if class_ is not UNSET:
            field_dict["class"] = class_
        if partial_fee is not UNSET:
            field_dict["partialFee"] = partial_fee
        if kind is not UNSET:
            field_dict["kind"] = kind

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
        class_: Union[Unset, RuntimeDispatchInfoClass]
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = RuntimeDispatchInfoClass(_class_)

        partial_fee = d.pop("partialFee", UNSET)

        kind = d.pop("kind", UNSET)

        runtime_dispatch_info = cls(
            weight=weight,
            class_=class_,
            partial_fee=partial_fee,
            kind=kind,
        )

        runtime_dispatch_info.additional_properties = d
        return runtime_dispatch_info

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
