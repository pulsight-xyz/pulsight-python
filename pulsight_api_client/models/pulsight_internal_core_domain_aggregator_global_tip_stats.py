from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorGlobalTipStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorGlobalTipStats:
    """
    Attributes:
        p50_tip_lamports (float | Unset):
        p90_tip_lamports (float | Unset):
        priority_fee_sum (int | Unset):
        swap_count (int | Unset):
        tip_avg_lamports (float | Unset):
        tip_count (int | Unset):
        tip_sum_lamports (int | Unset):
        tipped_fraction (float | Unset): TippedFraction is tip_count / swap_count over the window (0..1).
        window (str | Unset):
    """

    p50_tip_lamports: float | Unset = UNSET
    p90_tip_lamports: float | Unset = UNSET
    priority_fee_sum: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    tip_avg_lamports: float | Unset = UNSET
    tip_count: int | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    tipped_fraction: float | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        p50_tip_lamports = self.p50_tip_lamports

        p90_tip_lamports = self.p90_tip_lamports

        priority_fee_sum = self.priority_fee_sum

        swap_count = self.swap_count

        tip_avg_lamports = self.tip_avg_lamports

        tip_count = self.tip_count

        tip_sum_lamports = self.tip_sum_lamports

        tipped_fraction = self.tipped_fraction

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if p50_tip_lamports is not UNSET:
            field_dict["p50_tip_lamports"] = p50_tip_lamports
        if p90_tip_lamports is not UNSET:
            field_dict["p90_tip_lamports"] = p90_tip_lamports
        if priority_fee_sum is not UNSET:
            field_dict["priority_fee_sum"] = priority_fee_sum
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if tip_avg_lamports is not UNSET:
            field_dict["tip_avg_lamports"] = tip_avg_lamports
        if tip_count is not UNSET:
            field_dict["tip_count"] = tip_count
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports
        if tipped_fraction is not UNSET:
            field_dict["tipped_fraction"] = tipped_fraction
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        p50_tip_lamports = d.pop("p50_tip_lamports", UNSET)

        p90_tip_lamports = d.pop("p90_tip_lamports", UNSET)

        priority_fee_sum = d.pop("priority_fee_sum", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        tip_avg_lamports = d.pop("tip_avg_lamports", UNSET)

        tip_count = d.pop("tip_count", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        tipped_fraction = d.pop("tipped_fraction", UNSET)

        window = d.pop("window", UNSET)

        pulsight_internal_core_domain_aggregator_global_tip_stats = cls(
            p50_tip_lamports=p50_tip_lamports,
            p90_tip_lamports=p90_tip_lamports,
            priority_fee_sum=priority_fee_sum,
            swap_count=swap_count,
            tip_avg_lamports=tip_avg_lamports,
            tip_count=tip_count,
            tip_sum_lamports=tip_sum_lamports,
            tipped_fraction=tipped_fraction,
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
