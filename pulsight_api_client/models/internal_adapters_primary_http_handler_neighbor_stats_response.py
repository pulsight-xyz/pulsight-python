from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerNeighborStatsResponse:
    """
    Attributes:
        realized_pnl_lamports (float | Unset): LAMPORTS — named for the unit, unlike the TraderStats field it comes
            from.
        realized_roi_pct (float | Unset):
        winrate (float | Unset):
    """

    realized_pnl_lamports: float | Unset = UNSET
    realized_roi_pct: float | Unset = UNSET
    winrate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        realized_pnl_lamports = self.realized_pnl_lamports

        realized_roi_pct = self.realized_roi_pct

        winrate = self.winrate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if realized_pnl_lamports is not UNSET:
            field_dict["realized_pnl_lamports"] = realized_pnl_lamports
        if realized_roi_pct is not UNSET:
            field_dict["realized_roi_pct"] = realized_roi_pct
        if winrate is not UNSET:
            field_dict["winrate"] = winrate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        realized_pnl_lamports = d.pop("realized_pnl_lamports", UNSET)

        realized_roi_pct = d.pop("realized_roi_pct", UNSET)

        winrate = d.pop("winrate", UNSET)

        internal_adapters_primary_http_handler_neighbor_stats_response = cls(
            realized_pnl_lamports=realized_pnl_lamports,
            realized_roi_pct=realized_roi_pct,
            winrate=winrate,
        )

        internal_adapters_primary_http_handler_neighbor_stats_response.additional_properties = d
        return internal_adapters_primary_http_handler_neighbor_stats_response

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
