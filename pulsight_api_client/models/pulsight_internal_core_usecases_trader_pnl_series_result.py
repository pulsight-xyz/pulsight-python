from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_trader_pnl_series_point import (
        PulsightInternalCoreUsecasesTraderPnlSeriesPoint,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderPnlSeriesResult")


@_attrs_define
class PulsightInternalCoreUsecasesTraderPnlSeriesResult:
    """
    Attributes:
        points (list[PulsightInternalCoreUsecasesTraderPnlSeriesPoint] | Unset):
        window (str | Unset):
    """

    points: list[PulsightInternalCoreUsecasesTraderPnlSeriesPoint] | Unset = UNSET
    window: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points is not UNSET:
            field_dict["points"] = points
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_trader_pnl_series_point import (
            PulsightInternalCoreUsecasesTraderPnlSeriesPoint,
        )

        d = dict(src_dict)
        _points = d.pop("points", UNSET)
        points: list[PulsightInternalCoreUsecasesTraderPnlSeriesPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = (
                    PulsightInternalCoreUsecasesTraderPnlSeriesPoint.from_dict(
                        points_item_data
                    )
                )

                points.append(points_item)

        window = d.pop("window", UNSET)

        pulsight_internal_core_usecases_trader_pnl_series_result = cls(
            points=points,
            window=window,
        )

        pulsight_internal_core_usecases_trader_pnl_series_result.additional_properties = d
        return pulsight_internal_core_usecases_trader_pnl_series_result

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
