from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerOhlcvRow")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerOhlcvRow:
    """
    Attributes:
        buy_volume_sol (float | Unset):
        close (float | Unset):
        high (float | Unset):
        low (float | Unset):
        open_ (float | Unset):
        pool_sol (float | Unset):
        sell_volume_sol (float | Unset):
        swap_count (int | Unset):
        time (int | Unset):
        token_volume (float | Unset):
        volume_sol (float | Unset): buy + sell
    """

    buy_volume_sol: float | Unset = UNSET
    close: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    open_: float | Unset = UNSET
    pool_sol: float | Unset = UNSET
    sell_volume_sol: float | Unset = UNSET
    swap_count: int | Unset = UNSET
    time: int | Unset = UNSET
    token_volume: float | Unset = UNSET
    volume_sol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_volume_sol = self.buy_volume_sol

        close = self.close

        high = self.high

        low = self.low

        open_ = self.open_

        pool_sol = self.pool_sol

        sell_volume_sol = self.sell_volume_sol

        swap_count = self.swap_count

        time = self.time

        token_volume = self.token_volume

        volume_sol = self.volume_sol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_volume_sol is not UNSET:
            field_dict["buy_volume_sol"] = buy_volume_sol
        if close is not UNSET:
            field_dict["close"] = close
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if open_ is not UNSET:
            field_dict["open"] = open_
        if pool_sol is not UNSET:
            field_dict["pool_sol"] = pool_sol
        if sell_volume_sol is not UNSET:
            field_dict["sell_volume_sol"] = sell_volume_sol
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if time is not UNSET:
            field_dict["time"] = time
        if token_volume is not UNSET:
            field_dict["token_volume"] = token_volume
        if volume_sol is not UNSET:
            field_dict["volume_sol"] = volume_sol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        buy_volume_sol = d.pop("buy_volume_sol", UNSET)

        close = d.pop("close", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        open_ = d.pop("open", UNSET)

        pool_sol = d.pop("pool_sol", UNSET)

        sell_volume_sol = d.pop("sell_volume_sol", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        time = d.pop("time", UNSET)

        token_volume = d.pop("token_volume", UNSET)

        volume_sol = d.pop("volume_sol", UNSET)

        internal_adapters_primary_http_handler_ohlcv_row = cls(
            buy_volume_sol=buy_volume_sol,
            close=close,
            high=high,
            low=low,
            open_=open_,
            pool_sol=pool_sol,
            sell_volume_sol=sell_volume_sol,
            swap_count=swap_count,
            time=time,
            token_volume=token_volume,
            volume_sol=volume_sol,
        )

        internal_adapters_primary_http_handler_ohlcv_row.additional_properties = d
        return internal_adapters_primary_http_handler_ohlcv_row

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
