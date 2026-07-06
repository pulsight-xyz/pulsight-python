from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerTokensRow")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerTokensRow:
    """
    Attributes:
        buy_tx_count (int | Unset):
        cost_basis_lamports (str | Unset):
        first_buy_ts (str | Unset):
        holding_pnl_lamports (float | Unset):
        last_active_ts (str | Unset):
        mint (str | Unset):
        mint_decimals (int | Unset):
        mint_logo_uri (str | Unset):
        mint_name (str | Unset):
        mint_symbol (str | Unset):
        realized_profit (float | Unset):
        sell_tx_count (int | Unset):
        token_balance (str | Unset):
        total_fees (float | Unset):
        total_invested (float | Unset):
        trader (str | Unset):
        updated_at (str | Unset):
    """

    buy_tx_count: int | Unset = UNSET
    cost_basis_lamports: str | Unset = UNSET
    first_buy_ts: str | Unset = UNSET
    holding_pnl_lamports: float | Unset = UNSET
    last_active_ts: str | Unset = UNSET
    mint: str | Unset = UNSET
    mint_decimals: int | Unset = UNSET
    mint_logo_uri: str | Unset = UNSET
    mint_name: str | Unset = UNSET
    mint_symbol: str | Unset = UNSET
    realized_profit: float | Unset = UNSET
    sell_tx_count: int | Unset = UNSET
    token_balance: str | Unset = UNSET
    total_fees: float | Unset = UNSET
    total_invested: float | Unset = UNSET
    trader: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_tx_count = self.buy_tx_count

        cost_basis_lamports = self.cost_basis_lamports

        first_buy_ts = self.first_buy_ts

        holding_pnl_lamports = self.holding_pnl_lamports

        last_active_ts = self.last_active_ts

        mint = self.mint

        mint_decimals = self.mint_decimals

        mint_logo_uri = self.mint_logo_uri

        mint_name = self.mint_name

        mint_symbol = self.mint_symbol

        realized_profit = self.realized_profit

        sell_tx_count = self.sell_tx_count

        token_balance = self.token_balance

        total_fees = self.total_fees

        total_invested = self.total_invested

        trader = self.trader

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_tx_count is not UNSET:
            field_dict["buy_tx_count"] = buy_tx_count
        if cost_basis_lamports is not UNSET:
            field_dict["cost_basis_lamports"] = cost_basis_lamports
        if first_buy_ts is not UNSET:
            field_dict["first_buy_ts"] = first_buy_ts
        if holding_pnl_lamports is not UNSET:
            field_dict["holding_pnl_lamports"] = holding_pnl_lamports
        if last_active_ts is not UNSET:
            field_dict["last_active_ts"] = last_active_ts
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mint_decimals is not UNSET:
            field_dict["mint_decimals"] = mint_decimals
        if mint_logo_uri is not UNSET:
            field_dict["mint_logo_uri"] = mint_logo_uri
        if mint_name is not UNSET:
            field_dict["mint_name"] = mint_name
        if mint_symbol is not UNSET:
            field_dict["mint_symbol"] = mint_symbol
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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buy_tx_count = d.pop("buy_tx_count", UNSET)

        cost_basis_lamports = d.pop("cost_basis_lamports", UNSET)

        first_buy_ts = d.pop("first_buy_ts", UNSET)

        holding_pnl_lamports = d.pop("holding_pnl_lamports", UNSET)

        last_active_ts = d.pop("last_active_ts", UNSET)

        mint = d.pop("mint", UNSET)

        mint_decimals = d.pop("mint_decimals", UNSET)

        mint_logo_uri = d.pop("mint_logo_uri", UNSET)

        mint_name = d.pop("mint_name", UNSET)

        mint_symbol = d.pop("mint_symbol", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        sell_tx_count = d.pop("sell_tx_count", UNSET)

        token_balance = d.pop("token_balance", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        total_invested = d.pop("total_invested", UNSET)

        trader = d.pop("trader", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        internal_adapters_primary_http_handler_tokens_row = cls(
            buy_tx_count=buy_tx_count,
            cost_basis_lamports=cost_basis_lamports,
            first_buy_ts=first_buy_ts,
            holding_pnl_lamports=holding_pnl_lamports,
            last_active_ts=last_active_ts,
            mint=mint,
            mint_decimals=mint_decimals,
            mint_logo_uri=mint_logo_uri,
            mint_name=mint_name,
            mint_symbol=mint_symbol,
            realized_profit=realized_profit,
            sell_tx_count=sell_tx_count,
            token_balance=token_balance,
            total_fees=total_fees,
            total_invested=total_invested,
            trader=trader,
            updated_at=updated_at,
        )

        internal_adapters_primary_http_handler_tokens_row.additional_properties = d
        return internal_adapters_primary_http_handler_tokens_row

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
