from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestEstimate")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestEstimate:
    """
    Attributes:
        credits_ (int | Unset): Credits is what the run would debit: one api credit per estimated tick.
        estimated_ticks (int | Unset): EstimatedTicks is the run's tick count: candles in the window times
            the scope's token slots (times the pools per mint on a per-pool run).
        max_tick_budget (int | Unset): MaxTickBudget is the per-run tick ceiling, the most a run may cost.
        max_window_secs (int | Unset): MaxWindowSecs is the longest window the request's timeframe allows, in
            seconds; 0 means unlimited.
        mints_count (int | Unset): MintsCount is how many tokens the scope admits over the window: the
            explicit list, or the strategy's own selection resolved minute by
            minute as a run resolves it.
        within_budget (bool | Unset): WithinBudget reports EstimatedTicks <= MaxTickBudget.
        within_window (bool | Unset): WithinWindow reports that the window fits MaxWindowSecs.
    """

    credits_: int | Unset = UNSET
    estimated_ticks: int | Unset = UNSET
    max_tick_budget: int | Unset = UNSET
    max_window_secs: int | Unset = UNSET
    mints_count: int | Unset = UNSET
    within_budget: bool | Unset = UNSET
    within_window: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        estimated_ticks = self.estimated_ticks

        max_tick_budget = self.max_tick_budget

        max_window_secs = self.max_window_secs

        mints_count = self.mints_count

        within_budget = self.within_budget

        within_window = self.within_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if estimated_ticks is not UNSET:
            field_dict["estimated_ticks"] = estimated_ticks
        if max_tick_budget is not UNSET:
            field_dict["max_tick_budget"] = max_tick_budget
        if max_window_secs is not UNSET:
            field_dict["max_window_secs"] = max_window_secs
        if mints_count is not UNSET:
            field_dict["mints_count"] = mints_count
        if within_budget is not UNSET:
            field_dict["within_budget"] = within_budget
        if within_window is not UNSET:
            field_dict["within_window"] = within_window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        credits_ = d.pop("credits", UNSET)

        estimated_ticks = d.pop("estimated_ticks", UNSET)

        max_tick_budget = d.pop("max_tick_budget", UNSET)

        max_window_secs = d.pop("max_window_secs", UNSET)

        mints_count = d.pop("mints_count", UNSET)

        within_budget = d.pop("within_budget", UNSET)

        within_window = d.pop("within_window", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_estimate = cls(
            credits_=credits_,
            estimated_ticks=estimated_ticks,
            max_tick_budget=max_tick_budget,
            max_window_secs=max_window_secs,
            mints_count=mints_count,
            within_budget=within_budget,
            within_window=within_window,
        )

        pulsight_internal_core_usecases_backtest_backtest_estimate.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_estimate

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
