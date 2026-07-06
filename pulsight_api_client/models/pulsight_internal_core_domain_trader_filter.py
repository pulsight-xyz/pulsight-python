from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_filter_filters import (
        PulsightInternalCoreDomainTraderFilterFilters,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderFilter")


@_attrs_define
class PulsightInternalCoreDomainTraderFilter:
    """
    Attributes:
        created_at (str | Unset):
        filters (PulsightInternalCoreDomainTraderFilterFilters | Unset):
        id (str | Unset):
        is_default (bool | Unset):
        name (str | Unset):
        updated_at (str | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    filters: PulsightInternalCoreDomainTraderFilterFilters | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        id = self.id

        is_default = self.is_default

        name = self.name

        updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_trader_filter_filters import (
            PulsightInternalCoreDomainTraderFilterFilters,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: PulsightInternalCoreDomainTraderFilterFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = PulsightInternalCoreDomainTraderFilterFilters.from_dict(_filters)

        id = d.pop("id", UNSET)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        pulsight_internal_core_domain_trader_filter = cls(
            created_at=created_at,
            filters=filters,
            id=id,
            is_default=is_default,
            name=name,
            updated_at=updated_at,
            user_id=user_id,
        )

        pulsight_internal_core_domain_trader_filter.additional_properties = d
        return pulsight_internal_core_domain_trader_filter

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
