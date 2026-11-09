from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestTargetMintComparison")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestTargetMintComparison:
    """
    Attributes:
        followed_pct (float | Unset): FollowedPct is our buys over the target's, in percent; absent when the
            target bought nothing.
        mint (str | Unset):
        our_buys (int | Unset):
        our_realized_sol (float | Unset):
        our_sells (int | Unset):
        target_buys (int | Unset):
        target_sells (int | Unset):
        target_sol_in (float | Unset): TargetSolIn and TargetSolOut are the SOL the target spent buying and
            received selling in the window; their difference is a cash flow, not a
            realized PnL, since a position can stay open.
        target_sol_out (float | Unset):
    """

    followed_pct: float | Unset = UNSET
    mint: str | Unset = UNSET
    our_buys: int | Unset = UNSET
    our_realized_sol: float | Unset = UNSET
    our_sells: int | Unset = UNSET
    target_buys: int | Unset = UNSET
    target_sells: int | Unset = UNSET
    target_sol_in: float | Unset = UNSET
    target_sol_out: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followed_pct = self.followed_pct

        mint = self.mint

        our_buys = self.our_buys

        our_realized_sol = self.our_realized_sol

        our_sells = self.our_sells

        target_buys = self.target_buys

        target_sells = self.target_sells

        target_sol_in = self.target_sol_in

        target_sol_out = self.target_sol_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if followed_pct is not UNSET:
            field_dict["followed_pct"] = followed_pct
        if mint is not UNSET:
            field_dict["mint"] = mint
        if our_buys is not UNSET:
            field_dict["our_buys"] = our_buys
        if our_realized_sol is not UNSET:
            field_dict["our_realized_sol"] = our_realized_sol
        if our_sells is not UNSET:
            field_dict["our_sells"] = our_sells
        if target_buys is not UNSET:
            field_dict["target_buys"] = target_buys
        if target_sells is not UNSET:
            field_dict["target_sells"] = target_sells
        if target_sol_in is not UNSET:
            field_dict["target_sol_in"] = target_sol_in
        if target_sol_out is not UNSET:
            field_dict["target_sol_out"] = target_sol_out

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        followed_pct = d.pop("followed_pct", UNSET)

        mint = d.pop("mint", UNSET)

        our_buys = d.pop("our_buys", UNSET)

        our_realized_sol = d.pop("our_realized_sol", UNSET)

        our_sells = d.pop("our_sells", UNSET)

        target_buys = d.pop("target_buys", UNSET)

        target_sells = d.pop("target_sells", UNSET)

        target_sol_in = d.pop("target_sol_in", UNSET)

        target_sol_out = d.pop("target_sol_out", UNSET)

        pulsight_internal_core_usecases_backtest_target_mint_comparison = cls(
            followed_pct=followed_pct,
            mint=mint,
            our_buys=our_buys,
            our_realized_sol=our_realized_sol,
            our_sells=our_sells,
            target_buys=target_buys,
            target_sells=target_sells,
            target_sol_in=target_sol_in,
            target_sol_out=target_sol_out,
        )

        pulsight_internal_core_usecases_backtest_target_mint_comparison.additional_properties = d
        return pulsight_internal_core_usecases_backtest_target_mint_comparison

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
