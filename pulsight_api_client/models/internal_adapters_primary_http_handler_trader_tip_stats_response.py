from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse:
    """
    Attributes:
        exec_premium (float | Unset):
        priority_fee_sum (int | Unset):
        swap_count (int | Unset):
        tip_aggression_ratio (float | Unset):
        tip_avg_lamports (float | Unset):
        tip_count (int | Unset):
        tip_sum_lamports (int | Unset):
        trader (str | Unset):
        volume_in_sum (int | Unset):
        window (str | Unset):
    """

    exec_premium: float | Unset = UNSET
    priority_fee_sum: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    tip_aggression_ratio: float | Unset = UNSET
    tip_avg_lamports: float | Unset = UNSET
    tip_count: int | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    trader: str | Unset = UNSET
    volume_in_sum: int | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exec_premium = self.exec_premium

        priority_fee_sum = self.priority_fee_sum

        swap_count = self.swap_count

        tip_aggression_ratio = self.tip_aggression_ratio

        tip_avg_lamports = self.tip_avg_lamports

        tip_count = self.tip_count

        tip_sum_lamports = self.tip_sum_lamports

        trader = self.trader

        volume_in_sum = self.volume_in_sum

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exec_premium is not UNSET:
            field_dict["exec_premium"] = exec_premium
        if priority_fee_sum is not UNSET:
            field_dict["priority_fee_sum"] = priority_fee_sum
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if tip_aggression_ratio is not UNSET:
            field_dict["tip_aggression_ratio"] = tip_aggression_ratio
        if tip_avg_lamports is not UNSET:
            field_dict["tip_avg_lamports"] = tip_avg_lamports
        if tip_count is not UNSET:
            field_dict["tip_count"] = tip_count
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports
        if trader is not UNSET:
            field_dict["trader"] = trader
        if volume_in_sum is not UNSET:
            field_dict["volume_in_sum"] = volume_in_sum
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exec_premium = d.pop("exec_premium", UNSET)

        priority_fee_sum = d.pop("priority_fee_sum", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        tip_aggression_ratio = d.pop("tip_aggression_ratio", UNSET)

        tip_avg_lamports = d.pop("tip_avg_lamports", UNSET)

        tip_count = d.pop("tip_count", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        trader = d.pop("trader", UNSET)

        volume_in_sum = d.pop("volume_in_sum", UNSET)

        window = d.pop("window", UNSET)

        internal_adapters_primary_http_handler_trader_tip_stats_response = cls(
            exec_premium=exec_premium,
            priority_fee_sum=priority_fee_sum,
            swap_count=swap_count,
            tip_aggression_ratio=tip_aggression_ratio,
            tip_avg_lamports=tip_avg_lamports,
            tip_count=tip_count,
            tip_sum_lamports=tip_sum_lamports,
            trader=trader,
            volume_in_sum=volume_in_sum,
            window=window,
        )

        internal_adapters_primary_http_handler_trader_tip_stats_response.additional_properties = d
        return internal_adapters_primary_http_handler_trader_tip_stats_response

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
