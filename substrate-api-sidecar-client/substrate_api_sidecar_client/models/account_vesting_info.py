from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.vesting_schedule import VestingSchedule


T = TypeVar("T", bound="AccountVestingInfo")


@_attrs_define
class AccountVestingInfo:
    """Sidecar version's <= v10.0.0 have a`vesting` return value that defaults to an object for when there is no available
    vesting-info data. It also returns a `VestingInfo` as an object. For Sidecar >=11.0.0, that value will now default
    as an array when there is no value, and `Vec<PalletsPalletVestingInfo>` is returned when there is.

        Attributes:
            at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
            vesting (Union[Unset, list['VestingSchedule']]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    vesting: Union[Unset, list["VestingSchedule"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        vesting: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vesting, Unset):
            vesting = []
            for vesting_item_data in self.vesting:
                vesting_item = vesting_item_data.to_dict()
                vesting.append(vesting_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if vesting is not UNSET:
            field_dict["vesting"] = vesting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.vesting_schedule import VestingSchedule

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        vesting = []
        _vesting = d.pop("vesting", UNSET)
        for vesting_item_data in _vesting or []:
            vesting_item = VestingSchedule.from_dict(vesting_item_data)

            vesting.append(vesting_item)

        account_vesting_info = cls(
            at=at,
            vesting=vesting,
        )

        account_vesting_info.additional_properties = d
        return account_vesting_info

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
