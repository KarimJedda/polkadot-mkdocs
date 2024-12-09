from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.para import Para


T = TypeVar("T", bound="Paras")


@_attrs_define
class Paras:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        paras (Union[Unset, list['Para']]):
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    paras: Union[Unset, list["Para"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        paras: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.paras, Unset):
            paras = []
            for paras_item_data in self.paras:
                paras_item = paras_item_data.to_dict()
                paras.append(paras_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if paras is not UNSET:
            field_dict["paras"] = paras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.para import Para

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        paras = []
        _paras = d.pop("paras", UNSET)
        for paras_item_data in _paras or []:
            paras_item = Para.from_dict(paras_item_data)

            paras.append(paras_item)

        paras = cls(
            at=at,
            paras=paras,
        )

        paras.additional_properties = d
        return paras

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
