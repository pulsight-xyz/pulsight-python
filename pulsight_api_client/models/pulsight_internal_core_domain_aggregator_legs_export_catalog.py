from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorLegsExportCatalog")


@_attrs_define
class PulsightInternalCoreDomainAggregatorLegsExportCatalog:
    """
    Attributes:
        days (list[str] | Unset): Days are the exportable UTC days, newest first (YYYY-MM-DD).
        facts (list[str] | Unset): Facts are the token facts files every exportable day carries.
        facts_schema (str | Unset): FactsSchema is the column set of the token facts files. Example: facts-2.
        insiders_since_ms (int | Unset): InsidersSinceMs is when the insider plane found its first insider (unix ms), 0
            before it found any; insider holdings before it are unknown.
        ledger_start_ms (int | Unset): LedgerStartMs is the time of the oldest leg the ledger holds (unix ms), 0 when it
            holds none; a pool's swaps before it are unknown.
        parts (int | Unset): Parts is how many parts each day is split into; a pool's legs are always in part pool_id %
            parts. Example: 16.
        schema (str | Unset): Schema is the column set every part of every day carries. Example: legs-4.
    """

    days: list[str] | Unset = UNSET
    facts: list[str] | Unset = UNSET
    facts_schema: str | Unset = UNSET
    insiders_since_ms: int | Unset = UNSET
    ledger_start_ms: int | Unset = UNSET
    parts: int | Unset = UNSET
    schema: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        facts: list[str] | Unset = UNSET
        if not isinstance(self.facts, Unset):
            facts = self.facts

        facts_schema = self.facts_schema

        insiders_since_ms = self.insiders_since_ms

        ledger_start_ms = self.ledger_start_ms

        parts = self.parts

        schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if facts is not UNSET:
            field_dict["facts"] = facts
        if facts_schema is not UNSET:
            field_dict["facts_schema"] = facts_schema
        if insiders_since_ms is not UNSET:
            field_dict["insiders_since_ms"] = insiders_since_ms
        if ledger_start_ms is not UNSET:
            field_dict["ledger_start_ms"] = ledger_start_ms
        if parts is not UNSET:
            field_dict["parts"] = parts
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        days = cast(list[str], d.pop("days", UNSET))

        facts = cast(list[str], d.pop("facts", UNSET))

        facts_schema = d.pop("facts_schema", UNSET)

        insiders_since_ms = d.pop("insiders_since_ms", UNSET)

        ledger_start_ms = d.pop("ledger_start_ms", UNSET)

        parts = d.pop("parts", UNSET)

        schema = d.pop("schema", UNSET)

        pulsight_internal_core_domain_aggregator_legs_export_catalog = cls(
            days=days,
            facts=facts,
            facts_schema=facts_schema,
            insiders_since_ms=insiders_since_ms,
            ledger_start_ms=ledger_start_ms,
            parts=parts,
            schema=schema,
        )

        pulsight_internal_core_domain_aggregator_legs_export_catalog.additional_properties = d
        return pulsight_internal_core_domain_aggregator_legs_export_catalog

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
