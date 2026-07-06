from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerBestRunRef")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerBestRunRef:
    """
    Attributes:
        backtest_id (str | Unset):
        pnl_sol (float | Unset):
        strategy_id (str | Unset):
        strategy_name (str | Unset):
    """

    backtest_id: str | Unset = UNSET
    pnl_sol: float | Unset = UNSET
    strategy_id: str | Unset = UNSET
    strategy_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backtest_id = self.backtest_id

        pnl_sol = self.pnl_sol

        strategy_id = self.strategy_id

        strategy_name = self.strategy_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backtest_id is not UNSET:
            field_dict["backtest_id"] = backtest_id
        if pnl_sol is not UNSET:
            field_dict["pnl_sol"] = pnl_sol
        if strategy_id is not UNSET:
            field_dict["strategy_id"] = strategy_id
        if strategy_name is not UNSET:
            field_dict["strategy_name"] = strategy_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backtest_id = d.pop("backtest_id", UNSET)

        pnl_sol = d.pop("pnl_sol", UNSET)

        strategy_id = d.pop("strategy_id", UNSET)

        strategy_name = d.pop("strategy_name", UNSET)

        internal_adapters_primary_http_handler_best_run_ref = cls(
            backtest_id=backtest_id,
            pnl_sol=pnl_sol,
            strategy_id=strategy_id,
            strategy_name=strategy_name,
        )

        internal_adapters_primary_http_handler_best_run_ref.additional_properties = d
        return internal_adapters_primary_http_handler_best_run_ref

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
