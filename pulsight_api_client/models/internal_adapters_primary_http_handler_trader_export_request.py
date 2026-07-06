from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_trader_export_request_filters import (
        InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerTraderExportRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerTraderExportRequest:
    """
    Attributes:
        columns (list[str] | Unset):
        direction (str | Unset):
        filters (InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters | Unset):
        format_ (str | Unset):
        sort_by (str | Unset):
    """

    columns: list[str] | Unset = UNSET
    direction: str | Unset = UNSET
    filters: InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters | Unset = (
        UNSET
    )
    format_: str | Unset = UNSET
    sort_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: list[str] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        direction = self.direction

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        format_ = self.format_

        sort_by = self.sort_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if direction is not UNSET:
            field_dict["direction"] = direction
        if filters is not UNSET:
            field_dict["filters"] = filters
        if format_ is not UNSET:
            field_dict["format"] = format_
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_adapters_primary_http_handler_trader_export_request_filters import (
            InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters,
        )

        d = dict(src_dict)
        columns = cast(list[str], d.pop("columns", UNSET))

        direction = d.pop("direction", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = (
                InternalAdaptersPrimaryHttpHandlerTraderExportRequestFilters.from_dict(
                    _filters
                )
            )

        format_ = d.pop("format", UNSET)

        sort_by = d.pop("sort_by", UNSET)

        internal_adapters_primary_http_handler_trader_export_request = cls(
            columns=columns,
            direction=direction,
            filters=filters,
            format_=format_,
            sort_by=sort_by,
        )

        internal_adapters_primary_http_handler_trader_export_request.additional_properties = d
        return internal_adapters_primary_http_handler_trader_export_request

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
