from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_finalize import BlockFinalize
    from ..models.block_initialize import BlockInitialize
    from ..models.decoded_xcm_msgs_decoded_xcm_msgs import DecodedXcmMsgsDecodedXcmMsgs
    from ..models.digest_item import DigestItem
    from ..models.extrinsic import Extrinsic


T = TypeVar("T", bound="BlockWithDecodedXcmMsgs")


@_attrs_define
class BlockWithDecodedXcmMsgs:
    """Block information that includes the decoded XCM messages if any are found in the queried block. If not, the
    decodedXcmMsgs object will be returned with three empty arrays corresponding to each direction, horizontalMessages,
    downwardMessages, upwardMessages.

        Attributes:
            number (Union[Unset, str]): The block's height.
            hash_ (Union[Unset, str]): The block's hash.
            parent_hash (Union[Unset, str]): The hash of the parent block.
            state_root (Union[Unset, str]): The state root after executing this block.
            extrinsic_root (Union[Unset, str]): The Merkle root of the extrinsics.
            author_id (Union[Unset, str]): The account ID of the block author (may be undefined for some chains).
            logs (Union[Unset, list['DigestItem']]): Array of `DigestItem`s associated with the block.
            on_initialize (Union[Unset, BlockInitialize]): Object with an array of `SanitizedEvent`s that occurred during
                block initialization with the `method` and `data` for each.
            extrinsics (Union[Unset, list['Extrinsic']]): Array of extrinsics (inherents and transactions) within the block.
            on_finalize (Union[Unset, BlockFinalize]): Object with an array of `SanitizedEvent`s that occurred during block
                construction finalization with the `method` and `data` for each.
            finalized (Union[Unset, bool]): A boolean identifying whether the block is finalized or not. Note: on chains
                that do not have deterministic finality this field is omitted.
            decoded_xcm_msgs (Union[Unset, DecodedXcmMsgsDecodedXcmMsgs]):
    """

    number: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    parent_hash: Union[Unset, str] = UNSET
    state_root: Union[Unset, str] = UNSET
    extrinsic_root: Union[Unset, str] = UNSET
    author_id: Union[Unset, str] = UNSET
    logs: Union[Unset, list["DigestItem"]] = UNSET
    on_initialize: Union[Unset, "BlockInitialize"] = UNSET
    extrinsics: Union[Unset, list["Extrinsic"]] = UNSET
    on_finalize: Union[Unset, "BlockFinalize"] = UNSET
    finalized: Union[Unset, bool] = UNSET
    decoded_xcm_msgs: Union[Unset, "DecodedXcmMsgsDecodedXcmMsgs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        hash_ = self.hash_

        parent_hash = self.parent_hash

        state_root = self.state_root

        extrinsic_root = self.extrinsic_root

        author_id = self.author_id

        logs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        on_initialize: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.on_initialize, Unset):
            on_initialize = self.on_initialize.to_dict()

        extrinsics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.extrinsics, Unset):
            extrinsics = []
            for extrinsics_item_data in self.extrinsics:
                extrinsics_item = extrinsics_item_data.to_dict()
                extrinsics.append(extrinsics_item)

        on_finalize: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.on_finalize, Unset):
            on_finalize = self.on_finalize.to_dict()

        finalized = self.finalized

        decoded_xcm_msgs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.decoded_xcm_msgs, Unset):
            decoded_xcm_msgs = self.decoded_xcm_msgs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if parent_hash is not UNSET:
            field_dict["parentHash"] = parent_hash
        if state_root is not UNSET:
            field_dict["stateRoot"] = state_root
        if extrinsic_root is not UNSET:
            field_dict["extrinsicRoot"] = extrinsic_root
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if logs is not UNSET:
            field_dict["logs"] = logs
        if on_initialize is not UNSET:
            field_dict["onInitialize"] = on_initialize
        if extrinsics is not UNSET:
            field_dict["extrinsics"] = extrinsics
        if on_finalize is not UNSET:
            field_dict["onFinalize"] = on_finalize
        if finalized is not UNSET:
            field_dict["finalized"] = finalized
        if decoded_xcm_msgs is not UNSET:
            field_dict["decodedXcmMsgs"] = decoded_xcm_msgs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_finalize import BlockFinalize
        from ..models.block_initialize import BlockInitialize
        from ..models.decoded_xcm_msgs_decoded_xcm_msgs import DecodedXcmMsgsDecodedXcmMsgs
        from ..models.digest_item import DigestItem
        from ..models.extrinsic import Extrinsic

        d = src_dict.copy()
        number = d.pop("number", UNSET)

        hash_ = d.pop("hash", UNSET)

        parent_hash = d.pop("parentHash", UNSET)

        state_root = d.pop("stateRoot", UNSET)

        extrinsic_root = d.pop("extrinsicRoot", UNSET)

        author_id = d.pop("authorId", UNSET)

        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = DigestItem.from_dict(logs_item_data)

            logs.append(logs_item)

        _on_initialize = d.pop("onInitialize", UNSET)
        on_initialize: Union[Unset, BlockInitialize]
        if isinstance(_on_initialize, Unset):
            on_initialize = UNSET
        else:
            on_initialize = BlockInitialize.from_dict(_on_initialize)

        extrinsics = []
        _extrinsics = d.pop("extrinsics", UNSET)
        for extrinsics_item_data in _extrinsics or []:
            extrinsics_item = Extrinsic.from_dict(extrinsics_item_data)

            extrinsics.append(extrinsics_item)

        _on_finalize = d.pop("onFinalize", UNSET)
        on_finalize: Union[Unset, BlockFinalize]
        if isinstance(_on_finalize, Unset):
            on_finalize = UNSET
        else:
            on_finalize = BlockFinalize.from_dict(_on_finalize)

        finalized = d.pop("finalized", UNSET)

        _decoded_xcm_msgs = d.pop("decodedXcmMsgs", UNSET)
        decoded_xcm_msgs: Union[Unset, DecodedXcmMsgsDecodedXcmMsgs]
        if isinstance(_decoded_xcm_msgs, Unset):
            decoded_xcm_msgs = UNSET
        else:
            decoded_xcm_msgs = DecodedXcmMsgsDecodedXcmMsgs.from_dict(_decoded_xcm_msgs)

        block_with_decoded_xcm_msgs = cls(
            number=number,
            hash_=hash_,
            parent_hash=parent_hash,
            state_root=state_root,
            extrinsic_root=extrinsic_root,
            author_id=author_id,
            logs=logs,
            on_initialize=on_initialize,
            extrinsics=extrinsics,
            on_finalize=on_finalize,
            finalized=finalized,
            decoded_xcm_msgs=decoded_xcm_msgs,
        )

        block_with_decoded_xcm_msgs.additional_properties = d
        return block_with_decoded_xcm_msgs

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
