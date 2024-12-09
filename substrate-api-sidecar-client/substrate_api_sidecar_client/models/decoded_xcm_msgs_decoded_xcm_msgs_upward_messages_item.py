from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item_data import (
        DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData,
    )


T = TypeVar("T", bound="DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem")


@_attrs_define
class DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem:
    """
    Attributes:
        origin_para_id (Union[Unset, str]): The Parachain id that the specific XCM message was sent from.
        data (Union[Unset, DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData]): The decoded instructions included in
            the XCM message and their respective fields.
    """

    origin_para_id: Union[Unset, str] = UNSET
    data: Union[Unset, "DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin_para_id = self.origin_para_id

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin_para_id is not UNSET:
            field_dict["originParaId"] = origin_para_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item_data import (
            DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData,
        )

        d = src_dict.copy()
        origin_para_id = d.pop("originParaId", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItemData.from_dict(_data)

        decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item = cls(
            origin_para_id=origin_para_id,
            data=data,
        )

        decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item.additional_properties = d
        return decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item

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
