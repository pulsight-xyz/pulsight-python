from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyBandPoint")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyBandPoint:
    """
    Attributes:
        band_bps (int | Unset):
        fill_rate_pct (float | Unset):
        filled (int | Unset):
        marginal_fills (int | Unset): Fills this rung adds over the previous (tighter) rung, and what they are
            worth priced at the target's own realised exit. This is the number the
            band decision turns on: a rung that adds fills at a negative return is
            buying losses, however much it improves the fill rate.
        marginal_pnl_pct (float | Unset):
        mean_entry_vs_target_bps (float | Unset): Mean execution price of the filled trades against the target's own
            fill
            price. Positive is worse for the copier, matching copyability's sign.
        mean_pnl_pct (float | Unset): Expected return over everything filled at this band, same pricing.
            NULL when no filled trade has a priceable exit.
    """

    band_bps: int | Unset = UNSET
    fill_rate_pct: float | Unset = UNSET
    filled: int | Unset = UNSET
    marginal_fills: int | Unset = UNSET
    marginal_pnl_pct: float | Unset = UNSET
    mean_entry_vs_target_bps: float | Unset = UNSET
    mean_pnl_pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band_bps = self.band_bps

        fill_rate_pct = self.fill_rate_pct

        filled = self.filled

        marginal_fills = self.marginal_fills

        marginal_pnl_pct = self.marginal_pnl_pct

        mean_entry_vs_target_bps = self.mean_entry_vs_target_bps

        mean_pnl_pct = self.mean_pnl_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band_bps is not UNSET:
            field_dict["band_bps"] = band_bps
        if fill_rate_pct is not UNSET:
            field_dict["fill_rate_pct"] = fill_rate_pct
        if filled is not UNSET:
            field_dict["filled"] = filled
        if marginal_fills is not UNSET:
            field_dict["marginal_fills"] = marginal_fills
        if marginal_pnl_pct is not UNSET:
            field_dict["marginal_pnl_pct"] = marginal_pnl_pct
        if mean_entry_vs_target_bps is not UNSET:
            field_dict["mean_entry_vs_target_bps"] = mean_entry_vs_target_bps
        if mean_pnl_pct is not UNSET:
            field_dict["mean_pnl_pct"] = mean_pnl_pct

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        band_bps = d.pop("band_bps", UNSET)

        fill_rate_pct = d.pop("fill_rate_pct", UNSET)

        filled = d.pop("filled", UNSET)

        marginal_fills = d.pop("marginal_fills", UNSET)

        marginal_pnl_pct = d.pop("marginal_pnl_pct", UNSET)

        mean_entry_vs_target_bps = d.pop("mean_entry_vs_target_bps", UNSET)

        mean_pnl_pct = d.pop("mean_pnl_pct", UNSET)

        pulsight_internal_core_domain_trader_copy_band_point = cls(
            band_bps=band_bps,
            fill_rate_pct=fill_rate_pct,
            filled=filled,
            marginal_fills=marginal_fills,
            marginal_pnl_pct=marginal_pnl_pct,
            mean_entry_vs_target_bps=mean_entry_vs_target_bps,
            mean_pnl_pct=mean_pnl_pct,
        )

        pulsight_internal_core_domain_trader_copy_band_point.additional_properties = d
        return pulsight_internal_core_domain_trader_copy_band_point

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
