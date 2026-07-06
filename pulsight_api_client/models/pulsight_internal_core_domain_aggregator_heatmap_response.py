from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_tip_heatmap_point import (
        PulsightInternalCoreDomainAggregatorTipHeatmapPoint,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorHeatmapResponse")


@_attrs_define
class PulsightInternalCoreDomainAggregatorHeatmapResponse:
    """
    Attributes:
        bucket (str | Unset):
        horizon_hours (int | Unset):
        points (list[PulsightInternalCoreDomainAggregatorTipHeatmapPoint] | Unset):
    """

    bucket: str | Unset = UNSET
    horizon_hours: int | Unset = UNSET
    points: list[PulsightInternalCoreDomainAggregatorTipHeatmapPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        horizon_hours = self.horizon_hours

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if horizon_hours is not UNSET:
            field_dict["horizon_hours"] = horizon_hours
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_aggregator_tip_heatmap_point import (
            PulsightInternalCoreDomainAggregatorTipHeatmapPoint,
        )

        d = dict(src_dict)
        bucket = d.pop("bucket", UNSET)

        horizon_hours = d.pop("horizon_hours", UNSET)

        _points = d.pop("points", UNSET)
        points: list[PulsightInternalCoreDomainAggregatorTipHeatmapPoint] | Unset = (
            UNSET
        )
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = (
                    PulsightInternalCoreDomainAggregatorTipHeatmapPoint.from_dict(
                        points_item_data
                    )
                )

                points.append(points_item)

        pulsight_internal_core_domain_aggregator_heatmap_response = cls(
            bucket=bucket,
            horizon_hours=horizon_hours,
            points=points,
        )

        pulsight_internal_core_domain_aggregator_heatmap_response.additional_properties = d
        return pulsight_internal_core_domain_aggregator_heatmap_response

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
