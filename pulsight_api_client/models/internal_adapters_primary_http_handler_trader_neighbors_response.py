from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_neighbor_row_response import (
        InternalAdaptersPrimaryHttpHandlerNeighborRowResponse,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse:
    """
    Attributes:
        neighbors (list[InternalAdaptersPrimaryHttpHandlerNeighborRowResponse] | Unset):
        plane (str | Unset):
        relation (str | Unset):
        source (str | Unset):
        subject_entries (int | Unset):
        trader (str | Unset):
        window_days (int | Unset):
    """

    neighbors: list[InternalAdaptersPrimaryHttpHandlerNeighborRowResponse] | Unset = (
        UNSET
    )
    plane: str | Unset = UNSET
    relation: str | Unset = UNSET
    source: str | Unset = UNSET
    subject_entries: int | Unset = UNSET
    trader: str | Unset = UNSET
    window_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        neighbors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.neighbors, Unset):
            neighbors = []
            for neighbors_item_data in self.neighbors:
                neighbors_item = neighbors_item_data.to_dict()
                neighbors.append(neighbors_item)

        plane = self.plane

        relation = self.relation

        source = self.source

        subject_entries = self.subject_entries

        trader = self.trader

        window_days = self.window_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if neighbors is not UNSET:
            field_dict["neighbors"] = neighbors
        if plane is not UNSET:
            field_dict["plane"] = plane
        if relation is not UNSET:
            field_dict["relation"] = relation
        if source is not UNSET:
            field_dict["source"] = source
        if subject_entries is not UNSET:
            field_dict["subject_entries"] = subject_entries
        if trader is not UNSET:
            field_dict["trader"] = trader
        if window_days is not UNSET:
            field_dict["window_days"] = window_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.internal_adapters_primary_http_handler_neighbor_row_response import (
            InternalAdaptersPrimaryHttpHandlerNeighborRowResponse,
        )

        d = dict(src_dict)
        _neighbors = d.pop("neighbors", UNSET)
        neighbors: (
            list[InternalAdaptersPrimaryHttpHandlerNeighborRowResponse] | Unset
        ) = UNSET
        if _neighbors is not UNSET:
            neighbors = []
            for neighbors_item_data in _neighbors:
                neighbors_item = (
                    InternalAdaptersPrimaryHttpHandlerNeighborRowResponse.from_dict(
                        neighbors_item_data
                    )
                )

                neighbors.append(neighbors_item)

        plane = d.pop("plane", UNSET)

        relation = d.pop("relation", UNSET)

        source = d.pop("source", UNSET)

        subject_entries = d.pop("subject_entries", UNSET)

        trader = d.pop("trader", UNSET)

        window_days = d.pop("window_days", UNSET)

        internal_adapters_primary_http_handler_trader_neighbors_response = cls(
            neighbors=neighbors,
            plane=plane,
            relation=relation,
            source=source,
            subject_entries=subject_entries,
            trader=trader,
            window_days=window_days,
        )

        internal_adapters_primary_http_handler_trader_neighbors_response.additional_properties = d
        return internal_adapters_primary_http_handler_trader_neighbors_response

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
