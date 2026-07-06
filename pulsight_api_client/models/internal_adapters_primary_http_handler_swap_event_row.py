from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerSwapEventRow")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerSwapEventRow:
    """
    Attributes:
        amount_in (float | Unset):
        amount_out (float | Unset):
        arb_pnl_lamports (int | Unset):
        dex (str | Unset):
        fee (int | Unset):
        is_arb (bool | Unset):
        is_buy (bool | Unset):
        mint (str | Unset):
        pool (str | Unset):
        priority_fee_lamports (int | Unset):
        quote_mint (str | Unset):
        realized_profit (int | Unset):
        signature (str | Unset):
        sold_more_than_bought (bool | Unset):
        sold_without_buy (bool | Unset):
        tip_lamports (int | Unset):
        tip_service (str | Unset):
        trader (str | Unset):
        ts (int | Unset):
        virtual_sol (int | Unset): null — not in Pulsight SwapRow
        virtual_token (str | Unset): null — not in Pulsight SwapRow
    """

    amount_in: float | Unset = UNSET
    amount_out: float | Unset = UNSET
    arb_pnl_lamports: int | Unset = UNSET
    dex: str | Unset = UNSET
    fee: int | Unset = UNSET
    is_arb: bool | Unset = UNSET
    is_buy: bool | Unset = UNSET
    mint: str | Unset = UNSET
    pool: str | Unset = UNSET
    priority_fee_lamports: int | Unset = UNSET
    quote_mint: str | Unset = UNSET
    realized_profit: int | Unset = UNSET
    signature: str | Unset = UNSET
    sold_more_than_bought: bool | Unset = UNSET
    sold_without_buy: bool | Unset = UNSET
    tip_lamports: int | Unset = UNSET
    tip_service: str | Unset = UNSET
    trader: str | Unset = UNSET
    ts: int | Unset = UNSET
    virtual_sol: int | Unset = UNSET
    virtual_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_in = self.amount_in

        amount_out = self.amount_out

        arb_pnl_lamports = self.arb_pnl_lamports

        dex = self.dex

        fee = self.fee

        is_arb = self.is_arb

        is_buy = self.is_buy

        mint = self.mint

        pool = self.pool

        priority_fee_lamports = self.priority_fee_lamports

        quote_mint = self.quote_mint

        realized_profit = self.realized_profit

        signature = self.signature

        sold_more_than_bought = self.sold_more_than_bought

        sold_without_buy = self.sold_without_buy

        tip_lamports = self.tip_lamports

        tip_service = self.tip_service

        trader = self.trader

        ts = self.ts

        virtual_sol = self.virtual_sol

        virtual_token = self.virtual_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_in is not UNSET:
            field_dict["amount_in"] = amount_in
        if amount_out is not UNSET:
            field_dict["amount_out"] = amount_out
        if arb_pnl_lamports is not UNSET:
            field_dict["arb_pnl_lamports"] = arb_pnl_lamports
        if dex is not UNSET:
            field_dict["dex"] = dex
        if fee is not UNSET:
            field_dict["fee"] = fee
        if is_arb is not UNSET:
            field_dict["is_arb"] = is_arb
        if is_buy is not UNSET:
            field_dict["is_buy"] = is_buy
        if mint is not UNSET:
            field_dict["mint"] = mint
        if pool is not UNSET:
            field_dict["pool"] = pool
        if priority_fee_lamports is not UNSET:
            field_dict["priority_fee_lamports"] = priority_fee_lamports
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if signature is not UNSET:
            field_dict["signature"] = signature
        if sold_more_than_bought is not UNSET:
            field_dict["sold_more_than_bought"] = sold_more_than_bought
        if sold_without_buy is not UNSET:
            field_dict["sold_without_buy"] = sold_without_buy
        if tip_lamports is not UNSET:
            field_dict["tip_lamports"] = tip_lamports
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service
        if trader is not UNSET:
            field_dict["trader"] = trader
        if ts is not UNSET:
            field_dict["ts"] = ts
        if virtual_sol is not UNSET:
            field_dict["virtual_sol"] = virtual_sol
        if virtual_token is not UNSET:
            field_dict["virtual_token"] = virtual_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_in = d.pop("amount_in", UNSET)

        amount_out = d.pop("amount_out", UNSET)

        arb_pnl_lamports = d.pop("arb_pnl_lamports", UNSET)

        dex = d.pop("dex", UNSET)

        fee = d.pop("fee", UNSET)

        is_arb = d.pop("is_arb", UNSET)

        is_buy = d.pop("is_buy", UNSET)

        mint = d.pop("mint", UNSET)

        pool = d.pop("pool", UNSET)

        priority_fee_lamports = d.pop("priority_fee_lamports", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        signature = d.pop("signature", UNSET)

        sold_more_than_bought = d.pop("sold_more_than_bought", UNSET)

        sold_without_buy = d.pop("sold_without_buy", UNSET)

        tip_lamports = d.pop("tip_lamports", UNSET)

        tip_service = d.pop("tip_service", UNSET)

        trader = d.pop("trader", UNSET)

        ts = d.pop("ts", UNSET)

        virtual_sol = d.pop("virtual_sol", UNSET)

        virtual_token = d.pop("virtual_token", UNSET)

        internal_adapters_primary_http_handler_swap_event_row = cls(
            amount_in=amount_in,
            amount_out=amount_out,
            arb_pnl_lamports=arb_pnl_lamports,
            dex=dex,
            fee=fee,
            is_arb=is_arb,
            is_buy=is_buy,
            mint=mint,
            pool=pool,
            priority_fee_lamports=priority_fee_lamports,
            quote_mint=quote_mint,
            realized_profit=realized_profit,
            signature=signature,
            sold_more_than_bought=sold_more_than_bought,
            sold_without_buy=sold_without_buy,
            tip_lamports=tip_lamports,
            tip_service=tip_service,
            trader=trader,
            ts=ts,
            virtual_sol=virtual_sol,
            virtual_token=virtual_token,
        )

        internal_adapters_primary_http_handler_swap_event_row.additional_properties = d
        return internal_adapters_primary_http_handler_swap_event_row

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
