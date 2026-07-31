from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintTraderRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintTraderRow:
    """
    Attributes:
        arb_tx_count (int | Unset): Distinct is_arb transactions for this (trader, mint). Same rationale
            as TraderTokenPosition.ArbTxCount: shown alongside buy/sell, never
            subtracted, so lopsided counts on arbitrage wallets are legible.
        buy_tx_count (int | Unset):
        cost_basis_lamports (str | Unset):
        directional_buy_tx_count (int | Unset): Directional counts EXCLUDE arbitrage rows, so the three numbers the UI
            shows are disjoint: directional buys / directional sells / arb txs.
            Overlapping them is what made an arb wallet read "11 buys / 2 sells /
            11 arb" -- every one of those buys WAS one of the arbs. A pure
            arbitrageur now reads 0 / 0 / N, which is the truth: it never took a
            directional position in the token.

            buy_tx_count / sell_tx_count keep their original meaning (all rows,
            matching the trader_token_stats rollup that the leaderboard and its
            `f=` filters read) so nothing downstream shifts under them.
        directional_sell_tx_count (int | Unset):
        first_buy_ts (str | Unset):
        holding_pnl_lamports (int | Unset):
        is_bundler (bool | Unset):
        is_insider (bool | Unset):
        is_sniper (bool | Unset):
        label (str | Unset): Label/LabelType identify a known wallet (CEX/fee/...) from the
            admin-managed registry; empty when unknown.
        label_type (str | Unset):
        last_active_ts (str | Unset):
        pct_of_supply (float | Unset): PctOfSupply is the holder's % of circulating supply, set on the
            top-holders path (now sourced from on-chain holder_balances). nil on the
            top-traders path. IsSniper/IsBundler/IsInsider flag cohort membership
            (bundler/insider populate in phase 2 — always false until then).
        realized_profit (int | Unset):
        sell_tx_count (int | Unset):
        token_balance (str | Unset):
        total_fees (int | Unset):
        total_invested (int | Unset):
        trader (str | Unset):
    """

    arb_tx_count: int | Unset = UNSET
    buy_tx_count: int | Unset = UNSET
    cost_basis_lamports: str | Unset = UNSET
    directional_buy_tx_count: int | Unset = UNSET
    directional_sell_tx_count: int | Unset = UNSET
    first_buy_ts: str | Unset = UNSET
    holding_pnl_lamports: int | Unset = UNSET
    is_bundler: bool | Unset = UNSET
    is_insider: bool | Unset = UNSET
    is_sniper: bool | Unset = UNSET
    label: str | Unset = UNSET
    label_type: str | Unset = UNSET
    last_active_ts: str | Unset = UNSET
    pct_of_supply: float | Unset = UNSET
    realized_profit: int | Unset = UNSET
    sell_tx_count: int | Unset = UNSET
    token_balance: str | Unset = UNSET
    total_fees: int | Unset = UNSET
    total_invested: int | Unset = UNSET
    trader: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_tx_count = self.arb_tx_count

        buy_tx_count = self.buy_tx_count

        cost_basis_lamports = self.cost_basis_lamports

        directional_buy_tx_count = self.directional_buy_tx_count

        directional_sell_tx_count = self.directional_sell_tx_count

        first_buy_ts = self.first_buy_ts

        holding_pnl_lamports = self.holding_pnl_lamports

        is_bundler = self.is_bundler

        is_insider = self.is_insider

        is_sniper = self.is_sniper

        label = self.label

        label_type = self.label_type

        last_active_ts = self.last_active_ts

        pct_of_supply = self.pct_of_supply

        realized_profit = self.realized_profit

        sell_tx_count = self.sell_tx_count

        token_balance = self.token_balance

        total_fees = self.total_fees

        total_invested = self.total_invested

        trader = self.trader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_tx_count is not UNSET:
            field_dict["arb_tx_count"] = arb_tx_count
        if buy_tx_count is not UNSET:
            field_dict["buy_tx_count"] = buy_tx_count
        if cost_basis_lamports is not UNSET:
            field_dict["cost_basis_lamports"] = cost_basis_lamports
        if directional_buy_tx_count is not UNSET:
            field_dict["directional_buy_tx_count"] = directional_buy_tx_count
        if directional_sell_tx_count is not UNSET:
            field_dict["directional_sell_tx_count"] = directional_sell_tx_count
        if first_buy_ts is not UNSET:
            field_dict["first_buy_ts"] = first_buy_ts
        if holding_pnl_lamports is not UNSET:
            field_dict["holding_pnl_lamports"] = holding_pnl_lamports
        if is_bundler is not UNSET:
            field_dict["is_bundler"] = is_bundler
        if is_insider is not UNSET:
            field_dict["is_insider"] = is_insider
        if is_sniper is not UNSET:
            field_dict["is_sniper"] = is_sniper
        if label is not UNSET:
            field_dict["label"] = label
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if last_active_ts is not UNSET:
            field_dict["last_active_ts"] = last_active_ts
        if pct_of_supply is not UNSET:
            field_dict["pct_of_supply"] = pct_of_supply
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if sell_tx_count is not UNSET:
            field_dict["sell_tx_count"] = sell_tx_count
        if token_balance is not UNSET:
            field_dict["token_balance"] = token_balance
        if total_fees is not UNSET:
            field_dict["total_fees"] = total_fees
        if total_invested is not UNSET:
            field_dict["total_invested"] = total_invested
        if trader is not UNSET:
            field_dict["trader"] = trader

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arb_tx_count = d.pop("arb_tx_count", UNSET)

        buy_tx_count = d.pop("buy_tx_count", UNSET)

        cost_basis_lamports = d.pop("cost_basis_lamports", UNSET)

        directional_buy_tx_count = d.pop("directional_buy_tx_count", UNSET)

        directional_sell_tx_count = d.pop("directional_sell_tx_count", UNSET)

        first_buy_ts = d.pop("first_buy_ts", UNSET)

        holding_pnl_lamports = d.pop("holding_pnl_lamports", UNSET)

        is_bundler = d.pop("is_bundler", UNSET)

        is_insider = d.pop("is_insider", UNSET)

        is_sniper = d.pop("is_sniper", UNSET)

        label = d.pop("label", UNSET)

        label_type = d.pop("label_type", UNSET)

        last_active_ts = d.pop("last_active_ts", UNSET)

        pct_of_supply = d.pop("pct_of_supply", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        sell_tx_count = d.pop("sell_tx_count", UNSET)

        token_balance = d.pop("token_balance", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        total_invested = d.pop("total_invested", UNSET)

        trader = d.pop("trader", UNSET)

        pulsight_internal_core_domain_aggregator_mint_trader_row = cls(
            arb_tx_count=arb_tx_count,
            buy_tx_count=buy_tx_count,
            cost_basis_lamports=cost_basis_lamports,
            directional_buy_tx_count=directional_buy_tx_count,
            directional_sell_tx_count=directional_sell_tx_count,
            first_buy_ts=first_buy_ts,
            holding_pnl_lamports=holding_pnl_lamports,
            is_bundler=is_bundler,
            is_insider=is_insider,
            is_sniper=is_sniper,
            label=label,
            label_type=label_type,
            last_active_ts=last_active_ts,
            pct_of_supply=pct_of_supply,
            realized_profit=realized_profit,
            sell_tx_count=sell_tx_count,
            token_balance=token_balance,
            total_fees=total_fees,
            total_invested=total_invested,
            trader=trader,
        )

        pulsight_internal_core_domain_aggregator_mint_trader_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_trader_row

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
