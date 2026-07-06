from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_trader_behavioral_stats import (
        PulsightInternalCoreDomainAggregatorTraderBehavioralStats,
    )
    from ..models.pulsight_internal_core_domain_aggregator_trader_period_stats_row import (
        PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow,
    )
    from ..models.pulsight_internal_core_usecases_trader_daily_profit_entry import (
        PulsightInternalCoreUsecasesTraderDailyProfitEntry,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderTraderListItem")


@_attrs_define
class PulsightInternalCoreUsecasesTraderTraderListItem:
    """
    Attributes:
        active_hours_count (int | Unset):
        arb_tx_ratio_30d (float | Unset):
        arb_tx_ratio_7d (float | Unset):
        avg_buy_count_per_token (float | Unset):
        avg_first_buy_reactivity (float | Unset):
        avg_holding_time (float | Unset):
        avg_realized_profit_30d (float | Unset):
        avg_realized_profit_7d (float | Unset):
        avg_sell_count_per_token (float | Unset):
        behavioral_30d (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        behavioral_7d (PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset):
        buy_30d (int | Unset):
        buy_7d (int | Unset):
        buy_sell_ratio_30d (float | Unset):
        buy_sell_ratio_7d (float | Unset):
        buy_size_cv (float | Unset):
        chain (str | Unset):
        created_at (str | Unset):
        daily_profit_30d (list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset):
        daily_profit_7d (list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset):
        didnt_buy_sells_30d (int | Unset):
        didnt_buy_sells_7d (int | Unset): Uncovered-sell counters (CA migration 000018): sells with no
            observed buy of the mint / sells exceeding the observed bought
            balance, scoped to the window.
        dust_tx_ratio (float | Unset):
        has_avatar (bool | Unset):
        holding_pnl_lamports (float | Unset): HoldingPnlLamports is the wallet's current unrealised PnL across
            all open positions, in lamports. Nil when CA has no live price
            quote for any of the held mints.
        id (str | Unset):
        is_favorite (bool | Unset):
        last_active_timestamp (int | Unset):
        median_buy_count_per_token (float | Unset):
        median_first_buy_reactivity (float | Unset):
        median_holding_time (float | Unset):
        median_realized_profit_30d (float | Unset):
        median_realized_profit_7d (float | Unset):
        median_sell_count_per_token (float | Unset):
        mm_score (int | Unset):
        name (str | Unset):
        oldest_trade_at (int | Unset):
        periods (list[PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow] | Unset): Periods is one row per
            canonical UTC-aligned window (1d, 7d, 30d,
            all) from CA's `trader_period_stats_for`. Drives the
            "Calendar-based UTC windows" panel on the trader-detail page.
        pnl_0x_2x_num_30d (int | Unset):
        pnl_0x_2x_num_7d (int | Unset):
        pnl_2x_5x_num_30d (int | Unset):
        pnl_2x_5x_num_7d (int | Unset):
        pnl_distribution (list[int] | Unset): PnlDistribution is the 5-bucket realised-PnL distribution for
            the request window: [<-50%, -50–0%, 0–2×, 2–5×, >5×]. Nil when
            the snapshot wasn't inlined.
        pnl_gt_5x_num_30d (int | Unset):
        pnl_gt_5x_num_7d (int | Unset):
        pnl_lt_nd5_num_30d (int | Unset):
        pnl_lt_nd5_num_7d (int | Unset):
        pnl_nd5_0x_num_30d (int | Unset):
        pnl_nd5_0x_num_7d (int | Unset):
        pnl_sparkline_7d (list[float] | Unset): PnlSparkline7d is the 7-day realised-PnL series, oldest first,
            expressed in lamports per day on the wire (matches CA's BIGINT
            storage and the FormattedSol contract elsewhere). Nil when the
            snapshot wasn't inlined.
        profit_per_trade (float | Unset):
        realized_profit (float | Unset):
        realized_profit_30d (float | Unset):
        realized_profit_7d (float | Unset):
        realized_profit_pnl_30d (float | Unset):
        realized_profit_pnl_7d (float | Unset):
        rebalancing_ratio (float | Unset):
        risk_level (str | Unset):
        risk_score (int | Unset):
        sell_30d (int | Unset):
        sell_7d (int | Unset):
        sol_balance (float | Unset):
        sold_gt_bought_sells_30d (int | Unset):
        sold_gt_bought_sells_7d (int | Unset):
        tags (list[str] | Unset):
        token_num_30d (int | Unset):
        token_num_7d (int | Unset):
        tokens_created (int | Unset): TokensCreated / TokensGraduated are the wallet's lifetime
            creator-token counts (distinct mints created, and the subset that
            graduated). Inlined from the folded snapshot; nil when the snapshot
            wasn't inlined. Mirror the creator_tokens_* leaderboard filters.
        tokens_graduated (int | Unset):
        total_profit (float | Unset):
        total_profit_30d (float | Unset):
        total_profit_7d (float | Unset):
        total_profit_pnl_30d (float | Unset):
        total_profit_pnl_7d (float | Unset):
        total_value (float | Unset):
        total_volume_usd (float | Unset):
        trade_interval_cv (float | Unset):
        trade_interval_mean (float | Unset):
        twitter_username (str | Unset):
        unrealized_profit (float | Unset):
        unrealized_profit_30d (float | Unset):
        unrealized_profit_7d (float | Unset):
        unrealized_profit_pnl_30d (float | Unset):
        unrealized_profit_pnl_7d (float | Unset):
        updated_at (str | Unset):
        wallet_address (str | Unset):
        winrate_30d (float | Unset):
        winrate_7d (float | Unset):
    """

    active_hours_count: int | Unset = UNSET
    arb_tx_ratio_30d: float | Unset = UNSET
    arb_tx_ratio_7d: float | Unset = UNSET
    avg_buy_count_per_token: float | Unset = UNSET
    avg_first_buy_reactivity: float | Unset = UNSET
    avg_holding_time: float | Unset = UNSET
    avg_realized_profit_30d: float | Unset = UNSET
    avg_realized_profit_7d: float | Unset = UNSET
    avg_sell_count_per_token: float | Unset = UNSET
    behavioral_30d: (
        PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset
    ) = UNSET
    behavioral_7d: PulsightInternalCoreDomainAggregatorTraderBehavioralStats | Unset = (
        UNSET
    )
    buy_30d: int | Unset = UNSET
    buy_7d: int | Unset = UNSET
    buy_sell_ratio_30d: float | Unset = UNSET
    buy_sell_ratio_7d: float | Unset = UNSET
    buy_size_cv: float | Unset = UNSET
    chain: str | Unset = UNSET
    created_at: str | Unset = UNSET
    daily_profit_30d: (
        list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset
    ) = UNSET
    daily_profit_7d: (
        list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset
    ) = UNSET
    didnt_buy_sells_30d: int | Unset = UNSET
    didnt_buy_sells_7d: int | Unset = UNSET
    dust_tx_ratio: float | Unset = UNSET
    has_avatar: bool | Unset = UNSET
    holding_pnl_lamports: float | Unset = UNSET
    id: str | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    last_active_timestamp: int | Unset = UNSET
    median_buy_count_per_token: float | Unset = UNSET
    median_first_buy_reactivity: float | Unset = UNSET
    median_holding_time: float | Unset = UNSET
    median_realized_profit_30d: float | Unset = UNSET
    median_realized_profit_7d: float | Unset = UNSET
    median_sell_count_per_token: float | Unset = UNSET
    mm_score: int | Unset = UNSET
    name: str | Unset = UNSET
    oldest_trade_at: int | Unset = UNSET
    periods: list[PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow] | Unset = (
        UNSET
    )
    pnl_0x_2x_num_30d: int | Unset = UNSET
    pnl_0x_2x_num_7d: int | Unset = UNSET
    pnl_2x_5x_num_30d: int | Unset = UNSET
    pnl_2x_5x_num_7d: int | Unset = UNSET
    pnl_distribution: list[int] | Unset = UNSET
    pnl_gt_5x_num_30d: int | Unset = UNSET
    pnl_gt_5x_num_7d: int | Unset = UNSET
    pnl_lt_nd5_num_30d: int | Unset = UNSET
    pnl_lt_nd5_num_7d: int | Unset = UNSET
    pnl_nd5_0x_num_30d: int | Unset = UNSET
    pnl_nd5_0x_num_7d: int | Unset = UNSET
    pnl_sparkline_7d: list[float] | Unset = UNSET
    profit_per_trade: float | Unset = UNSET
    realized_profit: float | Unset = UNSET
    realized_profit_30d: float | Unset = UNSET
    realized_profit_7d: float | Unset = UNSET
    realized_profit_pnl_30d: float | Unset = UNSET
    realized_profit_pnl_7d: float | Unset = UNSET
    rebalancing_ratio: float | Unset = UNSET
    risk_level: str | Unset = UNSET
    risk_score: int | Unset = UNSET
    sell_30d: int | Unset = UNSET
    sell_7d: int | Unset = UNSET
    sol_balance: float | Unset = UNSET
    sold_gt_bought_sells_30d: int | Unset = UNSET
    sold_gt_bought_sells_7d: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    token_num_30d: int | Unset = UNSET
    token_num_7d: int | Unset = UNSET
    tokens_created: int | Unset = UNSET
    tokens_graduated: int | Unset = UNSET
    total_profit: float | Unset = UNSET
    total_profit_30d: float | Unset = UNSET
    total_profit_7d: float | Unset = UNSET
    total_profit_pnl_30d: float | Unset = UNSET
    total_profit_pnl_7d: float | Unset = UNSET
    total_value: float | Unset = UNSET
    total_volume_usd: float | Unset = UNSET
    trade_interval_cv: float | Unset = UNSET
    trade_interval_mean: float | Unset = UNSET
    twitter_username: str | Unset = UNSET
    unrealized_profit: float | Unset = UNSET
    unrealized_profit_30d: float | Unset = UNSET
    unrealized_profit_7d: float | Unset = UNSET
    unrealized_profit_pnl_30d: float | Unset = UNSET
    unrealized_profit_pnl_7d: float | Unset = UNSET
    updated_at: str | Unset = UNSET
    wallet_address: str | Unset = UNSET
    winrate_30d: float | Unset = UNSET
    winrate_7d: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_hours_count = self.active_hours_count

        arb_tx_ratio_30d = self.arb_tx_ratio_30d

        arb_tx_ratio_7d = self.arb_tx_ratio_7d

        avg_buy_count_per_token = self.avg_buy_count_per_token

        avg_first_buy_reactivity = self.avg_first_buy_reactivity

        avg_holding_time = self.avg_holding_time

        avg_realized_profit_30d = self.avg_realized_profit_30d

        avg_realized_profit_7d = self.avg_realized_profit_7d

        avg_sell_count_per_token = self.avg_sell_count_per_token

        behavioral_30d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_30d, Unset):
            behavioral_30d = self.behavioral_30d.to_dict()

        behavioral_7d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavioral_7d, Unset):
            behavioral_7d = self.behavioral_7d.to_dict()

        buy_30d = self.buy_30d

        buy_7d = self.buy_7d

        buy_sell_ratio_30d = self.buy_sell_ratio_30d

        buy_sell_ratio_7d = self.buy_sell_ratio_7d

        buy_size_cv = self.buy_size_cv

        chain = self.chain

        created_at = self.created_at

        daily_profit_30d: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily_profit_30d, Unset):
            daily_profit_30d = []
            for daily_profit_30d_item_data in self.daily_profit_30d:
                daily_profit_30d_item = daily_profit_30d_item_data.to_dict()
                daily_profit_30d.append(daily_profit_30d_item)

        daily_profit_7d: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily_profit_7d, Unset):
            daily_profit_7d = []
            for daily_profit_7d_item_data in self.daily_profit_7d:
                daily_profit_7d_item = daily_profit_7d_item_data.to_dict()
                daily_profit_7d.append(daily_profit_7d_item)

        didnt_buy_sells_30d = self.didnt_buy_sells_30d

        didnt_buy_sells_7d = self.didnt_buy_sells_7d

        dust_tx_ratio = self.dust_tx_ratio

        has_avatar = self.has_avatar

        holding_pnl_lamports = self.holding_pnl_lamports

        id = self.id

        is_favorite = self.is_favorite

        last_active_timestamp = self.last_active_timestamp

        median_buy_count_per_token = self.median_buy_count_per_token

        median_first_buy_reactivity = self.median_first_buy_reactivity

        median_holding_time = self.median_holding_time

        median_realized_profit_30d = self.median_realized_profit_30d

        median_realized_profit_7d = self.median_realized_profit_7d

        median_sell_count_per_token = self.median_sell_count_per_token

        mm_score = self.mm_score

        name = self.name

        oldest_trade_at = self.oldest_trade_at

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        pnl_0x_2x_num_30d = self.pnl_0x_2x_num_30d

        pnl_0x_2x_num_7d = self.pnl_0x_2x_num_7d

        pnl_2x_5x_num_30d = self.pnl_2x_5x_num_30d

        pnl_2x_5x_num_7d = self.pnl_2x_5x_num_7d

        pnl_distribution: list[int] | Unset = UNSET
        if not isinstance(self.pnl_distribution, Unset):
            pnl_distribution = self.pnl_distribution

        pnl_gt_5x_num_30d = self.pnl_gt_5x_num_30d

        pnl_gt_5x_num_7d = self.pnl_gt_5x_num_7d

        pnl_lt_nd5_num_30d = self.pnl_lt_nd5_num_30d

        pnl_lt_nd5_num_7d = self.pnl_lt_nd5_num_7d

        pnl_nd5_0x_num_30d = self.pnl_nd5_0x_num_30d

        pnl_nd5_0x_num_7d = self.pnl_nd5_0x_num_7d

        pnl_sparkline_7d: list[float] | Unset = UNSET
        if not isinstance(self.pnl_sparkline_7d, Unset):
            pnl_sparkline_7d = self.pnl_sparkline_7d

        profit_per_trade = self.profit_per_trade

        realized_profit = self.realized_profit

        realized_profit_30d = self.realized_profit_30d

        realized_profit_7d = self.realized_profit_7d

        realized_profit_pnl_30d = self.realized_profit_pnl_30d

        realized_profit_pnl_7d = self.realized_profit_pnl_7d

        rebalancing_ratio = self.rebalancing_ratio

        risk_level = self.risk_level

        risk_score = self.risk_score

        sell_30d = self.sell_30d

        sell_7d = self.sell_7d

        sol_balance = self.sol_balance

        sold_gt_bought_sells_30d = self.sold_gt_bought_sells_30d

        sold_gt_bought_sells_7d = self.sold_gt_bought_sells_7d

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        token_num_30d = self.token_num_30d

        token_num_7d = self.token_num_7d

        tokens_created = self.tokens_created

        tokens_graduated = self.tokens_graduated

        total_profit = self.total_profit

        total_profit_30d = self.total_profit_30d

        total_profit_7d = self.total_profit_7d

        total_profit_pnl_30d = self.total_profit_pnl_30d

        total_profit_pnl_7d = self.total_profit_pnl_7d

        total_value = self.total_value

        total_volume_usd = self.total_volume_usd

        trade_interval_cv = self.trade_interval_cv

        trade_interval_mean = self.trade_interval_mean

        twitter_username = self.twitter_username

        unrealized_profit = self.unrealized_profit

        unrealized_profit_30d = self.unrealized_profit_30d

        unrealized_profit_7d = self.unrealized_profit_7d

        unrealized_profit_pnl_30d = self.unrealized_profit_pnl_30d

        unrealized_profit_pnl_7d = self.unrealized_profit_pnl_7d

        updated_at = self.updated_at

        wallet_address = self.wallet_address

        winrate_30d = self.winrate_30d

        winrate_7d = self.winrate_7d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_hours_count is not UNSET:
            field_dict["active_hours_count"] = active_hours_count
        if arb_tx_ratio_30d is not UNSET:
            field_dict["arb_tx_ratio_30d"] = arb_tx_ratio_30d
        if arb_tx_ratio_7d is not UNSET:
            field_dict["arb_tx_ratio_7d"] = arb_tx_ratio_7d
        if avg_buy_count_per_token is not UNSET:
            field_dict["avg_buy_count_per_token"] = avg_buy_count_per_token
        if avg_first_buy_reactivity is not UNSET:
            field_dict["avg_first_buy_reactivity"] = avg_first_buy_reactivity
        if avg_holding_time is not UNSET:
            field_dict["avg_holding_time"] = avg_holding_time
        if avg_realized_profit_30d is not UNSET:
            field_dict["avg_realized_profit_30d"] = avg_realized_profit_30d
        if avg_realized_profit_7d is not UNSET:
            field_dict["avg_realized_profit_7d"] = avg_realized_profit_7d
        if avg_sell_count_per_token is not UNSET:
            field_dict["avg_sell_count_per_token"] = avg_sell_count_per_token
        if behavioral_30d is not UNSET:
            field_dict["behavioral_30d"] = behavioral_30d
        if behavioral_7d is not UNSET:
            field_dict["behavioral_7d"] = behavioral_7d
        if buy_30d is not UNSET:
            field_dict["buy_30d"] = buy_30d
        if buy_7d is not UNSET:
            field_dict["buy_7d"] = buy_7d
        if buy_sell_ratio_30d is not UNSET:
            field_dict["buy_sell_ratio_30d"] = buy_sell_ratio_30d
        if buy_sell_ratio_7d is not UNSET:
            field_dict["buy_sell_ratio_7d"] = buy_sell_ratio_7d
        if buy_size_cv is not UNSET:
            field_dict["buy_size_cv"] = buy_size_cv
        if chain is not UNSET:
            field_dict["chain"] = chain
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if daily_profit_30d is not UNSET:
            field_dict["daily_profit_30d"] = daily_profit_30d
        if daily_profit_7d is not UNSET:
            field_dict["daily_profit_7d"] = daily_profit_7d
        if didnt_buy_sells_30d is not UNSET:
            field_dict["didnt_buy_sells_30d"] = didnt_buy_sells_30d
        if didnt_buy_sells_7d is not UNSET:
            field_dict["didnt_buy_sells_7d"] = didnt_buy_sells_7d
        if dust_tx_ratio is not UNSET:
            field_dict["dust_tx_ratio"] = dust_tx_ratio
        if has_avatar is not UNSET:
            field_dict["has_avatar"] = has_avatar
        if holding_pnl_lamports is not UNSET:
            field_dict["holding_pnl_lamports"] = holding_pnl_lamports
        if id is not UNSET:
            field_dict["id"] = id
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if last_active_timestamp is not UNSET:
            field_dict["last_active_timestamp"] = last_active_timestamp
        if median_buy_count_per_token is not UNSET:
            field_dict["median_buy_count_per_token"] = median_buy_count_per_token
        if median_first_buy_reactivity is not UNSET:
            field_dict["median_first_buy_reactivity"] = median_first_buy_reactivity
        if median_holding_time is not UNSET:
            field_dict["median_holding_time"] = median_holding_time
        if median_realized_profit_30d is not UNSET:
            field_dict["median_realized_profit_30d"] = median_realized_profit_30d
        if median_realized_profit_7d is not UNSET:
            field_dict["median_realized_profit_7d"] = median_realized_profit_7d
        if median_sell_count_per_token is not UNSET:
            field_dict["median_sell_count_per_token"] = median_sell_count_per_token
        if mm_score is not UNSET:
            field_dict["mm_score"] = mm_score
        if name is not UNSET:
            field_dict["name"] = name
        if oldest_trade_at is not UNSET:
            field_dict["oldest_trade_at"] = oldest_trade_at
        if periods is not UNSET:
            field_dict["periods"] = periods
        if pnl_0x_2x_num_30d is not UNSET:
            field_dict["pnl_0x_2x_num_30d"] = pnl_0x_2x_num_30d
        if pnl_0x_2x_num_7d is not UNSET:
            field_dict["pnl_0x_2x_num_7d"] = pnl_0x_2x_num_7d
        if pnl_2x_5x_num_30d is not UNSET:
            field_dict["pnl_2x_5x_num_30d"] = pnl_2x_5x_num_30d
        if pnl_2x_5x_num_7d is not UNSET:
            field_dict["pnl_2x_5x_num_7d"] = pnl_2x_5x_num_7d
        if pnl_distribution is not UNSET:
            field_dict["pnl_distribution"] = pnl_distribution
        if pnl_gt_5x_num_30d is not UNSET:
            field_dict["pnl_gt_5x_num_30d"] = pnl_gt_5x_num_30d
        if pnl_gt_5x_num_7d is not UNSET:
            field_dict["pnl_gt_5x_num_7d"] = pnl_gt_5x_num_7d
        if pnl_lt_nd5_num_30d is not UNSET:
            field_dict["pnl_lt_nd5_num_30d"] = pnl_lt_nd5_num_30d
        if pnl_lt_nd5_num_7d is not UNSET:
            field_dict["pnl_lt_nd5_num_7d"] = pnl_lt_nd5_num_7d
        if pnl_nd5_0x_num_30d is not UNSET:
            field_dict["pnl_nd5_0x_num_30d"] = pnl_nd5_0x_num_30d
        if pnl_nd5_0x_num_7d is not UNSET:
            field_dict["pnl_nd5_0x_num_7d"] = pnl_nd5_0x_num_7d
        if pnl_sparkline_7d is not UNSET:
            field_dict["pnl_sparkline_7d"] = pnl_sparkline_7d
        if profit_per_trade is not UNSET:
            field_dict["profit_per_trade"] = profit_per_trade
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if realized_profit_30d is not UNSET:
            field_dict["realized_profit_30d"] = realized_profit_30d
        if realized_profit_7d is not UNSET:
            field_dict["realized_profit_7d"] = realized_profit_7d
        if realized_profit_pnl_30d is not UNSET:
            field_dict["realized_profit_pnl_30d"] = realized_profit_pnl_30d
        if realized_profit_pnl_7d is not UNSET:
            field_dict["realized_profit_pnl_7d"] = realized_profit_pnl_7d
        if rebalancing_ratio is not UNSET:
            field_dict["rebalancing_ratio"] = rebalancing_ratio
        if risk_level is not UNSET:
            field_dict["risk_level"] = risk_level
        if risk_score is not UNSET:
            field_dict["risk_score"] = risk_score
        if sell_30d is not UNSET:
            field_dict["sell_30d"] = sell_30d
        if sell_7d is not UNSET:
            field_dict["sell_7d"] = sell_7d
        if sol_balance is not UNSET:
            field_dict["sol_balance"] = sol_balance
        if sold_gt_bought_sells_30d is not UNSET:
            field_dict["sold_gt_bought_sells_30d"] = sold_gt_bought_sells_30d
        if sold_gt_bought_sells_7d is not UNSET:
            field_dict["sold_gt_bought_sells_7d"] = sold_gt_bought_sells_7d
        if tags is not UNSET:
            field_dict["tags"] = tags
        if token_num_30d is not UNSET:
            field_dict["token_num_30d"] = token_num_30d
        if token_num_7d is not UNSET:
            field_dict["token_num_7d"] = token_num_7d
        if tokens_created is not UNSET:
            field_dict["tokens_created"] = tokens_created
        if tokens_graduated is not UNSET:
            field_dict["tokens_graduated"] = tokens_graduated
        if total_profit is not UNSET:
            field_dict["total_profit"] = total_profit
        if total_profit_30d is not UNSET:
            field_dict["total_profit_30d"] = total_profit_30d
        if total_profit_7d is not UNSET:
            field_dict["total_profit_7d"] = total_profit_7d
        if total_profit_pnl_30d is not UNSET:
            field_dict["total_profit_pnl_30d"] = total_profit_pnl_30d
        if total_profit_pnl_7d is not UNSET:
            field_dict["total_profit_pnl_7d"] = total_profit_pnl_7d
        if total_value is not UNSET:
            field_dict["total_value"] = total_value
        if total_volume_usd is not UNSET:
            field_dict["total_volume_usd"] = total_volume_usd
        if trade_interval_cv is not UNSET:
            field_dict["trade_interval_cv"] = trade_interval_cv
        if trade_interval_mean is not UNSET:
            field_dict["trade_interval_mean"] = trade_interval_mean
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if unrealized_profit is not UNSET:
            field_dict["unrealized_profit"] = unrealized_profit
        if unrealized_profit_30d is not UNSET:
            field_dict["unrealized_profit_30d"] = unrealized_profit_30d
        if unrealized_profit_7d is not UNSET:
            field_dict["unrealized_profit_7d"] = unrealized_profit_7d
        if unrealized_profit_pnl_30d is not UNSET:
            field_dict["unrealized_profit_pnl_30d"] = unrealized_profit_pnl_30d
        if unrealized_profit_pnl_7d is not UNSET:
            field_dict["unrealized_profit_pnl_7d"] = unrealized_profit_pnl_7d
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if wallet_address is not UNSET:
            field_dict["wallet_address"] = wallet_address
        if winrate_30d is not UNSET:
            field_dict["winrate_30d"] = winrate_30d
        if winrate_7d is not UNSET:
            field_dict["winrate_7d"] = winrate_7d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_aggregator_trader_behavioral_stats import (
            PulsightInternalCoreDomainAggregatorTraderBehavioralStats,
        )
        from ..models.pulsight_internal_core_domain_aggregator_trader_period_stats_row import (
            PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow,
        )
        from ..models.pulsight_internal_core_usecases_trader_daily_profit_entry import (
            PulsightInternalCoreUsecasesTraderDailyProfitEntry,
        )

        d = dict(src_dict)
        active_hours_count = d.pop("active_hours_count", UNSET)

        arb_tx_ratio_30d = d.pop("arb_tx_ratio_30d", UNSET)

        arb_tx_ratio_7d = d.pop("arb_tx_ratio_7d", UNSET)

        avg_buy_count_per_token = d.pop("avg_buy_count_per_token", UNSET)

        avg_first_buy_reactivity = d.pop("avg_first_buy_reactivity", UNSET)

        avg_holding_time = d.pop("avg_holding_time", UNSET)

        avg_realized_profit_30d = d.pop("avg_realized_profit_30d", UNSET)

        avg_realized_profit_7d = d.pop("avg_realized_profit_7d", UNSET)

        avg_sell_count_per_token = d.pop("avg_sell_count_per_token", UNSET)

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

        buy_30d = d.pop("buy_30d", UNSET)

        buy_7d = d.pop("buy_7d", UNSET)

        buy_sell_ratio_30d = d.pop("buy_sell_ratio_30d", UNSET)

        buy_sell_ratio_7d = d.pop("buy_sell_ratio_7d", UNSET)

        buy_size_cv = d.pop("buy_size_cv", UNSET)

        chain = d.pop("chain", UNSET)

        created_at = d.pop("created_at", UNSET)

        _daily_profit_30d = d.pop("daily_profit_30d", UNSET)
        daily_profit_30d: (
            list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset
        ) = UNSET
        if _daily_profit_30d is not UNSET:
            daily_profit_30d = []
            for daily_profit_30d_item_data in _daily_profit_30d:
                daily_profit_30d_item = (
                    PulsightInternalCoreUsecasesTraderDailyProfitEntry.from_dict(
                        daily_profit_30d_item_data
                    )
                )

                daily_profit_30d.append(daily_profit_30d_item)

        _daily_profit_7d = d.pop("daily_profit_7d", UNSET)
        daily_profit_7d: (
            list[PulsightInternalCoreUsecasesTraderDailyProfitEntry] | Unset
        ) = UNSET
        if _daily_profit_7d is not UNSET:
            daily_profit_7d = []
            for daily_profit_7d_item_data in _daily_profit_7d:
                daily_profit_7d_item = (
                    PulsightInternalCoreUsecasesTraderDailyProfitEntry.from_dict(
                        daily_profit_7d_item_data
                    )
                )

                daily_profit_7d.append(daily_profit_7d_item)

        didnt_buy_sells_30d = d.pop("didnt_buy_sells_30d", UNSET)

        didnt_buy_sells_7d = d.pop("didnt_buy_sells_7d", UNSET)

        dust_tx_ratio = d.pop("dust_tx_ratio", UNSET)

        has_avatar = d.pop("has_avatar", UNSET)

        holding_pnl_lamports = d.pop("holding_pnl_lamports", UNSET)

        id = d.pop("id", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        last_active_timestamp = d.pop("last_active_timestamp", UNSET)

        median_buy_count_per_token = d.pop("median_buy_count_per_token", UNSET)

        median_first_buy_reactivity = d.pop("median_first_buy_reactivity", UNSET)

        median_holding_time = d.pop("median_holding_time", UNSET)

        median_realized_profit_30d = d.pop("median_realized_profit_30d", UNSET)

        median_realized_profit_7d = d.pop("median_realized_profit_7d", UNSET)

        median_sell_count_per_token = d.pop("median_sell_count_per_token", UNSET)

        mm_score = d.pop("mm_score", UNSET)

        name = d.pop("name", UNSET)

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

        pnl_0x_2x_num_30d = d.pop("pnl_0x_2x_num_30d", UNSET)

        pnl_0x_2x_num_7d = d.pop("pnl_0x_2x_num_7d", UNSET)

        pnl_2x_5x_num_30d = d.pop("pnl_2x_5x_num_30d", UNSET)

        pnl_2x_5x_num_7d = d.pop("pnl_2x_5x_num_7d", UNSET)

        pnl_distribution = cast(list[int], d.pop("pnl_distribution", UNSET))

        pnl_gt_5x_num_30d = d.pop("pnl_gt_5x_num_30d", UNSET)

        pnl_gt_5x_num_7d = d.pop("pnl_gt_5x_num_7d", UNSET)

        pnl_lt_nd5_num_30d = d.pop("pnl_lt_nd5_num_30d", UNSET)

        pnl_lt_nd5_num_7d = d.pop("pnl_lt_nd5_num_7d", UNSET)

        pnl_nd5_0x_num_30d = d.pop("pnl_nd5_0x_num_30d", UNSET)

        pnl_nd5_0x_num_7d = d.pop("pnl_nd5_0x_num_7d", UNSET)

        pnl_sparkline_7d = cast(list[float], d.pop("pnl_sparkline_7d", UNSET))

        profit_per_trade = d.pop("profit_per_trade", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        realized_profit_30d = d.pop("realized_profit_30d", UNSET)

        realized_profit_7d = d.pop("realized_profit_7d", UNSET)

        realized_profit_pnl_30d = d.pop("realized_profit_pnl_30d", UNSET)

        realized_profit_pnl_7d = d.pop("realized_profit_pnl_7d", UNSET)

        rebalancing_ratio = d.pop("rebalancing_ratio", UNSET)

        risk_level = d.pop("risk_level", UNSET)

        risk_score = d.pop("risk_score", UNSET)

        sell_30d = d.pop("sell_30d", UNSET)

        sell_7d = d.pop("sell_7d", UNSET)

        sol_balance = d.pop("sol_balance", UNSET)

        sold_gt_bought_sells_30d = d.pop("sold_gt_bought_sells_30d", UNSET)

        sold_gt_bought_sells_7d = d.pop("sold_gt_bought_sells_7d", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_num_30d = d.pop("token_num_30d", UNSET)

        token_num_7d = d.pop("token_num_7d", UNSET)

        tokens_created = d.pop("tokens_created", UNSET)

        tokens_graduated = d.pop("tokens_graduated", UNSET)

        total_profit = d.pop("total_profit", UNSET)

        total_profit_30d = d.pop("total_profit_30d", UNSET)

        total_profit_7d = d.pop("total_profit_7d", UNSET)

        total_profit_pnl_30d = d.pop("total_profit_pnl_30d", UNSET)

        total_profit_pnl_7d = d.pop("total_profit_pnl_7d", UNSET)

        total_value = d.pop("total_value", UNSET)

        total_volume_usd = d.pop("total_volume_usd", UNSET)

        trade_interval_cv = d.pop("trade_interval_cv", UNSET)

        trade_interval_mean = d.pop("trade_interval_mean", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        unrealized_profit = d.pop("unrealized_profit", UNSET)

        unrealized_profit_30d = d.pop("unrealized_profit_30d", UNSET)

        unrealized_profit_7d = d.pop("unrealized_profit_7d", UNSET)

        unrealized_profit_pnl_30d = d.pop("unrealized_profit_pnl_30d", UNSET)

        unrealized_profit_pnl_7d = d.pop("unrealized_profit_pnl_7d", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        wallet_address = d.pop("wallet_address", UNSET)

        winrate_30d = d.pop("winrate_30d", UNSET)

        winrate_7d = d.pop("winrate_7d", UNSET)

        pulsight_internal_core_usecases_trader_trader_list_item = cls(
            active_hours_count=active_hours_count,
            arb_tx_ratio_30d=arb_tx_ratio_30d,
            arb_tx_ratio_7d=arb_tx_ratio_7d,
            avg_buy_count_per_token=avg_buy_count_per_token,
            avg_first_buy_reactivity=avg_first_buy_reactivity,
            avg_holding_time=avg_holding_time,
            avg_realized_profit_30d=avg_realized_profit_30d,
            avg_realized_profit_7d=avg_realized_profit_7d,
            avg_sell_count_per_token=avg_sell_count_per_token,
            behavioral_30d=behavioral_30d,
            behavioral_7d=behavioral_7d,
            buy_30d=buy_30d,
            buy_7d=buy_7d,
            buy_sell_ratio_30d=buy_sell_ratio_30d,
            buy_sell_ratio_7d=buy_sell_ratio_7d,
            buy_size_cv=buy_size_cv,
            chain=chain,
            created_at=created_at,
            daily_profit_30d=daily_profit_30d,
            daily_profit_7d=daily_profit_7d,
            didnt_buy_sells_30d=didnt_buy_sells_30d,
            didnt_buy_sells_7d=didnt_buy_sells_7d,
            dust_tx_ratio=dust_tx_ratio,
            has_avatar=has_avatar,
            holding_pnl_lamports=holding_pnl_lamports,
            id=id,
            is_favorite=is_favorite,
            last_active_timestamp=last_active_timestamp,
            median_buy_count_per_token=median_buy_count_per_token,
            median_first_buy_reactivity=median_first_buy_reactivity,
            median_holding_time=median_holding_time,
            median_realized_profit_30d=median_realized_profit_30d,
            median_realized_profit_7d=median_realized_profit_7d,
            median_sell_count_per_token=median_sell_count_per_token,
            mm_score=mm_score,
            name=name,
            oldest_trade_at=oldest_trade_at,
            periods=periods,
            pnl_0x_2x_num_30d=pnl_0x_2x_num_30d,
            pnl_0x_2x_num_7d=pnl_0x_2x_num_7d,
            pnl_2x_5x_num_30d=pnl_2x_5x_num_30d,
            pnl_2x_5x_num_7d=pnl_2x_5x_num_7d,
            pnl_distribution=pnl_distribution,
            pnl_gt_5x_num_30d=pnl_gt_5x_num_30d,
            pnl_gt_5x_num_7d=pnl_gt_5x_num_7d,
            pnl_lt_nd5_num_30d=pnl_lt_nd5_num_30d,
            pnl_lt_nd5_num_7d=pnl_lt_nd5_num_7d,
            pnl_nd5_0x_num_30d=pnl_nd5_0x_num_30d,
            pnl_nd5_0x_num_7d=pnl_nd5_0x_num_7d,
            pnl_sparkline_7d=pnl_sparkline_7d,
            profit_per_trade=profit_per_trade,
            realized_profit=realized_profit,
            realized_profit_30d=realized_profit_30d,
            realized_profit_7d=realized_profit_7d,
            realized_profit_pnl_30d=realized_profit_pnl_30d,
            realized_profit_pnl_7d=realized_profit_pnl_7d,
            rebalancing_ratio=rebalancing_ratio,
            risk_level=risk_level,
            risk_score=risk_score,
            sell_30d=sell_30d,
            sell_7d=sell_7d,
            sol_balance=sol_balance,
            sold_gt_bought_sells_30d=sold_gt_bought_sells_30d,
            sold_gt_bought_sells_7d=sold_gt_bought_sells_7d,
            tags=tags,
            token_num_30d=token_num_30d,
            token_num_7d=token_num_7d,
            tokens_created=tokens_created,
            tokens_graduated=tokens_graduated,
            total_profit=total_profit,
            total_profit_30d=total_profit_30d,
            total_profit_7d=total_profit_7d,
            total_profit_pnl_30d=total_profit_pnl_30d,
            total_profit_pnl_7d=total_profit_pnl_7d,
            total_value=total_value,
            total_volume_usd=total_volume_usd,
            trade_interval_cv=trade_interval_cv,
            trade_interval_mean=trade_interval_mean,
            twitter_username=twitter_username,
            unrealized_profit=unrealized_profit,
            unrealized_profit_30d=unrealized_profit_30d,
            unrealized_profit_7d=unrealized_profit_7d,
            unrealized_profit_pnl_30d=unrealized_profit_pnl_30d,
            unrealized_profit_pnl_7d=unrealized_profit_pnl_7d,
            updated_at=updated_at,
            wallet_address=wallet_address,
            winrate_30d=winrate_30d,
            winrate_7d=winrate_7d,
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
