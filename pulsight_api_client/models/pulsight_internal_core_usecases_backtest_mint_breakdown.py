from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestMintBreakdown")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestMintBreakdown:
    """
    Attributes:
        buys (int | Unset):
        declines (int | Unset): Declines counts the target swaps on the mint a copy exec wanted to act
            on but did not fill.
        fees_sol (float | Unset): FeesSol is the swap, tip, platform and transfer fees its fills paid.
        first_ts (str | Unset):
        held_at_end (bool | Unset): HeldAtEnd reports a position still open when the run ended.
        last_ts (str | Unset):
        mint (str | Unset):
        pool (str | Unset): Pool is the pool most of the mint's fills priced on.
        realized_pnl_sol (float | Unset):
        sells (int | Unset):
    """

    buys: int | Unset = UNSET
    declines: int | Unset = UNSET
    fees_sol: float | Unset = UNSET
    first_ts: str | Unset = UNSET
    held_at_end: bool | Unset = UNSET
    last_ts: str | Unset = UNSET
    mint: str | Unset = UNSET
    pool: str | Unset = UNSET
    realized_pnl_sol: float | Unset = UNSET
    sells: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buys = self.buys

        declines = self.declines

        fees_sol = self.fees_sol

        first_ts = self.first_ts

        held_at_end = self.held_at_end

        last_ts = self.last_ts

        mint = self.mint

        pool = self.pool

        realized_pnl_sol = self.realized_pnl_sol

        sells = self.sells

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buys is not UNSET:
            field_dict["buys"] = buys
        if declines is not UNSET:
            field_dict["declines"] = declines
        if fees_sol is not UNSET:
            field_dict["fees_sol"] = fees_sol
        if first_ts is not UNSET:
            field_dict["first_ts"] = first_ts
        if held_at_end is not UNSET:
            field_dict["held_at_end"] = held_at_end
        if last_ts is not UNSET:
            field_dict["last_ts"] = last_ts
        if mint is not UNSET:
            field_dict["mint"] = mint
        if pool is not UNSET:
            field_dict["pool"] = pool
        if realized_pnl_sol is not UNSET:
            field_dict["realized_pnl_sol"] = realized_pnl_sol
        if sells is not UNSET:
            field_dict["sells"] = sells

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        buys = d.pop("buys", UNSET)

        declines = d.pop("declines", UNSET)

        fees_sol = d.pop("fees_sol", UNSET)

        first_ts = d.pop("first_ts", UNSET)

        held_at_end = d.pop("held_at_end", UNSET)

        last_ts = d.pop("last_ts", UNSET)

        mint = d.pop("mint", UNSET)

        pool = d.pop("pool", UNSET)

        realized_pnl_sol = d.pop("realized_pnl_sol", UNSET)

        sells = d.pop("sells", UNSET)

        pulsight_internal_core_usecases_backtest_mint_breakdown = cls(
            buys=buys,
            declines=declines,
            fees_sol=fees_sol,
            first_ts=first_ts,
            held_at_end=held_at_end,
            last_ts=last_ts,
            mint=mint,
            pool=pool,
            realized_pnl_sol=realized_pnl_sol,
            sells=sells,
        )

        pulsight_internal_core_usecases_backtest_mint_breakdown.additional_properties = d
        return pulsight_internal_core_usecases_backtest_mint_breakdown

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
