from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_trader_tag_source import (
    PulsightInternalCoreDomainTraderTagSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderTag")


@_attrs_define
class PulsightInternalCoreDomainTraderTag:
    """
    Attributes:
        created_at (str | Unset):
        description (str | Unset):
        id (str | Unset):
        name (str | Unset):
        source (PulsightInternalCoreDomainTraderTagSource | Unset):
    """

    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    source: PulsightInternalCoreDomainTraderTagSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        id = self.id

        name = self.name

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _source = d.pop("source", UNSET)
        source: PulsightInternalCoreDomainTraderTagSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PulsightInternalCoreDomainTraderTagSource(_source)

        pulsight_internal_core_domain_trader_tag = cls(
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            source=source,
        )

        pulsight_internal_core_domain_trader_tag.additional_properties = d
        return pulsight_internal_core_domain_trader_tag

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
