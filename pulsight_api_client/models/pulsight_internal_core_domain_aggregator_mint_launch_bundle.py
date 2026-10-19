from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintLaunchBundle")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintLaunchBundle:
    """
    Attributes:
        measured_at (int | Unset): MeasuredAt is when the bundle became measurable, unix seconds: 302 s
            after the mint's first trade, when its seal falls due.
        pct (float | Unset): Pct is the share of supply the launch bundle took, in percent — the
            risk card's bundled at launch.
    """

    measured_at: int | Unset = UNSET
    pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at = self.measured_at

        pct = self.pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measured_at"] = measured_at
        if pct is not UNSET:
            field_dict["pct"] = pct

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        measured_at = d.pop("measured_at", UNSET)

        pct = d.pop("pct", UNSET)

        pulsight_internal_core_domain_aggregator_mint_launch_bundle = cls(
            measured_at=measured_at,
            pct=pct,
        )

        pulsight_internal_core_domain_aggregator_mint_launch_bundle.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_launch_bundle

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
