from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_usecases_backtest_capital_model import (
    PulsightInternalCoreUsecasesBacktestCapitalModel,
)
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
        capital_model (PulsightInternalCoreUsecasesBacktestCapitalModel | Unset):
        capital_required_sol (float | Unset): CapitalRequiredSol is the starting balance that would have kept the cash
            at or above zero along the same fills: max(StartingBalanceSol,
            StartingBalanceSol-MinCashSol).
        cash_declined_buys (int | Unset): CashDeclinedBuys counts the buy attempts the run declined before sending
            because the cash left could not pay them (`insufficient_balance`,
            tx_failed false), candle-driven Emit buys included; CashDeclinedSol is
            the SOL they asked for. Each one also counts in CopiesDeclined or
            EmitBuysDeclined.
        cash_declined_sol (float | Unset):
        cash_failed_buys (int | Unset): CashFailedBuys counts the buy attempts sent while the cash was at or
            below zero, which failed and paid nothing (`insufficient_balance`,
            tx_failed true), candle-driven Emit buys included; CashFailedSol is the
            SOL they asked for. Each one also counts in CopiesDeclined or
            EmitBuysDeclined.
        cash_failed_sol (float | Unset):
        copies_declined (int | Unset): CopiesDeclined counts target swaps a signal-driven exec wanted to act
            on but that a RULE or the run's cash refused: cooldown, sizing,
            max_buys_per_open_position, exposure cap, bracket placement, rate limit,
            cash left too short, a buy that failed on an empty cash — plus the sells
            this run sat out because the target only sold tokens it had never
            mirrored. Reverts and unpriced skips have their own counters and are not
            in here. Every one is persisted as a `backtest_declines` row with its reason, so the
            trade history reads as a complete account of the target's swaps.
            Additive JSONB field — old rows decode as 0.
        copies_reverted (int | Unset): CopiesReverted counts copy fills the slippage gate REJECTED: the pool's
            landing price had drifted past the exec's slippage_bps between the
            target's swap and our simulated landing. Unlike CopiesSkippedUnpriced
            this is an EXECUTION OUTCOME, not a coverage gap — the data was fine,
            the market moved, and a real transaction would have landed and reverted.
            Each revert still pays its tip + priority fee (folded into
            FeesPaidSol/TipsPaidSol and broken out in RevertFeesSol). Only possible
            on latency_slots > 0 runs. Additive JSONB field — old rows decode as 0.
        copies_skipped_non_sol_quote (int | Unset): CopiesSkippedNonSolQuote is the part of CopiesSkippedUnpriced whose
            cause is the pool's quote: the target swapped in a USDC-, USDT- or
            token-quoted pool whose leg carries no SOL price, so there is no route
            to copy it and the run skips it (`non_sol_quote`). Additive JSONB
            field — old rows decode as 0.
        copies_skipped_pool_not_simulated (int | Unset): CopiesSkippedPoolNotSimulated counts target swaps a per-pool
            run saw on a
            market it carried no instrument for (past the per-mint pool cap, or a
            pool the catalog does not know). They fold into the target book and are
            recorded once as `pool_not_simulated`; nothing fills. A per-pool
            artefact, not in CopiesSkippedUnpriced. Additive JSONB field.
        copies_skipped_unpriced (int | Unset): CopiesSkippedUnpriced counts mirror BUYS that passed every rule and
            would have fired, but whose triggering swap could not be priced honestly
            — so they were NOT traded. A signal-driven exit on such a swap is never
            skipped: it fills at a fallback mark (ExitsAtFallbackMark). Two causes,
            both data-side:

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
        emit_buys_declined (int | Unset): EmitBuysDeclined counts the candle closes on which an Emit buy whose
            rule held was refused by a rule or the run's cash — sizing,
            max_buys_per_open_position, exposure cap, bracket placement, rate limit,
            cash left too short, a buy that failed on an empty cash — once per
            refusal: an Emit buy refused on consecutive closes for the same reason
            counts once, until it fills, a close finds it not ready to fire or the
            reason (or, for insufficient_balance, tx_failed) changes. Each
            one is persisted as a `backtest_declines` row with its reason, source
            `emit_buy` and no triggering swap. An Emit buy a target's swap triggered
            counts in CopiesDeclined instead. Additive JSONB field — old rows decode
            as 0.
        ending_balance_sol (float | Unset):
        exits_at_fallback_mark (int | Unset): ExitsAtFallbackMark counts signal-driven exits whose triggering swap
            could not be priced (no SOL price on the leg, or no honest post-swap
            price) and that filled anyway on the run's own market: at the last mark
            (the last candle close, or the latest priceable swap before the first
            close) and its pool depth, else at the position's average cost. A copy
            sell needs only the target's fraction and the run's own market, so the
            run sells instead of holding the bag. Additive JSONB
            field — old rows decode as 0.
        exits_unmarked (int | Unset): ExitsUnmarked is the part of ExitsAtFallbackMark that found no mark at
            all and filled at the position's average cost with no depth term, so
            it realizes no price move, only its costs. Additive JSONB field — old rows
            decode as 0.
        fees_paid_sol (float | Unset):
        held_positions (list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset): HeldPositions is every mint
            still open at run end — the bags the
            strategy never sold, valued at their liquidity-aware exit (see
            BacktestPosition). Their UnrealizedPnlSol sums into UnrealizedPnlSol
            above. Empty when the strategy closed everything (all "Sold all").
            Additive JSONB field — pre-existing rows decode as nil.
        landing_contested_pct (float | Unset): LandingContestedPct is the share (0-100) of filled copies whose pool saw
            at least one other tx inside the latency gap — how often somebody
            reached the pool first. Nil when the run had no landing fills.
        latency_slots (int | Unset): LatencySlots echoes the run's landing latency (req.LatencySlots) so a
            result is readable as which fill model produced it. 0 ⇒ the zero-latency
            model. Additive JSONB field — old rows decode as 0, which is what they
            ran. When > 0, the four fields below describe the landing plane.
        losses (int | Unset):
        max_drawdown_sol (float | Unset):
        min_cash_sol (float | Unset): MinCashSol is the low point of the run's cash, walked in replay order:
            the starting balance minus every buy's size and costs, plus every sell's
            proceeds net of costs, minus reverted fills' costs. Under the portfolio
            capital model a buy the cash cannot pay never fills, so it dips below
            zero only when a fill's fixed fees outrun the fee headroom a buy keeps;
            under unlimited_capital, negative means the run spent SOL the starting
            balance never had.
        native_reserve_pct (float | Unset): NativeReservePct echoes the run's native reserve (req.NativeReservePct).
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
        platform_fee_bps (int | Unset): PlatformFeeBps is the platform fee rate the run charged: the account's
            rate when the run was submitted.
        platform_fees_paid_sol (float | Unset): PlatformFeesPaidSol is the platform fee paid across every fill, folded
            out of realized PnL like priority fees and tips.
        positions_opened_unmarked (int | Unset): PositionsOpenedUnmarked counts positions the run opened while it had NO
            price to mark them with, so that every price-based exit rule
            (take-profit, stop, trailing stop, max-drawdown) evaluated as undefined
            and could not fire. A copy seeds the mark from its own triggering swap
            until the first candle closes, so a run records 0; a non-zero value is a
            run from before that rule. Additive JSONB field — old rows decode as 0.
        realized_pnl_sol (float | Unset):
        revert_fees_sol (float | Unset): RevertFeesSol is the tip + priority-fee total burned by CopiesReverted
            fills — money spent on txs that opened or closed nothing. Already
            included in FeesPaidSol/TipsPaidSol; broken out so the cost of a
            too-tight slippage setting is visible on its own. NOT walked into
            MaxDrawdownSol (the drawdown walk only sees trade rows) — a documented
            approximation.
        roi_pct (float | Unset):
        scope_exits_unpriced (int | Unset): ScopeExitsUnpriced counts the forced closes an `on_retire: sell` policy
            could not fill because nothing had priced the token yet when it left
            the selection: the position stays open, its exits keep firing, and
            whatever is left at the end is marked in HeldPositions. Additive JSONB
            field — old rows decode as 0.
        simulation_assumptions (list[str] | Unset): SimulationAssumptions is free-text notes about which real-world
            cost components the simulator did NOT model (route hops, MEV,
            partial fills, pre-trade gas estimation, etc.). Rendered
            prominently on the result page so users don't read "won 4.2 SOL"
            too literally. A run list carries them only with include=assumptions.
        starting_balance_sol (float | Unset):
        target_avg_price_impact_pct (float | Unset):
        target_median_price_impact_pct (float | Unset):
        tips_paid_sol (float | Unset):
        total_pnl_sol (float | Unset):
        trades (int | Unset):
        transfer_fees_paid_sol (float | Unset): TransferFeesPaidSol is the SOL value Token-2022 transfer fees took
            across
            every fill; it is already inside the fill prices, so it is not folded again.
        unrealized_pnl_sol (float | Unset):
        warnings (list[str] | Unset): Warnings are caveats about this run's own inputs, such as a token
            selection that stopped at its candidate cap. Additive JSONB field.
        wins (int | Unset):
    """

    avg_landing_drift_bps: float | Unset = UNSET
    capital_model: PulsightInternalCoreUsecasesBacktestCapitalModel | Unset = UNSET
    capital_required_sol: float | Unset = UNSET
    cash_declined_buys: int | Unset = UNSET
    cash_declined_sol: float | Unset = UNSET
    cash_failed_buys: int | Unset = UNSET
    cash_failed_sol: float | Unset = UNSET
    copies_declined: int | Unset = UNSET
    copies_reverted: int | Unset = UNSET
    copies_skipped_non_sol_quote: int | Unset = UNSET
    copies_skipped_pool_not_simulated: int | Unset = UNSET
    copies_skipped_unpriced: int | Unset = UNSET
    emit_buys_declined: int | Unset = UNSET
    ending_balance_sol: float | Unset = UNSET
    exits_at_fallback_mark: int | Unset = UNSET
    exits_unmarked: int | Unset = UNSET
    fees_paid_sol: float | Unset = UNSET
    held_positions: (
        list[PulsightInternalCoreUsecasesBacktestBacktestPosition] | Unset
    ) = UNSET
    landing_contested_pct: float | Unset = UNSET
    latency_slots: int | Unset = UNSET
    losses: int | Unset = UNSET
    max_drawdown_sol: float | Unset = UNSET
    min_cash_sol: float | Unset = UNSET
    native_reserve_pct: float | Unset = UNSET
    our_avg_price_impact_pct: float | Unset = UNSET
    our_median_price_impact_pct: float | Unset = UNSET
    per_pool: bool | Unset = UNSET
    platform_fee_bps: int | Unset = UNSET
    platform_fees_paid_sol: float | Unset = UNSET
    positions_opened_unmarked: int | Unset = UNSET
    realized_pnl_sol: float | Unset = UNSET
    revert_fees_sol: float | Unset = UNSET
    roi_pct: float | Unset = UNSET
    scope_exits_unpriced: int | Unset = UNSET
    simulation_assumptions: list[str] | Unset = UNSET
    starting_balance_sol: float | Unset = UNSET
    target_avg_price_impact_pct: float | Unset = UNSET
    target_median_price_impact_pct: float | Unset = UNSET
    tips_paid_sol: float | Unset = UNSET
    total_pnl_sol: float | Unset = UNSET
    trades: int | Unset = UNSET
    transfer_fees_paid_sol: float | Unset = UNSET
    unrealized_pnl_sol: float | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    wins: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_landing_drift_bps = self.avg_landing_drift_bps

        capital_model: str | Unset = UNSET
        if not isinstance(self.capital_model, Unset):
            capital_model = self.capital_model.value

        capital_required_sol = self.capital_required_sol

        cash_declined_buys = self.cash_declined_buys

        cash_declined_sol = self.cash_declined_sol

        cash_failed_buys = self.cash_failed_buys

        cash_failed_sol = self.cash_failed_sol

        copies_declined = self.copies_declined

        copies_reverted = self.copies_reverted

        copies_skipped_non_sol_quote = self.copies_skipped_non_sol_quote

        copies_skipped_pool_not_simulated = self.copies_skipped_pool_not_simulated

        copies_skipped_unpriced = self.copies_skipped_unpriced

        emit_buys_declined = self.emit_buys_declined

        ending_balance_sol = self.ending_balance_sol

        exits_at_fallback_mark = self.exits_at_fallback_mark

        exits_unmarked = self.exits_unmarked

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

        min_cash_sol = self.min_cash_sol

        native_reserve_pct = self.native_reserve_pct

        our_avg_price_impact_pct = self.our_avg_price_impact_pct

        our_median_price_impact_pct = self.our_median_price_impact_pct

        per_pool = self.per_pool

        platform_fee_bps = self.platform_fee_bps

        platform_fees_paid_sol = self.platform_fees_paid_sol

        positions_opened_unmarked = self.positions_opened_unmarked

        realized_pnl_sol = self.realized_pnl_sol

        revert_fees_sol = self.revert_fees_sol

        roi_pct = self.roi_pct

        scope_exits_unpriced = self.scope_exits_unpriced

        simulation_assumptions: list[str] | Unset = UNSET
        if not isinstance(self.simulation_assumptions, Unset):
            simulation_assumptions = self.simulation_assumptions

        starting_balance_sol = self.starting_balance_sol

        target_avg_price_impact_pct = self.target_avg_price_impact_pct

        target_median_price_impact_pct = self.target_median_price_impact_pct

        tips_paid_sol = self.tips_paid_sol

        total_pnl_sol = self.total_pnl_sol

        trades = self.trades

        transfer_fees_paid_sol = self.transfer_fees_paid_sol

        unrealized_pnl_sol = self.unrealized_pnl_sol

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_landing_drift_bps is not UNSET:
            field_dict["avg_landing_drift_bps"] = avg_landing_drift_bps
        if capital_model is not UNSET:
            field_dict["capital_model"] = capital_model
        if capital_required_sol is not UNSET:
            field_dict["capital_required_sol"] = capital_required_sol
        if cash_declined_buys is not UNSET:
            field_dict["cash_declined_buys"] = cash_declined_buys
        if cash_declined_sol is not UNSET:
            field_dict["cash_declined_sol"] = cash_declined_sol
        if cash_failed_buys is not UNSET:
            field_dict["cash_failed_buys"] = cash_failed_buys
        if cash_failed_sol is not UNSET:
            field_dict["cash_failed_sol"] = cash_failed_sol
        if copies_declined is not UNSET:
            field_dict["copies_declined"] = copies_declined
        if copies_reverted is not UNSET:
            field_dict["copies_reverted"] = copies_reverted
        if copies_skipped_non_sol_quote is not UNSET:
            field_dict["copies_skipped_non_sol_quote"] = copies_skipped_non_sol_quote
        if copies_skipped_pool_not_simulated is not UNSET:
            field_dict["copies_skipped_pool_not_simulated"] = (
                copies_skipped_pool_not_simulated
            )
        if copies_skipped_unpriced is not UNSET:
            field_dict["copies_skipped_unpriced"] = copies_skipped_unpriced
        if emit_buys_declined is not UNSET:
            field_dict["emit_buys_declined"] = emit_buys_declined
        if ending_balance_sol is not UNSET:
            field_dict["ending_balance_sol"] = ending_balance_sol
        if exits_at_fallback_mark is not UNSET:
            field_dict["exits_at_fallback_mark"] = exits_at_fallback_mark
        if exits_unmarked is not UNSET:
            field_dict["exits_unmarked"] = exits_unmarked
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
        if min_cash_sol is not UNSET:
            field_dict["min_cash_sol"] = min_cash_sol
        if native_reserve_pct is not UNSET:
            field_dict["native_reserve_pct"] = native_reserve_pct
        if our_avg_price_impact_pct is not UNSET:
            field_dict["our_avg_price_impact_pct"] = our_avg_price_impact_pct
        if our_median_price_impact_pct is not UNSET:
            field_dict["our_median_price_impact_pct"] = our_median_price_impact_pct
        if per_pool is not UNSET:
            field_dict["per_pool"] = per_pool
        if platform_fee_bps is not UNSET:
            field_dict["platform_fee_bps"] = platform_fee_bps
        if platform_fees_paid_sol is not UNSET:
            field_dict["platform_fees_paid_sol"] = platform_fees_paid_sol
        if positions_opened_unmarked is not UNSET:
            field_dict["positions_opened_unmarked"] = positions_opened_unmarked
        if realized_pnl_sol is not UNSET:
            field_dict["realized_pnl_sol"] = realized_pnl_sol
        if revert_fees_sol is not UNSET:
            field_dict["revert_fees_sol"] = revert_fees_sol
        if roi_pct is not UNSET:
            field_dict["roi_pct"] = roi_pct
        if scope_exits_unpriced is not UNSET:
            field_dict["scope_exits_unpriced"] = scope_exits_unpriced
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
        if transfer_fees_paid_sol is not UNSET:
            field_dict["transfer_fees_paid_sol"] = transfer_fees_paid_sol
        if unrealized_pnl_sol is not UNSET:
            field_dict["unrealized_pnl_sol"] = unrealized_pnl_sol
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
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

        _capital_model = d.pop("capital_model", UNSET)
        capital_model: PulsightInternalCoreUsecasesBacktestCapitalModel | Unset
        if isinstance(_capital_model, Unset):
            capital_model = UNSET
        else:
            capital_model = PulsightInternalCoreUsecasesBacktestCapitalModel(
                _capital_model
            )

        capital_required_sol = d.pop("capital_required_sol", UNSET)

        cash_declined_buys = d.pop("cash_declined_buys", UNSET)

        cash_declined_sol = d.pop("cash_declined_sol", UNSET)

        cash_failed_buys = d.pop("cash_failed_buys", UNSET)

        cash_failed_sol = d.pop("cash_failed_sol", UNSET)

        copies_declined = d.pop("copies_declined", UNSET)

        copies_reverted = d.pop("copies_reverted", UNSET)

        copies_skipped_non_sol_quote = d.pop("copies_skipped_non_sol_quote", UNSET)

        copies_skipped_pool_not_simulated = d.pop(
            "copies_skipped_pool_not_simulated", UNSET
        )

        copies_skipped_unpriced = d.pop("copies_skipped_unpriced", UNSET)

        emit_buys_declined = d.pop("emit_buys_declined", UNSET)

        ending_balance_sol = d.pop("ending_balance_sol", UNSET)

        exits_at_fallback_mark = d.pop("exits_at_fallback_mark", UNSET)

        exits_unmarked = d.pop("exits_unmarked", UNSET)

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

        min_cash_sol = d.pop("min_cash_sol", UNSET)

        native_reserve_pct = d.pop("native_reserve_pct", UNSET)

        our_avg_price_impact_pct = d.pop("our_avg_price_impact_pct", UNSET)

        our_median_price_impact_pct = d.pop("our_median_price_impact_pct", UNSET)

        per_pool = d.pop("per_pool", UNSET)

        platform_fee_bps = d.pop("platform_fee_bps", UNSET)

        platform_fees_paid_sol = d.pop("platform_fees_paid_sol", UNSET)

        positions_opened_unmarked = d.pop("positions_opened_unmarked", UNSET)

        realized_pnl_sol = d.pop("realized_pnl_sol", UNSET)

        revert_fees_sol = d.pop("revert_fees_sol", UNSET)

        roi_pct = d.pop("roi_pct", UNSET)

        scope_exits_unpriced = d.pop("scope_exits_unpriced", UNSET)

        simulation_assumptions = cast(list[str], d.pop("simulation_assumptions", UNSET))

        starting_balance_sol = d.pop("starting_balance_sol", UNSET)

        target_avg_price_impact_pct = d.pop("target_avg_price_impact_pct", UNSET)

        target_median_price_impact_pct = d.pop("target_median_price_impact_pct", UNSET)

        tips_paid_sol = d.pop("tips_paid_sol", UNSET)

        total_pnl_sol = d.pop("total_pnl_sol", UNSET)

        trades = d.pop("trades", UNSET)

        transfer_fees_paid_sol = d.pop("transfer_fees_paid_sol", UNSET)

        unrealized_pnl_sol = d.pop("unrealized_pnl_sol", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        wins = d.pop("wins", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_summary = cls(
            avg_landing_drift_bps=avg_landing_drift_bps,
            capital_model=capital_model,
            capital_required_sol=capital_required_sol,
            cash_declined_buys=cash_declined_buys,
            cash_declined_sol=cash_declined_sol,
            cash_failed_buys=cash_failed_buys,
            cash_failed_sol=cash_failed_sol,
            copies_declined=copies_declined,
            copies_reverted=copies_reverted,
            copies_skipped_non_sol_quote=copies_skipped_non_sol_quote,
            copies_skipped_pool_not_simulated=copies_skipped_pool_not_simulated,
            copies_skipped_unpriced=copies_skipped_unpriced,
            emit_buys_declined=emit_buys_declined,
            ending_balance_sol=ending_balance_sol,
            exits_at_fallback_mark=exits_at_fallback_mark,
            exits_unmarked=exits_unmarked,
            fees_paid_sol=fees_paid_sol,
            held_positions=held_positions,
            landing_contested_pct=landing_contested_pct,
            latency_slots=latency_slots,
            losses=losses,
            max_drawdown_sol=max_drawdown_sol,
            min_cash_sol=min_cash_sol,
            native_reserve_pct=native_reserve_pct,
            our_avg_price_impact_pct=our_avg_price_impact_pct,
            our_median_price_impact_pct=our_median_price_impact_pct,
            per_pool=per_pool,
            platform_fee_bps=platform_fee_bps,
            platform_fees_paid_sol=platform_fees_paid_sol,
            positions_opened_unmarked=positions_opened_unmarked,
            realized_pnl_sol=realized_pnl_sol,
            revert_fees_sol=revert_fees_sol,
            roi_pct=roi_pct,
            scope_exits_unpriced=scope_exits_unpriced,
            simulation_assumptions=simulation_assumptions,
            starting_balance_sol=starting_balance_sol,
            target_avg_price_impact_pct=target_avg_price_impact_pct,
            target_median_price_impact_pct=target_median_price_impact_pct,
            tips_paid_sol=tips_paid_sol,
            total_pnl_sol=total_pnl_sol,
            trades=trades,
            transfer_fees_paid_sol=transfer_fees_paid_sol,
            unrealized_pnl_sol=unrealized_pnl_sol,
            warnings=warnings,
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
