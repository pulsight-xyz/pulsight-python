from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_equity_point import (
        PulsightInternalCoreUsecasesBacktestEquityPoint,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestEquityCurve")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestEquityCurve:
    """
    Attributes:
        max_drawdown_at (str | Unset):
        max_drawdown_sol (float | Unset):
        points (list[PulsightInternalCoreUsecasesBacktestEquityPoint] | Unset):
        sampled_every_n_steps (int | Unset): SampledEveryNSteps is 1 when every step is a point, more when the walk
            was sampled to MaxEquityPoints.
    """

    max_drawdown_at: str | Unset = UNSET
    max_drawdown_sol: float | Unset = UNSET
    points: list[PulsightInternalCoreUsecasesBacktestEquityPoint] | Unset = UNSET
    sampled_every_n_steps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_drawdown_at = self.max_drawdown_at

        max_drawdown_sol = self.max_drawdown_sol

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        sampled_every_n_steps = self.sampled_every_n_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_drawdown_at is not UNSET:
            field_dict["max_drawdown_at"] = max_drawdown_at
        if max_drawdown_sol is not UNSET:
            field_dict["max_drawdown_sol"] = max_drawdown_sol
        if points is not UNSET:
            field_dict["points"] = points
        if sampled_every_n_steps is not UNSET:
            field_dict["sampled_every_n_steps"] = sampled_every_n_steps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_usecases_backtest_equity_point import (
            PulsightInternalCoreUsecasesBacktestEquityPoint,
        )

        d = dict(src_dict)
        max_drawdown_at = d.pop("max_drawdown_at", UNSET)

        max_drawdown_sol = d.pop("max_drawdown_sol", UNSET)

        _points = d.pop("points", UNSET)
        points: list[PulsightInternalCoreUsecasesBacktestEquityPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = PulsightInternalCoreUsecasesBacktestEquityPoint.from_dict(
                    points_item_data
                )

                points.append(points_item)

        sampled_every_n_steps = d.pop("sampled_every_n_steps", UNSET)

        pulsight_internal_core_usecases_backtest_equity_curve = cls(
            max_drawdown_at=max_drawdown_at,
            max_drawdown_sol=max_drawdown_sol,
            points=points,
            sampled_every_n_steps=sampled_every_n_steps,
        )

        pulsight_internal_core_usecases_backtest_equity_curve.additional_properties = d
        return pulsight_internal_core_usecases_backtest_equity_curve

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
