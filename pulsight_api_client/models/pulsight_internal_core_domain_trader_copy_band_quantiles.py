from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyBandQuantiles")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyBandQuantiles:
    """
    Attributes:
        fills (int | Unset):
        max_bps (int | Unset):
        p50_bps (int | Unset):
        p75_bps (int | Unset):
        p90_bps (int | Unset):
        p95_bps (int | Unset):
    """

    fills: int | Unset = UNSET
    max_bps: int | Unset = UNSET
    p50_bps: int | Unset = UNSET
    p75_bps: int | Unset = UNSET
    p90_bps: int | Unset = UNSET
    p95_bps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fills = self.fills

        max_bps = self.max_bps

        p50_bps = self.p50_bps

        p75_bps = self.p75_bps

        p90_bps = self.p90_bps

        p95_bps = self.p95_bps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fills is not UNSET:
            field_dict["fills"] = fills
        if max_bps is not UNSET:
            field_dict["max_bps"] = max_bps
        if p50_bps is not UNSET:
            field_dict["p50_bps"] = p50_bps
        if p75_bps is not UNSET:
            field_dict["p75_bps"] = p75_bps
        if p90_bps is not UNSET:
            field_dict["p90_bps"] = p90_bps
        if p95_bps is not UNSET:
            field_dict["p95_bps"] = p95_bps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fills = d.pop("fills", UNSET)

        max_bps = d.pop("max_bps", UNSET)

        p50_bps = d.pop("p50_bps", UNSET)

        p75_bps = d.pop("p75_bps", UNSET)

        p90_bps = d.pop("p90_bps", UNSET)

        p95_bps = d.pop("p95_bps", UNSET)

        pulsight_internal_core_domain_trader_copy_band_quantiles = cls(
            fills=fills,
            max_bps=max_bps,
            p50_bps=p50_bps,
            p75_bps=p75_bps,
            p90_bps=p90_bps,
            p95_bps=p95_bps,
        )

        pulsight_internal_core_domain_trader_copy_band_quantiles.additional_properties = d
        return pulsight_internal_core_domain_trader_copy_band_quantiles

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
