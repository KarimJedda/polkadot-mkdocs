from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_raw_digest import BlockRawDigest


T = TypeVar("T", bound="BlockRaw")


@_attrs_define
class BlockRaw:
    """
    Attributes:
        number (Union[Unset, str]): The block's height.
        parent_hash (Union[Unset, str]): The hash of the parent block.
        state_root (Union[Unset, str]): The state root after executing this block.
        extrinsic_root (Union[Unset, str]): The Merkle root of the extrinsics.
        digest (Union[Unset, BlockRawDigest]):
        extrinsics (Union[Unset, list[str]]): Array of raw extrinsics (inherents and transactions) within the block.
    """

    number: Union[Unset, str] = UNSET
    parent_hash: Union[Unset, str] = UNSET
    state_root: Union[Unset, str] = UNSET
    extrinsic_root: Union[Unset, str] = UNSET
    digest: Union[Unset, "BlockRawDigest"] = UNSET
    extrinsics: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        parent_hash = self.parent_hash

        state_root = self.state_root

        extrinsic_root = self.extrinsic_root

        digest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest.to_dict()

        extrinsics: Union[Unset, list[str]] = UNSET
        if not isinstance(self.extrinsics, Unset):
            extrinsics = self.extrinsics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if parent_hash is not UNSET:
            field_dict["parentHash"] = parent_hash
        if state_root is not UNSET:
            field_dict["stateRoot"] = state_root
        if extrinsic_root is not UNSET:
            field_dict["extrinsicRoot"] = extrinsic_root
        if digest is not UNSET:
            field_dict["digest"] = digest
        if extrinsics is not UNSET:
            field_dict["extrinsics"] = extrinsics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_raw_digest import BlockRawDigest

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        parent_hash = d.pop("parentHash", UNSET)

        state_root = d.pop("stateRoot", UNSET)

        extrinsic_root = d.pop("extrinsicRoot", UNSET)

        _digest = d.pop("digest", UNSET)
        digest: Union[Unset, BlockRawDigest]
        if isinstance(_digest, Unset):
            digest = UNSET
        else:
            digest = BlockRawDigest.from_dict(_digest)

        extrinsics = cast(list[str], d.pop("extrinsics", UNSET))

        block_raw = cls(
            number=number,
            parent_hash=parent_hash,
            state_root=state_root,
            extrinsic_root=extrinsic_root,
            digest=digest,
            extrinsics=extrinsics,
        )

        block_raw.additional_properties = d
        return block_raw

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
