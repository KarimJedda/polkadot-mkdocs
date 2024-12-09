from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fund_info_last_constribution import FundInfoLastConstribution
from ..types import UNSET, Unset

T = TypeVar("T", bound="FundInfo")


@_attrs_define
class FundInfo:
    """
    Attributes:
        depositor (Union[Unset, str]):
        verifier (Union[Unset, str]):
        deposit (Union[Unset, str]):
        raised (Union[Unset, str]):
        end (Union[Unset, str]):
        cap (Union[Unset, str]):
        last_constribution (Union[Unset, FundInfoLastConstribution]):
        first_period (Union[Unset, str]):
        last_period (Union[Unset, str]):
        trie_index (Union[Unset, str]):
    """

    depositor: Union[Unset, str] = UNSET
    verifier: Union[Unset, str] = UNSET
    deposit: Union[Unset, str] = UNSET
    raised: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    cap: Union[Unset, str] = UNSET
    last_constribution: Union[Unset, FundInfoLastConstribution] = UNSET
    first_period: Union[Unset, str] = UNSET
    last_period: Union[Unset, str] = UNSET
    trie_index: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depositor = self.depositor

        verifier = self.verifier

        deposit = self.deposit

        raised = self.raised

        end = self.end

        cap = self.cap

        last_constribution: Union[Unset, str] = UNSET
        if not isinstance(self.last_constribution, Unset):
            last_constribution = self.last_constribution.value

        first_period = self.first_period

        last_period = self.last_period

        trie_index = self.trie_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if depositor is not UNSET:
            field_dict["depositor"] = depositor
        if verifier is not UNSET:
            field_dict["verifier"] = verifier
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if raised is not UNSET:
            field_dict["raised"] = raised
        if end is not UNSET:
            field_dict["end"] = end
        if cap is not UNSET:
            field_dict["cap"] = cap
        if last_constribution is not UNSET:
            field_dict["lastConstribution"] = last_constribution
        if first_period is not UNSET:
            field_dict["firstPeriod"] = first_period
        if last_period is not UNSET:
            field_dict["lastPeriod"] = last_period
        if trie_index is not UNSET:
            field_dict["trieIndex"] = trie_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        depositor = d.pop("depositor", UNSET)

        verifier = d.pop("verifier", UNSET)

        deposit = d.pop("deposit", UNSET)

        raised = d.pop("raised", UNSET)

        end = d.pop("end", UNSET)

        cap = d.pop("cap", UNSET)

        _last_constribution = d.pop("lastConstribution", UNSET)
        last_constribution: Union[Unset, FundInfoLastConstribution]
        if isinstance(_last_constribution, Unset):
            last_constribution = UNSET
        else:
            last_constribution = FundInfoLastConstribution(_last_constribution)

        first_period = d.pop("firstPeriod", UNSET)

        last_period = d.pop("lastPeriod", UNSET)

        trie_index = d.pop("trieIndex", UNSET)

        fund_info = cls(
            depositor=depositor,
            verifier=verifier,
            deposit=deposit,
            raised=raised,
            end=end,
            cap=cap,
            last_constribution=last_constribution,
            first_period=first_period,
            last_period=last_period,
            trie_index=trie_index,
        )

        fund_info.additional_properties = d
        return fund_info

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
