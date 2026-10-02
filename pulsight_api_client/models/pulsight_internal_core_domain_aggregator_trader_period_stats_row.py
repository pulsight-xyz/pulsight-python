from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow:
    """
    Attributes:
        arb_pnl_lamports (int | Unset): ArbPnlLamports — the window's arbitrage take-home (tx-grain), ALREADY
            included in RealizedProfit and NetRealizedProfit. Exposed so the UI can
            show the split.
        arb_pnl_usd (int | Unset):
        arb_tx_ratio (float | Unset): ArbTxRatio is the fraction (0..1) of the window's transactions that
            were arbitrage. 0 when the window has no trades.
        buy_amount_lamports (int | Unset):
        buy_amount_usd (int | Unset): The Usd twins are the same money figures on the trades' USD stamps
            (micro-USD), with the win/loss split and winrate measured on them.
        buy_sell_ratio (float | Unset):
        cashback_claimed_lamports (int | Unset): CashbackClaimedLamports — pump cashback the wallet CLAIMED and kept in
            the window (cash basis). A POSITIVE cost-block component.
        cashback_claimed_usd (int | Unset):
        didnt_buy_sells (int | Unset): DidntBuySells / SoldGtBoughtSells count the window's uncovered sells:
            sells of a mint with no observed buy, and sells that exceeded the
            observed bought balance.
        failed_cost_lamports (int | Unset): FailedCostLamports — fees burned on failed venue-mentioning txs plus
            the fees+tips of landed no-CPI arb probes. 0 when none were recorded.
        failed_cost_usd (int | Unset):
        loss_profit (int | Unset):
        loss_profit_usd (int | Unset):
        loss_sells (int | Unset):
        loss_sells_usd (int | Unset):
        net_realized_profit (int | Unset): NetRealizedProfit is the board row's net PnL: RealizedProfit minus
            TotalFees, TotalTips and FailedCostLamports, plus the kept cashback and
            the holder rewards received — what the wallet actually kept. This is the
            HEADLINE PnL; RealizedProfit is the pre-cost component (accrual + arb
            take-home).
        net_realized_profit_usd (int | Unset):
        realized_profit (int | Unset): RealizedProfit is the window's PnL: accrual realized profit PLUS the
            arbitrage take-home (ArbPnlLamports). The two are disjoint (an arb round
            trip books zero realized), so the sum is exact.
        realized_profit_usd (int | Unset):
        sell_amount_lamports (int | Unset):
        sell_amount_usd (int | Unset):
        sold_gt_bought_sells (int | Unset):
        swap_count (int | Unset):
        token_num (int | Unset):
        total_buys (int | Unset):
        total_fees (int | Unset): TotalFees is the window's execution costs other than tips: network fees
            (base + priority) counted once per transaction, plus venue, platform and
            cashback-on-top fees.
        total_fees_usd (int | Unset):
        total_sells (int | Unset):
        total_tips (int | Unset): TotalTips — builder/MEV tips paid on the window's successful txs.
        total_tips_usd (int | Unset):
        trader (str | Unset):
        uncovered_proceeds_lamports (int | Unset): UncoveredProceeds — proceeds of the window's sells of tokens with no
            known cost (received by transfer, or beyond the recorded buys). Neither
            RealizedProfit nor NetRealizedProfit includes them.
        uncovered_proceeds_usd (int | Unset):
        win_profit (int | Unset):
        win_profit_usd (int | Unset):
        win_sells (int | Unset):
        win_sells_usd (int | Unset):
        window_label (str | Unset):
        winrate (float | Unset):
        winrate_usd (float | Unset):
    """

    arb_pnl_lamports: int | Unset = UNSET
    arb_pnl_usd: int | Unset = UNSET
    arb_tx_ratio: float | Unset = UNSET
    buy_amount_lamports: int | Unset = UNSET
    buy_amount_usd: int | Unset = UNSET
    buy_sell_ratio: float | Unset = UNSET
    cashback_claimed_lamports: int | Unset = UNSET
    cashback_claimed_usd: int | Unset = UNSET
    didnt_buy_sells: int | Unset = UNSET
    failed_cost_lamports: int | Unset = UNSET
    failed_cost_usd: int | Unset = UNSET
    loss_profit: int | Unset = UNSET
    loss_profit_usd: int | Unset = UNSET
    loss_sells: int | Unset = UNSET
    loss_sells_usd: int | Unset = UNSET
    net_realized_profit: int | Unset = UNSET
    net_realized_profit_usd: int | Unset = UNSET
    realized_profit: int | Unset = UNSET
    realized_profit_usd: int | Unset = UNSET
    sell_amount_lamports: int | Unset = UNSET
    sell_amount_usd: int | Unset = UNSET
    sold_gt_bought_sells: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    token_num: int | Unset = UNSET
    total_buys: int | Unset = UNSET
    total_fees: int | Unset = UNSET
    total_fees_usd: int | Unset = UNSET
    total_sells: int | Unset = UNSET
    total_tips: int | Unset = UNSET
    total_tips_usd: int | Unset = UNSET
    trader: str | Unset = UNSET
    uncovered_proceeds_lamports: int | Unset = UNSET
    uncovered_proceeds_usd: int | Unset = UNSET
    win_profit: int | Unset = UNSET
    win_profit_usd: int | Unset = UNSET
    win_sells: int | Unset = UNSET
    win_sells_usd: int | Unset = UNSET
    window_label: str | Unset = UNSET
    winrate: float | Unset = UNSET
    winrate_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_pnl_lamports = self.arb_pnl_lamports

        arb_pnl_usd = self.arb_pnl_usd

        arb_tx_ratio = self.arb_tx_ratio

        buy_amount_lamports = self.buy_amount_lamports

        buy_amount_usd = self.buy_amount_usd

        buy_sell_ratio = self.buy_sell_ratio

        cashback_claimed_lamports = self.cashback_claimed_lamports

        cashback_claimed_usd = self.cashback_claimed_usd

        didnt_buy_sells = self.didnt_buy_sells

        failed_cost_lamports = self.failed_cost_lamports

        failed_cost_usd = self.failed_cost_usd

        loss_profit = self.loss_profit

        loss_profit_usd = self.loss_profit_usd

        loss_sells = self.loss_sells

        loss_sells_usd = self.loss_sells_usd

        net_realized_profit = self.net_realized_profit

        net_realized_profit_usd = self.net_realized_profit_usd

        realized_profit = self.realized_profit

        realized_profit_usd = self.realized_profit_usd

        sell_amount_lamports = self.sell_amount_lamports

        sell_amount_usd = self.sell_amount_usd

        sold_gt_bought_sells = self.sold_gt_bought_sells

        swap_count = self.swap_count

        token_num = self.token_num

        total_buys = self.total_buys

        total_fees = self.total_fees

        total_fees_usd = self.total_fees_usd

        total_sells = self.total_sells

        total_tips = self.total_tips

        total_tips_usd = self.total_tips_usd

        trader = self.trader

        uncovered_proceeds_lamports = self.uncovered_proceeds_lamports

        uncovered_proceeds_usd = self.uncovered_proceeds_usd

        win_profit = self.win_profit

        win_profit_usd = self.win_profit_usd

        win_sells = self.win_sells

        win_sells_usd = self.win_sells_usd

        window_label = self.window_label

        winrate = self.winrate

        winrate_usd = self.winrate_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_pnl_lamports is not UNSET:
            field_dict["arb_pnl_lamports"] = arb_pnl_lamports
        if arb_pnl_usd is not UNSET:
            field_dict["arb_pnl_usd"] = arb_pnl_usd
        if arb_tx_ratio is not UNSET:
            field_dict["arb_tx_ratio"] = arb_tx_ratio
        if buy_amount_lamports is not UNSET:
            field_dict["buy_amount_lamports"] = buy_amount_lamports
        if buy_amount_usd is not UNSET:
            field_dict["buy_amount_usd"] = buy_amount_usd
        if buy_sell_ratio is not UNSET:
            field_dict["buy_sell_ratio"] = buy_sell_ratio
        if cashback_claimed_lamports is not UNSET:
            field_dict["cashback_claimed_lamports"] = cashback_claimed_lamports
        if cashback_claimed_usd is not UNSET:
            field_dict["cashback_claimed_usd"] = cashback_claimed_usd
        if didnt_buy_sells is not UNSET:
            field_dict["didnt_buy_sells"] = didnt_buy_sells
        if failed_cost_lamports is not UNSET:
            field_dict["failed_cost_lamports"] = failed_cost_lamports
        if failed_cost_usd is not UNSET:
            field_dict["failed_cost_usd"] = failed_cost_usd
        if loss_profit is not UNSET:
            field_dict["loss_profit"] = loss_profit
        if loss_profit_usd is not UNSET:
            field_dict["loss_profit_usd"] = loss_profit_usd
        if loss_sells is not UNSET:
            field_dict["loss_sells"] = loss_sells
        if loss_sells_usd is not UNSET:
            field_dict["loss_sells_usd"] = loss_sells_usd
        if net_realized_profit is not UNSET:
            field_dict["net_realized_profit"] = net_realized_profit
        if net_realized_profit_usd is not UNSET:
            field_dict["net_realized_profit_usd"] = net_realized_profit_usd
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if realized_profit_usd is not UNSET:
            field_dict["realized_profit_usd"] = realized_profit_usd
        if sell_amount_lamports is not UNSET:
            field_dict["sell_amount_lamports"] = sell_amount_lamports
        if sell_amount_usd is not UNSET:
            field_dict["sell_amount_usd"] = sell_amount_usd
        if sold_gt_bought_sells is not UNSET:
            field_dict["sold_gt_bought_sells"] = sold_gt_bought_sells
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if token_num is not UNSET:
            field_dict["token_num"] = token_num
        if total_buys is not UNSET:
            field_dict["total_buys"] = total_buys
        if total_fees is not UNSET:
            field_dict["total_fees"] = total_fees
        if total_fees_usd is not UNSET:
            field_dict["total_fees_usd"] = total_fees_usd
        if total_sells is not UNSET:
            field_dict["total_sells"] = total_sells
        if total_tips is not UNSET:
            field_dict["total_tips"] = total_tips
        if total_tips_usd is not UNSET:
            field_dict["total_tips_usd"] = total_tips_usd
        if trader is not UNSET:
            field_dict["trader"] = trader
        if uncovered_proceeds_lamports is not UNSET:
            field_dict["uncovered_proceeds_lamports"] = uncovered_proceeds_lamports
        if uncovered_proceeds_usd is not UNSET:
            field_dict["uncovered_proceeds_usd"] = uncovered_proceeds_usd
        if win_profit is not UNSET:
            field_dict["win_profit"] = win_profit
        if win_profit_usd is not UNSET:
            field_dict["win_profit_usd"] = win_profit_usd
        if win_sells is not UNSET:
            field_dict["win_sells"] = win_sells
        if win_sells_usd is not UNSET:
            field_dict["win_sells_usd"] = win_sells_usd
        if window_label is not UNSET:
            field_dict["window_label"] = window_label
        if winrate is not UNSET:
            field_dict["winrate"] = winrate
        if winrate_usd is not UNSET:
            field_dict["winrate_usd"] = winrate_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arb_pnl_lamports = d.pop("arb_pnl_lamports", UNSET)

        arb_pnl_usd = d.pop("arb_pnl_usd", UNSET)

        arb_tx_ratio = d.pop("arb_tx_ratio", UNSET)

        buy_amount_lamports = d.pop("buy_amount_lamports", UNSET)

        buy_amount_usd = d.pop("buy_amount_usd", UNSET)

        buy_sell_ratio = d.pop("buy_sell_ratio", UNSET)

        cashback_claimed_lamports = d.pop("cashback_claimed_lamports", UNSET)

        cashback_claimed_usd = d.pop("cashback_claimed_usd", UNSET)

        didnt_buy_sells = d.pop("didnt_buy_sells", UNSET)

        failed_cost_lamports = d.pop("failed_cost_lamports", UNSET)

        failed_cost_usd = d.pop("failed_cost_usd", UNSET)

        loss_profit = d.pop("loss_profit", UNSET)

        loss_profit_usd = d.pop("loss_profit_usd", UNSET)

        loss_sells = d.pop("loss_sells", UNSET)

        loss_sells_usd = d.pop("loss_sells_usd", UNSET)

        net_realized_profit = d.pop("net_realized_profit", UNSET)

        net_realized_profit_usd = d.pop("net_realized_profit_usd", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        realized_profit_usd = d.pop("realized_profit_usd", UNSET)

        sell_amount_lamports = d.pop("sell_amount_lamports", UNSET)

        sell_amount_usd = d.pop("sell_amount_usd", UNSET)

        sold_gt_bought_sells = d.pop("sold_gt_bought_sells", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        token_num = d.pop("token_num", UNSET)

        total_buys = d.pop("total_buys", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        total_fees_usd = d.pop("total_fees_usd", UNSET)

        total_sells = d.pop("total_sells", UNSET)

        total_tips = d.pop("total_tips", UNSET)

        total_tips_usd = d.pop("total_tips_usd", UNSET)

        trader = d.pop("trader", UNSET)

        uncovered_proceeds_lamports = d.pop("uncovered_proceeds_lamports", UNSET)

        uncovered_proceeds_usd = d.pop("uncovered_proceeds_usd", UNSET)

        win_profit = d.pop("win_profit", UNSET)

        win_profit_usd = d.pop("win_profit_usd", UNSET)

        win_sells = d.pop("win_sells", UNSET)

        win_sells_usd = d.pop("win_sells_usd", UNSET)

        window_label = d.pop("window_label", UNSET)

        winrate = d.pop("winrate", UNSET)

        winrate_usd = d.pop("winrate_usd", UNSET)

        pulsight_internal_core_domain_aggregator_trader_period_stats_row = cls(
            arb_pnl_lamports=arb_pnl_lamports,
            arb_pnl_usd=arb_pnl_usd,
            arb_tx_ratio=arb_tx_ratio,
            buy_amount_lamports=buy_amount_lamports,
            buy_amount_usd=buy_amount_usd,
            buy_sell_ratio=buy_sell_ratio,
            cashback_claimed_lamports=cashback_claimed_lamports,
            cashback_claimed_usd=cashback_claimed_usd,
            didnt_buy_sells=didnt_buy_sells,
            failed_cost_lamports=failed_cost_lamports,
            failed_cost_usd=failed_cost_usd,
            loss_profit=loss_profit,
            loss_profit_usd=loss_profit_usd,
            loss_sells=loss_sells,
            loss_sells_usd=loss_sells_usd,
            net_realized_profit=net_realized_profit,
            net_realized_profit_usd=net_realized_profit_usd,
            realized_profit=realized_profit,
            realized_profit_usd=realized_profit_usd,
            sell_amount_lamports=sell_amount_lamports,
            sell_amount_usd=sell_amount_usd,
            sold_gt_bought_sells=sold_gt_bought_sells,
            swap_count=swap_count,
            token_num=token_num,
            total_buys=total_buys,
            total_fees=total_fees,
            total_fees_usd=total_fees_usd,
            total_sells=total_sells,
            total_tips=total_tips,
            total_tips_usd=total_tips_usd,
            trader=trader,
            uncovered_proceeds_lamports=uncovered_proceeds_lamports,
            uncovered_proceeds_usd=uncovered_proceeds_usd,
            win_profit=win_profit,
            win_profit_usd=win_profit_usd,
            win_sells=win_sells,
            win_sells_usd=win_sells_usd,
            window_label=window_label,
            winrate=winrate,
            winrate_usd=winrate_usd,
        )

        pulsight_internal_core_domain_aggregator_trader_period_stats_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trader_period_stats_row

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
