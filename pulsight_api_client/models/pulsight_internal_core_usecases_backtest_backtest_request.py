from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

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
        latency_slots (int | Unset): LatencySlots is the copy-fill landing latency in slots (blocks),
            0..MaxLatencySlots. 0 (default) keeps the zero-latency model: a copy
            fills at the target's own post-swap price with slippage charged as a
            flat haircut. 1..3 fills at the pool's EMPIRICAL resting price that many
            slots after the target's swap, and the exec's slippage_bps becomes a
            REVERT GATE instead of a charge — the fill is rejected (tip + priority
            fee still paid) when the landing price drifted past the tolerance,
            matching how a transaction's min_out floor behaves. Only copy-style
            fills (Copy* and Target-signal-driven Emits) are affected; candle-driven
            fills already price on the bucket close.
        native_reserve_pct (float | Unset): NativeReservePct keeps that share of the run's cash (0..50, a percentage)
            out of reach of buys, with a 0.01 SOL floor when above 0, as a live
            session's native_reserve_pct does. 0 (default) reserves nothing, as a
            paper session does. Refused with unlimited_capital.
        per_pool (bool | Unset): PerPool, when true, simulates each of a mint's significant markets as an
            INDEPENDENT instrument — its own candle stream, indicators, ledger and
            (for copy strategies) the target swaps on THAT pool — instead of a single
            dominant/pinned pool per mint. Off ⇒ the historical one-position-per-mint
            behaviour. Mutually exclusive with a SingleMint pool pin (a pin already
            selects one market). Fans out compute by up to MaxPoolsPerMint per mint,
            reflected in the tick-budget estimate.
        scope (PulsightInternalCoreUsecasesBacktestTokenScope | Unset):
        starting_balance_sol (float | Unset):
        strategy_id (str | Unset):
        time_range (PulsightInternalCoreUsecasesBacktestTimeRange | Unset):
        timeframe (PulsightInternalCoreDomainAggregatorTimeframe | Unset):
        unlimited_capital (bool | Unset): UnlimitedCapital lifts the run's cash gate: every buy fills whatever the
            cash, which may go negative, as runs did before the gate existed. Off
            (default), a buy the cash cannot pay is an `insufficient_balance` decline.
        venue (PulsightInternalCoreDomainStrategyVenueID | Unset):
    """

    latency_slots: int | Unset = UNSET
    native_reserve_pct: float | Unset = UNSET
    per_pool: bool | Unset = UNSET
    scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset = UNSET
    starting_balance_sol: float | Unset = UNSET
    strategy_id: str | Unset = UNSET
    time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset = UNSET
    timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset = UNSET
    unlimited_capital: bool | Unset = UNSET
    venue: PulsightInternalCoreDomainStrategyVenueID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latency_slots = self.latency_slots

        native_reserve_pct = self.native_reserve_pct

        per_pool = self.per_pool

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

        unlimited_capital = self.unlimited_capital

        venue: str | Unset = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latency_slots is not UNSET:
            field_dict["latency_slots"] = latency_slots
        if native_reserve_pct is not UNSET:
            field_dict["native_reserve_pct"] = native_reserve_pct
        if per_pool is not UNSET:
            field_dict["per_pool"] = per_pool
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
        if unlimited_capital is not UNSET:
            field_dict["unlimited_capital"] = unlimited_capital
        if venue is not UNSET:
            field_dict["venue"] = venue

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_usecases_backtest_time_range import (
            PulsightInternalCoreUsecasesBacktestTimeRange,
        )
        from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
            PulsightInternalCoreUsecasesBacktestTokenScope,
        )

        d = dict(src_dict)
        latency_slots = d.pop("latency_slots", UNSET)

        native_reserve_pct = d.pop("native_reserve_pct", UNSET)

        per_pool = d.pop("per_pool", UNSET)

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

        unlimited_capital = d.pop("unlimited_capital", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: PulsightInternalCoreDomainStrategyVenueID | Unset
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = PulsightInternalCoreDomainStrategyVenueID(_venue)

        pulsight_internal_core_usecases_backtest_backtest_request = cls(
            latency_slots=latency_slots,
            native_reserve_pct=native_reserve_pct,
            per_pool=per_pool,
            scope=scope,
            starting_balance_sol=starting_balance_sol,
            strategy_id=strategy_id,
            time_range=time_range,
            timeframe=timeframe,
            unlimited_capital=unlimited_capital,
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
