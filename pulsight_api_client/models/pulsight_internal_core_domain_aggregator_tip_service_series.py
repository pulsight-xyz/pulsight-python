from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_tip_service_series_row import (
        PulsightInternalCoreDomainAggregatorTipServiceSeriesRow,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipServiceSeries")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipServiceSeries:
    """
    Attributes:
        bucket_secs (int | Unset): BucketSecs is the bucket width in seconds; buckets start on multiples
            of it since the Unix epoch.
        buckets (list[int] | Unset): Buckets is every bucket start from `from` through the bucket
            containing `to`, ascending.
        from_ (int | Unset): From is the first bucket's start (unix seconds).
        services (list[PulsightInternalCoreDomainAggregatorTipServiceSeriesRow] | Unset): Services is ordered by the
            window's tipped transactions, descending.
        to (int | Unset): To is the read time (unix seconds); the last bucket contains it and is
            still filling.
        window (str | Unset):
    """

    bucket_secs: int | Unset = UNSET
    buckets: list[int] | Unset = UNSET
    from_: int | Unset = UNSET
    services: list[PulsightInternalCoreDomainAggregatorTipServiceSeriesRow] | Unset = (
        UNSET
    )
    to: int | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_secs = self.bucket_secs

        buckets: list[int] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = self.buckets

        from_ = self.from_

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        to = self.to

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_secs is not UNSET:
            field_dict["bucket_secs"] = bucket_secs
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if from_ is not UNSET:
            field_dict["from"] = from_
        if services is not UNSET:
            field_dict["services"] = services
        if to is not UNSET:
            field_dict["to"] = to
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_tip_service_series_row import (
            PulsightInternalCoreDomainAggregatorTipServiceSeriesRow,
        )

        d = dict(src_dict)
        bucket_secs = d.pop("bucket_secs", UNSET)

        buckets = cast(list[int], d.pop("buckets", UNSET))

        from_ = d.pop("from", UNSET)

        _services = d.pop("services", UNSET)
        services: (
            list[PulsightInternalCoreDomainAggregatorTipServiceSeriesRow] | Unset
        ) = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = (
                    PulsightInternalCoreDomainAggregatorTipServiceSeriesRow.from_dict(
                        services_item_data
                    )
                )

                services.append(services_item)

        to = d.pop("to", UNSET)

        window = d.pop("window", UNSET)

        pulsight_internal_core_domain_aggregator_tip_service_series = cls(
            bucket_secs=bucket_secs,
            buckets=buckets,
            from_=from_,
            services=services,
            to=to,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_tip_service_series.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_service_series

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
