from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_neighbor_stats_response import (
        InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerNeighborRowResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerNeighborRowResponse:
    """
    Attributes:
        follow_rate (float | Unset):
        hits (int | Unset):
        med_slot_delta (int | Unset):
        mutual_rate (float | Unset):
        neighbor_entries (int | Unset):
        stats (InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse | Unset):
        wallet (str | Unset):
    """

    follow_rate: float | Unset = UNSET
    hits: int | Unset = UNSET
    med_slot_delta: int | Unset = UNSET
    mutual_rate: float | Unset = UNSET
    neighbor_entries: int | Unset = UNSET
    stats: InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse | Unset = UNSET
    wallet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_rate = self.follow_rate

        hits = self.hits

        med_slot_delta = self.med_slot_delta

        mutual_rate = self.mutual_rate

        neighbor_entries = self.neighbor_entries

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        wallet = self.wallet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if follow_rate is not UNSET:
            field_dict["follow_rate"] = follow_rate
        if hits is not UNSET:
            field_dict["hits"] = hits
        if med_slot_delta is not UNSET:
            field_dict["med_slot_delta"] = med_slot_delta
        if mutual_rate is not UNSET:
            field_dict["mutual_rate"] = mutual_rate
        if neighbor_entries is not UNSET:
            field_dict["neighbor_entries"] = neighbor_entries
        if stats is not UNSET:
            field_dict["stats"] = stats
        if wallet is not UNSET:
            field_dict["wallet"] = wallet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.internal_adapters_primary_http_handler_neighbor_stats_response import (
            InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse,
        )

        d = dict(src_dict)
        follow_rate = d.pop("follow_rate", UNSET)

        hits = d.pop("hits", UNSET)

        med_slot_delta = d.pop("med_slot_delta", UNSET)

        mutual_rate = d.pop("mutual_rate", UNSET)

        neighbor_entries = d.pop("neighbor_entries", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse.from_dict(
                _stats
            )

        wallet = d.pop("wallet", UNSET)

        internal_adapters_primary_http_handler_neighbor_row_response = cls(
            follow_rate=follow_rate,
            hits=hits,
            med_slot_delta=med_slot_delta,
            mutual_rate=mutual_rate,
            neighbor_entries=neighbor_entries,
            stats=stats,
            wallet=wallet,
        )

        internal_adapters_primary_http_handler_neighbor_row_response.additional_properties = d
        return internal_adapters_primary_http_handler_neighbor_row_response

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
