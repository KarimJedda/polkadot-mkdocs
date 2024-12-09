from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.paras_headers_para_id import ParasHeadersParaId


T = TypeVar("T", bound="ParasHeaders")


@_attrs_define
class ParasHeaders:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        para_id (Union[Unset, ParasHeadersParaId]): The key is not named `paraId` and will be the number of the
            parachain. There is technically no limit to the number of paraId keys there can be.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    para_id: Union[Unset, "ParasHeadersParaId"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        para_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.para_id, Unset):
            para_id = self.para_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if para_id is not UNSET:
            field_dict["paraId"] = para_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.paras_headers_para_id import ParasHeadersParaId

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        _para_id = d.pop("paraId", UNSET)
        para_id: Union[Unset, ParasHeadersParaId]
        if isinstance(_para_id, Unset):
            para_id = UNSET
        else:
            para_id = ParasHeadersParaId.from_dict(_para_id)

        paras_headers = cls(
            at=at,
            para_id=para_id,
        )

        paras_headers.additional_properties = d
        return paras_headers

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
