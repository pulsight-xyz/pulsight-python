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
        parts (int | Unset): Parts is how many parts each day is split into; a pool's legs are always in part pool_id %
            parts. Example: 16.
        schema (str | Unset): Schema is the column set every part of every day carries. Example: legs-1.
        venues (list[str] | Unset): Venues are the venues whose legs are exported.
    """

    days: list[str] | Unset = UNSET
    parts: int | Unset = UNSET
    schema: str | Unset = UNSET
    venues: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        parts = self.parts

        schema = self.schema

        venues: list[str] | Unset = UNSET
        if not isinstance(self.venues, Unset):
            venues = self.venues

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if parts is not UNSET:
            field_dict["parts"] = parts
        if schema is not UNSET:
            field_dict["schema"] = schema
        if venues is not UNSET:
            field_dict["venues"] = venues

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        days = cast(list[str], d.pop("days", UNSET))

        parts = d.pop("parts", UNSET)

        schema = d.pop("schema", UNSET)

        venues = cast(list[str], d.pop("venues", UNSET))

        pulsight_internal_core_domain_aggregator_legs_export_catalog = cls(
            days=days,
            parts=parts,
            schema=schema,
            venues=venues,
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
