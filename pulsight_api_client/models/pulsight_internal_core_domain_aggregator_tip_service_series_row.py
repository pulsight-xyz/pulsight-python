from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipServiceSeriesRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipServiceSeriesRow:
    """
    Attributes:
        tip_service (str | Unset):
        tipped_count (list[int] | Unset): TippedCount is aligned with `buckets`; a bucket without one is 0.
    """

    tip_service: str | Unset = UNSET
    tipped_count: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tip_service = self.tip_service

        tipped_count: list[int] | Unset = UNSET
        if not isinstance(self.tipped_count, Unset):
            tipped_count = self.tipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service
        if tipped_count is not UNSET:
            field_dict["tipped_count"] = tipped_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tip_service = d.pop("tip_service", UNSET)

        tipped_count = cast(list[int], d.pop("tipped_count", UNSET))

        pulsight_internal_core_domain_aggregator_tip_service_series_row = cls(
            tip_service=tip_service,
            tipped_count=tipped_count,
        )

        pulsight_internal_core_domain_aggregator_tip_service_series_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_service_series_row

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
