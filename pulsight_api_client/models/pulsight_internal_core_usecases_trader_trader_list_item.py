from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_trader_behavioral_stats import (
        PulsightInternalCoreDomainAggregatorTraderBehavioralStats,
    )
    from ..models.pulsight_internal_core_domain_aggregator_trader_period_stats_row import (
        PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow,
    )
    from ..models.pulsight_internal_core_usecases_trader_trader_pnl_distribution_row import (
        PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderTraderListItem")


@_attrs_define
class PulsightInternalCoreUsecasesTraderTraderListItem:
    """
    Attributes:
        arb_tx_ratio_1d (float | Unset):
        arb_tx_ratio_30d (float | Unset):
        arb_tx_ratio_7d (float | Unset):
        arb_tx_ratio_all (float | Unset):
        avg_buy_count_per_token (float | Unset):
        avg_first_buy_reactivity (float | Unset):
        avg_holding_time (float | Unset):
        avg_realized_profit_1d (float | Unset):
        avg_realized_profit_1d_usd (float | Unset):
        avg_realized_profit_30d (float | Unset):
        avg_realized_profit_30d_usd (float | Unset):
        avg_realized_profit_7d (float | Unset):
        avg_realized_profit_7d_usd (float | Unset):
        avg_realized_profit_all (float | Unset):
        avg_realized_profit_all_usd (float | Unset):
        avg_sell_count_per_token (float | Unset):
        behavioral_1d (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        behavioral_30d (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        behavioral_7d (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        behavioral_all (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        buy_1d (int | Unset):
        buy_30d (int | Unset):
        buy_7d (int | Unset):
        buy_all (int | Unset):
        buy_sell_ratio_1d (float | Unset):
        buy_sell_ratio_30d (float | Unset):
        buy_sell_ratio_7d (float | Unset):
        buy_sell_ratio_all (float | Unset):
        cashback_1d (float | Unset):
        cashback_1d_usd (float | Unset):
        cashback_30d (float | Unset):
        cashback_30d_usd (float | Unset):
        cashback_7d (float | Unset): Pump cashback: accrued in the window (the screening signal) and
            swept. Claimed is ALREADY inside NetProfit7d — never add it on top.
        cashback_7d_usd (float | Unset):
        cashback_all (float | Unset):
        cashback_all_usd (float | Unset):
        cashback_claim_count_1d (int | Unset):
        cashback_claim_count_30d (int | Unset):
        cashback_claim_count_7d (int | Unset):
        cashback_claim_count_all (int | Unset):
        cashback_claimed_1d (float | Unset):
        cashback_claimed_1d_usd (float | Unset):
        cashback_claimed_30d (float | Unset):
        cashback_claimed_30d_usd (float | Unset):
        cashback_claimed_7d (float | Unset):
        cashback_claimed_7d_usd (float | Unset):
        cashback_claimed_all (float | Unset):
        cashback_claimed_all_usd (float | Unset):
        cashback_share_1d (float | Unset):
        cashback_share_30d (float | Unset):
        cashback_share_7d (float | Unset):
        cashback_share_all (float | Unset):
        chain (str | Unset):
        created_at (str | Unset):
        didnt_buy_sells_1d (int | Unset):
        didnt_buy_sells_30d (int | Unset):
        didnt_buy_sells_7d (int | Unset): Uncovered-sell counters: sells with no observed buy of the mint /
            sells exceeding the observed bought balance, scoped to the window.
        didnt_buy_sells_all (int | Unset):
        failed_txs_1d (int | Unset):
        failed_txs_30d (int | Unset):
        failed_txs_7d (int | Unset):
        failed_txs_all (int | Unset): There is deliberately no lifetime success/spam rate here: their
            denominator is the one read that cannot prune by partition, so it is
            not paid per listing page. The trader-detail reliability panel serves
            them per wallet.
        holder_reward_payouts_1d (int | Unset):
        holder_reward_payouts_30d (int | Unset):
        holder_reward_payouts_7d (int | Unset):
        holder_reward_payouts_all (int | Unset):
        holder_rewards_1d (float | Unset):
        holder_rewards_1d_usd (float | Unset):
        holder_rewards_30d (float | Unset):
        holder_rewards_30d_usd (float | Unset):
        holder_rewards_7d (float | Unset):
        holder_rewards_7d_usd (float | Unset):
        holder_rewards_all (float | Unset):
        holder_rewards_all_usd (float | Unset):
        holding_pnl_lamports (float | Unset): HoldingPnlLamports is the wallet's current unrealised PnL across
            all open positions, in lamports, off its board row. Nil when no held
            position carries a mark.
        holding_pnl_usd (float | Unset): HoldingPnlUsd, PnlDistributionUsd and PnlSparkline7dUsd are the USD
            twins of the three snapshot figures below (micro-USD, stamped at
            execution), and TraderUsd carries the twin of every windowed money
            figure on the row.
        id (str | Unset):
        label (str | Unset): Label/LabelType identify a known wallet (CEX/fee/KOL/...) from the
            known_addresses registry; empty when the wallet isn't labelled.
        label_type (str | Unset):
        landed_txs_1d (int | Unset):
        landed_txs_30d (int | Unset):
        landed_txs_7d (int | Unset):
        landed_txs_all (int | Unset):
        last_active_timestamp (int | Unset):
        median_buy_count_per_token (float | Unset):
        median_first_buy_reactivity (float | Unset):
        median_holding_time (float | Unset):
        median_realized_profit_1d (float | Unset):
        median_realized_profit_1d_usd (float | Unset):
        median_realized_profit_30d (float | Unset):
        median_realized_profit_30d_usd (float | Unset):
        median_realized_profit_7d (float | Unset):
        median_realized_profit_7d_usd (float | Unset):
        median_realized_profit_all (float | Unset):
        median_realized_profit_all_usd (float | Unset):
        median_sell_count_per_token (float | Unset):
        net_profit_1d (float | Unset):
        net_profit_1d_usd (float | Unset):
        net_profit_30d (float | Unset):
        net_profit_30d_usd (float | Unset):
        net_profit_7d (float | Unset): Net-of-costs figures — see trader.Trader for the definitions.
        net_profit_7d_usd (float | Unset):
        net_profit_all (float | Unset):
        net_profit_all_usd (float | Unset):
        oldest_trade_at (int | Unset):
        periods (list[PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow] | Unset): Periods is one row per
            canonical window (1d, 7d, 30d, all) off the
            wallet's board row. Drives the period stats panel on the
            trader-detail page.
        pnl_distribution (list[int] | Unset): PnlDistribution is the 5-bucket realised-PnL distribution for
            the request window: [<-50%, -50–0%, 0–2×, 2–5×, >5×]. Nil when
            the snapshot wasn't inlined.
        pnl_distribution_usd (list[int] | Unset):
        pnl_distributions (list[PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow] | Unset): PnlDistributions
            is one 5-bucket realised-PnL distribution row per
            canonical window (1d, 7d, 30d, all), windowed for real — unlike the
            list path's snapshot-folded PnlDistribution above, which is the
            leaderboard's all-time buckets. Drives the trader-detail "PnL
            distribution" chips and their window toggle.
        pnl_sparkline_7d (list[float] | Unset): PnlSparkline7d is the 7-day realised-PnL series, oldest first,
            expressed in lamports per day on the wire (the FormattedSol
            contract). Nil when the snapshot wasn't inlined.
        pnl_sparkline_7d_usd (list[float] | Unset):
        realized_profit (float | Unset):
        realized_profit_1d (float | Unset): 1-day window. Same measures and derivations as the 7d/30d blocks,
            hydrated per page instead of read off the leaderboard — DISPLAY-only,
            so neither `sort` nor an `f=` clause can address these.
        realized_profit_1d_usd (float | Unset):
        realized_profit_30d (float | Unset):
        realized_profit_30d_usd (float | Unset):
        realized_profit_7d (float | Unset):
        realized_profit_7d_usd (float | Unset):
        realized_profit_all_usd (float | Unset):
        realized_profit_pnl_30d (float | Unset):
        realized_profit_pnl_7d (float | Unset):
        rewards_total_1d (float | Unset):
        rewards_total_1d_usd (float | Unset):
        rewards_total_30d (float | Unset):
        rewards_total_30d_usd (float | Unset):
        rewards_total_7d (float | Unset):
        rewards_total_7d_usd (float | Unset):
        rewards_total_all (float | Unset):
        rewards_total_all_usd (float | Unset):
        roi_1d (float | Unset):
        roi_1d_usd (float | Unset):
        roi_30d_usd (float | Unset):
        roi_7d_usd (float | Unset):
        roi_all (float | Unset): Lifetime window, also DISPLAY-only; the gross figure is
            RealizedProfit. No lifetime failure record is served: the failed-tx
            planes are TTL-bounded to three months while the landed side is not,
            so a lifetime success or spam rate would be structurally flattering.
        roi_all_usd (float | Unset):
        sell_1d (int | Unset):
        sell_30d (int | Unset):
        sell_7d (int | Unset):
        sell_all (int | Unset):
        sol_balance (float | Unset):
        sold_gt_bought_sells_1d (int | Unset):
        sold_gt_bought_sells_30d (int | Unset):
        sold_gt_bought_sells_7d (int | Unset):
        sold_gt_bought_sells_all (int | Unset):
        spam_rate_1d (float | Unset):
        spam_rate_30d (float | Unset):
        spam_rate_7d (float | Unset):
        success_rate_1d (float | Unset):
        success_rate_30d (float | Unset):
        success_rate_7d (float | Unset):
        tags (list[str] | Unset):
        token_num_1d (int | Unset):
        token_num_30d (int | Unset):
        token_num_7d (int | Unset):
        token_num_all (int | Unset):
        tokens_created (int | Unset): TokensCreated / TokensGraduated are the wallet's lifetime
            creator-token counts (distinct mints created, and the subset that
            graduated). Inlined from the folded snapshot; nil when the snapshot
            wasn't inlined. Mirror the creator_tokens_* leaderboard filters.
        tokens_graduated (int | Unset):
        total_costs_1d (float | Unset):
        total_costs_1d_usd (float | Unset):
        total_costs_30d (float | Unset):
        total_costs_30d_usd (float | Unset):
        total_costs_7d (float | Unset):
        total_costs_7d_usd (float | Unset):
        total_costs_all (float | Unset):
        total_costs_all_usd (float | Unset):
        total_profit_30d (float | Unset):
        total_profit_7d (float | Unset):
        total_profit_pnl_30d (float | Unset):
        total_profit_pnl_7d (float | Unset):
        updated_at (str | Unset):
        wallet_address (str | Unset):
        winrate_1d (float | Unset):
        winrate_1d_usd (float | Unset):
        winrate_30d (float | Unset):
        winrate_30d_usd (float | Unset):
        winrate_7d (float | Unset):
        winrate_7d_usd (float | Unset):
        winrate_all (float | Unset):
        winrate_all_usd (float | Unset):
    """

    arb_tx_ratio_1d: float | Unset = UNSET
    arb_tx_ratio_30d: float | Unset = UNSET
    arb_tx_ratio_7d: float | Unset = UNSET
    arb_tx_ratio_all: float | Unset = UNSET
    avg_buy_count_per_token: float | Unset = UNSET
    avg_first_buy_reactivity: float | Unset = UNSET
    avg_holding_time: float | Unset = UNSET
    avg_realized_profit_1d: float | Unset = UNSET
    avg_realized_profit_1d_usd: float | Unset = UNSET
    avg_realized_profit_30d: float | Unset = UNSET
    avg_realized_profit_30d_usd: float | Unset = UNSET
    avg_realized_profit_7d: float | Unset = UNSET
    avg_realized_profit_7d_usd: float | Unset = UNSET
    avg_realized_profit_all: float | Unset = UNSET
    avg_realized_profit_all_usd: float | Unset = UNSET
    avg_sell_count_per_token: float | Unset = UNSET
    behavioral_1d: PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset = (
        UNSET
    )
    behavioral_30d: (
        PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
    ) = UNSET
    behavioral_7d: PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset = (
        UNSET
    )
    behavioral_all: (
        PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
    ) = UNSET
    buy_1d: int | Unset = UNSET
    buy_30d: int | Unset = UNSET
    buy_7d: int | Unset = UNSET
    buy_all: int | Unset = UNSET
    buy_sell_ratio_1d: float | Unset = UNSET
    buy_sell_ratio_30d: float | Unset = UNSET
    buy_sell_ratio_7d: float | Unset = UNSET
    buy_sell_ratio_all: float | Unset = UNSET
    cashback_1d: float | Unset = UNSET
    cashback_1d_usd: float | Unset = UNSET
    cashback_30d: float | Unset = UNSET
    cashback_30d_usd: float | Unset = UNSET
    cashback_7d: float | Unset = UNSET
    cashback_7d_usd: float | Unset = UNSET
    cashback_all: float | Unset = UNSET
    cashback_all_usd: float | Unset = UNSET
    cashback_claim_count_1d: int | Unset = UNSET
    cashback_claim_count_30d: int | Unset = UNSET
    cashback_claim_count_7d: int | Unset = UNSET
    cashback_claim_count_all: int | Unset = UNSET
    cashback_claimed_1d: float | Unset = UNSET
    cashback_claimed_1d_usd: float | Unset = UNSET
    cashback_claimed_30d: float | Unset = UNSET
    cashback_claimed_30d_usd: float | Unset = UNSET
    cashback_claimed_7d: float | Unset = UNSET
    cashback_claimed_7d_usd: float | Unset = UNSET
    cashback_claimed_all: float | Unset = UNSET
    cashback_claimed_all_usd: float | Unset = UNSET
    cashback_share_1d: float | Unset = UNSET
    cashback_share_30d: float | Unset = UNSET
    cashback_share_7d: float | Unset = UNSET
    cashback_share_all: float | Unset = UNSET
    chain: str | Unset = UNSET
    created_at: str | Unset = UNSET
    didnt_buy_sells_1d: int | Unset = UNSET
    didnt_buy_sells_30d: int | Unset = UNSET
    didnt_buy_sells_7d: int | Unset = UNSET
    didnt_buy_sells_all: int | Unset = UNSET
    failed_txs_1d: int | Unset = UNSET
    failed_txs_30d: int | Unset = UNSET
    failed_txs_7d: int | Unset = UNSET
    failed_txs_all: int | Unset = UNSET
    holder_reward_payouts_1d: int | Unset = UNSET
    holder_reward_payouts_30d: int | Unset = UNSET
    holder_reward_payouts_7d: int | Unset = UNSET
    holder_reward_payouts_all: int | Unset = UNSET
    holder_rewards_1d: float | Unset = UNSET
    holder_rewards_1d_usd: float | Unset = UNSET
    holder_rewards_30d: float | Unset = UNSET
    holder_rewards_30d_usd: float | Unset = UNSET
    holder_rewards_7d: float | Unset = UNSET
    holder_rewards_7d_usd: float | Unset = UNSET
    holder_rewards_all: float | Unset = UNSET
    holder_rewards_all_usd: float | Unset = UNSET
    holding_pnl_lamports: float | Unset = UNSET
    holding_pnl_usd: float | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    label_type: str | Unset = UNSET
    landed_txs_1d: int | Unset = UNSET
    landed_txs_30d: int | Unset = UNSET
    landed_txs_7d: int | Unset = UNSET
    landed_txs_all: int | Unset = UNSET
    last_active_timestamp: int | Unset = UNSET
    median_buy_count_per_token: float | Unset = UNSET
    median_first_buy_reactivity: float | Unset = UNSET
    median_holding_time: float | Unset = UNSET
    median_realized_profit_1d: float | Unset = UNSET
    median_realized_profit_1d_usd: float | Unset = UNSET
    median_realized_profit_30d: float | Unset = UNSET
    median_realized_profit_30d_usd: float | Unset = UNSET
    median_realized_profit_7d: float | Unset = UNSET
    median_realized_profit_7d_usd: float | Unset = UNSET
    median_realized_profit_all: float | Unset = UNSET
    median_realized_profit_all_usd: float | Unset = UNSET
    median_sell_count_per_token: float | Unset = UNSET
    net_profit_1d: float | Unset = UNSET
    net_profit_1d_usd: float | Unset = UNSET
    net_profit_30d: float | Unset = UNSET
    net_profit_30d_usd: float | Unset = UNSET
    net_profit_7d: float | Unset = UNSET
    net_profit_7d_usd: float | Unset = UNSET
    net_profit_all: float | Unset = UNSET
    net_profit_all_usd: float | Unset = UNSET
    oldest_trade_at: int | Unset = UNSET
    periods: list[PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow] | Unset = (
        UNSET
    )
    pnl_distribution: list[int] | Unset = UNSET
    pnl_distribution_usd: list[int] | Unset = UNSET
    pnl_distributions: (
        list[PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow] | Unset
    ) = UNSET
    pnl_sparkline_7d: list[float] | Unset = UNSET
    pnl_sparkline_7d_usd: list[float] | Unset = UNSET
    realized_profit: float | Unset = UNSET
    realized_profit_1d: float | Unset = UNSET
    realized_profit_1d_usd: float | Unset = UNSET
    realized_profit_30d: float | Unset = UNSET
    realized_profit_30d_usd: float | Unset = UNSET
    realized_profit_7d: float | Unset = UNSET
    realized_profit_7d_usd: float | Unset = UNSET
    realized_profit_all_usd: float | Unset = UNSET
    realized_profit_pnl_30d: float | Unset = UNSET
    realized_profit_pnl_7d: float | Unset = UNSET
    rewards_total_1d: float | Unset = UNSET
    rewards_total_1d_usd: float | Unset = UNSET
    rewards_total_30d: float | Unset = UNSET
    rewards_total_30d_usd: float | Unset = UNSET
    rewards_total_7d: float | Unset = UNSET
    rewards_total_7d_usd: float | Unset = UNSET
    rewards_total_all: float | Unset = UNSET
    rewards_total_all_usd: float | Unset = UNSET
    roi_1d: float | Unset = UNSET
    roi_1d_usd: float | Unset = UNSET
    roi_30d_usd: float | Unset = UNSET
    roi_7d_usd: float | Unset = UNSET
    roi_all: float | Unset = UNSET
    roi_all_usd: float | Unset = UNSET
    sell_1d: int | Unset = UNSET
    sell_30d: int | Unset = UNSET
    sell_7d: int | Unset = UNSET
    sell_all: int | Unset = UNSET
    sol_balance: float | Unset = UNSET
    sold_gt_bought_sells_1d: int | Unset = UNSET
    sold_gt_bought_sells_30d: int | Unset = UNSET
    sold_gt_bought_sells_7d: int | Unset = UNSET
    sold_gt_bought_sells_all: int | Unset = UNSET
    spam_rate_1d: float | Unset = UNSET
    spam_rate_30d: float | Unset = UNSET
    spam_rate_7d: float | Unset = UNSET
    success_rate_1d: float | Unset = UNSET
    success_rate_30d: float | Unset = UNSET
    success_rate_7d: float | Unset = UNSET
    tags: list[str] | Unset = UNSET
    token_num_1d: int | Unset = UNSET
    token_num_30d: int | Unset = UNSET
    token_num_7d: int | Unset = UNSET
    token_num_all: int | Unset = UNSET
    tokens_created: int | Unset = UNSET
    tokens_graduated: int | Unset = UNSET
    total_costs_1d: float | Unset = UNSET
    total_costs_1d_usd: float | Unset = UNSET
    total_costs_30d: float | Unset = UNSET
    total_costs_30d_usd: float | Unset = UNSET
    total_costs_7d: float | Unset = UNSET
    total_costs_7d_usd: float | Unset = UNSET
    total_costs_all: float | Unset = UNSET
    total_costs_all_usd: float | Unset = UNSET
    total_profit_30d: float | Unset = UNSET
    total_profit_7d: float | Unset = UNSET
    total_profit_pnl_30d: float | Unset = UNSET
    total_profit_pnl_7d: float | Unset = UNSET
    updated_at: str | Unset = UNSET
    wallet_address: str | Unset = UNSET
    winrate_1d: float | Unset = UNSET
    winrate_1d_usd: float | Unset = UNSET
    winrate_30d: float | Unset = UNSET
    winrate_30d_usd: float | Unset = UNSET
    winrate_7d: float | Unset = UNSET
    winrate_7d_usd: float | Unset = UNSET
    winrate_all: float | Unset = UNSET
    winrate_all_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_tx_ratio_1d = self.arb_tx_ratio_1d

        arb_tx_ratio_30d = self.arb_tx_ratio_30d

        arb_tx_ratio_7d = self.arb_tx_ratio_7d

        arb_tx_ratio_all = self.arb_tx_ratio_all

        avg_buy_count_per_token = self.avg_buy_count_per_token

        avg_first_buy_reactivity = self.avg_first_buy_reactivity

        avg_holding_time = self.avg_holding_time

        avg_realized_profit_1d = self.avg_realized_profit_1d

        avg_realized_profit_1d_usd = self.avg_realized_profit_1d_usd

        avg_realized_profit_30d = self.avg_realized_profit_30d

        avg_realized_profit_30d_usd = self.avg_realized_profit_30d_usd

        avg_realized_profit_7d = self.avg_realized_profit_7d

        avg_realized_profit_7d_usd = self.avg_realized_profit_7d_usd

        avg_realized_profit_all = self.avg_realized_profit_all

        avg_realized_profit_all_usd = self.avg_realized_profit_all_usd

        avg_sell_count_per_token = self.avg_sell_count_per_token

        behavioral_1d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_1d, Unset):
            behavioral_1d = self.behavioral_1d.to_dict()

        behavioral_30d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_30d, Unset):
            behavioral_30d = self.behavioral_30d.to_dict()

        behavioral_7d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_7d, Unset):
            behavioral_7d = self.behavioral_7d.to_dict()

        behavioral_all: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_all, Unset):
            behavioral_all = self.behavioral_all.to_dict()

        buy_1d = self.buy_1d

        buy_30d = self.buy_30d

        buy_7d = self.buy_7d

        buy_all = self.buy_all

        buy_sell_ratio_1d = self.buy_sell_ratio_1d

        buy_sell_ratio_30d = self.buy_sell_ratio_30d

        buy_sell_ratio_7d = self.buy_sell_ratio_7d

        buy_sell_ratio_all = self.buy_sell_ratio_all

        cashback_1d = self.cashback_1d

        cashback_1d_usd = self.cashback_1d_usd

        cashback_30d = self.cashback_30d

        cashback_30d_usd = self.cashback_30d_usd

        cashback_7d = self.cashback_7d

        cashback_7d_usd = self.cashback_7d_usd

        cashback_all = self.cashback_all

        cashback_all_usd = self.cashback_all_usd

        cashback_claim_count_1d = self.cashback_claim_count_1d

        cashback_claim_count_30d = self.cashback_claim_count_30d

        cashback_claim_count_7d = self.cashback_claim_count_7d

        cashback_claim_count_all = self.cashback_claim_count_all

        cashback_claimed_1d = self.cashback_claimed_1d

        cashback_claimed_1d_usd = self.cashback_claimed_1d_usd

        cashback_claimed_30d = self.cashback_claimed_30d

        cashback_claimed_30d_usd = self.cashback_claimed_30d_usd

        cashback_claimed_7d = self.cashback_claimed_7d

        cashback_claimed_7d_usd = self.cashback_claimed_7d_usd

        cashback_claimed_all = self.cashback_claimed_all

        cashback_claimed_all_usd = self.cashback_claimed_all_usd

        cashback_share_1d = self.cashback_share_1d

        cashback_share_30d = self.cashback_share_30d

        cashback_share_7d = self.cashback_share_7d

        cashback_share_all = self.cashback_share_all

        chain = self.chain

        created_at = self.created_at

        didnt_buy_sells_1d = self.didnt_buy_sells_1d

        didnt_buy_sells_30d = self.didnt_buy_sells_30d

        didnt_buy_sells_7d = self.didnt_buy_sells_7d

        didnt_buy_sells_all = self.didnt_buy_sells_all

        failed_txs_1d = self.failed_txs_1d

        failed_txs_30d = self.failed_txs_30d

        failed_txs_7d = self.failed_txs_7d

        failed_txs_all = self.failed_txs_all

        holder_reward_payouts_1d = self.holder_reward_payouts_1d

        holder_reward_payouts_30d = self.holder_reward_payouts_30d

        holder_reward_payouts_7d = self.holder_reward_payouts_7d

        holder_reward_payouts_all = self.holder_reward_payouts_all

        holder_rewards_1d = self.holder_rewards_1d

        holder_rewards_1d_usd = self.holder_rewards_1d_usd

        holder_rewards_30d = self.holder_rewards_30d

        holder_rewards_30d_usd = self.holder_rewards_30d_usd

        holder_rewards_7d = self.holder_rewards_7d

        holder_rewards_7d_usd = self.holder_rewards_7d_usd

        holder_rewards_all = self.holder_rewards_all

        holder_rewards_all_usd = self.holder_rewards_all_usd

        holding_pnl_lamports = self.holding_pnl_lamports

        holding_pnl_usd = self.holding_pnl_usd

        id = self.id

        label = self.label

        label_type = self.label_type

        landed_txs_1d = self.landed_txs_1d

        landed_txs_30d = self.landed_txs_30d

        landed_txs_7d = self.landed_txs_7d

        landed_txs_all = self.landed_txs_all

        last_active_timestamp = self.last_active_timestamp

        median_buy_count_per_token = self.median_buy_count_per_token

        median_first_buy_reactivity = self.median_first_buy_reactivity

        median_holding_time = self.median_holding_time

        median_realized_profit_1d = self.median_realized_profit_1d

        median_realized_profit_1d_usd = self.median_realized_profit_1d_usd

        median_realized_profit_30d = self.median_realized_profit_30d

        median_realized_profit_30d_usd = self.median_realized_profit_30d_usd

        median_realized_profit_7d = self.median_realized_profit_7d

        median_realized_profit_7d_usd = self.median_realized_profit_7d_usd

        median_realized_profit_all = self.median_realized_profit_all

        median_realized_profit_all_usd = self.median_realized_profit_all_usd

        median_sell_count_per_token = self.median_sell_count_per_token

        net_profit_1d = self.net_profit_1d

        net_profit_1d_usd = self.net_profit_1d_usd

        net_profit_30d = self.net_profit_30d

        net_profit_30d_usd = self.net_profit_30d_usd

        net_profit_7d = self.net_profit_7d

        net_profit_7d_usd = self.net_profit_7d_usd

        net_profit_all = self.net_profit_all

        net_profit_all_usd = self.net_profit_all_usd

        oldest_trade_at = self.oldest_trade_at

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        pnl_distribution: list[int] | Unset = UNSET
        if not isinstance(self.pnl_distribution, Unset):
            pnl_distribution = self.pnl_distribution

        pnl_distribution_usd: list[int] | Unset = UNSET
        if not isinstance(self.pnl_distribution_usd, Unset):
            pnl_distribution_usd = self.pnl_distribution_usd

        pnl_distributions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pnl_distributions, Unset):
            pnl_distributions = []
            for pnl_distributions_item_data in self.pnl_distributions:
                pnl_distributions_item = pnl_distributions_item_data.to_dict()
                pnl_distributions.append(pnl_distributions_item)

        pnl_sparkline_7d: list[float] | Unset = UNSET
        if not isinstance(self.pnl_sparkline_7d, Unset):
            pnl_sparkline_7d = self.pnl_sparkline_7d

        pnl_sparkline_7d_usd: list[float] | Unset = UNSET
        if not isinstance(self.pnl_sparkline_7d_usd, Unset):
            pnl_sparkline_7d_usd = self.pnl_sparkline_7d_usd

        realized_profit = self.realized_profit

        realized_profit_1d = self.realized_profit_1d

        realized_profit_1d_usd = self.realized_profit_1d_usd

        realized_profit_30d = self.realized_profit_30d

        realized_profit_30d_usd = self.realized_profit_30d_usd

        realized_profit_7d = self.realized_profit_7d

        realized_profit_7d_usd = self.realized_profit_7d_usd

        realized_profit_all_usd = self.realized_profit_all_usd

        realized_profit_pnl_30d = self.realized_profit_pnl_30d

        realized_profit_pnl_7d = self.realized_profit_pnl_7d

        rewards_total_1d = self.rewards_total_1d

        rewards_total_1d_usd = self.rewards_total_1d_usd

        rewards_total_30d = self.rewards_total_30d

        rewards_total_30d_usd = self.rewards_total_30d_usd

        rewards_total_7d = self.rewards_total_7d

        rewards_total_7d_usd = self.rewards_total_7d_usd

        rewards_total_all = self.rewards_total_all

        rewards_total_all_usd = self.rewards_total_all_usd

        roi_1d = self.roi_1d

        roi_1d_usd = self.roi_1d_usd

        roi_30d_usd = self.roi_30d_usd

        roi_7d_usd = self.roi_7d_usd

        roi_all = self.roi_all

        roi_all_usd = self.roi_all_usd

        sell_1d = self.sell_1d

        sell_30d = self.sell_30d

        sell_7d = self.sell_7d

        sell_all = self.sell_all

        sol_balance = self.sol_balance

        sold_gt_bought_sells_1d = self.sold_gt_bought_sells_1d

        sold_gt_bought_sells_30d = self.sold_gt_bought_sells_30d

        sold_gt_bought_sells_7d = self.sold_gt_bought_sells_7d

        sold_gt_bought_sells_all = self.sold_gt_bought_sells_all

        spam_rate_1d = self.spam_rate_1d

        spam_rate_30d = self.spam_rate_30d

        spam_rate_7d = self.spam_rate_7d

        success_rate_1d = self.success_rate_1d

        success_rate_30d = self.success_rate_30d

        success_rate_7d = self.success_rate_7d

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        token_num_1d = self.token_num_1d

        token_num_30d = self.token_num_30d

        token_num_7d = self.token_num_7d

        token_num_all = self.token_num_all

        tokens_created = self.tokens_created

        tokens_graduated = self.tokens_graduated

        total_costs_1d = self.total_costs_1d

        total_costs_1d_usd = self.total_costs_1d_usd

        total_costs_30d = self.total_costs_30d

        total_costs_30d_usd = self.total_costs_30d_usd

        total_costs_7d = self.total_costs_7d

        total_costs_7d_usd = self.total_costs_7d_usd

        total_costs_all = self.total_costs_all

        total_costs_all_usd = self.total_costs_all_usd

        total_profit_30d = self.total_profit_30d

        total_profit_7d = self.total_profit_7d

        total_profit_pnl_30d = self.total_profit_pnl_30d

        total_profit_pnl_7d = self.total_profit_pnl_7d

        updated_at = self.updated_at

        wallet_address = self.wallet_address

        winrate_1d = self.winrate_1d

        winrate_1d_usd = self.winrate_1d_usd

        winrate_30d = self.winrate_30d

        winrate_30d_usd = self.winrate_30d_usd

        winrate_7d = self.winrate_7d

        winrate_7d_usd = self.winrate_7d_usd

        winrate_all = self.winrate_all

        winrate_all_usd = self.winrate_all_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_tx_ratio_1d is not UNSET:
            field_dict["arb_tx_ratio_1d"] = arb_tx_ratio_1d
        if arb_tx_ratio_30d is not UNSET:
            field_dict["arb_tx_ratio_30d"] = arb_tx_ratio_30d
        if arb_tx_ratio_7d is not UNSET:
            field_dict["arb_tx_ratio_7d"] = arb_tx_ratio_7d
        if arb_tx_ratio_all is not UNSET:
            field_dict["arb_tx_ratio_all"] = arb_tx_ratio_all
        if avg_buy_count_per_token is not UNSET:
            field_dict["avg_buy_count_per_token"] = avg_buy_count_per_token
        if avg_first_buy_reactivity is not UNSET:
            field_dict["avg_first_buy_reactivity"] = avg_first_buy_reactivity
        if avg_holding_time is not UNSET:
            field_dict["avg_holding_time"] = avg_holding_time
        if avg_realized_profit_1d is not UNSET:
            field_dict["avg_realized_profit_1d"] = avg_realized_profit_1d
        if avg_realized_profit_1d_usd is not UNSET:
            field_dict["avg_realized_profit_1d_usd"] = avg_realized_profit_1d_usd
        if avg_realized_profit_30d is not UNSET:
            field_dict["avg_realized_profit_30d"] = avg_realized_profit_30d
        if avg_realized_profit_30d_usd is not UNSET:
            field_dict["avg_realized_profit_30d_usd"] = avg_realized_profit_30d_usd
        if avg_realized_profit_7d is not UNSET:
            field_dict["avg_realized_profit_7d"] = avg_realized_profit_7d
        if avg_realized_profit_7d_usd is not UNSET:
            field_dict["avg_realized_profit_7d_usd"] = avg_realized_profit_7d_usd
        if avg_realized_profit_all is not UNSET:
            field_dict["avg_realized_profit_all"] = avg_realized_profit_all
        if avg_realized_profit_all_usd is not UNSET:
            field_dict["avg_realized_profit_all_usd"] = avg_realized_profit_all_usd
        if avg_sell_count_per_token is not UNSET:
            field_dict["avg_sell_count_per_token"] = avg_sell_count_per_token
        if behavioral_1d is not UNSET:
            field_dict["behavioral_1d"] = behavioral_1d
        if behavioral_30d is not UNSET:
            field_dict["behavioral_30d"] = behavioral_30d
        if behavioral_7d is not UNSET:
            field_dict["behavioral_7d"] = behavioral_7d
        if behavioral_all is not UNSET:
            field_dict["behavioral_all"] = behavioral_all
        if buy_1d is not UNSET:
            field_dict["buy_1d"] = buy_1d
        if buy_30d is not UNSET:
            field_dict["buy_30d"] = buy_30d
        if buy_7d is not UNSET:
            field_dict["buy_7d"] = buy_7d
        if buy_all is not UNSET:
            field_dict["buy_all"] = buy_all
        if buy_sell_ratio_1d is not UNSET:
            field_dict["buy_sell_ratio_1d"] = buy_sell_ratio_1d
        if buy_sell_ratio_30d is not UNSET:
            field_dict["buy_sell_ratio_30d"] = buy_sell_ratio_30d
        if buy_sell_ratio_7d is not UNSET:
            field_dict["buy_sell_ratio_7d"] = buy_sell_ratio_7d
        if buy_sell_ratio_all is not UNSET:
            field_dict["buy_sell_ratio_all"] = buy_sell_ratio_all
        if cashback_1d is not UNSET:
            field_dict["cashback_1d"] = cashback_1d
        if cashback_1d_usd is not UNSET:
            field_dict["cashback_1d_usd"] = cashback_1d_usd
        if cashback_30d is not UNSET:
            field_dict["cashback_30d"] = cashback_30d
        if cashback_30d_usd is not UNSET:
            field_dict["cashback_30d_usd"] = cashback_30d_usd
        if cashback_7d is not UNSET:
            field_dict["cashback_7d"] = cashback_7d
        if cashback_7d_usd is not UNSET:
            field_dict["cashback_7d_usd"] = cashback_7d_usd
        if cashback_all is not UNSET:
            field_dict["cashback_all"] = cashback_all
        if cashback_all_usd is not UNSET:
            field_dict["cashback_all_usd"] = cashback_all_usd
        if cashback_claim_count_1d is not UNSET:
            field_dict["cashback_claim_count_1d"] = cashback_claim_count_1d
        if cashback_claim_count_30d is not UNSET:
            field_dict["cashback_claim_count_30d"] = cashback_claim_count_30d
        if cashback_claim_count_7d is not UNSET:
            field_dict["cashback_claim_count_7d"] = cashback_claim_count_7d
        if cashback_claim_count_all is not UNSET:
            field_dict["cashback_claim_count_all"] = cashback_claim_count_all
        if cashback_claimed_1d is not UNSET:
            field_dict["cashback_claimed_1d"] = cashback_claimed_1d
        if cashback_claimed_1d_usd is not UNSET:
            field_dict["cashback_claimed_1d_usd"] = cashback_claimed_1d_usd
        if cashback_claimed_30d is not UNSET:
            field_dict["cashback_claimed_30d"] = cashback_claimed_30d
        if cashback_claimed_30d_usd is not UNSET:
            field_dict["cashback_claimed_30d_usd"] = cashback_claimed_30d_usd
        if cashback_claimed_7d is not UNSET:
            field_dict["cashback_claimed_7d"] = cashback_claimed_7d
        if cashback_claimed_7d_usd is not UNSET:
            field_dict["cashback_claimed_7d_usd"] = cashback_claimed_7d_usd
        if cashback_claimed_all is not UNSET:
            field_dict["cashback_claimed_all"] = cashback_claimed_all
        if cashback_claimed_all_usd is not UNSET:
            field_dict["cashback_claimed_all_usd"] = cashback_claimed_all_usd
        if cashback_share_1d is not UNSET:
            field_dict["cashback_share_1d"] = cashback_share_1d
        if cashback_share_30d is not UNSET:
            field_dict["cashback_share_30d"] = cashback_share_30d
        if cashback_share_7d is not UNSET:
            field_dict["cashback_share_7d"] = cashback_share_7d
        if cashback_share_all is not UNSET:
            field_dict["cashback_share_all"] = cashback_share_all
        if chain is not UNSET:
            field_dict["chain"] = chain
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if didnt_buy_sells_1d is not UNSET:
            field_dict["didnt_buy_sells_1d"] = didnt_buy_sells_1d
        if didnt_buy_sells_30d is not UNSET:
            field_dict["didnt_buy_sells_30d"] = didnt_buy_sells_30d
        if didnt_buy_sells_7d is not UNSET:
            field_dict["didnt_buy_sells_7d"] = didnt_buy_sells_7d
        if didnt_buy_sells_all is not UNSET:
            field_dict["didnt_buy_sells_all"] = didnt_buy_sells_all
        if failed_txs_1d is not UNSET:
            field_dict["failed_txs_1d"] = failed_txs_1d
        if failed_txs_30d is not UNSET:
            field_dict["failed_txs_30d"] = failed_txs_30d
        if failed_txs_7d is not UNSET:
            field_dict["failed_txs_7d"] = failed_txs_7d
        if failed_txs_all is not UNSET:
            field_dict["failed_txs_all"] = failed_txs_all
        if holder_reward_payouts_1d is not UNSET:
            field_dict["holder_reward_payouts_1d"] = holder_reward_payouts_1d
        if holder_reward_payouts_30d is not UNSET:
            field_dict["holder_reward_payouts_30d"] = holder_reward_payouts_30d
        if holder_reward_payouts_7d is not UNSET:
            field_dict["holder_reward_payouts_7d"] = holder_reward_payouts_7d
        if holder_reward_payouts_all is not UNSET:
            field_dict["holder_reward_payouts_all"] = holder_reward_payouts_all
        if holder_rewards_1d is not UNSET:
            field_dict["holder_rewards_1d"] = holder_rewards_1d
        if holder_rewards_1d_usd is not UNSET:
            field_dict["holder_rewards_1d_usd"] = holder_rewards_1d_usd
        if holder_rewards_30d is not UNSET:
            field_dict["holder_rewards_30d"] = holder_rewards_30d
        if holder_rewards_30d_usd is not UNSET:
            field_dict["holder_rewards_30d_usd"] = holder_rewards_30d_usd
        if holder_rewards_7d is not UNSET:
            field_dict["holder_rewards_7d"] = holder_rewards_7d
        if holder_rewards_7d_usd is not UNSET:
            field_dict["holder_rewards_7d_usd"] = holder_rewards_7d_usd
        if holder_rewards_all is not UNSET:
            field_dict["holder_rewards_all"] = holder_rewards_all
        if holder_rewards_all_usd is not UNSET:
            field_dict["holder_rewards_all_usd"] = holder_rewards_all_usd
        if holding_pnl_lamports is not UNSET:
            field_dict["holding_pnl_lamports"] = holding_pnl_lamports
        if holding_pnl_usd is not UNSET:
            field_dict["holding_pnl_usd"] = holding_pnl_usd
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if landed_txs_1d is not UNSET:
            field_dict["landed_txs_1d"] = landed_txs_1d
        if landed_txs_30d is not UNSET:
            field_dict["landed_txs_30d"] = landed_txs_30d
        if landed_txs_7d is not UNSET:
            field_dict["landed_txs_7d"] = landed_txs_7d
        if landed_txs_all is not UNSET:
            field_dict["landed_txs_all"] = landed_txs_all
        if last_active_timestamp is not UNSET:
            field_dict["last_active_timestamp"] = last_active_timestamp
        if median_buy_count_per_token is not UNSET:
            field_dict["median_buy_count_per_token"] = median_buy_count_per_token
        if median_first_buy_reactivity is not UNSET:
            field_dict["median_first_buy_reactivity"] = median_first_buy_reactivity
        if median_holding_time is not UNSET:
            field_dict["median_holding_time"] = median_holding_time
        if median_realized_profit_1d is not UNSET:
            field_dict["median_realized_profit_1d"] = median_realized_profit_1d
        if median_realized_profit_1d_usd is not UNSET:
            field_dict["median_realized_profit_1d_usd"] = median_realized_profit_1d_usd
        if median_realized_profit_30d is not UNSET:
            field_dict["median_realized_profit_30d"] = median_realized_profit_30d
        if median_realized_profit_30d_usd is not UNSET:
            field_dict["median_realized_profit_30d_usd"] = (
                median_realized_profit_30d_usd
            )
        if median_realized_profit_7d is not UNSET:
            field_dict["median_realized_profit_7d"] = median_realized_profit_7d
        if median_realized_profit_7d_usd is not UNSET:
            field_dict["median_realized_profit_7d_usd"] = median_realized_profit_7d_usd
        if median_realized_profit_all is not UNSET:
            field_dict["median_realized_profit_all"] = median_realized_profit_all
        if median_realized_profit_all_usd is not UNSET:
            field_dict["median_realized_profit_all_usd"] = (
                median_realized_profit_all_usd
            )
        if median_sell_count_per_token is not UNSET:
            field_dict["median_sell_count_per_token"] = median_sell_count_per_token
        if net_profit_1d is not UNSET:
            field_dict["net_profit_1d"] = net_profit_1d
        if net_profit_1d_usd is not UNSET:
            field_dict["net_profit_1d_usd"] = net_profit_1d_usd
        if net_profit_30d is not UNSET:
            field_dict["net_profit_30d"] = net_profit_30d
        if net_profit_30d_usd is not UNSET:
            field_dict["net_profit_30d_usd"] = net_profit_30d_usd
        if net_profit_7d is not UNSET:
            field_dict["net_profit_7d"] = net_profit_7d
        if net_profit_7d_usd is not UNSET:
            field_dict["net_profit_7d_usd"] = net_profit_7d_usd
        if net_profit_all is not UNSET:
            field_dict["net_profit_all"] = net_profit_all
        if net_profit_all_usd is not UNSET:
            field_dict["net_profit_all_usd"] = net_profit_all_usd
        if oldest_trade_at is not UNSET:
            field_dict["oldest_trade_at"] = oldest_trade_at
        if periods is not UNSET:
            field_dict["periods"] = periods
        if pnl_distribution is not UNSET:
            field_dict["pnl_distribution"] = pnl_distribution
        if pnl_distribution_usd is not UNSET:
            field_dict["pnl_distribution_usd"] = pnl_distribution_usd
        if pnl_distributions is not UNSET:
            field_dict["pnl_distributions"] = pnl_distributions
        if pnl_sparkline_7d is not UNSET:
            field_dict["pnl_sparkline_7d"] = pnl_sparkline_7d
        if pnl_sparkline_7d_usd is not UNSET:
            field_dict["pnl_sparkline_7d_usd"] = pnl_sparkline_7d_usd
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if realized_profit_1d is not UNSET:
            field_dict["realized_profit_1d"] = realized_profit_1d
        if realized_profit_1d_usd is not UNSET:
            field_dict["realized_profit_1d_usd"] = realized_profit_1d_usd
        if realized_profit_30d is not UNSET:
            field_dict["realized_profit_30d"] = realized_profit_30d
        if realized_profit_30d_usd is not UNSET:
            field_dict["realized_profit_30d_usd"] = realized_profit_30d_usd
        if realized_profit_7d is not UNSET:
            field_dict["realized_profit_7d"] = realized_profit_7d
        if realized_profit_7d_usd is not UNSET:
            field_dict["realized_profit_7d_usd"] = realized_profit_7d_usd
        if realized_profit_all_usd is not UNSET:
            field_dict["realized_profit_all_usd"] = realized_profit_all_usd
        if realized_profit_pnl_30d is not UNSET:
            field_dict["realized_profit_pnl_30d"] = realized_profit_pnl_30d
        if realized_profit_pnl_7d is not UNSET:
            field_dict["realized_profit_pnl_7d"] = realized_profit_pnl_7d
        if rewards_total_1d is not UNSET:
            field_dict["rewards_total_1d"] = rewards_total_1d
        if rewards_total_1d_usd is not UNSET:
            field_dict["rewards_total_1d_usd"] = rewards_total_1d_usd
        if rewards_total_30d is not UNSET:
            field_dict["rewards_total_30d"] = rewards_total_30d
        if rewards_total_30d_usd is not UNSET:
            field_dict["rewards_total_30d_usd"] = rewards_total_30d_usd
        if rewards_total_7d is not UNSET:
            field_dict["rewards_total_7d"] = rewards_total_7d
        if rewards_total_7d_usd is not UNSET:
            field_dict["rewards_total_7d_usd"] = rewards_total_7d_usd
        if rewards_total_all is not UNSET:
            field_dict["rewards_total_all"] = rewards_total_all
        if rewards_total_all_usd is not UNSET:
            field_dict["rewards_total_all_usd"] = rewards_total_all_usd
        if roi_1d is not UNSET:
            field_dict["roi_1d"] = roi_1d
        if roi_1d_usd is not UNSET:
            field_dict["roi_1d_usd"] = roi_1d_usd
        if roi_30d_usd is not UNSET:
            field_dict["roi_30d_usd"] = roi_30d_usd
        if roi_7d_usd is not UNSET:
            field_dict["roi_7d_usd"] = roi_7d_usd
        if roi_all is not UNSET:
            field_dict["roi_all"] = roi_all
        if roi_all_usd is not UNSET:
            field_dict["roi_all_usd"] = roi_all_usd
        if sell_1d is not UNSET:
            field_dict["sell_1d"] = sell_1d
        if sell_30d is not UNSET:
            field_dict["sell_30d"] = sell_30d
        if sell_7d is not UNSET:
            field_dict["sell_7d"] = sell_7d
        if sell_all is not UNSET:
            field_dict["sell_all"] = sell_all
        if sol_balance is not UNSET:
            field_dict["sol_balance"] = sol_balance
        if sold_gt_bought_sells_1d is not UNSET:
            field_dict["sold_gt_bought_sells_1d"] = sold_gt_bought_sells_1d
        if sold_gt_bought_sells_30d is not UNSET:
            field_dict["sold_gt_bought_sells_30d"] = sold_gt_bought_sells_30d
        if sold_gt_bought_sells_7d is not UNSET:
            field_dict["sold_gt_bought_sells_7d"] = sold_gt_bought_sells_7d
        if sold_gt_bought_sells_all is not UNSET:
            field_dict["sold_gt_bought_sells_all"] = sold_gt_bought_sells_all
        if spam_rate_1d is not UNSET:
            field_dict["spam_rate_1d"] = spam_rate_1d
        if spam_rate_30d is not UNSET:
            field_dict["spam_rate_30d"] = spam_rate_30d
        if spam_rate_7d is not UNSET:
            field_dict["spam_rate_7d"] = spam_rate_7d
        if success_rate_1d is not UNSET:
            field_dict["success_rate_1d"] = success_rate_1d
        if success_rate_30d is not UNSET:
            field_dict["success_rate_30d"] = success_rate_30d
        if success_rate_7d is not UNSET:
            field_dict["success_rate_7d"] = success_rate_7d
        if tags is not UNSET:
            field_dict["tags"] = tags
        if token_num_1d is not UNSET:
            field_dict["token_num_1d"] = token_num_1d
        if token_num_30d is not UNSET:
            field_dict["token_num_30d"] = token_num_30d
        if token_num_7d is not UNSET:
            field_dict["token_num_7d"] = token_num_7d
        if token_num_all is not UNSET:
            field_dict["token_num_all"] = token_num_all
        if tokens_created is not UNSET:
            field_dict["tokens_created"] = tokens_created
        if tokens_graduated is not UNSET:
            field_dict["tokens_graduated"] = tokens_graduated
        if total_costs_1d is not UNSET:
            field_dict["total_costs_1d"] = total_costs_1d
        if total_costs_1d_usd is not UNSET:
            field_dict["total_costs_1d_usd"] = total_costs_1d_usd
        if total_costs_30d is not UNSET:
            field_dict["total_costs_30d"] = total_costs_30d
        if total_costs_30d_usd is not UNSET:
            field_dict["total_costs_30d_usd"] = total_costs_30d_usd
        if total_costs_7d is not UNSET:
            field_dict["total_costs_7d"] = total_costs_7d
        if total_costs_7d_usd is not UNSET:
            field_dict["total_costs_7d_usd"] = total_costs_7d_usd
        if total_costs_all is not UNSET:
            field_dict["total_costs_all"] = total_costs_all
        if total_costs_all_usd is not UNSET:
            field_dict["total_costs_all_usd"] = total_costs_all_usd
        if total_profit_30d is not UNSET:
            field_dict["total_profit_30d"] = total_profit_30d
        if total_profit_7d is not UNSET:
            field_dict["total_profit_7d"] = total_profit_7d
        if total_profit_pnl_30d is not UNSET:
            field_dict["total_profit_pnl_30d"] = total_profit_pnl_30d
        if total_profit_pnl_7d is not UNSET:
            field_dict["total_profit_pnl_7d"] = total_profit_pnl_7d
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if wallet_address is not UNSET:
            field_dict["wallet_address"] = wallet_address
        if winrate_1d is not UNSET:
            field_dict["winrate_1d"] = winrate_1d
        if winrate_1d_usd is not UNSET:
            field_dict["winrate_1d_usd"] = winrate_1d_usd
        if winrate_30d is not UNSET:
            field_dict["winrate_30d"] = winrate_30d
        if winrate_30d_usd is not UNSET:
            field_dict["winrate_30d_usd"] = winrate_30d_usd
        if winrate_7d is not UNSET:
            field_dict["winrate_7d"] = winrate_7d
        if winrate_7d_usd is not UNSET:
            field_dict["winrate_7d_usd"] = winrate_7d_usd
        if winrate_all is not UNSET:
            field_dict["winrate_all"] = winrate_all
        if winrate_all_usd is not UNSET:
            field_dict["winrate_all_usd"] = winrate_all_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_trader_behavioral_stats import (
            PulsightInternalCoreDomainAggregatorTraderBehavioralStats,
        )
        from ..models.pulsight_internal_core_domain_aggregator_trader_period_stats_row import (
            PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow,
        )
        from ..models.pulsight_internal_core_usecases_trader_trader_pnl_distribution_row import (
            PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow,
        )

        d = dict(src_dict)
        arb_tx_ratio_1d = d.pop("arb_tx_ratio_1d", UNSET)

        arb_tx_ratio_30d = d.pop("arb_tx_ratio_30d", UNSET)

        arb_tx_ratio_7d = d.pop("arb_tx_ratio_7d", UNSET)

        arb_tx_ratio_all = d.pop("arb_tx_ratio_all", UNSET)

        avg_buy_count_per_token = d.pop("avg_buy_count_per_token", UNSET)

        avg_first_buy_reactivity = d.pop("avg_first_buy_reactivity", UNSET)

        avg_holding_time = d.pop("avg_holding_time", UNSET)

        avg_realized_profit_1d = d.pop("avg_realized_profit_1d", UNSET)

        avg_realized_profit_1d_usd = d.pop("avg_realized_profit_1d_usd", UNSET)

        avg_realized_profit_30d = d.pop("avg_realized_profit_30d", UNSET)

        avg_realized_profit_30d_usd = d.pop("avg_realized_profit_30d_usd", UNSET)

        avg_realized_profit_7d = d.pop("avg_realized_profit_7d", UNSET)

        avg_realized_profit_7d_usd = d.pop("avg_realized_profit_7d_usd", UNSET)

        avg_realized_profit_all = d.pop("avg_realized_profit_all", UNSET)

        avg_realized_profit_all_usd = d.pop("avg_realized_profit_all_usd", UNSET)

        avg_sell_count_per_token = d.pop("avg_sell_count_per_token", UNSET)

        _behavioral_1d = d.pop("behavioral_1d", UNSET)
        behavioral_1d: PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
        if isinstance(_behavioral_1d, Unset):
            behavioral_1d = UNSET
        else:
            behavioral_1d = (
                PulsightInternalCoreDomainAggregatorTraderBehavioralStats.from_dict(
                    _behavioral_1d
                )
            )

        _behavioral_30d = d.pop("behavioral_30d", UNSET)
        behavioral_30d: (
            PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
        )
        if isinstance(_behavioral_30d, Unset):
            behavioral_30d = UNSET
        else:
            behavioral_30d = (
                PulsightInternalCoreDomainAggregatorTraderBehavioralStats.from_dict(
                    _behavioral_30d
                )
            )

        _behavioral_7d = d.pop("behavioral_7d", UNSET)
        behavioral_7d: PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
        if isinstance(_behavioral_7d, Unset):
            behavioral_7d = UNSET
        else:
            behavioral_7d = (
                PulsightInternalCoreDomainAggregatorTraderBehavioralStats.from_dict(
                    _behavioral_7d
                )
            )

        _behavioral_all = d.pop("behavioral_all", UNSET)
        behavioral_all: (
            PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
        )
        if isinstance(_behavioral_all, Unset):
            behavioral_all = UNSET
        else:
            behavioral_all = (
                PulsightInternalCoreDomainAggregatorTraderBehavioralStats.from_dict(
                    _behavioral_all
                )
            )

        buy_1d = d.pop("buy_1d", UNSET)

        buy_30d = d.pop("buy_30d", UNSET)

        buy_7d = d.pop("buy_7d", UNSET)

        buy_all = d.pop("buy_all", UNSET)

        buy_sell_ratio_1d = d.pop("buy_sell_ratio_1d", UNSET)

        buy_sell_ratio_30d = d.pop("buy_sell_ratio_30d", UNSET)

        buy_sell_ratio_7d = d.pop("buy_sell_ratio_7d", UNSET)

        buy_sell_ratio_all = d.pop("buy_sell_ratio_all", UNSET)

        cashback_1d = d.pop("cashback_1d", UNSET)

        cashback_1d_usd = d.pop("cashback_1d_usd", UNSET)

        cashback_30d = d.pop("cashback_30d", UNSET)

        cashback_30d_usd = d.pop("cashback_30d_usd", UNSET)

        cashback_7d = d.pop("cashback_7d", UNSET)

        cashback_7d_usd = d.pop("cashback_7d_usd", UNSET)

        cashback_all = d.pop("cashback_all", UNSET)

        cashback_all_usd = d.pop("cashback_all_usd", UNSET)

        cashback_claim_count_1d = d.pop("cashback_claim_count_1d", UNSET)

        cashback_claim_count_30d = d.pop("cashback_claim_count_30d", UNSET)

        cashback_claim_count_7d = d.pop("cashback_claim_count_7d", UNSET)

        cashback_claim_count_all = d.pop("cashback_claim_count_all", UNSET)

        cashback_claimed_1d = d.pop("cashback_claimed_1d", UNSET)

        cashback_claimed_1d_usd = d.pop("cashback_claimed_1d_usd", UNSET)

        cashback_claimed_30d = d.pop("cashback_claimed_30d", UNSET)

        cashback_claimed_30d_usd = d.pop("cashback_claimed_30d_usd", UNSET)

        cashback_claimed_7d = d.pop("cashback_claimed_7d", UNSET)

        cashback_claimed_7d_usd = d.pop("cashback_claimed_7d_usd", UNSET)

        cashback_claimed_all = d.pop("cashback_claimed_all", UNSET)

        cashback_claimed_all_usd = d.pop("cashback_claimed_all_usd", UNSET)

        cashback_share_1d = d.pop("cashback_share_1d", UNSET)

        cashback_share_30d = d.pop("cashback_share_30d", UNSET)

        cashback_share_7d = d.pop("cashback_share_7d", UNSET)

        cashback_share_all = d.pop("cashback_share_all", UNSET)

        chain = d.pop("chain", UNSET)

        created_at = d.pop("created_at", UNSET)

        didnt_buy_sells_1d = d.pop("didnt_buy_sells_1d", UNSET)

        didnt_buy_sells_30d = d.pop("didnt_buy_sells_30d", UNSET)

        didnt_buy_sells_7d = d.pop("didnt_buy_sells_7d", UNSET)

        didnt_buy_sells_all = d.pop("didnt_buy_sells_all", UNSET)

        failed_txs_1d = d.pop("failed_txs_1d", UNSET)

        failed_txs_30d = d.pop("failed_txs_30d", UNSET)

        failed_txs_7d = d.pop("failed_txs_7d", UNSET)

        failed_txs_all = d.pop("failed_txs_all", UNSET)

        holder_reward_payouts_1d = d.pop("holder_reward_payouts_1d", UNSET)

        holder_reward_payouts_30d = d.pop("holder_reward_payouts_30d", UNSET)

        holder_reward_payouts_7d = d.pop("holder_reward_payouts_7d", UNSET)

        holder_reward_payouts_all = d.pop("holder_reward_payouts_all", UNSET)

        holder_rewards_1d = d.pop("holder_rewards_1d", UNSET)

        holder_rewards_1d_usd = d.pop("holder_rewards_1d_usd", UNSET)

        holder_rewards_30d = d.pop("holder_rewards_30d", UNSET)

        holder_rewards_30d_usd = d.pop("holder_rewards_30d_usd", UNSET)

        holder_rewards_7d = d.pop("holder_rewards_7d", UNSET)

        holder_rewards_7d_usd = d.pop("holder_rewards_7d_usd", UNSET)

        holder_rewards_all = d.pop("holder_rewards_all", UNSET)

        holder_rewards_all_usd = d.pop("holder_rewards_all_usd", UNSET)

        holding_pnl_lamports = d.pop("holding_pnl_lamports", UNSET)

        holding_pnl_usd = d.pop("holding_pnl_usd", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        label_type = d.pop("label_type", UNSET)

        landed_txs_1d = d.pop("landed_txs_1d", UNSET)

        landed_txs_30d = d.pop("landed_txs_30d", UNSET)

        landed_txs_7d = d.pop("landed_txs_7d", UNSET)

        landed_txs_all = d.pop("landed_txs_all", UNSET)

        last_active_timestamp = d.pop("last_active_timestamp", UNSET)

        median_buy_count_per_token = d.pop("median_buy_count_per_token", UNSET)

        median_first_buy_reactivity = d.pop("median_first_buy_reactivity", UNSET)

        median_holding_time = d.pop("median_holding_time", UNSET)

        median_realized_profit_1d = d.pop("median_realized_profit_1d", UNSET)

        median_realized_profit_1d_usd = d.pop("median_realized_profit_1d_usd", UNSET)

        median_realized_profit_30d = d.pop("median_realized_profit_30d", UNSET)

        median_realized_profit_30d_usd = d.pop("median_realized_profit_30d_usd", UNSET)

        median_realized_profit_7d = d.pop("median_realized_profit_7d", UNSET)

        median_realized_profit_7d_usd = d.pop("median_realized_profit_7d_usd", UNSET)

        median_realized_profit_all = d.pop("median_realized_profit_all", UNSET)

        median_realized_profit_all_usd = d.pop("median_realized_profit_all_usd", UNSET)

        median_sell_count_per_token = d.pop("median_sell_count_per_token", UNSET)

        net_profit_1d = d.pop("net_profit_1d", UNSET)

        net_profit_1d_usd = d.pop("net_profit_1d_usd", UNSET)

        net_profit_30d = d.pop("net_profit_30d", UNSET)

        net_profit_30d_usd = d.pop("net_profit_30d_usd", UNSET)

        net_profit_7d = d.pop("net_profit_7d", UNSET)

        net_profit_7d_usd = d.pop("net_profit_7d_usd", UNSET)

        net_profit_all = d.pop("net_profit_all", UNSET)

        net_profit_all_usd = d.pop("net_profit_all_usd", UNSET)

        oldest_trade_at = d.pop("oldest_trade_at", UNSET)

        _periods = d.pop("periods", UNSET)
        periods: (
            list[PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow] | Unset
        ) = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = (
                    PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow.from_dict(
                        periods_item_data
                    )
                )

                periods.append(periods_item)

        pnl_distribution = cast(list[int], d.pop("pnl_distribution", UNSET))

        pnl_distribution_usd = cast(list[int], d.pop("pnl_distribution_usd", UNSET))

        _pnl_distributions = d.pop("pnl_distributions", UNSET)
        pnl_distributions: (
            list[PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow] | Unset
        ) = UNSET
        if _pnl_distributions is not UNSET:
            pnl_distributions = []
            for pnl_distributions_item_data in _pnl_distributions:
                pnl_distributions_item = PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow.from_dict(
                    pnl_distributions_item_data
                )

                pnl_distributions.append(pnl_distributions_item)

        pnl_sparkline_7d = cast(list[float], d.pop("pnl_sparkline_7d", UNSET))

        pnl_sparkline_7d_usd = cast(list[float], d.pop("pnl_sparkline_7d_usd", UNSET))

        realized_profit = d.pop("realized_profit", UNSET)

        realized_profit_1d = d.pop("realized_profit_1d", UNSET)

        realized_profit_1d_usd = d.pop("realized_profit_1d_usd", UNSET)

        realized_profit_30d = d.pop("realized_profit_30d", UNSET)

        realized_profit_30d_usd = d.pop("realized_profit_30d_usd", UNSET)

        realized_profit_7d = d.pop("realized_profit_7d", UNSET)

        realized_profit_7d_usd = d.pop("realized_profit_7d_usd", UNSET)

        realized_profit_all_usd = d.pop("realized_profit_all_usd", UNSET)

        realized_profit_pnl_30d = d.pop("realized_profit_pnl_30d", UNSET)

        realized_profit_pnl_7d = d.pop("realized_profit_pnl_7d", UNSET)

        rewards_total_1d = d.pop("rewards_total_1d", UNSET)

        rewards_total_1d_usd = d.pop("rewards_total_1d_usd", UNSET)

        rewards_total_30d = d.pop("rewards_total_30d", UNSET)

        rewards_total_30d_usd = d.pop("rewards_total_30d_usd", UNSET)

        rewards_total_7d = d.pop("rewards_total_7d", UNSET)

        rewards_total_7d_usd = d.pop("rewards_total_7d_usd", UNSET)

        rewards_total_all = d.pop("rewards_total_all", UNSET)

        rewards_total_all_usd = d.pop("rewards_total_all_usd", UNSET)

        roi_1d = d.pop("roi_1d", UNSET)

        roi_1d_usd = d.pop("roi_1d_usd", UNSET)

        roi_30d_usd = d.pop("roi_30d_usd", UNSET)

        roi_7d_usd = d.pop("roi_7d_usd", UNSET)

        roi_all = d.pop("roi_all", UNSET)

        roi_all_usd = d.pop("roi_all_usd", UNSET)

        sell_1d = d.pop("sell_1d", UNSET)

        sell_30d = d.pop("sell_30d", UNSET)

        sell_7d = d.pop("sell_7d", UNSET)

        sell_all = d.pop("sell_all", UNSET)

        sol_balance = d.pop("sol_balance", UNSET)

        sold_gt_bought_sells_1d = d.pop("sold_gt_bought_sells_1d", UNSET)

        sold_gt_bought_sells_30d = d.pop("sold_gt_bought_sells_30d", UNSET)

        sold_gt_bought_sells_7d = d.pop("sold_gt_bought_sells_7d", UNSET)

        sold_gt_bought_sells_all = d.pop("sold_gt_bought_sells_all", UNSET)

        spam_rate_1d = d.pop("spam_rate_1d", UNSET)

        spam_rate_30d = d.pop("spam_rate_30d", UNSET)

        spam_rate_7d = d.pop("spam_rate_7d", UNSET)

        success_rate_1d = d.pop("success_rate_1d", UNSET)

        success_rate_30d = d.pop("success_rate_30d", UNSET)

        success_rate_7d = d.pop("success_rate_7d", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_num_1d = d.pop("token_num_1d", UNSET)

        token_num_30d = d.pop("token_num_30d", UNSET)

        token_num_7d = d.pop("token_num_7d", UNSET)

        token_num_all = d.pop("token_num_all", UNSET)

        tokens_created = d.pop("tokens_created", UNSET)

        tokens_graduated = d.pop("tokens_graduated", UNSET)

        total_costs_1d = d.pop("total_costs_1d", UNSET)

        total_costs_1d_usd = d.pop("total_costs_1d_usd", UNSET)

        total_costs_30d = d.pop("total_costs_30d", UNSET)

        total_costs_30d_usd = d.pop("total_costs_30d_usd", UNSET)

        total_costs_7d = d.pop("total_costs_7d", UNSET)

        total_costs_7d_usd = d.pop("total_costs_7d_usd", UNSET)

        total_costs_all = d.pop("total_costs_all", UNSET)

        total_costs_all_usd = d.pop("total_costs_all_usd", UNSET)

        total_profit_30d = d.pop("total_profit_30d", UNSET)

        total_profit_7d = d.pop("total_profit_7d", UNSET)

        total_profit_pnl_30d = d.pop("total_profit_pnl_30d", UNSET)

        total_profit_pnl_7d = d.pop("total_profit_pnl_7d", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        wallet_address = d.pop("wallet_address", UNSET)

        winrate_1d = d.pop("winrate_1d", UNSET)

        winrate_1d_usd = d.pop("winrate_1d_usd", UNSET)

        winrate_30d = d.pop("winrate_30d", UNSET)

        winrate_30d_usd = d.pop("winrate_30d_usd", UNSET)

        winrate_7d = d.pop("winrate_7d", UNSET)

        winrate_7d_usd = d.pop("winrate_7d_usd", UNSET)

        winrate_all = d.pop("winrate_all", UNSET)

        winrate_all_usd = d.pop("winrate_all_usd", UNSET)

        pulsight_internal_core_usecases_trader_trader_list_item = cls(
            arb_tx_ratio_1d=arb_tx_ratio_1d,
            arb_tx_ratio_30d=arb_tx_ratio_30d,
            arb_tx_ratio_7d=arb_tx_ratio_7d,
            arb_tx_ratio_all=arb_tx_ratio_all,
            avg_buy_count_per_token=avg_buy_count_per_token,
            avg_first_buy_reactivity=avg_first_buy_reactivity,
            avg_holding_time=avg_holding_time,
            avg_realized_profit_1d=avg_realized_profit_1d,
            avg_realized_profit_1d_usd=avg_realized_profit_1d_usd,
            avg_realized_profit_30d=avg_realized_profit_30d,
            avg_realized_profit_30d_usd=avg_realized_profit_30d_usd,
            avg_realized_profit_7d=avg_realized_profit_7d,
            avg_realized_profit_7d_usd=avg_realized_profit_7d_usd,
            avg_realized_profit_all=avg_realized_profit_all,
            avg_realized_profit_all_usd=avg_realized_profit_all_usd,
            avg_sell_count_per_token=avg_sell_count_per_token,
            behavioral_1d=behavioral_1d,
            behavioral_30d=behavioral_30d,
            behavioral_7d=behavioral_7d,
            behavioral_all=behavioral_all,
            buy_1d=buy_1d,
            buy_30d=buy_30d,
            buy_7d=buy_7d,
            buy_all=buy_all,
            buy_sell_ratio_1d=buy_sell_ratio_1d,
            buy_sell_ratio_30d=buy_sell_ratio_30d,
            buy_sell_ratio_7d=buy_sell_ratio_7d,
            buy_sell_ratio_all=buy_sell_ratio_all,
            cashback_1d=cashback_1d,
            cashback_1d_usd=cashback_1d_usd,
            cashback_30d=cashback_30d,
            cashback_30d_usd=cashback_30d_usd,
            cashback_7d=cashback_7d,
            cashback_7d_usd=cashback_7d_usd,
            cashback_all=cashback_all,
            cashback_all_usd=cashback_all_usd,
            cashback_claim_count_1d=cashback_claim_count_1d,
            cashback_claim_count_30d=cashback_claim_count_30d,
            cashback_claim_count_7d=cashback_claim_count_7d,
            cashback_claim_count_all=cashback_claim_count_all,
            cashback_claimed_1d=cashback_claimed_1d,
            cashback_claimed_1d_usd=cashback_claimed_1d_usd,
            cashback_claimed_30d=cashback_claimed_30d,
            cashback_claimed_30d_usd=cashback_claimed_30d_usd,
            cashback_claimed_7d=cashback_claimed_7d,
            cashback_claimed_7d_usd=cashback_claimed_7d_usd,
            cashback_claimed_all=cashback_claimed_all,
            cashback_claimed_all_usd=cashback_claimed_all_usd,
            cashback_share_1d=cashback_share_1d,
            cashback_share_30d=cashback_share_30d,
            cashback_share_7d=cashback_share_7d,
            cashback_share_all=cashback_share_all,
            chain=chain,
            created_at=created_at,
            didnt_buy_sells_1d=didnt_buy_sells_1d,
            didnt_buy_sells_30d=didnt_buy_sells_30d,
            didnt_buy_sells_7d=didnt_buy_sells_7d,
            didnt_buy_sells_all=didnt_buy_sells_all,
            failed_txs_1d=failed_txs_1d,
            failed_txs_30d=failed_txs_30d,
            failed_txs_7d=failed_txs_7d,
            failed_txs_all=failed_txs_all,
            holder_reward_payouts_1d=holder_reward_payouts_1d,
            holder_reward_payouts_30d=holder_reward_payouts_30d,
            holder_reward_payouts_7d=holder_reward_payouts_7d,
            holder_reward_payouts_all=holder_reward_payouts_all,
            holder_rewards_1d=holder_rewards_1d,
            holder_rewards_1d_usd=holder_rewards_1d_usd,
            holder_rewards_30d=holder_rewards_30d,
            holder_rewards_30d_usd=holder_rewards_30d_usd,
            holder_rewards_7d=holder_rewards_7d,
            holder_rewards_7d_usd=holder_rewards_7d_usd,
            holder_rewards_all=holder_rewards_all,
            holder_rewards_all_usd=holder_rewards_all_usd,
            holding_pnl_lamports=holding_pnl_lamports,
            holding_pnl_usd=holding_pnl_usd,
            id=id,
            label=label,
            label_type=label_type,
            landed_txs_1d=landed_txs_1d,
            landed_txs_30d=landed_txs_30d,
            landed_txs_7d=landed_txs_7d,
            landed_txs_all=landed_txs_all,
            last_active_timestamp=last_active_timestamp,
            median_buy_count_per_token=median_buy_count_per_token,
            median_first_buy_reactivity=median_first_buy_reactivity,
            median_holding_time=median_holding_time,
            median_realized_profit_1d=median_realized_profit_1d,
            median_realized_profit_1d_usd=median_realized_profit_1d_usd,
            median_realized_profit_30d=median_realized_profit_30d,
            median_realized_profit_30d_usd=median_realized_profit_30d_usd,
            median_realized_profit_7d=median_realized_profit_7d,
            median_realized_profit_7d_usd=median_realized_profit_7d_usd,
            median_realized_profit_all=median_realized_profit_all,
            median_realized_profit_all_usd=median_realized_profit_all_usd,
            median_sell_count_per_token=median_sell_count_per_token,
            net_profit_1d=net_profit_1d,
            net_profit_1d_usd=net_profit_1d_usd,
            net_profit_30d=net_profit_30d,
            net_profit_30d_usd=net_profit_30d_usd,
            net_profit_7d=net_profit_7d,
            net_profit_7d_usd=net_profit_7d_usd,
            net_profit_all=net_profit_all,
            net_profit_all_usd=net_profit_all_usd,
            oldest_trade_at=oldest_trade_at,
            periods=periods,
            pnl_distribution=pnl_distribution,
            pnl_distribution_usd=pnl_distribution_usd,
            pnl_distributions=pnl_distributions,
            pnl_sparkline_7d=pnl_sparkline_7d,
            pnl_sparkline_7d_usd=pnl_sparkline_7d_usd,
            realized_profit=realized_profit,
            realized_profit_1d=realized_profit_1d,
            realized_profit_1d_usd=realized_profit_1d_usd,
            realized_profit_30d=realized_profit_30d,
            realized_profit_30d_usd=realized_profit_30d_usd,
            realized_profit_7d=realized_profit_7d,
            realized_profit_7d_usd=realized_profit_7d_usd,
            realized_profit_all_usd=realized_profit_all_usd,
            realized_profit_pnl_30d=realized_profit_pnl_30d,
            realized_profit_pnl_7d=realized_profit_pnl_7d,
            rewards_total_1d=rewards_total_1d,
            rewards_total_1d_usd=rewards_total_1d_usd,
            rewards_total_30d=rewards_total_30d,
            rewards_total_30d_usd=rewards_total_30d_usd,
            rewards_total_7d=rewards_total_7d,
            rewards_total_7d_usd=rewards_total_7d_usd,
            rewards_total_all=rewards_total_all,
            rewards_total_all_usd=rewards_total_all_usd,
            roi_1d=roi_1d,
            roi_1d_usd=roi_1d_usd,
            roi_30d_usd=roi_30d_usd,
            roi_7d_usd=roi_7d_usd,
            roi_all=roi_all,
            roi_all_usd=roi_all_usd,
            sell_1d=sell_1d,
            sell_30d=sell_30d,
            sell_7d=sell_7d,
            sell_all=sell_all,
            sol_balance=sol_balance,
            sold_gt_bought_sells_1d=sold_gt_bought_sells_1d,
            sold_gt_bought_sells_30d=sold_gt_bought_sells_30d,
            sold_gt_bought_sells_7d=sold_gt_bought_sells_7d,
            sold_gt_bought_sells_all=sold_gt_bought_sells_all,
            spam_rate_1d=spam_rate_1d,
            spam_rate_30d=spam_rate_30d,
            spam_rate_7d=spam_rate_7d,
            success_rate_1d=success_rate_1d,
            success_rate_30d=success_rate_30d,
            success_rate_7d=success_rate_7d,
            tags=tags,
            token_num_1d=token_num_1d,
            token_num_30d=token_num_30d,
            token_num_7d=token_num_7d,
            token_num_all=token_num_all,
            tokens_created=tokens_created,
            tokens_graduated=tokens_graduated,
            total_costs_1d=total_costs_1d,
            total_costs_1d_usd=total_costs_1d_usd,
            total_costs_30d=total_costs_30d,
            total_costs_30d_usd=total_costs_30d_usd,
            total_costs_7d=total_costs_7d,
            total_costs_7d_usd=total_costs_7d_usd,
            total_costs_all=total_costs_all,
            total_costs_all_usd=total_costs_all_usd,
            total_profit_30d=total_profit_30d,
            total_profit_7d=total_profit_7d,
            total_profit_pnl_30d=total_profit_pnl_30d,
            total_profit_pnl_7d=total_profit_pnl_7d,
            updated_at=updated_at,
            wallet_address=wallet_address,
            winrate_1d=winrate_1d,
            winrate_1d_usd=winrate_1d_usd,
            winrate_30d=winrate_30d,
            winrate_30d_usd=winrate_30d_usd,
            winrate_7d=winrate_7d,
            winrate_7d_usd=winrate_7d_usd,
            winrate_all=winrate_all,
            winrate_all_usd=winrate_all_usd,
        )

        pulsight_internal_core_usecases_trader_trader_list_item.additional_properties = d
        return pulsight_internal_core_usecases_trader_trader_list_item

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
