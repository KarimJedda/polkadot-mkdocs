from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decoded_xcm_msgs_decoded_xcm_msgs_downward_messages_item import (
        DecodedXcmMsgsDecodedXcmMsgsDownwardMessagesItem,
    )
    from ..models.decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item import (
        DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem,
    )
    from ..models.decoded_xcm_msgs_horizontal_messages_in_parachain_item import (
        DecodedXcmMsgsHorizontalMessagesInParachainItem,
    )
    from ..models.decoded_xcm_msgs_horizontal_messages_in_relay_item import DecodedXcmMsgsHorizontalMessagesInRelayItem


T = TypeVar("T", bound="DecodedXcmMsgsDecodedXcmMsgs")


@_attrs_define
class DecodedXcmMsgsDecodedXcmMsgs:
    """
    Attributes:
        horizontal_messages (Union[Unset, list['DecodedXcmMsgsHorizontalMessagesInParachainItem'],
            list['DecodedXcmMsgsHorizontalMessagesInRelayItem']]):
        downward_messages (Union[Unset, list['DecodedXcmMsgsDecodedXcmMsgsDownwardMessagesItem']]):
        upward_messages (Union[Unset, list['DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem']]):
    """

    horizontal_messages: Union[
        Unset,
        list["DecodedXcmMsgsHorizontalMessagesInParachainItem"],
        list["DecodedXcmMsgsHorizontalMessagesInRelayItem"],
    ] = UNSET
    downward_messages: Union[Unset, list["DecodedXcmMsgsDecodedXcmMsgsDownwardMessagesItem"]] = UNSET
    upward_messages: Union[Unset, list["DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        horizontal_messages: Union[Unset, list[dict[str, Any]]]
        if isinstance(self.horizontal_messages, Unset):
            horizontal_messages = UNSET
        elif isinstance(self.horizontal_messages, list):
            horizontal_messages = []
            for componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item_data in self.horizontal_messages:
                componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item = (
                    componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item_data.to_dict()
                )
                horizontal_messages.append(componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item)

        else:
            horizontal_messages = []
            for (
                componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item_data
            ) in self.horizontal_messages:
                componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item = (
                    componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item_data.to_dict()
                )
                horizontal_messages.append(componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item)

        downward_messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.downward_messages, Unset):
            downward_messages = []
            for downward_messages_item_data in self.downward_messages:
                downward_messages_item = downward_messages_item_data.to_dict()
                downward_messages.append(downward_messages_item)

        upward_messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.upward_messages, Unset):
            upward_messages = []
            for upward_messages_item_data in self.upward_messages:
                upward_messages_item = upward_messages_item_data.to_dict()
                upward_messages.append(upward_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if horizontal_messages is not UNSET:
            field_dict["horizontalMessages"] = horizontal_messages
        if downward_messages is not UNSET:
            field_dict["downwardMessages"] = downward_messages
        if upward_messages is not UNSET:
            field_dict["upwardMessages"] = upward_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.decoded_xcm_msgs_decoded_xcm_msgs_downward_messages_item import (
            DecodedXcmMsgsDecodedXcmMsgsDownwardMessagesItem,
        )
        from ..models.decoded_xcm_msgs_decoded_xcm_msgs_upward_messages_item import (
            DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem,
        )
        from ..models.decoded_xcm_msgs_horizontal_messages_in_parachain_item import (
            DecodedXcmMsgsHorizontalMessagesInParachainItem,
        )
        from ..models.decoded_xcm_msgs_horizontal_messages_in_relay_item import (
            DecodedXcmMsgsHorizontalMessagesInRelayItem,
        )

        d = src_dict.copy()

        def _parse_horizontal_messages(
            data: object,
        ) -> Union[
            Unset,
            list["DecodedXcmMsgsHorizontalMessagesInParachainItem"],
            list["DecodedXcmMsgsHorizontalMessagesInRelayItem"],
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                horizontal_messages_type_0 = []
                _horizontal_messages_type_0 = data
                for (
                    componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item_data
                ) in _horizontal_messages_type_0:
                    componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item = (
                        DecodedXcmMsgsHorizontalMessagesInRelayItem.from_dict(
                            componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item_data
                        )
                    )

                    horizontal_messages_type_0.append(
                        componentsschemas_decoded_xcm_msgs_horizontal_messages_in_relay_item
                    )

                return horizontal_messages_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            horizontal_messages_type_1 = []
            _horizontal_messages_type_1 = data
            for (
                componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item_data
            ) in _horizontal_messages_type_1:
                componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item = (
                    DecodedXcmMsgsHorizontalMessagesInParachainItem.from_dict(
                        componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item_data
                    )
                )

                horizontal_messages_type_1.append(
                    componentsschemas_decoded_xcm_msgs_horizontal_messages_in_parachain_item
                )

            return horizontal_messages_type_1

        horizontal_messages = _parse_horizontal_messages(d.pop("horizontalMessages", UNSET))

        downward_messages = []
        _downward_messages = d.pop("downwardMessages", UNSET)
        for downward_messages_item_data in _downward_messages or []:
            downward_messages_item = DecodedXcmMsgsDecodedXcmMsgsDownwardMessagesItem.from_dict(
                downward_messages_item_data
            )

            downward_messages.append(downward_messages_item)

        upward_messages = []
        _upward_messages = d.pop("upwardMessages", UNSET)
        for upward_messages_item_data in _upward_messages or []:
            upward_messages_item = DecodedXcmMsgsDecodedXcmMsgsUpwardMessagesItem.from_dict(upward_messages_item_data)

            upward_messages.append(upward_messages_item)

        decoded_xcm_msgs_decoded_xcm_msgs = cls(
            horizontal_messages=horizontal_messages,
            downward_messages=downward_messages,
            upward_messages=upward_messages,
        )

        decoded_xcm_msgs_decoded_xcm_msgs.additional_properties = d
        return decoded_xcm_msgs_decoded_xcm_msgs

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
