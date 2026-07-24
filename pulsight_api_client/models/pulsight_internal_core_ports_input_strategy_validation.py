from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCorePortsInputStrategyValidation")


@_attrs_define
class PulsightInternalCorePortsInputStrategyValidation:
    """
    Attributes:
        errors (list[str] | Unset):
        valid (bool | Unset):
    """

    errors: list[str] | Unset = UNSET
    valid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        valid = self.valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors", UNSET))

        valid = d.pop("valid", UNSET)

        pulsight_internal_core_ports_input_strategy_validation = cls(
            errors=errors,
            valid=valid,
        )

        pulsight_internal_core_ports_input_strategy_validation.additional_properties = d
        return pulsight_internal_core_ports_input_strategy_validation

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
