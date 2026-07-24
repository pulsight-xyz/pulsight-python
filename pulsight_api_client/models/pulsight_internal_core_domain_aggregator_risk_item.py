from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_risk_level import (
    PulsightInternalCoreDomainAggregatorRiskLevel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorRiskItem")


@_attrs_define
class PulsightInternalCoreDomainAggregatorRiskItem:
    """
    Attributes:
        description (str | Unset):
        level (PulsightInternalCoreDomainAggregatorRiskLevel | Unset):
        name (str | Unset):
        score (int | Unset):
        value (str | Unset):
    """

    description: str | Unset = UNSET
    level: PulsightInternalCoreDomainAggregatorRiskLevel | Unset = UNSET
    name: str | Unset = UNSET
    score: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        name = self.name

        score = self.score

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if score is not UNSET:
            field_dict["score"] = score
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _level = d.pop("level", UNSET)
        level: PulsightInternalCoreDomainAggregatorRiskLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = PulsightInternalCoreDomainAggregatorRiskLevel(_level)

        name = d.pop("name", UNSET)

        score = d.pop("score", UNSET)

        value = d.pop("value", UNSET)

        pulsight_internal_core_domain_aggregator_risk_item = cls(
            description=description,
            level=level,
            name=name,
            score=score,
            value=value,
        )

        pulsight_internal_core_domain_aggregator_risk_item.additional_properties = d
        return pulsight_internal_core_domain_aggregator_risk_item

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
