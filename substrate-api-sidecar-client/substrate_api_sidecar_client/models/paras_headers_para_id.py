from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paras_headers_para_id_digest import ParasHeadersParaIdDigest


T = TypeVar("T", bound="ParasHeadersParaId")


@_attrs_define
class ParasHeadersParaId:
    """The key is not named `paraId` and will be the number of the parachain. There is technically no limit to the number
    of paraId keys there can be.

        Attributes:
            hash_ (Union[Unset, str]): The block's hash.
            number (Union[Unset, str]): The block's height.
            parent_hash (Union[Unset, str]): The hash of the parent block.
            state_root (Union[Unset, str]): The state root after executing this block.
            extrinsics_root (Union[Unset, str]): The Merkle root of the extrinsics.
            digest (Union[Unset, ParasHeadersParaIdDigest]):
    """

    hash_: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    parent_hash: Union[Unset, str] = UNSET
    state_root: Union[Unset, str] = UNSET
    extrinsics_root: Union[Unset, str] = UNSET
    digest: Union[Unset, "ParasHeadersParaIdDigest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        number = self.number

        parent_hash = self.parent_hash

        state_root = self.state_root

        extrinsics_root = self.extrinsics_root

        digest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if number is not UNSET:
            field_dict["number"] = number
        if parent_hash is not UNSET:
            field_dict["parentHash"] = parent_hash
        if state_root is not UNSET:
            field_dict["stateRoot"] = state_root
        if extrinsics_root is not UNSET:
            field_dict["extrinsicsRoot"] = extrinsics_root
        if digest is not UNSET:
            field_dict["digest"] = digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.paras_headers_para_id_digest import ParasHeadersParaIdDigest

        d = src_dict.copy()
        hash_ = d.pop("hash", UNSET)

        number = d.pop("number", UNSET)

        parent_hash = d.pop("parentHash", UNSET)

        state_root = d.pop("stateRoot", UNSET)

        extrinsics_root = d.pop("extrinsicsRoot", UNSET)

        _digest = d.pop("digest", UNSET)
        digest: Union[Unset, ParasHeadersParaIdDigest]
        if isinstance(_digest, Unset):
            digest = UNSET
        else:
            digest = ParasHeadersParaIdDigest.from_dict(_digest)

        paras_headers_para_id = cls(
            hash_=hash_,
            number=number,
            parent_hash=parent_hash,
            state_root=state_root,
            extrinsics_root=extrinsics_root,
            digest=digest,
        )

        paras_headers_para_id.additional_properties = d
        return paras_headers_para_id

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
