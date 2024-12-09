from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decoded_xcm_msgs_decoded_xcm_msgs import DecodedXcmMsgsDecodedXcmMsgs


T = TypeVar("T", bound="DecodedXcmMsgs")


@_attrs_define
class DecodedXcmMsgs:
    """Object with three arrays, one for every XCM direction. The arrays are populated or left empty based on the direction
    of the current XCM message that is being decoded. The XCM messages can be Upward and/or Horizontal (`in transit`)
    messages when connected to a Relay chain. When connected to a Parachain, the messages can be Downward and/or
    Horizontal. One or more messages can be present in a single block. In case of multiple messages from the same
    paraIds (originParaId and/or destinationParaId), the messages will be shown under the field `data`.

        Attributes:
            decoded_xcm_msgs (Union[Unset, DecodedXcmMsgsDecodedXcmMsgs]):
    """

    decoded_xcm_msgs: Union[Unset, "DecodedXcmMsgsDecodedXcmMsgs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decoded_xcm_msgs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.decoded_xcm_msgs, Unset):
            decoded_xcm_msgs = self.decoded_xcm_msgs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decoded_xcm_msgs is not UNSET:
            field_dict["decodedXcmMsgs"] = decoded_xcm_msgs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.decoded_xcm_msgs_decoded_xcm_msgs import DecodedXcmMsgsDecodedXcmMsgs

        d = src_dict.copy()
        _decoded_xcm_msgs = d.pop("decodedXcmMsgs", UNSET)
        decoded_xcm_msgs: Union[Unset, DecodedXcmMsgsDecodedXcmMsgs]
        if isinstance(_decoded_xcm_msgs, Unset):
            decoded_xcm_msgs = UNSET
        else:
            decoded_xcm_msgs = DecodedXcmMsgsDecodedXcmMsgs.from_dict(_decoded_xcm_msgs)

        decoded_xcm_msgs = cls(
            decoded_xcm_msgs=decoded_xcm_msgs,
        )

        decoded_xcm_msgs.additional_properties = d
        return decoded_xcm_msgs

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
