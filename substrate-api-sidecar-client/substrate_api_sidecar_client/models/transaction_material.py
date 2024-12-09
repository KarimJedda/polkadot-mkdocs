from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers


T = TypeVar("T", bound="TransactionMaterial")


@_attrs_define
class TransactionMaterial:
    """Note: `chainName`, `specName`, and `specVersion` are used to define a type registry with a set of signed extensions
    and types. For Polkadot and Kusama, `chainName` is not used in defining this registry, but in other Substrate-based
    chains that re-launch their network without changing the `specName`, the `chainName` would be needed to create the
    correct registry. Substrate Reference: - `RuntimeVersion`:
    https://crates.parity.io/sp_version/struct.RuntimeVersion.html - `SignedExtension`:
    https://crates.parity.io/sp_runtime/traits/trait.SignedExtension.html -  FRAME Support:
    https://crates.parity.io/frame_support/metadata/index.html

        Attributes:
            at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
            genesis_hash (Union[Unset, str]): The hash of the chain's genesis block.
            chain_name (Union[Unset, str]): The chain's name.
            spec_name (Union[Unset, str]): The chain's spec.
            spec_version (Union[Unset, str]): The spec version. Always increased in a runtime upgrade.
            tx_version (Union[Unset, str]): The transaction version. Common `txVersion` numbers indicate that the
                transaction encoding format and method indices are the same. Needed for decoding in an offline environment.
                Adding new transactions does not change `txVersion`.
            metadata (Union[Unset, str]): The chain's metadata. It will only be present when the metadata query param is
                used.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    genesis_hash: Union[Unset, str] = UNSET
    chain_name: Union[Unset, str] = UNSET
    spec_name: Union[Unset, str] = UNSET
    spec_version: Union[Unset, str] = UNSET
    tx_version: Union[Unset, str] = UNSET
    metadata: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        genesis_hash = self.genesis_hash

        chain_name = self.chain_name

        spec_name = self.spec_name

        spec_version = self.spec_version

        tx_version = self.tx_version

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if genesis_hash is not UNSET:
            field_dict["genesisHash"] = genesis_hash
        if chain_name is not UNSET:
            field_dict["chainName"] = chain_name
        if spec_name is not UNSET:
            field_dict["specName"] = spec_name
        if spec_version is not UNSET:
            field_dict["specVersion"] = spec_version
        if tx_version is not UNSET:
            field_dict["txVersion"] = tx_version
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        genesis_hash = d.pop("genesisHash", UNSET)

        chain_name = d.pop("chainName", UNSET)

        spec_name = d.pop("specName", UNSET)

        spec_version = d.pop("specVersion", UNSET)

        tx_version = d.pop("txVersion", UNSET)

        metadata = d.pop("metadata", UNSET)

        transaction_material = cls(
            at=at,
            genesis_hash=genesis_hash,
            chain_name=chain_name,
            spec_name=spec_name,
            spec_version=spec_version,
            tx_version=tx_version,
            metadata=metadata,
        )

        transaction_material.additional_properties = d
        return transaction_material

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
