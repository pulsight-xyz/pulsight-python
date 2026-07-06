from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_aggregator_timeframe import (
    PulsightInternalCoreDomainAggregatorTimeframe,
)
from ..models.pulsight_internal_core_domain_strategy_venue_id import (
    PulsightInternalCoreDomainStrategyVenueID,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_time_range import (
        PulsightInternalCoreUsecasesBacktestTimeRange,
    )
    from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
        PulsightInternalCoreUsecasesBacktestTokenScope,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestRequest")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestRequest:
    """
    Attributes:
        scope (PulsightInternalCoreUsecasesBacktestTokenScope | Unset):
        starting_balance_sol (float | Unset):
        strategy_id (str | Unset):
        time_range (PulsightInternalCoreUsecasesBacktestTimeRange | Unset):
        timeframe (PulsightInternalCoreDomainAggregatorTimeframe | Unset):
        venue (PulsightInternalCoreDomainStrategyVenueID | Unset):
    """

    scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset = UNSET
    starting_balance_sol: float | Unset = UNSET
    strategy_id: str | Unset = UNSET
    time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset = UNSET
    timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset = UNSET
    venue: PulsightInternalCoreDomainStrategyVenueID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        starting_balance_sol = self.starting_balance_sol

        strategy_id = self.strategy_id

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        timeframe: str | Unset = UNSET
        if not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value

        venue: str | Unset = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if starting_balance_sol is not UNSET:
            field_dict["starting_balance_sol"] = starting_balance_sol
        if strategy_id is not UNSET:
            field_dict["strategy_id"] = strategy_id
        if time_range is not UNSET:
            field_dict["time_range"] = time_range
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if venue is not UNSET:
            field_dict["venue"] = venue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_backtest_time_range import (
            PulsightInternalCoreUsecasesBacktestTimeRange,
        )
        from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
            PulsightInternalCoreUsecasesBacktestTokenScope,
        )

        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PulsightInternalCoreUsecasesBacktestTokenScope.from_dict(_scope)

        starting_balance_sol = d.pop("starting_balance_sol", UNSET)

        strategy_id = d.pop("strategy_id", UNSET)

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

        _venue = d.pop("venue", UNSET)
        venue: PulsightInternalCoreDomainStrategyVenueID | Unset
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = PulsightInternalCoreDomainStrategyVenueID(_venue)

        pulsight_internal_core_usecases_backtest_backtest_request = cls(
            scope=scope,
            starting_balance_sol=starting_balance_sol,
            strategy_id=strategy_id,
            time_range=time_range,
            timeframe=timeframe,
            venue=venue,
        )

        pulsight_internal_core_usecases_backtest_backtest_request.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_request

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
