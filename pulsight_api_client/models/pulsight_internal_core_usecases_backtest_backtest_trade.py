from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_usecases_backtest_side import (
    PulsightInternalCoreUsecasesBacktestSide,
)
from ..models.pulsight_internal_core_usecases_backtest_trade_source import (
    PulsightInternalCoreUsecasesBacktestTradeSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestTrade")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestTrade:
    """
    Attributes:
        backtest_id (str | Unset):
        fee_sol (float | Unset):
        idx (int | Unset):
        mint (str | Unset):
        pool_sol_at_trigger (float | Unset):
        price_impact_pct (float | Unset): PriceImpactPct is OUR own price impact on this fill, as a percent of the
            mid price (size / pool_sol, the constant-product average-fill premium).
            Nil when the engine had no pool snapshot at the tick (impact unknown →
            pricing degraded to slippage-only). A buy moves price up, a sell down;
            the magnitude is recorded either way.
        price_per_token (float | Unset):
        realized_pnl_sol (float | Unset):
        side (PulsightInternalCoreUsecasesBacktestSide | Unset):
        sol_amount (float | Unset):
        source (PulsightInternalCoreUsecasesBacktestTradeSource | Unset):
        target_price_impact_pct (float | Unset): TargetPriceImpactPct is the MIRRORED trader's own price impact on the
            swap we copied — set only on copy trades that executed at the same
            timestamp as the target (a true 1:1 mirror), where the target's move is
            folded into our fill price. Nil for emit trades and delayed copies.
        tip_sol (float | Unset):
        token_amount (float | Unset):
        triggering_swap_sig (str | Unset):
        ts (str | Unset):
    """

    backtest_id: str | Unset = UNSET
    fee_sol: float | Unset = UNSET
    idx: int | Unset = UNSET
    mint: str | Unset = UNSET
    pool_sol_at_trigger: float | Unset = UNSET
    price_impact_pct: float | Unset = UNSET
    price_per_token: float | Unset = UNSET
    realized_pnl_sol: float | Unset = UNSET
    side: PulsightInternalCoreUsecasesBacktestSide | Unset = UNSET
    sol_amount: float | Unset = UNSET
    source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset = UNSET
    target_price_impact_pct: float | Unset = UNSET
    tip_sol: float | Unset = UNSET
    token_amount: float | Unset = UNSET
    triggering_swap_sig: str | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backtest_id = self.backtest_id

        fee_sol = self.fee_sol

        idx = self.idx

        mint = self.mint

        pool_sol_at_trigger = self.pool_sol_at_trigger

        price_impact_pct = self.price_impact_pct

        price_per_token = self.price_per_token

        realized_pnl_sol = self.realized_pnl_sol

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        sol_amount = self.sol_amount

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        target_price_impact_pct = self.target_price_impact_pct

        tip_sol = self.tip_sol

        token_amount = self.token_amount

        triggering_swap_sig = self.triggering_swap_sig

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backtest_id is not UNSET:
            field_dict["backtest_id"] = backtest_id
        if fee_sol is not UNSET:
            field_dict["fee_sol"] = fee_sol
        if idx is not UNSET:
            field_dict["idx"] = idx
        if mint is not UNSET:
            field_dict["mint"] = mint
        if pool_sol_at_trigger is not UNSET:
            field_dict["pool_sol_at_trigger"] = pool_sol_at_trigger
        if price_impact_pct is not UNSET:
            field_dict["price_impact_pct"] = price_impact_pct
        if price_per_token is not UNSET:
            field_dict["price_per_token"] = price_per_token
        if realized_pnl_sol is not UNSET:
            field_dict["realized_pnl_sol"] = realized_pnl_sol
        if side is not UNSET:
            field_dict["side"] = side
        if sol_amount is not UNSET:
            field_dict["sol_amount"] = sol_amount
        if source is not UNSET:
            field_dict["source"] = source
        if target_price_impact_pct is not UNSET:
            field_dict["target_price_impact_pct"] = target_price_impact_pct
        if tip_sol is not UNSET:
            field_dict["tip_sol"] = tip_sol
        if token_amount is not UNSET:
            field_dict["token_amount"] = token_amount
        if triggering_swap_sig is not UNSET:
            field_dict["triggering_swap_sig"] = triggering_swap_sig
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backtest_id = d.pop("backtest_id", UNSET)

        fee_sol = d.pop("fee_sol", UNSET)

        idx = d.pop("idx", UNSET)

        mint = d.pop("mint", UNSET)

        pool_sol_at_trigger = d.pop("pool_sol_at_trigger", UNSET)

        price_impact_pct = d.pop("price_impact_pct", UNSET)

        price_per_token = d.pop("price_per_token", UNSET)

        realized_pnl_sol = d.pop("realized_pnl_sol", UNSET)

        _side = d.pop("side", UNSET)
        side: PulsightInternalCoreUsecasesBacktestSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PulsightInternalCoreUsecasesBacktestSide(_side)

        sol_amount = d.pop("sol_amount", UNSET)

        _source = d.pop("source", UNSET)
        source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PulsightInternalCoreUsecasesBacktestTradeSource(_source)

        target_price_impact_pct = d.pop("target_price_impact_pct", UNSET)

        tip_sol = d.pop("tip_sol", UNSET)

        token_amount = d.pop("token_amount", UNSET)

        triggering_swap_sig = d.pop("triggering_swap_sig", UNSET)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_trade = cls(
            backtest_id=backtest_id,
            fee_sol=fee_sol,
            idx=idx,
            mint=mint,
            pool_sol_at_trigger=pool_sol_at_trigger,
            price_impact_pct=price_impact_pct,
            price_per_token=price_per_token,
            realized_pnl_sol=realized_pnl_sol,
            side=side,
            sol_amount=sol_amount,
            source=source,
            target_price_impact_pct=target_price_impact_pct,
            tip_sol=tip_sol,
            token_amount=token_amount,
            triggering_swap_sig=triggering_swap_sig,
            ts=ts,
        )

        pulsight_internal_core_usecases_backtest_backtest_trade.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_trade

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
