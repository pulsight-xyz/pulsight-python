from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderTagsTrait")


@_attrs_define
class PulsightInternalCoreDomainTraderTagsTrait:
    """
    Attributes:
        closeness (float | Unset):
        value (list[str] | Unset):
    """

    closeness: float | Unset = UNSET
    value: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closeness = self.closeness

        value: list[str] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closeness is not UNSET:
            field_dict["closeness"] = closeness
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        closeness = d.pop("closeness", UNSET)

        value = cast(list[str], d.pop("value", UNSET))

        pulsight_internal_core_domain_trader_tags_trait = cls(
            closeness=closeness,
            value=value,
        )

        pulsight_internal_core_domain_trader_tags_trait.additional_properties = d
        return pulsight_internal_core_domain_trader_tags_trait

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
