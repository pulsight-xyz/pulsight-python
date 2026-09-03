from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyExecutionSummary")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyExecutionSummary:
    """
    Attributes:
        fills (int | Unset):
        follow_ons (int | Unset):
        median_pool_quote_lamports (int | Unset):
        median_target_impact_bps (float | Unset):
        signal_buys (int | Unset):
        size_lamports (int | Unset):
    """

    fills: int | Unset = UNSET
    follow_ons: int | Unset = UNSET
    median_pool_quote_lamports: int | Unset = UNSET
    median_target_impact_bps: float | Unset = UNSET
    signal_buys: int | Unset = UNSET
    size_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fills = self.fills

        follow_ons = self.follow_ons

        median_pool_quote_lamports = self.median_pool_quote_lamports

        median_target_impact_bps = self.median_target_impact_bps

        signal_buys = self.signal_buys

        size_lamports = self.size_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fills is not UNSET:
            field_dict["fills"] = fills
        if follow_ons is not UNSET:
            field_dict["follow_ons"] = follow_ons
        if median_pool_quote_lamports is not UNSET:
            field_dict["median_pool_quote_lamports"] = median_pool_quote_lamports
        if median_target_impact_bps is not UNSET:
            field_dict["median_target_impact_bps"] = median_target_impact_bps
        if signal_buys is not UNSET:
            field_dict["signal_buys"] = signal_buys
        if size_lamports is not UNSET:
            field_dict["size_lamports"] = size_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fills = d.pop("fills", UNSET)

        follow_ons = d.pop("follow_ons", UNSET)

        median_pool_quote_lamports = d.pop("median_pool_quote_lamports", UNSET)

        median_target_impact_bps = d.pop("median_target_impact_bps", UNSET)

        signal_buys = d.pop("signal_buys", UNSET)

        size_lamports = d.pop("size_lamports", UNSET)

        pulsight_internal_core_domain_trader_copy_execution_summary = cls(
            fills=fills,
            follow_ons=follow_ons,
            median_pool_quote_lamports=median_pool_quote_lamports,
            median_target_impact_bps=median_target_impact_bps,
            signal_buys=signal_buys,
            size_lamports=size_lamports,
        )

        pulsight_internal_core_domain_trader_copy_execution_summary.additional_properties = d
        return pulsight_internal_core_domain_trader_copy_execution_summary

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
