from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_tip_period_stats import (
        PulsightInternalCoreDomainAggregatorTipPeriodStats,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorGlobalTipStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorGlobalTipStats:
    """
    Attributes:
        p50_tip_lamports (float | Unset): P50TipLamports, P90TipLamports and P99TipLamports are the median, 90th
            and 99th percentile tip (t-digest estimates). Lamports only: there is no
            USD twin of a percentile.
        p90_tip_lamports (float | Unset):
        p99_tip_lamports (float | Unset):
        previous (PulsightInternalCoreDomainAggregatorTipPeriodStats | Unset):
        priority_fee_sum (int | Unset): PriorityFeeSum is the priority fees the tipped transactions paid
            alongside their tips, in lamports.
        priority_fee_sum_usd (int | Unset):
        swap_count (int | Unset): SwapCount is every landed transaction of the period, tipped or not,
            read off the hourly program plane with each hour weighted by its
            overlap with the period.
        tip_avg_lamports (float | Unset): TipAvgLamports is the mean tip per tipped transaction.
        tip_avg_usd (float | Unset):
        tip_count (int | Unset): TipCount is the number of tipped transactions.
        tip_sum_lamports (int | Unset): TipSumLamports is the tips those transactions paid.
        tip_sum_usd (int | Unset):
        tipped_fraction (float | Unset): TippedFraction is tip_count / swap_count (0..1).
        tipped_volume_fraction (float | Unset): TippedVolumeFraction is tipped_volume_lamports / total_volume_lamports
            (0..1).
        tipped_volume_lamports (int | Unset): TippedVolumeLamports is the value the tipped transactions traded.
        tipped_volume_usd (int | Unset):
        total_volume_lamports (int | Unset): TotalVolumeLamports is the value every landed transaction traded,
            weighted like SwapCount.
        total_volume_usd (int | Unset):
        window (str | Unset):
    """

    p50_tip_lamports: float | Unset = UNSET
    p90_tip_lamports: float | Unset = UNSET
    p99_tip_lamports: float | Unset = UNSET
    previous: PulsightInternalCoreDomainAggregatorTipPeriodStats | Unset = UNSET
    priority_fee_sum: int | Unset = UNSET
    priority_fee_sum_usd: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    tip_avg_lamports: float | Unset = UNSET
    tip_avg_usd: float | Unset = UNSET
    tip_count: int | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    tip_sum_usd: int | Unset = UNSET
    tipped_fraction: float | Unset = UNSET
    tipped_volume_fraction: float | Unset = UNSET
    tipped_volume_lamports: int | Unset = UNSET
    tipped_volume_usd: int | Unset = UNSET
    total_volume_lamports: int | Unset = UNSET
    total_volume_usd: int | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        p50_tip_lamports = self.p50_tip_lamports

        p90_tip_lamports = self.p90_tip_lamports

        p99_tip_lamports = self.p99_tip_lamports

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        priority_fee_sum = self.priority_fee_sum

        priority_fee_sum_usd = self.priority_fee_sum_usd

        swap_count = self.swap_count

        tip_avg_lamports = self.tip_avg_lamports

        tip_avg_usd = self.tip_avg_usd

        tip_count = self.tip_count

        tip_sum_lamports = self.tip_sum_lamports

        tip_sum_usd = self.tip_sum_usd

        tipped_fraction = self.tipped_fraction

        tipped_volume_fraction = self.tipped_volume_fraction

        tipped_volume_lamports = self.tipped_volume_lamports

        tipped_volume_usd = self.tipped_volume_usd

        total_volume_lamports = self.total_volume_lamports

        total_volume_usd = self.total_volume_usd

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if p50_tip_lamports is not UNSET:
            field_dict["p50_tip_lamports"] = p50_tip_lamports
        if p90_tip_lamports is not UNSET:
            field_dict["p90_tip_lamports"] = p90_tip_lamports
        if p99_tip_lamports is not UNSET:
            field_dict["p99_tip_lamports"] = p99_tip_lamports
        if previous is not UNSET:
            field_dict["previous"] = previous
        if priority_fee_sum is not UNSET:
            field_dict["priority_fee_sum"] = priority_fee_sum
        if priority_fee_sum_usd is not UNSET:
            field_dict["priority_fee_sum_usd"] = priority_fee_sum_usd
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if tip_avg_lamports is not UNSET:
            field_dict["tip_avg_lamports"] = tip_avg_lamports
        if tip_avg_usd is not UNSET:
            field_dict["tip_avg_usd"] = tip_avg_usd
        if tip_count is not UNSET:
            field_dict["tip_count"] = tip_count
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports
        if tip_sum_usd is not UNSET:
            field_dict["tip_sum_usd"] = tip_sum_usd
        if tipped_fraction is not UNSET:
            field_dict["tipped_fraction"] = tipped_fraction
        if tipped_volume_fraction is not UNSET:
            field_dict["tipped_volume_fraction"] = tipped_volume_fraction
        if tipped_volume_lamports is not UNSET:
            field_dict["tipped_volume_lamports"] = tipped_volume_lamports
        if tipped_volume_usd is not UNSET:
            field_dict["tipped_volume_usd"] = tipped_volume_usd
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports
        if total_volume_usd is not UNSET:
            field_dict["total_volume_usd"] = total_volume_usd
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_tip_period_stats import (
            PulsightInternalCoreDomainAggregatorTipPeriodStats,
        )

        d = dict(src_dict)
        p50_tip_lamports = d.pop("p50_tip_lamports", UNSET)

        p90_tip_lamports = d.pop("p90_tip_lamports", UNSET)

        p99_tip_lamports = d.pop("p99_tip_lamports", UNSET)

        _previous = d.pop("previous", UNSET)
        previous: PulsightInternalCoreDomainAggregatorTipPeriodStats | Unset
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = PulsightInternalCoreDomainAggregatorTipPeriodStats.from_dict(
                _previous
            )

        priority_fee_sum = d.pop("priority_fee_sum", UNSET)

        priority_fee_sum_usd = d.pop("priority_fee_sum_usd", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        tip_avg_lamports = d.pop("tip_avg_lamports", UNSET)

        tip_avg_usd = d.pop("tip_avg_usd", UNSET)

        tip_count = d.pop("tip_count", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        tip_sum_usd = d.pop("tip_sum_usd", UNSET)

        tipped_fraction = d.pop("tipped_fraction", UNSET)

        tipped_volume_fraction = d.pop("tipped_volume_fraction", UNSET)

        tipped_volume_lamports = d.pop("tipped_volume_lamports", UNSET)

        tipped_volume_usd = d.pop("tipped_volume_usd", UNSET)

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        total_volume_usd = d.pop("total_volume_usd", UNSET)

        window = d.pop("window", UNSET)

        pulsight_internal_core_domain_aggregator_global_tip_stats = cls(
            p50_tip_lamports=p50_tip_lamports,
            p90_tip_lamports=p90_tip_lamports,
            p99_tip_lamports=p99_tip_lamports,
            previous=previous,
            priority_fee_sum=priority_fee_sum,
            priority_fee_sum_usd=priority_fee_sum_usd,
            swap_count=swap_count,
            tip_avg_lamports=tip_avg_lamports,
            tip_avg_usd=tip_avg_usd,
            tip_count=tip_count,
            tip_sum_lamports=tip_sum_lamports,
            tip_sum_usd=tip_sum_usd,
            tipped_fraction=tipped_fraction,
            tipped_volume_fraction=tipped_volume_fraction,
            tipped_volume_lamports=tipped_volume_lamports,
            tipped_volume_usd=tipped_volume_usd,
            total_volume_lamports=total_volume_lamports,
            total_volume_usd=total_volume_usd,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_global_tip_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_global_tip_stats

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
