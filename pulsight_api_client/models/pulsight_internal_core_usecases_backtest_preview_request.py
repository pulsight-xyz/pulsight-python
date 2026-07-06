from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_aggregator_timeframe import (
    PulsightInternalCoreDomainAggregatorTimeframe,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
        PulsightInternalCoreDomainStrategyStrategyDef,
    )
    from ..models.pulsight_internal_core_usecases_backtest_time_range import (
        PulsightInternalCoreUsecasesBacktestTimeRange,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestPreviewRequest")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestPreviewRequest:
    """
    Attributes:
        def_ (PulsightInternalCoreDomainStrategyStrategyDef | Unset):
        mint (str | Unset):
        time_range (PulsightInternalCoreUsecasesBacktestTimeRange | Unset):
        timeframe (PulsightInternalCoreDomainAggregatorTimeframe | Unset):
    """

    def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset = UNSET
    mint: str | Unset = UNSET
    time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset = UNSET
    timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        def_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.def_, Unset):
            def_ = self.def_.to_dict()

        mint = self.mint

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        timeframe: str | Unset = UNSET
        if not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if def_ is not UNSET:
            field_dict["def"] = def_
        if mint is not UNSET:
            field_dict["mint"] = mint
        if time_range is not UNSET:
            field_dict["time_range"] = time_range
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
            PulsightInternalCoreDomainStrategyStrategyDef,
        )
        from ..models.pulsight_internal_core_usecases_backtest_time_range import (
            PulsightInternalCoreUsecasesBacktestTimeRange,
        )

        d = dict(src_dict)
        _def_ = d.pop("def", UNSET)
        def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset
        if isinstance(_def_, Unset):
            def_ = UNSET
        else:
            def_ = PulsightInternalCoreDomainStrategyStrategyDef.from_dict(_def_)

        mint = d.pop("mint", UNSET)

        _time_range = d.pop("time_range", UNSET)
        time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = PulsightInternalCoreUsecasesBacktestTimeRange.from_dict(
                _time_range
            )

        _timeframe = d.pop("timeframe", UNSET)
        timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset
        if isinstance(_timeframe, Unset):
            timeframe = UNSET
        else:
            timeframe = PulsightInternalCoreDomainAggregatorTimeframe(_timeframe)

        pulsight_internal_core_usecases_backtest_preview_request = cls(
            def_=def_,
            mint=mint,
            time_range=time_range,
            timeframe=timeframe,
        )

        pulsight_internal_core_usecases_backtest_preview_request.additional_properties = d
        return pulsight_internal_core_usecases_backtest_preview_request

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
