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

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestPreviewMarker")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestPreviewMarker:
    """
    Attributes:
        pool_sol_at_trigger (float | Unset):
        price (float | Unset): Price is the pessimistic execution price (slippage applied) so
            the marker lines up with what a real run would have recorded.
        side (PulsightInternalCoreUsecasesBacktestSide | Unset):
        source (PulsightInternalCoreUsecasesBacktestTradeSource | Unset):
        ts (int | Unset): TS is epoch seconds.
    """

    pool_sol_at_trigger: float | Unset = UNSET
    price: float | Unset = UNSET
    side: PulsightInternalCoreUsecasesBacktestSide | Unset = UNSET
    source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset = UNSET
    ts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pool_sol_at_trigger = self.pool_sol_at_trigger

        price = self.price

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pool_sol_at_trigger is not UNSET:
            field_dict["pool_sol_at_trigger"] = pool_sol_at_trigger
        if price is not UNSET:
            field_dict["price"] = price
        if side is not UNSET:
            field_dict["side"] = side
        if source is not UNSET:
            field_dict["source"] = source
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pool_sol_at_trigger = d.pop("pool_sol_at_trigger", UNSET)

        price = d.pop("price", UNSET)

        _side = d.pop("side", UNSET)
        side: PulsightInternalCoreUsecasesBacktestSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PulsightInternalCoreUsecasesBacktestSide(_side)

        _source = d.pop("source", UNSET)
        source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PulsightInternalCoreUsecasesBacktestTradeSource(_source)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_usecases_backtest_preview_marker = cls(
            pool_sol_at_trigger=pool_sol_at_trigger,
            price=price,
            side=side,
            source=source,
            ts=ts,
        )

        pulsight_internal_core_usecases_backtest_preview_marker.additional_properties = d
        return pulsight_internal_core_usecases_backtest_preview_marker

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
