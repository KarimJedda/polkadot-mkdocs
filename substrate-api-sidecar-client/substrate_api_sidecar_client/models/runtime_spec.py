from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.chain_type import ChainType
    from ..models.runtime_spec_properties import RuntimeSpecProperties


T = TypeVar("T", bound="RuntimeSpec")


@_attrs_define
class RuntimeSpec:
    """Version information related to the runtime.

    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        authoring_version (Union[Unset, str]): The version of the authorship interface. An authoring node will not
            attempt to author blocks unless this is equal to its native runtime.
        chain_type (Union[Unset, ChainType]): Type of the chain. It will return one of the following enum variants as a
            key. Live, Development, Local, or Custom. Each variant will have a value as null except when the ChainType is
            Custom, it will return a string. Example: {"live": null}.
        impl_version (Union[Unset, str]): Version of the implementation specification. Non-consensus-breaking
            optimizations are about the only changes that could be made which would result in only the `impl_version`
            changing. The `impl_version` is set to 0 when `spec_version` is incremented.
        spec_name (Union[Unset, str]): Identifies the different Substrate runtimes.
        spec_version (Union[Unset, str]): Version of the runtime specification.
        transaction_version (Union[Unset, str]): All existing dispatches are fully compatible when this number doesn't
            change. This number must change when an existing dispatchable (module ID, dispatch ID) is changed, either
            through an alteration in its user-level semantics, a parameter added/removed/changed, a dispatchable being
            removed, a module being removed, or a dispatchable/module changing its index.
        properties (Union[Unset, RuntimeSpecProperties]): Arbitrary properties defined in the chain spec.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    authoring_version: Union[Unset, str] = UNSET
    chain_type: Union[Unset, "ChainType"] = UNSET
    impl_version: Union[Unset, str] = UNSET
    spec_name: Union[Unset, str] = UNSET
    spec_version: Union[Unset, str] = UNSET
    transaction_version: Union[Unset, str] = UNSET
    properties: Union[Unset, "RuntimeSpecProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        authoring_version = self.authoring_version

        chain_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chain_type, Unset):
            chain_type = self.chain_type.to_dict()

        impl_version = self.impl_version

        spec_name = self.spec_name

        spec_version = self.spec_version

        transaction_version = self.transaction_version

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if authoring_version is not UNSET:
            field_dict["authoringVersion"] = authoring_version
        if chain_type is not UNSET:
            field_dict["chainType"] = chain_type
        if impl_version is not UNSET:
            field_dict["implVersion"] = impl_version
        if spec_name is not UNSET:
            field_dict["specName"] = spec_name
        if spec_version is not UNSET:
            field_dict["specVersion"] = spec_version
        if transaction_version is not UNSET:
            field_dict["transactionVersion"] = transaction_version
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.chain_type import ChainType
        from ..models.runtime_spec_properties import RuntimeSpecProperties

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        authoring_version = d.pop("authoringVersion", UNSET)

        _chain_type = d.pop("chainType", UNSET)
        chain_type: Union[Unset, ChainType]
        if isinstance(_chain_type, Unset):
            chain_type = UNSET
        else:
            chain_type = ChainType.from_dict(_chain_type)

        impl_version = d.pop("implVersion", UNSET)

        spec_name = d.pop("specName", UNSET)

        spec_version = d.pop("specVersion", UNSET)

        transaction_version = d.pop("transactionVersion", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, RuntimeSpecProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RuntimeSpecProperties.from_dict(_properties)

        runtime_spec = cls(
            at=at,
            authoring_version=authoring_version,
            chain_type=chain_type,
            impl_version=impl_version,
            spec_name=spec_name,
            spec_version=spec_version,
            transaction_version=transaction_version,
            properties=properties,
        )

        runtime_spec.additional_properties = d
        return runtime_spec

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
