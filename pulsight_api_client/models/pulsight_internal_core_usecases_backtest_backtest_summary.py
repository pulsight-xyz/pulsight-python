from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

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
        avg_landing_drift_bps (float | Unset): AvgLandingDriftBps is the mean ADVERSE-signed drift (bps) actually
            crossed by the run's FILLED copies — what latency cost on the fills that
            went through (reverted ones are excluded; their cost shows as
            RevertFeesSol + missed entries). Nil when the run had no landing fills.
        copies_reverted (int | Unset): CopiesReverted counts copy fills the slippage gate REJECTED: the pool's
            landing price had drifted past the exec's slippage_bps between the
            target's swap and our simulated landing. Unlike CopiesSkippedUnpriced
            this is an EXECUTION OUTCOME, not a coverage gap — the data was fine,
            the market moved, and a live bot's tx would have landed and reverted.
            Each revert still pays its tip + priority fee (folded into
            FeesPaidSol/TipsPaidSol and broken out in RevertFeesSol). Only possible
            on latency_slots > 0 runs. Additive JSONB field — old rows decode as 0.
        copies_skipped_unpriced (int | Unset): CopiesSkippedUnpriced counts mirror trades that passed every rule and
            would have fired, but whose triggering swap could not be priced honestly
            — so they were NOT traded. Two causes, both data-side:

              1. no post-swap price on the leg at all (every Meteora DLMM leg, and
                 every DAMM v2 / DBC leg ingested before those decoders were fixed);
              2. a leg whose reserve is impossible for a post-swap snapshot, which
                 means it is a PRE-swap one and its price is the pre-swap price
                 (PumpSwap — see postSwapReserveConsistent).

            A non-zero value means the run under-represents the strategy: it is a
            COVERAGE gap, not a signal quality one. Cause 1 makes a launch-sniping
            mirror over historical data skip most of its entries; cause 2 fires on
            exactly the large launch buys such a strategy targets. Surfaced so a
            mostly-skipped run reads as "not enough data" instead of quietly looking
            like a thin strategy — or worse, than being filled at a fictional price
            and looking profitable. Additive JSONB field — old rows decode as 0.
        ending_balance_sol (float | Unset):
        fees_paid_sol (float | Unset):
        held_positions (list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset): HeldPositions is every mint
            still open at run end — the bags the
            strategy never sold, valued at their liquidity-aware exit (see
            BacktestPosition). Their UnrealizedPnlSol sums into UnrealizedPnlSol
            above. Empty when the strategy closed everything (all "Sold all").
            Additive JSONB field — pre-existing rows decode as nil.
        landing_contested_pct (float | Unset): LandingContestedPct is the share (0-100) of filled copies whose pool saw
            at least one other tx inside the latency gap — how often somebody beat
            the bot to the pool. Nil when the run had no landing fills.
        latency_slots (int | Unset): LatencySlots echoes the run's landing latency (req.LatencySlots) so a
            result is readable as which fill model produced it. 0 ⇒ the zero-latency
            model. Additive JSONB field — old rows decode as 0, which is what they
            ran. When > 0, the four fields below describe the landing plane.
        losses (int | Unset):
        max_drawdown_sol (float | Unset):
        our_avg_price_impact_pct (float | Unset): Price-impact rollups, in percent of mid. "Our*" averages over every
            simulated trade that had a pool snapshot; "Target*" averages over the
            copy trades that mirrored a target swap 1:1 (same timestamp). Zero when
            no trade contributed (e.g. an indicator-only strategy, or a run with no
            pool data). Additive JSONB fields — pre-existing rows decode as 0.
        our_median_price_impact_pct (float | Unset):
        per_pool (bool | Unset): PerPool records whether the run simulated each market as an INDEPENDENT
            instrument (req.PerPool). It is persisted because it is the LEDGER
            BOUNDARY, and a reader cannot recover it from the trades: per-pool
            fidelity stamps every fill with the pool it priced against in EVERY mode,
            so a token that graduates mid-window (bonding curve → PumpSwap) carries
            two pools on ONE merged ledger and looks exactly like two independent
            instruments. The result page's per-token rollup used to guess from that
            stamp and split a graduating token in two — the buys on a row reading
            0.000, the realizing sells and all of the profit on another. Additive
            JSONB field; pre-existing rows decode as false, which is what all but an
            opt-in run was.
        positions_opened_unmarked (int | Unset): PositionsOpenedUnmarked counts positions the run opened while it had NO
            price to mark them with — so for as long as that lasted, every
            price-based exit rule (take-profit, stop, trailing stop, max-drawdown)
            evaluated as undefined and could not fire.

            It happens because a copy fills at the price the TARGET left behind, on
            the pool THEY traded, while the position is marked against the run's own
            candle stream. Normally those are the same market. They are not when the
            fill lands somewhere the stream does not cover — a parallel venue, or a
            market whose candles simply have not started yet.

            Like CopiesSkippedUnpriced this is a COVERAGE number, not a result: an
            exit rule that could not be evaluated did not decline to fire, it never
            ran, and the position rode on until something else closed it. A non-zero
            value means the run UNDER-represents its own exit rules — read the ROI
            with that in mind.

            Mid-window graduations used to dominate this and no longer do: the
            candle stream now merges a token's whole migration lineage, so a
            bonding-curve entry is marked from the moment it opens. Additive JSONB
            field — old rows decode as 0.
        realized_pnl_sol (float | Unset):
        revert_fees_sol (float | Unset): RevertFeesSol is the tip + priority-fee total burned by CopiesReverted
            fills — money spent on txs that opened or closed nothing. Already
            included in FeesPaidSol/TipsPaidSol; broken out so the cost of a
            too-tight slippage setting is visible on its own. NOT walked into
            MaxDrawdownSol (the drawdown walk only sees trade rows) — a documented
            approximation.
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

    avg_landing_drift_bps: float | Unset = UNSET
    copies_reverted: int | Unset = UNSET
    copies_skipped_unpriced: int | Unset = UNSET
    ending_balance_sol: float | Unset = UNSET
    fees_paid_sol: float | Unset = UNSET
    held_positions: (
        list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset
    ) = UNSET
    landing_contested_pct: float | Unset = UNSET
    latency_slots: int | Unset = UNSET
    losses: int | Unset = UNSET
    max_drawdown_sol: float | Unset = UNSET
    our_avg_price_impact_pct: float | Unset = UNSET
    our_median_price_impact_pct: float | Unset = UNSET
    per_pool: bool | Unset = UNSET
    positions_opened_unmarked: int | Unset = UNSET
    realized_pnl_sol: float | Unset = UNSET
    revert_fees_sol: float | Unset = UNSET
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
        avg_landing_drift_bps = self.avg_landing_drift_bps

        copies_reverted = self.copies_reverted

        copies_skipped_unpriced = self.copies_skipped_unpriced

        ending_balance_sol = self.ending_balance_sol

        fees_paid_sol = self.fees_paid_sol

        held_positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.held_positions, Unset):
            held_positions = []
            for held_positions_item_data in self.held_positions:
                held_positions_item = held_positions_item_data.to_dict()
                held_positions.append(held_positions_item)

        landing_contested_pct = self.landing_contested_pct

        latency_slots = self.latency_slots

        losses = self.losses

        max_drawdown_sol = self.max_drawdown_sol

        our_avg_price_impact_pct = self.our_avg_price_impact_pct

        our_median_price_impact_pct = self.our_median_price_impact_pct

        per_pool = self.per_pool

        positions_opened_unmarked = self.positions_opened_unmarked

        realized_pnl_sol = self.realized_pnl_sol

        revert_fees_sol = self.revert_fees_sol

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
        if avg_landing_drift_bps is not UNSET:
            field_dict["avg_landing_drift_bps"] = avg_landing_drift_bps
        if copies_reverted is not UNSET:
            field_dict["copies_reverted"] = copies_reverted
        if copies_skipped_unpriced is not UNSET:
            field_dict["copies_skipped_unpriced"] = copies_skipped_unpriced
        if ending_balance_sol is not UNSET:
            field_dict["ending_balance_sol"] = ending_balance_sol
        if fees_paid_sol is not UNSET:
            field_dict["fees_paid_sol"] = fees_paid_sol
        if held_positions is not UNSET:
            field_dict["held_positions"] = held_positions
        if landing_contested_pct is not UNSET:
            field_dict["landing_contested_pct"] = landing_contested_pct
        if latency_slots is not UNSET:
            field_dict["latency_slots"] = latency_slots
        if losses is not UNSET:
            field_dict["losses"] = losses
        if max_drawdown_sol is not UNSET:
            field_dict["max_drawdown_sol"] = max_drawdown_sol
        if our_avg_price_impact_pct is not UNSET:
            field_dict["our_avg_price_impact_pct"] = our_avg_price_impact_pct
        if our_median_price_impact_pct is not UNSET:
            field_dict["our_median_price_impact_pct"] = our_median_price_impact_pct
        if per_pool is not UNSET:
            field_dict["per_pool"] = per_pool
        if positions_opened_unmarked is not UNSET:
            field_dict["positions_opened_unmarked"] = positions_opened_unmarked
        if realized_pnl_sol is not UNSET:
            field_dict["realized_pnl_sol"] = realized_pnl_sol
        if revert_fees_sol is not UNSET:
            field_dict["revert_fees_sol"] = revert_fees_sol
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
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_usecases_backtest_backtest_position import (
            PulsightInternalCoreUsecasesBacktestBacktestPosition,
        )

        d = dict(src_dict)
        avg_landing_drift_bps = d.pop("avg_landing_drift_bps", UNSET)

        copies_reverted = d.pop("copies_reverted", UNSET)

        copies_skipped_unpriced = d.pop("copies_skipped_unpriced", UNSET)

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

        landing_contested_pct = d.pop("landing_contested_pct", UNSET)

        latency_slots = d.pop("latency_slots", UNSET)

        losses = d.pop("losses", UNSET)

        max_drawdown_sol = d.pop("max_drawdown_sol", UNSET)

        our_avg_price_impact_pct = d.pop("our_avg_price_impact_pct", UNSET)

        our_median_price_impact_pct = d.pop("our_median_price_impact_pct", UNSET)

        per_pool = d.pop("per_pool", UNSET)

        positions_opened_unmarked = d.pop("positions_opened_unmarked", UNSET)

        realized_pnl_sol = d.pop("realized_pnl_sol", UNSET)

        revert_fees_sol = d.pop("revert_fees_sol", UNSET)

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
            avg_landing_drift_bps=avg_landing_drift_bps,
            copies_reverted=copies_reverted,
            copies_skipped_unpriced=copies_skipped_unpriced,
            ending_balance_sol=ending_balance_sol,
            fees_paid_sol=fees_paid_sol,
            held_positions=held_positions,
            landing_contested_pct=landing_contested_pct,
            latency_slots=latency_slots,
            losses=losses,
            max_drawdown_sol=max_drawdown_sol,
            our_avg_price_impact_pct=our_avg_price_impact_pct,
            our_median_price_impact_pct=our_median_price_impact_pct,
            per_pool=per_pool,
            positions_opened_unmarked=positions_opened_unmarked,
            realized_pnl_sol=realized_pnl_sol,
            revert_fees_sol=revert_fees_sol,
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
