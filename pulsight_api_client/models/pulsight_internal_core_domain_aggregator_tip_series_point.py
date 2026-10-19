from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipSeriesPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipSeriesPoint:
    """
    Attributes:
        bucket_ts (int | Unset): BucketTS is the bucket start, unix seconds.
        p50_tip_lamports (float | Unset): P50TipLamports, P90TipLamports and P99TipLamports are the bucket's
            median, 90th and 99th percentile tip.
        p90_tip_lamports (float | Unset):
        p99_tip_lamports (float | Unset):
        priority_fee_sum (int | Unset):
        priority_fee_sum_usd (int | Unset):
        tip_sum_lamports (int | Unset):
        tip_sum_usd (int | Unset):
        tipped_count (int | Unset):
    """

    bucket_ts: int | Unset = UNSET
    p50_tip_lamports: float | Unset = UNSET
    p90_tip_lamports: float | Unset = UNSET
    p99_tip_lamports: float | Unset = UNSET
    priority_fee_sum: int | Unset = UNSET
    priority_fee_sum_usd: int | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    tip_sum_usd: int | Unset = UNSET
    tipped_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        p50_tip_lamports = self.p50_tip_lamports

        p90_tip_lamports = self.p90_tip_lamports

        p99_tip_lamports = self.p99_tip_lamports

        priority_fee_sum = self.priority_fee_sum

        priority_fee_sum_usd = self.priority_fee_sum_usd

        tip_sum_lamports = self.tip_sum_lamports

        tip_sum_usd = self.tip_sum_usd

        tipped_count = self.tipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if p50_tip_lamports is not UNSET:
            field_dict["p50_tip_lamports"] = p50_tip_lamports
        if p90_tip_lamports is not UNSET:
            field_dict["p90_tip_lamports"] = p90_tip_lamports
        if p99_tip_lamports is not UNSET:
            field_dict["p99_tip_lamports"] = p99_tip_lamports
        if priority_fee_sum is not UNSET:
            field_dict["priority_fee_sum"] = priority_fee_sum
        if priority_fee_sum_usd is not UNSET:
            field_dict["priority_fee_sum_usd"] = priority_fee_sum_usd
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports
        if tip_sum_usd is not UNSET:
            field_dict["tip_sum_usd"] = tip_sum_usd
        if tipped_count is not UNSET:
            field_dict["tipped_count"] = tipped_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        p50_tip_lamports = d.pop("p50_tip_lamports", UNSET)

        p90_tip_lamports = d.pop("p90_tip_lamports", UNSET)

        p99_tip_lamports = d.pop("p99_tip_lamports", UNSET)

        priority_fee_sum = d.pop("priority_fee_sum", UNSET)

        priority_fee_sum_usd = d.pop("priority_fee_sum_usd", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        tip_sum_usd = d.pop("tip_sum_usd", UNSET)

        tipped_count = d.pop("tipped_count", UNSET)

        pulsight_internal_core_domain_aggregator_tip_series_point = cls(
            bucket_ts=bucket_ts,
            p50_tip_lamports=p50_tip_lamports,
            p90_tip_lamports=p90_tip_lamports,
            p99_tip_lamports=p99_tip_lamports,
            priority_fee_sum=priority_fee_sum,
            priority_fee_sum_usd=priority_fee_sum_usd,
            tip_sum_lamports=tip_sum_lamports,
            tip_sum_usd=tip_sum_usd,
            tipped_count=tipped_count,
        )

        pulsight_internal_core_domain_aggregator_tip_series_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_series_point

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
