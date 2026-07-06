from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_daily_profit import (
        PulsightInternalCoreDomainTraderDailyProfit,
    )
    from ..models.pulsight_internal_core_domain_trader_pnl import (
        PulsightInternalCoreDomainTraderPnl,
    )
    from ..models.pulsight_internal_core_domain_trader_tag import (
        PulsightInternalCoreDomainTraderTag,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderTrader")


@_attrs_define
class PulsightInternalCoreDomainTraderTrader:
    """
    Attributes:
        active_hours_count (int | Unset):
        arb_tx_ratio_30d (float | Unset):
        arb_tx_ratio_7d (float | Unset):
        avatar (str | Unset):
        avg_buy_count_per_token (float | Unset): Per-token buy/sell counts
        avg_first_buy_reactivity (float | Unset): First-buy reactivity (seconds after token launch)
        avg_holding_time (float | Unset): Holding time (seconds)
        avg_realized_profit_30d (float | Unset):
        avg_realized_profit_7d (float | Unset): Realized profit per-mint averages / medians. UNIT: lamports
            (frontend FormattedSol divides by 1e9 on display).
        avg_sell_count_per_token (float | Unset):
        buy_30d (int | Unset):
        buy_7d (int | Unset):
        buy_sell_ratio_30d (float | Unset):
        buy_sell_ratio_7d (float | Unset): Computed ratios
        buy_size_cv (float | Unset):
        chain (str | Unset): "sol" | "eth"
        created_at (str | Unset):
        daily_profits (list[PulsightInternalCoreDomainTraderDailyProfit] | Unset):
        didnt_buy_sells_30d (int | Unset):
        didnt_buy_sells_7d (int | Unset): Uncovered-sell counters for the window (CA migration 000018):
            sells with no observed buy of the mint / sells exceeding the
            observed bought balance.
        dust_tx_ratio (float | Unset):
        id (str | Unset):
        is_favorite (bool | Unset):
        last_active_timestamp (int | Unset): Activity
        median_buy_count_per_token (float | Unset):
        median_first_buy_reactivity (float | Unset):
        median_holding_time (float | Unset):
        median_realized_profit_30d (float | Unset):
        median_realized_profit_7d (float | Unset):
        median_sell_count_per_token (float | Unset):
        mm_score (int | Unset):
        name (str | Unset): Identifiers / social
        oldest_trade_at (int | Unset):
        pnl_0x2x_num_30d (int | Unset):
        pnl_0x2x_num_7d (int | Unset): 0x to 2x
        pnl_2x5x_num_30d (int | Unset):
        pnl_2x5x_num_7d (int | Unset): 2x to 5x
        pnl_gt5x_num_30d (int | Unset):
        pnl_gt5x_num_7d (int | Unset): > 5x
        pnl_lt_nd5_num_30d (int | Unset): PnL distribution buckets — 30d
        pnl_lt_nd5_num_7d (int | Unset): PnL distribution buckets — 7d
        pnl_nd50x_num_30d (int | Unset):
        pnl_nd50x_num_7d (int | Unset): -5x to 0x
        pnls (list[PulsightInternalCoreDomainTraderPnl] | Unset):
        profit_per_trade (float | Unset):
        realized_profit (float | Unset):
        realized_profit_30d (float | Unset): 30-day period
        realized_profit_7d (float | Unset): 7-day period. UNIT for realized_profit_*: lamports.
        realized_profit_pnl_30d (float | Unset):
        realized_profit_pnl_7d (float | Unset):
        rebalancing_ratio (float | Unset):
        risk_level (str | Unset):
        risk_score (int | Unset): Risk assessment
        sell_30d (int | Unset):
        sell_7d (int | Unset):
        sol_balance (float | Unset): Balances. UNIT: lamports (BIGINT, held as *float64 for wire
            compatibility). The field name says "Sol" for historical reasons;
            the wire convention is lamports because the frontend's
            FormattedSol component divides by 1e9 itself.
        sold_gt_bought_sells_30d (int | Unset):
        sold_gt_bought_sells_7d (int | Unset):
        tags (list[PulsightInternalCoreDomainTraderTag] | Unset): Relations (loaded on demand)
        token_num_30d (int | Unset):
        token_num_7d (int | Unset):
        total_profit (float | Unset): Profit stats (all-time). UNIT: lamports (see SolBalance note).
        total_profit_30d (float | Unset):
        total_profit_7d (float | Unset):
        total_profit_pnl_30d (float | Unset):
        total_profit_pnl_7d (float | Unset):
        total_value (float | Unset):
        total_volume_usd (float | Unset):
        trade_interval_cv (float | Unset):
        trade_interval_mean (float | Unset): Market-maker detection
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
    avatar: str | Unset = UNSET
    avg_buy_count_per_token: float | Unset = UNSET
    avg_first_buy_reactivity: float | Unset = UNSET
    avg_holding_time: float | Unset = UNSET
    avg_realized_profit_30d: float | Unset = UNSET
    avg_realized_profit_7d: float | Unset = UNSET
    avg_sell_count_per_token: float | Unset = UNSET
    buy_30d: int | Unset = UNSET
    buy_7d: int | Unset = UNSET
    buy_sell_ratio_30d: float | Unset = UNSET
    buy_sell_ratio_7d: float | Unset = UNSET
    buy_size_cv: float | Unset = UNSET
    chain: str | Unset = UNSET
    created_at: str | Unset = UNSET
    daily_profits: list[PulsightInternalCoreDomainTraderDailyProfit] | Unset = UNSET
    didnt_buy_sells_30d: int | Unset = UNSET
    didnt_buy_sells_7d: int | Unset = UNSET
    dust_tx_ratio: float | Unset = UNSET
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
    pnl_0x2x_num_30d: int | Unset = UNSET
    pnl_0x2x_num_7d: int | Unset = UNSET
    pnl_2x5x_num_30d: int | Unset = UNSET
    pnl_2x5x_num_7d: int | Unset = UNSET
    pnl_gt5x_num_30d: int | Unset = UNSET
    pnl_gt5x_num_7d: int | Unset = UNSET
    pnl_lt_nd5_num_30d: int | Unset = UNSET
    pnl_lt_nd5_num_7d: int | Unset = UNSET
    pnl_nd50x_num_30d: int | Unset = UNSET
    pnl_nd50x_num_7d: int | Unset = UNSET
    pnls: list[PulsightInternalCoreDomainTraderPnl] | Unset = UNSET
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
    tags: list[PulsightInternalCoreDomainTraderTag] | Unset = UNSET
    token_num_30d: int | Unset = UNSET
    token_num_7d: int | Unset = UNSET
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

        avatar = self.avatar

        avg_buy_count_per_token = self.avg_buy_count_per_token

        avg_first_buy_reactivity = self.avg_first_buy_reactivity

        avg_holding_time = self.avg_holding_time

        avg_realized_profit_30d = self.avg_realized_profit_30d

        avg_realized_profit_7d = self.avg_realized_profit_7d

        avg_sell_count_per_token = self.avg_sell_count_per_token

        buy_30d = self.buy_30d

        buy_7d = self.buy_7d

        buy_sell_ratio_30d = self.buy_sell_ratio_30d

        buy_sell_ratio_7d = self.buy_sell_ratio_7d

        buy_size_cv = self.buy_size_cv

        chain = self.chain

        created_at = self.created_at

        daily_profits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily_profits, Unset):
            daily_profits = []
            for daily_profits_item_data in self.daily_profits:
                daily_profits_item = daily_profits_item_data.to_dict()
                daily_profits.append(daily_profits_item)

        didnt_buy_sells_30d = self.didnt_buy_sells_30d

        didnt_buy_sells_7d = self.didnt_buy_sells_7d

        dust_tx_ratio = self.dust_tx_ratio

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

        pnl_0x2x_num_30d = self.pnl_0x2x_num_30d

        pnl_0x2x_num_7d = self.pnl_0x2x_num_7d

        pnl_2x5x_num_30d = self.pnl_2x5x_num_30d

        pnl_2x5x_num_7d = self.pnl_2x5x_num_7d

        pnl_gt5x_num_30d = self.pnl_gt5x_num_30d

        pnl_gt5x_num_7d = self.pnl_gt5x_num_7d

        pnl_lt_nd5_num_30d = self.pnl_lt_nd5_num_30d

        pnl_lt_nd5_num_7d = self.pnl_lt_nd5_num_7d

        pnl_nd50x_num_30d = self.pnl_nd50x_num_30d

        pnl_nd50x_num_7d = self.pnl_nd50x_num_7d

        pnls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pnls, Unset):
            pnls = []
            for pnls_item_data in self.pnls:
                pnls_item = pnls_item_data.to_dict()
                pnls.append(pnls_item)

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

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        token_num_30d = self.token_num_30d

        token_num_7d = self.token_num_7d

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
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
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
        if daily_profits is not UNSET:
            field_dict["daily_profits"] = daily_profits
        if didnt_buy_sells_30d is not UNSET:
            field_dict["didnt_buy_sells_30d"] = didnt_buy_sells_30d
        if didnt_buy_sells_7d is not UNSET:
            field_dict["didnt_buy_sells_7d"] = didnt_buy_sells_7d
        if dust_tx_ratio is not UNSET:
            field_dict["dust_tx_ratio"] = dust_tx_ratio
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
        if pnl_0x2x_num_30d is not UNSET:
            field_dict["pnl_0x2x_num_30d"] = pnl_0x2x_num_30d
        if pnl_0x2x_num_7d is not UNSET:
            field_dict["pnl_0x2x_num_7d"] = pnl_0x2x_num_7d
        if pnl_2x5x_num_30d is not UNSET:
            field_dict["pnl_2x5x_num_30d"] = pnl_2x5x_num_30d
        if pnl_2x5x_num_7d is not UNSET:
            field_dict["pnl_2x5x_num_7d"] = pnl_2x5x_num_7d
        if pnl_gt5x_num_30d is not UNSET:
            field_dict["pnl_gt5x_num_30d"] = pnl_gt5x_num_30d
        if pnl_gt5x_num_7d is not UNSET:
            field_dict["pnl_gt5x_num_7d"] = pnl_gt5x_num_7d
        if pnl_lt_nd5_num_30d is not UNSET:
            field_dict["pnl_lt_nd5_num_30d"] = pnl_lt_nd5_num_30d
        if pnl_lt_nd5_num_7d is not UNSET:
            field_dict["pnl_lt_nd5_num_7d"] = pnl_lt_nd5_num_7d
        if pnl_nd50x_num_30d is not UNSET:
            field_dict["pnl_nd50x_num_30d"] = pnl_nd50x_num_30d
        if pnl_nd50x_num_7d is not UNSET:
            field_dict["pnl_nd50x_num_7d"] = pnl_nd50x_num_7d
        if pnls is not UNSET:
            field_dict["pnls"] = pnls
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
        from ..models.pulsight_internal_core_domain_trader_daily_profit import (
            PulsightInternalCoreDomainTraderDailyProfit,
        )
        from ..models.pulsight_internal_core_domain_trader_pnl import (
            PulsightInternalCoreDomainTraderPnl,
        )
        from ..models.pulsight_internal_core_domain_trader_tag import (
            PulsightInternalCoreDomainTraderTag,
        )

        d = dict(src_dict)
        active_hours_count = d.pop("active_hours_count", UNSET)

        arb_tx_ratio_30d = d.pop("arb_tx_ratio_30d", UNSET)

        arb_tx_ratio_7d = d.pop("arb_tx_ratio_7d", UNSET)

        avatar = d.pop("avatar", UNSET)

        avg_buy_count_per_token = d.pop("avg_buy_count_per_token", UNSET)

        avg_first_buy_reactivity = d.pop("avg_first_buy_reactivity", UNSET)

        avg_holding_time = d.pop("avg_holding_time", UNSET)

        avg_realized_profit_30d = d.pop("avg_realized_profit_30d", UNSET)

        avg_realized_profit_7d = d.pop("avg_realized_profit_7d", UNSET)

        avg_sell_count_per_token = d.pop("avg_sell_count_per_token", UNSET)

        buy_30d = d.pop("buy_30d", UNSET)

        buy_7d = d.pop("buy_7d", UNSET)

        buy_sell_ratio_30d = d.pop("buy_sell_ratio_30d", UNSET)

        buy_sell_ratio_7d = d.pop("buy_sell_ratio_7d", UNSET)

        buy_size_cv = d.pop("buy_size_cv", UNSET)

        chain = d.pop("chain", UNSET)

        created_at = d.pop("created_at", UNSET)

        _daily_profits = d.pop("daily_profits", UNSET)
        daily_profits: list[PulsightInternalCoreDomainTraderDailyProfit] | Unset = UNSET
        if _daily_profits is not UNSET:
            daily_profits = []
            for daily_profits_item_data in _daily_profits:
                daily_profits_item = (
                    PulsightInternalCoreDomainTraderDailyProfit.from_dict(
                        daily_profits_item_data
                    )
                )

                daily_profits.append(daily_profits_item)

        didnt_buy_sells_30d = d.pop("didnt_buy_sells_30d", UNSET)

        didnt_buy_sells_7d = d.pop("didnt_buy_sells_7d", UNSET)

        dust_tx_ratio = d.pop("dust_tx_ratio", UNSET)

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

        pnl_0x2x_num_30d = d.pop("pnl_0x2x_num_30d", UNSET)

        pnl_0x2x_num_7d = d.pop("pnl_0x2x_num_7d", UNSET)

        pnl_2x5x_num_30d = d.pop("pnl_2x5x_num_30d", UNSET)

        pnl_2x5x_num_7d = d.pop("pnl_2x5x_num_7d", UNSET)

        pnl_gt5x_num_30d = d.pop("pnl_gt5x_num_30d", UNSET)

        pnl_gt5x_num_7d = d.pop("pnl_gt5x_num_7d", UNSET)

        pnl_lt_nd5_num_30d = d.pop("pnl_lt_nd5_num_30d", UNSET)

        pnl_lt_nd5_num_7d = d.pop("pnl_lt_nd5_num_7d", UNSET)

        pnl_nd50x_num_30d = d.pop("pnl_nd50x_num_30d", UNSET)

        pnl_nd50x_num_7d = d.pop("pnl_nd50x_num_7d", UNSET)

        _pnls = d.pop("pnls", UNSET)
        pnls: list[PulsightInternalCoreDomainTraderPnl] | Unset = UNSET
        if _pnls is not UNSET:
            pnls = []
            for pnls_item_data in _pnls:
                pnls_item = PulsightInternalCoreDomainTraderPnl.from_dict(
                    pnls_item_data
                )

                pnls.append(pnls_item)

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

        _tags = d.pop("tags", UNSET)
        tags: list[PulsightInternalCoreDomainTraderTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = PulsightInternalCoreDomainTraderTag.from_dict(
                    tags_item_data
                )

                tags.append(tags_item)

        token_num_30d = d.pop("token_num_30d", UNSET)

        token_num_7d = d.pop("token_num_7d", UNSET)

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

        pulsight_internal_core_domain_trader_trader = cls(
            active_hours_count=active_hours_count,
            arb_tx_ratio_30d=arb_tx_ratio_30d,
            arb_tx_ratio_7d=arb_tx_ratio_7d,
            avatar=avatar,
            avg_buy_count_per_token=avg_buy_count_per_token,
            avg_first_buy_reactivity=avg_first_buy_reactivity,
            avg_holding_time=avg_holding_time,
            avg_realized_profit_30d=avg_realized_profit_30d,
            avg_realized_profit_7d=avg_realized_profit_7d,
            avg_sell_count_per_token=avg_sell_count_per_token,
            buy_30d=buy_30d,
            buy_7d=buy_7d,
            buy_sell_ratio_30d=buy_sell_ratio_30d,
            buy_sell_ratio_7d=buy_sell_ratio_7d,
            buy_size_cv=buy_size_cv,
            chain=chain,
            created_at=created_at,
            daily_profits=daily_profits,
            didnt_buy_sells_30d=didnt_buy_sells_30d,
            didnt_buy_sells_7d=didnt_buy_sells_7d,
            dust_tx_ratio=dust_tx_ratio,
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
            pnl_0x2x_num_30d=pnl_0x2x_num_30d,
            pnl_0x2x_num_7d=pnl_0x2x_num_7d,
            pnl_2x5x_num_30d=pnl_2x5x_num_30d,
            pnl_2x5x_num_7d=pnl_2x5x_num_7d,
            pnl_gt5x_num_30d=pnl_gt5x_num_30d,
            pnl_gt5x_num_7d=pnl_gt5x_num_7d,
            pnl_lt_nd5_num_30d=pnl_lt_nd5_num_30d,
            pnl_lt_nd5_num_7d=pnl_lt_nd5_num_7d,
            pnl_nd50x_num_30d=pnl_nd50x_num_30d,
            pnl_nd50x_num_7d=pnl_nd50x_num_7d,
            pnls=pnls,
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

        pulsight_internal_core_domain_trader_trader.additional_properties = d
        return pulsight_internal_core_domain_trader_trader

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
