from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DecodedXcmMsgsHorizontalMessagesInParachainItemData")


@_attrs_define
class DecodedXcmMsgsHorizontalMessagesInParachainItemData:
    """The decoded instructions included in the XCM message and their respective fields."""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        decoded_xcm_msgs_horizontal_messages_in_parachain_item_data = cls()

        decoded_xcm_msgs_horizontal_messages_in_parachain_item_data.additional_properties = d
        return decoded_xcm_msgs_horizontal_messages_in_parachain_item_data

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
