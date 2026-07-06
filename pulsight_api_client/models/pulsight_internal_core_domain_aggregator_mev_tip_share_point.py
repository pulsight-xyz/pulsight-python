from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMevTipSharePoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMevTipSharePoint:
    """
    Attributes:
        bucket_ts (int | Unset):
        share_pct (float | Unset):
        tipped_volume_lamports (int | Unset):
        total_volume_lamports (int | Unset):
    """

    bucket_ts: int | Unset = UNSET
    share_pct: float | Unset = UNSET
    tipped_volume_lamports: int | Unset = UNSET
    total_volume_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        share_pct = self.share_pct

        tipped_volume_lamports = self.tipped_volume_lamports

        total_volume_lamports = self.total_volume_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if share_pct is not UNSET:
            field_dict["share_pct"] = share_pct
        if tipped_volume_lamports is not UNSET:
            field_dict["tipped_volume_lamports"] = tipped_volume_lamports
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        share_pct = d.pop("share_pct", UNSET)

        tipped_volume_lamports = d.pop("tipped_volume_lamports", UNSET)

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_mev_tip_share_point = cls(
            bucket_ts=bucket_ts,
            share_pct=share_pct,
            tipped_volume_lamports=tipped_volume_lamports,
            total_volume_lamports=total_volume_lamports,
        )

        pulsight_internal_core_domain_aggregator_mev_tip_share_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mev_tip_share_point

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
