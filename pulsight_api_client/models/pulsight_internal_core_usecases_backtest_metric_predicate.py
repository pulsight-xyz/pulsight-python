from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_strategy_comparison_op import (
    PulsightInternalCoreDomainStrategyComparisonOp,
)
from ..models.pulsight_internal_core_usecases_backtest_selection_metric import (
    PulsightInternalCoreUsecasesBacktestSelectionMetric,
)
from ..models.pulsight_internal_core_usecases_backtest_selection_metric_window import (
    PulsightInternalCoreUsecasesBacktestSelectionMetricWindow,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestMetricPredicate")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestMetricPredicate:
    """
    Attributes:
        metric (PulsightInternalCoreUsecasesBacktestSelectionMetric | Unset):
        op (PulsightInternalCoreDomainStrategyComparisonOp | Unset):
        value (float | Unset):
        window (PulsightInternalCoreUsecasesBacktestSelectionMetricWindow | Unset):
    """

    metric: PulsightInternalCoreUsecasesBacktestSelectionMetric | Unset = UNSET
    op: PulsightInternalCoreDomainStrategyComparisonOp | Unset = UNSET
    value: float | Unset = UNSET
    window: PulsightInternalCoreUsecasesBacktestSelectionMetricWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        value = self.value

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _metric = d.pop("metric", UNSET)
        metric: PulsightInternalCoreUsecasesBacktestSelectionMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = PulsightInternalCoreUsecasesBacktestSelectionMetric(_metric)

        _op = d.pop("op", UNSET)
        op: PulsightInternalCoreDomainStrategyComparisonOp | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = PulsightInternalCoreDomainStrategyComparisonOp(_op)

        value = d.pop("value", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreUsecasesBacktestSelectionMetricWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreUsecasesBacktestSelectionMetricWindow(_window)

        pulsight_internal_core_usecases_backtest_metric_predicate = cls(
            metric=metric,
            op=op,
            value=value,
            window=window,
        )

        pulsight_internal_core_usecases_backtest_metric_predicate.additional_properties = d
        return pulsight_internal_core_usecases_backtest_metric_predicate

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
