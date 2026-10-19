from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_tip_adoption_point import (
        PulsightInternalCoreDomainAggregatorTipAdoptionPoint,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTipAdoption")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTipAdoption:
    """
    Attributes:
        bucket_secs (int | Unset): BucketSecs is the bucket width in seconds, a whole number of hours;
            buckets start on multiples of it since the Unix epoch.
        from_ (int | Unset): From is the first bucket's start (unix seconds).
        points (list[PulsightInternalCoreDomainAggregatorTipAdoptionPoint] | Unset): Points is ascending; a bucket with
            neither tipped nor landed
            transactions is absent.
        to (int | Unset): To is the read time (unix seconds); the bucket containing it is still
            filling.
        window (str | Unset):
    """

    bucket_secs: int | Unset = UNSET
    from_: int | Unset = UNSET
    points: list[PulsightInternalCoreDomainAggregatorTipAdoptionPoint] | Unset = UNSET
    to: int | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_secs = self.bucket_secs

        from_ = self.from_

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        to = self.to

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_secs is not UNSET:
            field_dict["bucket_secs"] = bucket_secs
        if from_ is not UNSET:
            field_dict["from"] = from_
        if points is not UNSET:
            field_dict["points"] = points
        if to is not UNSET:
            field_dict["to"] = to
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_tip_adoption_point import (
            PulsightInternalCoreDomainAggregatorTipAdoptionPoint,
        )

        d = dict(src_dict)
        bucket_secs = d.pop("bucket_secs", UNSET)

        from_ = d.pop("from", UNSET)

        _points = d.pop("points", UNSET)
        points: list[PulsightInternalCoreDomainAggregatorTipAdoptionPoint] | Unset = (
            UNSET
        )
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = (
                    PulsightInternalCoreDomainAggregatorTipAdoptionPoint.from_dict(
                        points_item_data
                    )
                )

                points.append(points_item)

        to = d.pop("to", UNSET)

        window = d.pop("window", UNSET)

        pulsight_internal_core_domain_aggregator_tip_adoption = cls(
            bucket_secs=bucket_secs,
            from_=from_,
            points=points,
            to=to,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_tip_adoption.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tip_adoption

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
