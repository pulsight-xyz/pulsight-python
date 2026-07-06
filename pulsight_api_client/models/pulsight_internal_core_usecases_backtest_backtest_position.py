from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestPosition")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestPosition:
    """
    Attributes:
        cost_basis_sol (float | Unset):
        exit_value_sol (float | Unset):
        final_price_sol (float | Unset): FinalPriceSol is the last candle mid (SOL/token), for reference next to
            the discounted exit value.
        mint (str | Unset):
        pool_state (str | Unset): PoolState flags the exit liquidity used to value the position:
            "ok" (priced into a live pool), "drained" (pool empty → unrealizable,
            ~total loss), or "unknown" (no pool snapshot → valued at raw mid).
        remaining_tokens (float | Unset):
        unrealized_pnl_sol (float | Unset):
    """

    cost_basis_sol: float | Unset = UNSET
    exit_value_sol: float | Unset = UNSET
    final_price_sol: float | Unset = UNSET
    mint: str | Unset = UNSET
    pool_state: str | Unset = UNSET
    remaining_tokens: float | Unset = UNSET
    unrealized_pnl_sol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_basis_sol = self.cost_basis_sol

        exit_value_sol = self.exit_value_sol

        final_price_sol = self.final_price_sol

        mint = self.mint

        pool_state = self.pool_state

        remaining_tokens = self.remaining_tokens

        unrealized_pnl_sol = self.unrealized_pnl_sol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_basis_sol is not UNSET:
            field_dict["cost_basis_sol"] = cost_basis_sol
        if exit_value_sol is not UNSET:
            field_dict["exit_value_sol"] = exit_value_sol
        if final_price_sol is not UNSET:
            field_dict["final_price_sol"] = final_price_sol
        if mint is not UNSET:
            field_dict["mint"] = mint
        if pool_state is not UNSET:
            field_dict["pool_state"] = pool_state
        if remaining_tokens is not UNSET:
            field_dict["remaining_tokens"] = remaining_tokens
        if unrealized_pnl_sol is not UNSET:
            field_dict["unrealized_pnl_sol"] = unrealized_pnl_sol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_basis_sol = d.pop("cost_basis_sol", UNSET)

        exit_value_sol = d.pop("exit_value_sol", UNSET)

        final_price_sol = d.pop("final_price_sol", UNSET)

        mint = d.pop("mint", UNSET)

        pool_state = d.pop("pool_state", UNSET)

        remaining_tokens = d.pop("remaining_tokens", UNSET)

        unrealized_pnl_sol = d.pop("unrealized_pnl_sol", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_position = cls(
            cost_basis_sol=cost_basis_sol,
            exit_value_sol=exit_value_sol,
            final_price_sol=final_price_sol,
            mint=mint,
            pool_state=pool_state,
            remaining_tokens=remaining_tokens,
            unrealized_pnl_sol=unrealized_pnl_sol,
        )

        pulsight_internal_core_usecases_backtest_backtest_position.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_position

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
