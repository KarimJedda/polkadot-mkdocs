from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_header_digest import BlockHeaderDigest


T = TypeVar("T", bound="BlockHeader")


@_attrs_define
class BlockHeader:
    """
    Attributes:
        parent_hash (Union[Unset, str]): The hash of the parent block.
        number (Union[Unset, str]): The block's height.
        state_root (Union[Unset, str]): The state root after executing this block.
        extrinsic_root (Union[Unset, str]): The Merkle root of the extrinsics.
        digest (Union[Unset, BlockHeaderDigest]):
    """

    parent_hash: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    state_root: Union[Unset, str] = UNSET
    extrinsic_root: Union[Unset, str] = UNSET
    digest: Union[Unset, "BlockHeaderDigest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_hash = self.parent_hash

        number = self.number

        state_root = self.state_root

        extrinsic_root = self.extrinsic_root

        digest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_hash is not UNSET:
            field_dict["parentHash"] = parent_hash
        if number is not UNSET:
            field_dict["number"] = number
        if state_root is not UNSET:
            field_dict["stateRoot"] = state_root
        if extrinsic_root is not UNSET:
            field_dict["extrinsicRoot"] = extrinsic_root
        if digest is not UNSET:
            field_dict["digest"] = digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_header_digest import BlockHeaderDigest

        d = src_dict.copy()
        parent_hash = d.pop("parentHash", UNSET)

        number = d.pop("number", UNSET)

        state_root = d.pop("stateRoot", UNSET)

        extrinsic_root = d.pop("extrinsicRoot", UNSET)

        _digest = d.pop("digest", UNSET)
        digest: Union[Unset, BlockHeaderDigest]
        if isinstance(_digest, Unset):
            digest = UNSET
        else:
            digest = BlockHeaderDigest.from_dict(_digest)

        block_header = cls(
            parent_hash=parent_hash,
            number=number,
            state_root=state_root,
            extrinsic_root=extrinsic_root,
            digest=digest,
        )

        block_header.additional_properties = d
        return block_header

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
