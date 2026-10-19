from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipAdoptionPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipAdoptionPoint:
    """
    Attributes:
        bucket_ts (int | Unset): BucketTS is the bucket start, unix seconds.
        landed_count (int | Unset): LandedCount is the bucket's landed transactions, tipped or not.
        tipped_count (int | Unset): TippedCount is the bucket's tipped transactions.
        tipped_volume_lamports (int | Unset): TippedVolumeLamports is the value the tipped transactions traded.
        tipped_volume_usd (int | Unset):
        total_volume_lamports (int | Unset): TotalVolumeLamports is the value every landed transaction traded.
        total_volume_usd (int | Unset):
        tx_share (float | Unset): TxShare is tipped_count / landed_count (0..1), null when nothing
            landed.
        volume_share (float | Unset): VolumeShare is tipped_volume_lamports / total_volume_lamports (0..1),
            null when nothing traded.
    """

    bucket_ts: int | Unset = UNSET
    landed_count: int | Unset = UNSET
    tipped_count: int | Unset = UNSET
    tipped_volume_lamports: int | Unset = UNSET
    tipped_volume_usd: int | Unset = UNSET
    total_volume_lamports: int | Unset = UNSET
    total_volume_usd: int | Unset = UNSET
    tx_share: float | Unset = UNSET
    volume_share: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_ts = self.bucket_ts

        landed_count = self.landed_count

        tipped_count = self.tipped_count

        tipped_volume_lamports = self.tipped_volume_lamports

        tipped_volume_usd = self.tipped_volume_usd

        total_volume_lamports = self.total_volume_lamports

        total_volume_usd = self.total_volume_usd

        tx_share = self.tx_share

        volume_share = self.volume_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_ts is not UNSET:
            field_dict["bucket_ts"] = bucket_ts
        if landed_count is not UNSET:
            field_dict["landed_count"] = landed_count
        if tipped_count is not UNSET:
            field_dict["tipped_count"] = tipped_count
        if tipped_volume_lamports is not UNSET:
            field_dict["tipped_volume_lamports"] = tipped_volume_lamports
        if tipped_volume_usd is not UNSET:
            field_dict["tipped_volume_usd"] = tipped_volume_usd
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports
        if total_volume_usd is not UNSET:
            field_dict["total_volume_usd"] = total_volume_usd
        if tx_share is not UNSET:
            field_dict["tx_share"] = tx_share
        if volume_share is not UNSET:
            field_dict["volume_share"] = volume_share

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bucket_ts = d.pop("bucket_ts", UNSET)

        landed_count = d.pop("landed_count", UNSET)

        tipped_count = d.pop("tipped_count", UNSET)

        tipped_volume_lamports = d.pop("tipped_volume_lamports", UNSET)

        tipped_volume_usd = d.pop("tipped_volume_usd", UNSET)

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        total_volume_usd = d.pop("total_volume_usd", UNSET)

        tx_share = d.pop("tx_share", UNSET)

        volume_share = d.pop("volume_share", UNSET)

        pulsight_internal_core_domain_aggregator_tip_adoption_point = cls(
            bucket_ts=bucket_ts,
            landed_count=landed_count,
            tipped_count=tipped_count,
            tipped_volume_lamports=tipped_volume_lamports,
            tipped_volume_usd=tipped_volume_usd,
            total_volume_lamports=total_volume_lamports,
            total_volume_usd=total_volume_usd,
            tx_share=tx_share,
            volume_share=volume_share,
        )

        pulsight_internal_core_domain_aggregator_tip_adoption_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_adoption_point

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
