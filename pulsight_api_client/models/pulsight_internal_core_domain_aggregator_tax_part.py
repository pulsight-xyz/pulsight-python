from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_tax_part_kind import (
    PulsightInternalCoreDomainAggregatorTaxPartKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTaxPart")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTaxPart:
    """
    Attributes:
        bps (float | Unset): Bps is the share in basis points of the traded value, to two decimals.
        kind (PulsightInternalCoreDomainAggregatorTaxPartKind | Unset): Kind names the share: `lp` (paid to liquidity
            providers), `protocol`
            (the venue), `fund` (the venue's fund), `platform` (the launchpad
            platform the pool belongs to), `creator` (the coin's creator),
            `holder_rewards` (the coin's holders), `cashback` (paid back to the
            trader).
    """

    bps: float | Unset = UNSET
    kind: PulsightInternalCoreDomainAggregatorTaxPartKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bps = self.bps

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bps is not UNSET:
            field_dict["bps"] = bps
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bps = d.pop("bps", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: PulsightInternalCoreDomainAggregatorTaxPartKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PulsightInternalCoreDomainAggregatorTaxPartKind(_kind)

        pulsight_internal_core_domain_aggregator_tax_part = cls(
            bps=bps,
            kind=kind,
        )

        pulsight_internal_core_domain_aggregator_tax_part.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tax_part

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
