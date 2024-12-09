from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_identifiers import BlockIdentifiers
    from ..models.staking_validators_validators_item import StakingValidatorsValidatorsItem
    from ..models.staking_validators_validators_to_be_chilled_item import StakingValidatorsValidatorsToBeChilledItem


T = TypeVar("T", bound="StakingValidators")


@_attrs_define
class StakingValidators:
    """
    Attributes:
        at (Union[Unset, BlockIdentifiers]): Block number and hash at which the call was made.
        validators (Union[Unset, list['StakingValidatorsValidatorsItem']]):
        validators_to_be_chilled (Union[Unset, list['StakingValidatorsValidatorsToBeChilledItem']]): Validators that
            will not be participating in the next era.
    """

    at: Union[Unset, "BlockIdentifiers"] = UNSET
    validators: Union[Unset, list["StakingValidatorsValidatorsItem"]] = UNSET
    validators_to_be_chilled: Union[Unset, list["StakingValidatorsValidatorsToBeChilledItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        validators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validators, Unset):
            validators = []
            for validators_item_data in self.validators:
                validators_item = validators_item_data.to_dict()
                validators.append(validators_item)

        validators_to_be_chilled: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validators_to_be_chilled, Unset):
            validators_to_be_chilled = []
            for validators_to_be_chilled_item_data in self.validators_to_be_chilled:
                validators_to_be_chilled_item = validators_to_be_chilled_item_data.to_dict()
                validators_to_be_chilled.append(validators_to_be_chilled_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if validators is not UNSET:
            field_dict["validators"] = validators
        if validators_to_be_chilled is not UNSET:
            field_dict["validatorsToBeChilled"] = validators_to_be_chilled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.block_identifiers import BlockIdentifiers
        from ..models.staking_validators_validators_item import StakingValidatorsValidatorsItem
        from ..models.staking_validators_validators_to_be_chilled_item import StakingValidatorsValidatorsToBeChilledItem

        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, BlockIdentifiers]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = BlockIdentifiers.from_dict(_at)

        validators = []
        _validators = d.pop("validators", UNSET)
        for validators_item_data in _validators or []:
            validators_item = StakingValidatorsValidatorsItem.from_dict(validators_item_data)

            validators.append(validators_item)

        validators_to_be_chilled = []
        _validators_to_be_chilled = d.pop("validatorsToBeChilled", UNSET)
        for validators_to_be_chilled_item_data in _validators_to_be_chilled or []:
            validators_to_be_chilled_item = StakingValidatorsValidatorsToBeChilledItem.from_dict(
                validators_to_be_chilled_item_data
            )

            validators_to_be_chilled.append(validators_to_be_chilled_item)

        staking_validators = cls(
            at=at,
            validators=validators,
            validators_to_be_chilled=validators_to_be_chilled,
        )

        staking_validators.additional_properties = d
        return staking_validators

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
