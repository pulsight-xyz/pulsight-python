from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipHeatmapPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipHeatmapPoint:
    """
    Attributes:
        bucket_ts (int | Unset): unix epoch seconds at bucket start
        median_tip_lamports (float | Unset):
        p90_tip_lamports (float | Unset):
        tipped_count (int | Unset):
    """

    bucket_ts: int | Unset = UNSET
    median_tip_lamports: float | Unset = UNSET
    p90_tip_lamports: float | Unset = UNSET
    tipped_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        median_tip_lamports = self.median_tip_lamports

        p90_tip_lamports = self.p90_tip_lamports

        tipped_count = self.tipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if median_tip_lamports is not UNSET:
            field_dict["median_tip_lamports"] = median_tip_lamports
        if p90_tip_lamports is not UNSET:
            field_dict["p90_tip_lamports"] = p90_tip_lamports
        if tipped_count is not UNSET:
            field_dict["tipped_count"] = tipped_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        median_tip_lamports = d.pop("median_tip_lamports", UNSET)

        p90_tip_lamports = d.pop("p90_tip_lamports", UNSET)

        tipped_count = d.pop("tipped_count", UNSET)

        pulsight_internal_core_domain_aggregator_tip_heatmap_point = cls(
            bucket_ts=bucket_ts,
            median_tip_lamports=median_tip_lamports,
            p90_tip_lamports=p90_tip_lamports,
            tipped_count=tipped_count,
        )

        pulsight_internal_core_domain_aggregator_tip_heatmap_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_heatmap_point

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
