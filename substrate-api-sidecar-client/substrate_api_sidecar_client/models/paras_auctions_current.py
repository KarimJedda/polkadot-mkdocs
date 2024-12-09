from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paras_auctions_current_phase import ParasAuctionsCurrentPhase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.winning_data import WinningData


T = TypeVar("T", bound="ParasAuctionsCurrent")


@_attrs_define
class ParasAuctionsCurrent:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        begin_end (Union[Unset, str]): Fist block (number) of the auction ending phase. `null` if there is no ongoing
            auction.
        finish_end (Union[Unset, str]): Last block (number) of the auction ending phase. `null` if there is no ongoing
            auction.
        phase (Union[Unset, ParasAuctionsCurrentPhase]): An auction can be in one of 4 phases. Both `startingPeriod` ()
            and `endingPeriod` indicate
            an ongoing auction, while `vrfDelay` lines up with the `AuctionStatus::VrfDelay` . Finally, a value of `null`
            indicates there is no ongoing auction. Keep in mind the that the `finishEnd` field is the block number the
            `endingPeriod` finishes and the `vrfDelay` period begins. The `vrfDelay` period is typically about an
            epoch long and no crowdloan contributions are accepted.
        auction_index (Union[Unset, str]): The auction number. If there is no current auction this will be the number
            of the previous auction.
        lease_periods (Union[Unset, list[str]]): Lease period indexes that may be bid on in this auction. `null` if
            there is no ongoing auction.
        winning (Union[Unset, list['WinningData']]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    begin_end: Union[Unset, str] = UNSET
    finish_end: Union[Unset, str] = UNSET
    phase: Union[Unset, ParasAuctionsCurrentPhase] = UNSET
    auction_index: Union[Unset, str] = UNSET
    lease_periods: Union[Unset, list[str]] = UNSET
    winning: Union[Unset, list["WinningData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        begin_end = self.begin_end

        finish_end = self.finish_end

        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        auction_index = self.auction_index

        lease_periods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lease_periods, Unset):
            lease_periods = self.lease_periods

        winning: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.winning, Unset):
            winning = []
            for winning_item_data in self.winning:
                winning_item = winning_item_data.to_dict()
                winning.append(winning_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if begin_end is not UNSET:
            field_dict["beginEnd"] = begin_end
        if finish_end is not UNSET:
            field_dict["finishEnd"] = finish_end
        if phase is not UNSET:
            field_dict["phase"] = phase
        if auction_index is not UNSET:
            field_dict["auctionIndex"] = auction_index
        if lease_periods is not UNSET:
            field_dict["leasePeriods"] = lease_periods
        if winning is not UNSET:
            field_dict["winning"] = winning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.winning_data import WinningData

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        begin_end = d.pop("beginEnd", UNSET)

        finish_end = d.pop("finishEnd", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, ParasAuctionsCurrentPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = ParasAuctionsCurrentPhase(_phase)

        auction_index = d.pop("auctionIndex", UNSET)

        lease_periods = cast(list[str], d.pop("leasePeriods", UNSET))

        winning = []
        _winning = d.pop("winning", UNSET)
        for winning_item_data in _winning or []:
            winning_item = WinningData.from_dict(winning_item_data)

            winning.append(winning_item)

        paras_auctions_current = cls(
            at=at,
            begin_end=begin_end,
            finish_end=finish_end,
            phase=phase,
            auction_index=auction_index,
            lease_periods=lease_periods,
            winning=winning,
        )

        paras_auctions_current.additional_properties = d
        return paras_auctions_current

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
