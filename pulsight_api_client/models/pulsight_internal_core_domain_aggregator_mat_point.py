from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMatPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMatPoint:
    """
    Attributes:
        bucket_ts (int | Unset):
        ma_1h (float | Unset):
        ma_5m (float | Unset):
        tip_avg (float | Unset):
    """

    bucket_ts: int | Unset = UNSET
    ma_1h: float | Unset = UNSET
    ma_5m: float | Unset = UNSET
    tip_avg: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        ma_1h = self.ma_1h

        ma_5m = self.ma_5m

        tip_avg = self.tip_avg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if ma_1h is not UNSET:
            field_dict["ma_1h"] = ma_1h
        if ma_5m is not UNSET:
            field_dict["ma_5m"] = ma_5m
        if tip_avg is not UNSET:
            field_dict["tip_avg"] = tip_avg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        ma_1h = d.pop("ma_1h", UNSET)

        ma_5m = d.pop("ma_5m", UNSET)

        tip_avg = d.pop("tip_avg", UNSET)

        pulsight_internal_core_domain_aggregator_mat_point = cls(
            bucket_ts=bucket_ts,
            ma_1h=ma_1h,
            ma_5m=ma_5m,
            tip_avg=tip_avg,
        )

        pulsight_internal_core_domain_aggregator_mat_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mat_point

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
