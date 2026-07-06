from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_preview_marker import (
        PulsightInternalCoreUsecasesBacktestPreviewMarker,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestPreviewResponse")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestPreviewResponse:
    """
    Attributes:
        markers (list[PulsightInternalCoreUsecasesBacktestPreviewMarker] | Unset):
        simulation_assumptions (list[str] | Unset):
    """

    markers: list[PulsightInternalCoreUsecasesBacktestPreviewMarker] | Unset = UNSET
    simulation_assumptions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.markers, Unset):
            markers = []
            for markers_item_data in self.markers:
                markers_item = markers_item_data.to_dict()
                markers.append(markers_item)

        simulation_assumptions: list[str] | Unset = UNSET
        if not isinstance(self.simulation_assumptions, Unset):
            simulation_assumptions = self.simulation_assumptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markers is not UNSET:
            field_dict["markers"] = markers
        if simulation_assumptions is not UNSET:
            field_dict["simulation_assumptions"] = simulation_assumptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_backtest_preview_marker import (
            PulsightInternalCoreUsecasesBacktestPreviewMarker,
        )

        d = dict(src_dict)
        _markers = d.pop("markers", UNSET)
        markers: list[PulsightInternalCoreUsecasesBacktestPreviewMarker] | Unset = UNSET
        if _markers is not UNSET:
            markers = []
            for markers_item_data in _markers:
                markers_item = (
                    PulsightInternalCoreUsecasesBacktestPreviewMarker.from_dict(
                        markers_item_data
                    )
                )

                markers.append(markers_item)

        simulation_assumptions = cast(list[str], d.pop("simulation_assumptions", UNSET))

        pulsight_internal_core_usecases_backtest_preview_response = cls(
            markers=markers,
            simulation_assumptions=simulation_assumptions,
        )

        pulsight_internal_core_usecases_backtest_preview_response.additional_properties = d
        return pulsight_internal_core_usecases_backtest_preview_response

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
