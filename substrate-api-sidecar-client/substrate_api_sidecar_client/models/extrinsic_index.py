from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.extrinsic import Extrinsic


T = TypeVar("T", bound="ExtrinsicIndex")


@_attrs_define
class ExtrinsicIndex:
    """A single extrinsic at a given block.

    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        extrinsic (Union[Unset, Extrinsic]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    extrinsic: Union[Unset, "Extrinsic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        extrinsic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extrinsic, Unset):
            extrinsic = self.extrinsic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if extrinsic is not UNSET:
            field_dict["extrinsic"] = extrinsic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.extrinsic import Extrinsic

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _extrinsic = d.pop("extrinsic", UNSET)
        extrinsic: Union[Unset, Extrinsic]
        if isinstance(_extrinsic, Unset):
            extrinsic = UNSET
        else:
            extrinsic = Extrinsic.from_dict(_extrinsic)

        extrinsic_index = cls(
            at=at,
            extrinsic=extrinsic,
        )

        extrinsic_index.additional_properties = d
        return extrinsic_index

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
