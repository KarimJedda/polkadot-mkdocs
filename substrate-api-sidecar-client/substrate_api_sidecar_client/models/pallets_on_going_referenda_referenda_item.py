from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pallets_on_going_referenda_referenda_item_enactment import PalletsOnGoingReferendaReferendaItemEnactment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pallets_on_going_referenda_referenda_item_deciding import PalletsOnGoingReferendaReferendaItemDeciding
    from ..models.pallets_on_going_referenda_referenda_item_decision_deposit import (
        PalletsOnGoingReferendaReferendaItemDecisionDeposit,
    )


T = TypeVar("T", bound="PalletsOnGoingReferendaReferendaItem")


@_attrs_define
class PalletsOnGoingReferendaReferendaItem:
    """
    Attributes:
        id (Union[Unset, str]): Referendum's id.
        decision_deposit (Union[Unset, PalletsOnGoingReferendaReferendaItemDecisionDeposit]): A deposit which is
            required for a referendum to progress to the decision phase.
        enactment (Union[Unset, PalletsOnGoingReferendaReferendaItemEnactment]): The enactment period of the referendum.
            It can be defined using either the `at` option, which specifies the exact block height when the referendum will
            be enacted, or the `after` option, which indicates the number of blocks after which the enactment will occur.
        submitted (Union[Unset, str]): The block number at which the referendum was submitted.
        deciding (Union[Unset, PalletsOnGoingReferendaReferendaItemDeciding]):
    """

    id: Union[Unset, str] = UNSET
    decision_deposit: Union[Unset, "PalletsOnGoingReferendaReferendaItemDecisionDeposit"] = UNSET
    enactment: Union[Unset, PalletsOnGoingReferendaReferendaItemEnactment] = UNSET
    submitted: Union[Unset, str] = UNSET
    deciding: Union[Unset, "PalletsOnGoingReferendaReferendaItemDeciding"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        decision_deposit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.decision_deposit, Unset):
            decision_deposit = self.decision_deposit.to_dict()

        enactment: Union[Unset, str] = UNSET
        if not isinstance(self.enactment, Unset):
            enactment = self.enactment.value

        submitted = self.submitted

        deciding: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deciding, Unset):
            deciding = self.deciding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if decision_deposit is not UNSET:
            field_dict["decisionDeposit"] = decision_deposit
        if enactment is not UNSET:
            field_dict["enactment"] = enactment
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if deciding is not UNSET:
            field_dict["deciding"] = deciding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pallets_on_going_referenda_referenda_item_deciding import (
            PalletsOnGoingReferendaReferendaItemDeciding,
        )
        from ..models.pallets_on_going_referenda_referenda_item_decision_deposit import (
            PalletsOnGoingReferendaReferendaItemDecisionDeposit,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _decision_deposit = d.pop("decisionDeposit", UNSET)
        decision_deposit: Union[Unset, PalletsOnGoingReferendaReferendaItemDecisionDeposit]
        if isinstance(_decision_deposit, Unset):
            decision_deposit = UNSET
        else:
            decision_deposit = PalletsOnGoingReferendaReferendaItemDecisionDeposit.from_dict(_decision_deposit)

        _enactment = d.pop("enactment", UNSET)
        enactment: Union[Unset, PalletsOnGoingReferendaReferendaItemEnactment]
        if isinstance(_enactment, Unset):
            enactment = UNSET
        else:
            enactment = PalletsOnGoingReferendaReferendaItemEnactment(_enactment)

        submitted = d.pop("submitted", UNSET)

        _deciding = d.pop("deciding", UNSET)
        deciding: Union[Unset, PalletsOnGoingReferendaReferendaItemDeciding]
        if isinstance(_deciding, Unset):
            deciding = UNSET
        else:
            deciding = PalletsOnGoingReferendaReferendaItemDeciding.from_dict(_deciding)

        pallets_on_going_referenda_referenda_item = cls(
            id=id,
            decision_deposit=decision_deposit,
            enactment=enactment,
            submitted=submitted,
            deciding=deciding,
        )

        pallets_on_going_referenda_referenda_item.additional_properties = d
        return pallets_on_going_referenda_referenda_item

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
