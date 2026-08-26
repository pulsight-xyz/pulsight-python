from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_program_daily_series_windows import (
        PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows,
    )
    from ..models.pulsight_internal_core_domain_aggregator_program_day_stat import (
        PulsightInternalCoreDomainAggregatorProgramDayStat,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramDailySeries")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramDailySeries:
    """
    Attributes:
        days (list[PulsightInternalCoreDomainAggregatorProgramDayStat] | Unset):
        program_id (str | Unset):
        window_days (int | Unset):
        windows (PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows | Unset):
    """

    days: list[PulsightInternalCoreDomainAggregatorProgramDayStat] | Unset = UNSET
    program_id: str | Unset = UNSET
    window_days: int | Unset = UNSET
    windows: PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        program_id = self.program_id

        window_days = self.window_days

        windows: dict[str, Any] | Unset = UNSET
        if not isinstance(self.windows, Unset):
            windows = self.windows.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if program_id is not UNSET:
            field_dict["program_id"] = program_id
        if window_days is not UNSET:
            field_dict["window_days"] = window_days
        if windows is not UNSET:
            field_dict["windows"] = windows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_program_daily_series_windows import (
            PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows,
        )
        from ..models.pulsight_internal_core_domain_aggregator_program_day_stat import (
            PulsightInternalCoreDomainAggregatorProgramDayStat,
        )

        d = dict(src_dict)
        _days = d.pop("days", UNSET)
        days: list[PulsightInternalCoreDomainAggregatorProgramDayStat] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = (
                    PulsightInternalCoreDomainAggregatorProgramDayStat.from_dict(
                        days_item_data
                    )
                )

                days.append(days_item)

        program_id = d.pop("program_id", UNSET)

        window_days = d.pop("window_days", UNSET)

        _windows = d.pop("windows", UNSET)
        windows: PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows | Unset
        if isinstance(_windows, Unset):
            windows = UNSET
        else:
            windows = (
                PulsightInternalCoreDomainAggregatorProgramDailySeriesWindows.from_dict(
                    _windows
                )
            )

        pulsight_internal_core_domain_aggregator_program_daily_series = cls(
            days=days,
            program_id=program_id,
            window_days=window_days,
            windows=windows,
        )

        pulsight_internal_core_domain_aggregator_program_daily_series.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_daily_series

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
