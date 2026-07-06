from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorOHLCVCandle")


@_attrs_define
class PulsightInternalCoreDomainAggregatorOHLCVCandle:
    """
    Attributes:
        bucket (str | Unset):
        buy_volume_sol (float | Unset):
        c (float | Unset):
        h (float | Unset):
        l (float | Unset):
        mint (str | Unset):
        o (float | Unset):
        pool_sol (float | Unset):
        sell_volume_sol (float | Unset):
        swap_count (int | Unset):
        token_volume (float | Unset):
    """

    bucket: str | Unset = UNSET
    buy_volume_sol: float | Unset = UNSET
    c: float | Unset = UNSET
    h: float | Unset = UNSET
    l: float | Unset = UNSET
    mint: str | Unset = UNSET
    o: float | Unset = UNSET
    pool_sol: float | Unset = UNSET
    sell_volume_sol: float | Unset = UNSET
    swap_count: int | Unset = UNSET
    token_volume: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        buy_volume_sol = self.buy_volume_sol

        c = self.c

        h = self.h

        l = self.l

        mint = self.mint

        o = self.o

        pool_sol = self.pool_sol

        sell_volume_sol = self.sell_volume_sol

        swap_count = self.swap_count

        token_volume = self.token_volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if buy_volume_sol is not UNSET:
            field_dict["buy_volume_sol"] = buy_volume_sol
        if c is not UNSET:
            field_dict["c"] = c
        if h is not UNSET:
            field_dict["h"] = h
        if l is not UNSET:
            field_dict["l"] = l
        if mint is not UNSET:
            field_dict["mint"] = mint
        if o is not UNSET:
            field_dict["o"] = o
        if pool_sol is not UNSET:
            field_dict["pool_sol"] = pool_sol
        if sell_volume_sol is not UNSET:
            field_dict["sell_volume_sol"] = sell_volume_sol
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if token_volume is not UNSET:
            field_dict["token_volume"] = token_volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket", UNSET)

        buy_volume_sol = d.pop("buy_volume_sol", UNSET)

        c = d.pop("c", UNSET)

        h = d.pop("h", UNSET)

        l = d.pop("l", UNSET)

        mint = d.pop("mint", UNSET)

        o = d.pop("o", UNSET)

        pool_sol = d.pop("pool_sol", UNSET)

        sell_volume_sol = d.pop("sell_volume_sol", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        token_volume = d.pop("token_volume", UNSET)

        pulsight_internal_core_domain_aggregator_ohlcv_candle = cls(
            bucket=bucket,
            buy_volume_sol=buy_volume_sol,
            c=c,
            h=h,
            l=l,
            mint=mint,
            o=o,
            pool_sol=pool_sol,
            sell_volume_sol=sell_volume_sol,
            swap_count=swap_count,
            token_volume=token_volume,
        )

        pulsight_internal_core_domain_aggregator_ohlcv_candle.additional_properties = d
        return pulsight_internal_core_domain_aggregator_ohlcv_candle

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
