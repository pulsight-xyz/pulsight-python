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
        base_reserve (int | Unset):
        buy_volume_sol (int | Unset):
        buy_volume_usd (int | Unset):
        close (float | Unset):
        depth_sol (int | Unset):
        depth_usd (int | Unset):
        high (float | Unset):
        low (float | Unset):
        open_ (float | Unset):
        quote_reserve (int | Unset):
        sell_volume_sol (int | Unset):
        sell_volume_usd (int | Unset):
        swap_count (int | Unset):
        time (int | Unset):
        volume_sol (int | Unset):
        volume_usd (int | Unset):
    """

    base_reserve: int | Unset = UNSET
    buy_volume_sol: int | Unset = UNSET
    buy_volume_usd: int | Unset = UNSET
    close: float | Unset = UNSET
    depth_sol: int | Unset = UNSET
    depth_usd: int | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    open_: float | Unset = UNSET
    quote_reserve: int | Unset = UNSET
    sell_volume_sol: int | Unset = UNSET
    sell_volume_usd: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    time: int | Unset = UNSET
    volume_sol: int | Unset = UNSET
    volume_usd: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_reserve = self.base_reserve

        buy_volume_sol = self.buy_volume_sol

        buy_volume_usd = self.buy_volume_usd

        close = self.close

        depth_sol = self.depth_sol

        depth_usd = self.depth_usd

        high = self.high

        low = self.low

        open_ = self.open_

        quote_reserve = self.quote_reserve

        sell_volume_sol = self.sell_volume_sol

        sell_volume_usd = self.sell_volume_usd

        swap_count = self.swap_count

        time = self.time

        volume_sol = self.volume_sol

        volume_usd = self.volume_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_reserve is not UNSET:
            field_dict["base_reserve"] = base_reserve
        if buy_volume_sol is not UNSET:
            field_dict["buy_volume_sol"] = buy_volume_sol
        if buy_volume_usd is not UNSET:
            field_dict["buy_volume_usd"] = buy_volume_usd
        if close is not UNSET:
            field_dict["close"] = close
        if depth_sol is not UNSET:
            field_dict["depth_sol"] = depth_sol
        if depth_usd is not UNSET:
            field_dict["depth_usd"] = depth_usd
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if open_ is not UNSET:
            field_dict["open"] = open_
        if quote_reserve is not UNSET:
            field_dict["quote_reserve"] = quote_reserve
        if sell_volume_sol is not UNSET:
            field_dict["sell_volume_sol"] = sell_volume_sol
        if sell_volume_usd is not UNSET:
            field_dict["sell_volume_usd"] = sell_volume_usd
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if time is not UNSET:
            field_dict["time"] = time
        if volume_sol is not UNSET:
            field_dict["volume_sol"] = volume_sol
        if volume_usd is not UNSET:
            field_dict["volume_usd"] = volume_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_reserve = d.pop("base_reserve", UNSET)

        buy_volume_sol = d.pop("buy_volume_sol", UNSET)

        buy_volume_usd = d.pop("buy_volume_usd", UNSET)

        close = d.pop("close", UNSET)

        depth_sol = d.pop("depth_sol", UNSET)

        depth_usd = d.pop("depth_usd", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        open_ = d.pop("open", UNSET)

        quote_reserve = d.pop("quote_reserve", UNSET)

        sell_volume_sol = d.pop("sell_volume_sol", UNSET)

        sell_volume_usd = d.pop("sell_volume_usd", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        time = d.pop("time", UNSET)

        volume_sol = d.pop("volume_sol", UNSET)

        volume_usd = d.pop("volume_usd", UNSET)

        internal_adapters_primary_http_handler_ohlcv_row = cls(
            base_reserve=base_reserve,
            buy_volume_sol=buy_volume_sol,
            buy_volume_usd=buy_volume_usd,
            close=close,
            depth_sol=depth_sol,
            depth_usd=depth_usd,
            high=high,
            low=low,
            open_=open_,
            quote_reserve=quote_reserve,
            sell_volume_sol=sell_volume_sol,
            sell_volume_usd=sell_volume_usd,
            swap_count=swap_count,
            time=time,
            volume_sol=volume_sol,
            volume_usd=volume_usd,
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
