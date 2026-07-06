from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipPriorityRatioPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipPriorityRatioPoint:
    """
    Attributes:
        bucket_ts (int | Unset):
        priority_fee_sum (int | Unset):
        ratio (float | Unset):
        tip_sum_lamports (int | Unset):
    """

    bucket_ts: int | Unset = UNSET
    priority_fee_sum: int | Unset = UNSET
    ratio: float | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        priority_fee_sum = self.priority_fee_sum

        ratio = self.ratio

        tip_sum_lamports = self.tip_sum_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if priority_fee_sum is not UNSET:
            field_dict["priority_fee_sum"] = priority_fee_sum
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        priority_fee_sum = d.pop("priority_fee_sum", UNSET)

        ratio = d.pop("ratio", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_tip_priority_ratio_point = cls(
            bucket_ts=bucket_ts,
            priority_fee_sum=priority_fee_sum,
            ratio=ratio,
            tip_sum_lamports=tip_sum_lamports,
        )

        pulsight_internal_core_domain_aggregator_tip_priority_ratio_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_priority_ratio_point

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
