from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.election_status_status import ElectionStatusStatus


T = TypeVar("T", bound="ElectionStatus")


@_attrs_define
class ElectionStatus:
    """Information about the off-chain election. Not included in response when `forceEra.isForceNone`.

    Attributes:
        status (Union[Unset, ElectionStatusStatus]): [Deprecated](Works for polkadot runtimes before v0.8.30).
            Era election status: either `Close: null` or `Open: <BlockNumber>`. A status of `Close` indicates that the
            submission window for solutions from off-chain Phragmen is not open. A status of `Open` indicates that the
            submission window for off-chain Phragmen solutions has been open since BlockNumber. N.B. when the submission
            window is open, certain extrinsics are not allowed because they would mutate the state that the off-chain
            Phragmen calculation relies on for calculating results.
        toggle_estimate (Union[Unset, str]): Upper bound estimate of the block height at which the `status` will switch.
    """

    status: Union[Unset, "ElectionStatusStatus"] = UNSET
    toggle_estimate: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        toggle_estimate = self.toggle_estimate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if toggle_estimate is not UNSET:
            field_dict["toggleEstimate"] = toggle_estimate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.election_status_status import ElectionStatusStatus

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ElectionStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ElectionStatusStatus.from_dict(_status)

        toggle_estimate = d.pop("toggleEstimate", UNSET)

        election_status = cls(
            status=status,
            toggle_estimate=toggle_estimate,
        )

        election_status.additional_properties = d
        return election_status

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
