from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorLpStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorLpStat:
    """
    Attributes:
        burned (bool | Unset):
    """

    burned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        burned = self.burned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if burned is not UNSET:
            field_dict["burned"] = burned

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        burned = d.pop("burned", UNSET)

        pulsight_internal_core_domain_aggregator_lp_stat = cls(
            burned=burned,
        )

        pulsight_internal_core_domain_aggregator_lp_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_lp_stat

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
