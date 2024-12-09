from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extrinsic_args import ExtrinsicArgs
    from ..models.extrinsic_method import ExtrinsicMethod
    from ..models.generic_extrinsic_era import GenericExtrinsicEra
    from ..models.runtime_dispatch_info import RuntimeDispatchInfo
    from ..models.sanitized_event import SanitizedEvent
    from ..models.signature import Signature


T = TypeVar("T", bound="Extrinsic")


@_attrs_define
class Extrinsic:
    """
    Attributes:
        method (Union[Unset, ExtrinsicMethod]): Extrinsic method
        signature (Union[Unset, Signature]): Object with `signature` and `signer`, or `null` if unsigned.
        nonce (Union[Unset, str]): Account nonce, if applicable.
        args (Union[Unset, ExtrinsicArgs]): Object of arguments keyed by parameter name. Note: if you are expecting an
            [`OpaqueCall`](https://substrate.dev/rustdocs/v2.0.0/pallet_multisig/type.OpaqueCall.html) and it is not decoded
            in the response (i.e. it is just a hex string), then Sidecar was not able to decode it and likely that it is not
            a valid call for the runtime.
        tip (Union[Unset, str]): Any tip added to the transaction.
        hash_ (Union[Unset, str]): The transaction's hash.
        info (Union[Unset, RuntimeDispatchInfo]): RuntimeDispatchInfo for the transaction. Includes the `partialFee`.
        era (Union[Unset, GenericExtrinsicEra]): The return value for era can either be `mortalEra`, or `immortalEra`
            and is represented as an enum in substrate. `immortalEra` meaning
            the transaction is valid forever. `mortalEra` consists of a tuple containing a period and phase.
            ex: `"{"mortalEra": ["64", "11"]}"`. The Period is the period of validity from the block hash found in the
            signing material.
            The Phase is the period that this transaction's lifetime begins (and, importantly,
            implies which block hash is included in the signature material).
             Example: {"mortalEra":["64", "11"]}.
        events (Union[Unset, list['SanitizedEvent']]): An array of `SanitizedEvent`s that occurred during extrinsic
            execution.
        success (Union[Unset, bool]): Whether or not the extrinsic succeeded.
        pays_fee (Union[Unset, bool]): Whether the extrinsic requires a fee. Careful! This field relates to whether or
            not the extrinsic requires a fee if called as a transaction. Block authors could insert the extrinsic as an
            inherent in the block and not pay a fee. Always check that `paysFee` is `true` and that the extrinsic is signed
            when reconciling old blocks.
    """

    method: Union[Unset, "ExtrinsicMethod"] = UNSET
    signature: Union[Unset, "Signature"] = UNSET
    nonce: Union[Unset, str] = UNSET
    args: Union[Unset, "ExtrinsicArgs"] = UNSET
    tip: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    info: Union[Unset, "RuntimeDispatchInfo"] = UNSET
    era: Union[Unset, "GenericExtrinsicEra"] = UNSET
    events: Union[Unset, list["SanitizedEvent"]] = UNSET
    success: Union[Unset, bool] = UNSET
    pays_fee: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.to_dict()

        signature: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        nonce = self.nonce

        args: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        tip = self.tip

        hash_ = self.hash_

        info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        era: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.era, Unset):
            era = self.era.to_dict()

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        success = self.success

        pays_fee = self.pays_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if signature is not UNSET:
            field_dict["signature"] = signature
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if args is not UNSET:
            field_dict["args"] = args
        if tip is not UNSET:
            field_dict["tip"] = tip
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if info is not UNSET:
            field_dict["info"] = info
        if era is not UNSET:
            field_dict["era"] = era
        if events is not UNSET:
            field_dict["events"] = events
        if success is not UNSET:
            field_dict["success"] = success
        if pays_fee is not UNSET:
            field_dict["paysFee"] = pays_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.extrinsic_args import ExtrinsicArgs
        from ..models.extrinsic_method import ExtrinsicMethod
        from ..models.generic_extrinsic_era import GenericExtrinsicEra
        from ..models.runtime_dispatch_info import RuntimeDispatchInfo
        from ..models.sanitized_event import SanitizedEvent
        from ..models.signature import Signature

        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, ExtrinsicMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ExtrinsicMethod.from_dict(_method)

        _signature = d.pop("signature", UNSET)
        signature: Union[Unset, Signature]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = Signature.from_dict(_signature)

        nonce = d.pop("nonce", UNSET)

        _args = d.pop("args", UNSET)
        args: Union[Unset, ExtrinsicArgs]
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = ExtrinsicArgs.from_dict(_args)

        tip = d.pop("tip", UNSET)

        hash_ = d.pop("hash", UNSET)

        _info = d.pop("info", UNSET)
        info: Union[Unset, RuntimeDispatchInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = RuntimeDispatchInfo.from_dict(_info)

        _era = d.pop("era", UNSET)
        era: Union[Unset, GenericExtrinsicEra]
        if isinstance(_era, Unset):
            era = UNSET
        else:
            era = GenericExtrinsicEra.from_dict(_era)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = SanitizedEvent.from_dict(events_item_data)

            events.append(events_item)

        success = d.pop("success", UNSET)

        pays_fee = d.pop("paysFee", UNSET)

        extrinsic = cls(
            method=method,
            signature=signature,
            nonce=nonce,
            args=args,
            tip=tip,
            hash_=hash_,
            info=info,
            era=era,
            events=events,
            success=success,
            pays_fee=pays_fee,
        )

        extrinsic.additional_properties = d
        return extrinsic

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
