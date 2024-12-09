from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChainType")


@_attrs_define
class ChainType:
    """Type of the chain. It will return one of the following enum variants as a key. Live, Development, Local, or Custom.
    Each variant will have a value as null except when the ChainType is Custom, it will return a string.

        Example:
            {"live": null}

        Attributes:
            live (Union[None, Unset, str]):
            development (Union[None, Unset, str]):
            local (Union[None, Unset, str]):
            custom (Union[Unset, str]):
    """

    live: Union[None, Unset, str] = UNSET
    development: Union[None, Unset, str] = UNSET
    local: Union[None, Unset, str] = UNSET
    custom: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        live: Union[None, Unset, str]
        if isinstance(self.live, Unset):
            live = UNSET
        else:
            live = self.live

        development: Union[None, Unset, str]
        if isinstance(self.development, Unset):
            development = UNSET
        else:
            development = self.development

        local: Union[None, Unset, str]
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        custom = self.custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if live is not UNSET:
            field_dict["live"] = live
        if development is not UNSET:
            field_dict["development"] = development
        if local is not UNSET:
            field_dict["local"] = local
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_live(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        live = _parse_live(d.pop("live", UNSET))

        def _parse_development(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        development = _parse_development(d.pop("development", UNSET))

        def _parse_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        local = _parse_local(d.pop("local", UNSET))

        custom = d.pop("custom", UNSET)

        chain_type = cls(
            live=live,
            development=development,
            local=local,
            custom=custom,
        )

        chain_type.additional_properties = d
        return chain_type

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
