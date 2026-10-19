from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorServiceDominanceRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorServiceDominanceRow:
    """
    Attributes:
        p50_tip_lamports (float | Unset): P50TipLamports and P90TipLamports are the median and 90th percentile
            tip paid to this service.
        p90_tip_lamports (float | Unset):
        prev_share_pct (float | Unset): PrevSharePct is SharePct over the window of equal length just before
            this one: 0 for a service absent from it, null for `all` and when the
            ledger does not cover it.
        share_pct (float | Unset):
        tip_avg_lamports (float | Unset): TipAvgLamports is the mean tip per tipped transaction.
        tip_avg_usd (float | Unset):
        tip_service (str | Unset):
        tip_share_pct (float | Unset): TipSharePct is this service's share of the tips paid in the window
            (0..100).
        tip_sum_lamports (int | Unset):
        tip_sum_usd (int | Unset): TipSumUsd is TipSumLamports on the transactions' USD stamps
            (micro-USD).
        tipped_count (int | Unset):
    """

    p50_tip_lamports: float | Unset = UNSET
    p90_tip_lamports: float | Unset = UNSET
    prev_share_pct: float | Unset = UNSET
    share_pct: float | Unset = UNSET
    tip_avg_lamports: float | Unset = UNSET
    tip_avg_usd: float | Unset = UNSET
    tip_service: str | Unset = UNSET
    tip_share_pct: float | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    tip_sum_usd: int | Unset = UNSET
    tipped_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        p50_tip_lamports = self.p50_tip_lamports

        p90_tip_lamports = self.p90_tip_lamports

        prev_share_pct = self.prev_share_pct

        share_pct = self.share_pct

        tip_avg_lamports = self.tip_avg_lamports

        tip_avg_usd = self.tip_avg_usd

        tip_service = self.tip_service

        tip_share_pct = self.tip_share_pct

        tip_sum_lamports = self.tip_sum_lamports

        tip_sum_usd = self.tip_sum_usd

        tipped_count = self.tipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if p50_tip_lamports is not UNSET:
            field_dict["p50_tip_lamports"] = p50_tip_lamports
        if p90_tip_lamports is not UNSET:
            field_dict["p90_tip_lamports"] = p90_tip_lamports
        if prev_share_pct is not UNSET:
            field_dict["prev_share_pct"] = prev_share_pct
        if share_pct is not UNSET:
            field_dict["share_pct"] = share_pct
        if tip_avg_lamports is not UNSET:
            field_dict["tip_avg_lamports"] = tip_avg_lamports
        if tip_avg_usd is not UNSET:
            field_dict["tip_avg_usd"] = tip_avg_usd
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service
        if tip_share_pct is not UNSET:
            field_dict["tip_share_pct"] = tip_share_pct
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
        p50_tip_lamports = d.pop("p50_tip_lamports", UNSET)

        p90_tip_lamports = d.pop("p90_tip_lamports", UNSET)

        prev_share_pct = d.pop("prev_share_pct", UNSET)

        share_pct = d.pop("share_pct", UNSET)

        tip_avg_lamports = d.pop("tip_avg_lamports", UNSET)

        tip_avg_usd = d.pop("tip_avg_usd", UNSET)

        tip_service = d.pop("tip_service", UNSET)

        tip_share_pct = d.pop("tip_share_pct", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        tip_sum_usd = d.pop("tip_sum_usd", UNSET)

        tipped_count = d.pop("tipped_count", UNSET)

        pulsight_internal_core_domain_aggregator_service_dominance_row = cls(
            p50_tip_lamports=p50_tip_lamports,
            p90_tip_lamports=p90_tip_lamports,
            prev_share_pct=prev_share_pct,
            share_pct=share_pct,
            tip_avg_lamports=tip_avg_lamports,
            tip_avg_usd=tip_avg_usd,
            tip_service=tip_service,
            tip_share_pct=tip_share_pct,
            tip_sum_lamports=tip_sum_lamports,
            tip_sum_usd=tip_sum_usd,
            tipped_count=tipped_count,
        )

        pulsight_internal_core_domain_aggregator_service_dominance_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_service_dominance_row

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
