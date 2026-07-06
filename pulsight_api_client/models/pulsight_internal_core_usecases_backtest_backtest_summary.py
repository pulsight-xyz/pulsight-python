from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_backtest_position import (
        PulsightInternalCoreUsecasesBacktestBacktestPosition,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestSummary")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestSummary:
    """
    Attributes:
        ending_balance_sol (float | Unset):
        fees_paid_sol (float | Unset):
        held_positions (list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset): HeldPositions is every mint
            still open at run end — the bags the
            strategy never sold, valued at their liquidity-aware exit (see
            BacktestPosition). Their UnrealizedPnlSol sums into UnrealizedPnlSol
            above. Empty when the strategy closed everything (all "Sold all").
            Additive JSONB field — pre-existing rows decode as nil.
        losses (int | Unset):
        max_drawdown_sol (float | Unset):
        our_avg_price_impact_pct (float | Unset): Price-impact rollups, in percent of mid. "Our*" averages over every
            simulated trade that had a pool snapshot; "Target*" averages over the
            copy trades that mirrored a target swap 1:1 (same timestamp). Zero when
            no trade contributed (e.g. an indicator-only strategy, or a run with no
            pool data). Additive JSONB fields — pre-existing rows decode as 0.
        our_median_price_impact_pct (float | Unset):
        realized_pnl_sol (float | Unset):
        roi_pct (float | Unset):
        simulation_assumptions (list[str] | Unset): SimulationAssumptions is free-text notes about which real-world
            cost components the simulator did NOT model (route hops, MEV,
            partial fills, pre-trade gas estimation, etc.). Rendered
            prominently on the result page so users don't read "won 4.2 SOL"
            too literally.
        starting_balance_sol (float | Unset):
        target_avg_price_impact_pct (float | Unset):
        target_median_price_impact_pct (float | Unset):
        tips_paid_sol (float | Unset):
        total_pnl_sol (float | Unset):
        trades (int | Unset):
        unrealized_pnl_sol (float | Unset):
        wins (int | Unset):
    """

    ending_balance_sol: float | Unset = UNSET
    fees_paid_sol: float | Unset = UNSET
    held_positions: (
        list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset
    ) = UNSET
    losses: int | Unset = UNSET
    max_drawdown_sol: float | Unset = UNSET
    our_avg_price_impact_pct: float | Unset = UNSET
    our_median_price_impact_pct: float | Unset = UNSET
    realized_pnl_sol: float | Unset = UNSET
    roi_pct: float | Unset = UNSET
    simulation_assumptions: list[str] | Unset = UNSET
    starting_balance_sol: float | Unset = UNSET
    target_avg_price_impact_pct: float | Unset = UNSET
    target_median_price_impact_pct: float | Unset = UNSET
    tips_paid_sol: float | Unset = UNSET
    total_pnl_sol: float | Unset = UNSET
    trades: int | Unset = UNSET
    unrealized_pnl_sol: float | Unset = UNSET
    wins: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ending_balance_sol = self.ending_balance_sol

        fees_paid_sol = self.fees_paid_sol

        held_positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.held_positions, Unset):
            held_positions = []
            for held_positions_item_data in self.held_positions:
                held_positions_item = held_positions_item_data.to_dict()
                held_positions.append(held_positions_item)

        losses = self.losses

        max_drawdown_sol = self.max_drawdown_sol

        our_avg_price_impact_pct = self.our_avg_price_impact_pct

        our_median_price_impact_pct = self.our_median_price_impact_pct

        realized_pnl_sol = self.realized_pnl_sol

        roi_pct = self.roi_pct

        simulation_assumptions: list[str] | Unset = UNSET
        if not isinstance(self.simulation_assumptions, Unset):
            simulation_assumptions = self.simulation_assumptions

        starting_balance_sol = self.starting_balance_sol

        target_avg_price_impact_pct = self.target_avg_price_impact_pct

        target_median_price_impact_pct = self.target_median_price_impact_pct

        tips_paid_sol = self.tips_paid_sol

        total_pnl_sol = self.total_pnl_sol

        trades = self.trades

        unrealized_pnl_sol = self.unrealized_pnl_sol

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ending_balance_sol is not UNSET:
            field_dict["ending_balance_sol"] = ending_balance_sol
        if fees_paid_sol is not UNSET:
            field_dict["fees_paid_sol"] = fees_paid_sol
        if held_positions is not UNSET:
            field_dict["held_positions"] = held_positions
        if losses is not UNSET:
            field_dict["losses"] = losses
        if max_drawdown_sol is not UNSET:
            field_dict["max_drawdown_sol"] = max_drawdown_sol
        if our_avg_price_impact_pct is not UNSET:
            field_dict["our_avg_price_impact_pct"] = our_avg_price_impact_pct
        if our_median_price_impact_pct is not UNSET:
            field_dict["our_median_price_impact_pct"] = our_median_price_impact_pct
        if realized_pnl_sol is not UNSET:
            field_dict["realized_pnl_sol"] = realized_pnl_sol
        if roi_pct is not UNSET:
            field_dict["roi_pct"] = roi_pct
        if simulation_assumptions is not UNSET:
            field_dict["simulation_assumptions"] = simulation_assumptions
        if starting_balance_sol is not UNSET:
            field_dict["starting_balance_sol"] = starting_balance_sol
        if target_avg_price_impact_pct is not UNSET:
            field_dict["target_avg_price_impact_pct"] = target_avg_price_impact_pct
        if target_median_price_impact_pct is not UNSET:
            field_dict["target_median_price_impact_pct"] = (
                target_median_price_impact_pct
            )
        if tips_paid_sol is not UNSET:
            field_dict["tips_paid_sol"] = tips_paid_sol
        if total_pnl_sol is not UNSET:
            field_dict["total_pnl_sol"] = total_pnl_sol
        if trades is not UNSET:
            field_dict["trades"] = trades
        if unrealized_pnl_sol is not UNSET:
            field_dict["unrealized_pnl_sol"] = unrealized_pnl_sol
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_backtest_backtest_position import (
            PulsightInternalCoreUsecasesBacktestBacktestPosition,
        )

        d = dict(src_dict)
        ending_balance_sol = d.pop("ending_balance_sol", UNSET)

        fees_paid_sol = d.pop("fees_paid_sol", UNSET)

        _held_positions = d.pop("held_positions", UNSET)
        held_positions: (
            list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset
        ) = UNSET
        if _held_positions is not UNSET:
            held_positions = []
            for held_positions_item_data in _held_positions:
                held_positions_item = (
                    PulsightInternalCoreUsecasesBacktestBacktestPosition.from_dict(
                        held_positions_item_data
                    )
                )

                held_positions.append(held_positions_item)

        losses = d.pop("losses", UNSET)

        max_drawdown_sol = d.pop("max_drawdown_sol", UNSET)

        our_avg_price_impact_pct = d.pop("our_avg_price_impact_pct", UNSET)

        our_median_price_impact_pct = d.pop("our_median_price_impact_pct", UNSET)

        realized_pnl_sol = d.pop("realized_pnl_sol", UNSET)

        roi_pct = d.pop("roi_pct", UNSET)

        simulation_assumptions = cast(list[str], d.pop("simulation_assumptions", UNSET))

        starting_balance_sol = d.pop("starting_balance_sol", UNSET)

        target_avg_price_impact_pct = d.pop("target_avg_price_impact_pct", UNSET)

        target_median_price_impact_pct = d.pop("target_median_price_impact_pct", UNSET)

        tips_paid_sol = d.pop("tips_paid_sol", UNSET)

        total_pnl_sol = d.pop("total_pnl_sol", UNSET)

        trades = d.pop("trades", UNSET)

        unrealized_pnl_sol = d.pop("unrealized_pnl_sol", UNSET)

        wins = d.pop("wins", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_summary = cls(
            ending_balance_sol=ending_balance_sol,
            fees_paid_sol=fees_paid_sol,
            held_positions=held_positions,
            losses=losses,
            max_drawdown_sol=max_drawdown_sol,
            our_avg_price_impact_pct=our_avg_price_impact_pct,
            our_median_price_impact_pct=our_median_price_impact_pct,
            realized_pnl_sol=realized_pnl_sol,
            roi_pct=roi_pct,
            simulation_assumptions=simulation_assumptions,
            starting_balance_sol=starting_balance_sol,
            target_avg_price_impact_pct=target_avg_price_impact_pct,
            target_median_price_impact_pct=target_median_price_impact_pct,
            tips_paid_sol=tips_paid_sol,
            total_pnl_sol=total_pnl_sol,
            trades=trades,
            unrealized_pnl_sol=unrealized_pnl_sol,
            wins=wins,
        )

        pulsight_internal_core_usecases_backtest_backtest_summary.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_summary

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
