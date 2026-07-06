from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderPeriodStatsRow:
    """
    Attributes:
        arb_tx_ratio (float | Unset): ArbTxRatio is the fraction (0..1) of the window's swaps that were
            arbitrage txs (is_arb). 0 when the window has no swaps.
        buy_amount_lamports (int | Unset):
        buy_sell_ratio (float | Unset):
        didnt_buy_sells (int | Unset): DidntBuySells / SoldGtBoughtSells count the window's uncovered
            sells: countIf(sold_without_buy) and countIf(sold_more_than_bought)
            over `swaps`. Replaces the retired phantom proceeds split (CA
            migration 000018_remove_phantom_tracking).
        loss_profit (int | Unset):
        loss_sells (int | Unset):
        realized_profit (int | Unset):
        sell_amount_lamports (int | Unset):
        sold_gt_bought_sells (int | Unset):
        swap_count (int | Unset):
        token_num (int | Unset):
        total_buys (int | Unset): Count fields are int64, not int: periodStatsOne casts them with
            toInt64() in SQL, and clickhouse-go scans an Int64 column only into
            *int64 (it rejects *int with code-typed "try using *int64"). JSON
            serialisation is identical either way.
        total_fees (int | Unset):
        total_sells (int | Unset):
        trader (str | Unset):
        win_profit (int | Unset):
        win_sells (int | Unset):
        window_label (str | Unset):
        winrate (float | Unset):
    """

    arb_tx_ratio: float | Unset = UNSET
    buy_amount_lamports: int | Unset = UNSET
    buy_sell_ratio: float | Unset = UNSET
    didnt_buy_sells: int | Unset = UNSET
    loss_profit: int | Unset = UNSET
    loss_sells: int | Unset = UNSET
    realized_profit: int | Unset = UNSET
    sell_amount_lamports: int | Unset = UNSET
    sold_gt_bought_sells: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    token_num: int | Unset = UNSET
    total_buys: int | Unset = UNSET
    total_fees: int | Unset = UNSET
    total_sells: int | Unset = UNSET
    trader: str | Unset = UNSET
    win_profit: int | Unset = UNSET
    win_sells: int | Unset = UNSET
    window_label: str | Unset = UNSET
    winrate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_tx_ratio = self.arb_tx_ratio

        buy_amount_lamports = self.buy_amount_lamports

        buy_sell_ratio = self.buy_sell_ratio

        didnt_buy_sells = self.didnt_buy_sells

        loss_profit = self.loss_profit

        loss_sells = self.loss_sells

        realized_profit = self.realized_profit

        sell_amount_lamports = self.sell_amount_lamports

        sold_gt_bought_sells = self.sold_gt_bought_sells

        swap_count = self.swap_count

        token_num = self.token_num

        total_buys = self.total_buys

        total_fees = self.total_fees

        total_sells = self.total_sells

        trader = self.trader

        win_profit = self.win_profit

        win_sells = self.win_sells

        window_label = self.window_label

        winrate = self.winrate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_tx_ratio is not UNSET:
            field_dict["arb_tx_ratio"] = arb_tx_ratio
        if buy_amount_lamports is not UNSET:
            field_dict["buy_amount_lamports"] = buy_amount_lamports
        if buy_sell_ratio is not UNSET:
            field_dict["buy_sell_ratio"] = buy_sell_ratio
        if didnt_buy_sells is not UNSET:
            field_dict["didnt_buy_sells"] = didnt_buy_sells
        if loss_profit is not UNSET:
            field_dict["loss_profit"] = loss_profit
        if loss_sells is not UNSET:
            field_dict["loss_sells"] = loss_sells
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if sell_amount_lamports is not UNSET:
            field_dict["sell_amount_lamports"] = sell_amount_lamports
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
        if total_sells is not UNSET:
            field_dict["total_sells"] = total_sells
        if trader is not UNSET:
            field_dict["trader"] = trader
        if win_profit is not UNSET:
            field_dict["win_profit"] = win_profit
        if win_sells is not UNSET:
            field_dict["win_sells"] = win_sells
        if window_label is not UNSET:
            field_dict["window_label"] = window_label
        if winrate is not UNSET:
            field_dict["winrate"] = winrate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arb_tx_ratio = d.pop("arb_tx_ratio", UNSET)

        buy_amount_lamports = d.pop("buy_amount_lamports", UNSET)

        buy_sell_ratio = d.pop("buy_sell_ratio", UNSET)

        didnt_buy_sells = d.pop("didnt_buy_sells", UNSET)

        loss_profit = d.pop("loss_profit", UNSET)

        loss_sells = d.pop("loss_sells", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        sell_amount_lamports = d.pop("sell_amount_lamports", UNSET)

        sold_gt_bought_sells = d.pop("sold_gt_bought_sells", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        token_num = d.pop("token_num", UNSET)

        total_buys = d.pop("total_buys", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        total_sells = d.pop("total_sells", UNSET)

        trader = d.pop("trader", UNSET)

        win_profit = d.pop("win_profit", UNSET)

        win_sells = d.pop("win_sells", UNSET)

        window_label = d.pop("window_label", UNSET)

        winrate = d.pop("winrate", UNSET)

        pulsight_internal_core_domain_aggregator_trader_period_stats_row = cls(
            arb_tx_ratio=arb_tx_ratio,
            buy_amount_lamports=buy_amount_lamports,
            buy_sell_ratio=buy_sell_ratio,
            didnt_buy_sells=didnt_buy_sells,
            loss_profit=loss_profit,
            loss_sells=loss_sells,
            realized_profit=realized_profit,
            sell_amount_lamports=sell_amount_lamports,
            sold_gt_bought_sells=sold_gt_bought_sells,
            swap_count=swap_count,
            token_num=token_num,
            total_buys=total_buys,
            total_fees=total_fees,
            total_sells=total_sells,
            trader=trader,
            win_profit=win_profit,
            win_sells=win_sells,
            window_label=window_label,
            winrate=winrate,
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
