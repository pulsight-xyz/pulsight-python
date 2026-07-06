from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_event_predicate import (
        PulsightInternalCoreUsecasesBacktestEventPredicate,
    )
    from ..models.pulsight_internal_core_usecases_backtest_metric_predicate import (
        PulsightInternalCoreUsecasesBacktestMetricPredicate,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestSelectionFilter")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestSelectionFilter:
    """
    Attributes:
        events (list[PulsightInternalCoreUsecasesBacktestEventPredicate] | Unset):
        metrics (list[PulsightInternalCoreUsecasesBacktestMetricPredicate] | Unset):
    """

    events: list[PulsightInternalCoreUsecasesBacktestEventPredicate] | Unset = UNSET
    metrics: list[PulsightInternalCoreUsecasesBacktestMetricPredicate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_backtest_event_predicate import (
            PulsightInternalCoreUsecasesBacktestEventPredicate,
        )
        from ..models.pulsight_internal_core_usecases_backtest_metric_predicate import (
            PulsightInternalCoreUsecasesBacktestMetricPredicate,
        )

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: list[PulsightInternalCoreUsecasesBacktestEventPredicate] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = (
                    PulsightInternalCoreUsecasesBacktestEventPredicate.from_dict(
                        events_item_data
                    )
                )

                events.append(events_item)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[PulsightInternalCoreUsecasesBacktestMetricPredicate] | Unset = (
            UNSET
        )
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = (
                    PulsightInternalCoreUsecasesBacktestMetricPredicate.from_dict(
                        metrics_item_data
                    )
                )

                metrics.append(metrics_item)

        pulsight_internal_core_usecases_backtest_selection_filter = cls(
            events=events,
            metrics=metrics,
        )

        pulsight_internal_core_usecases_backtest_selection_filter.additional_properties = d
        return pulsight_internal_core_usecases_backtest_selection_filter

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
