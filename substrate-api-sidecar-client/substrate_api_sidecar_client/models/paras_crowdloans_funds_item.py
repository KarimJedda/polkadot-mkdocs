from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fund_info import FundInfo


T = TypeVar("T", bound="ParasCrowdloansFundsItem")


@_attrs_define
class ParasCrowdloansFundsItem:
    """
    Attributes:
        para_id (Union[Unset, str]):
        fund_info (Union[Unset, FundInfo]):
    """

    para_id: Union[Unset, str] = UNSET
    fund_info: Union[Unset, "FundInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        para_id = self.para_id

        fund_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund_info, Unset):
            fund_info = self.fund_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if para_id is not UNSET:
            field_dict["paraId"] = para_id
        if fund_info is not UNSET:
            field_dict["fundInfo"] = fund_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.fund_info import FundInfo

        d = src_dict.copy()
        para_id = d.pop("paraId", UNSET)

        _fund_info = d.pop("fundInfo", UNSET)
        fund_info: Union[Unset, FundInfo]
        if isinstance(_fund_info, Unset):
            fund_info = UNSET
        else:
            fund_info = FundInfo.from_dict(_fund_info)

        paras_crowdloans_funds_item = cls(
            para_id=para_id,
            fund_info=fund_info,
        )

        paras_crowdloans_funds_item.additional_properties = d
        return paras_crowdloans_funds_item

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
