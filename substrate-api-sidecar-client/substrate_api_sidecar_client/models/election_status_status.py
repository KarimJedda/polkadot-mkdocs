from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ElectionStatusStatus")


@_attrs_define
class ElectionStatusStatus:
    """[Deprecated](Works for polkadot runtimes before v0.8.30).
    Era election status: either `Close: null` or `Open: <BlockNumber>`. A status of `Close` indicates that the
    submission window for solutions from off-chain Phragmen is not open. A status of `Open` indicates that the
    submission window for off-chain Phragmen solutions has been open since BlockNumber. N.B. when the submission window
    is open, certain extrinsics are not allowed because they would mutate the state that the off-chain Phragmen
    calculation relies on for calculating results.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        election_status_status = cls()

        election_status_status.additional_properties = d
        return election_status_status

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
