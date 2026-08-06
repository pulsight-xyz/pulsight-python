from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_backtest_settings_response_max_window_secs import (
        InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse:
    """
    Attributes:
        max_tick_budget (int | Unset):
        max_window_secs (InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs | Unset):
    """

    max_tick_budget: int | Unset = UNSET
    max_window_secs: (
        InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_tick_budget = self.max_tick_budget

        max_window_secs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_window_secs, Unset):
            max_window_secs = self.max_window_secs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_tick_budget is not UNSET:
            field_dict["max_tick_budget"] = max_tick_budget
        if max_window_secs is not UNSET:
            field_dict["max_window_secs"] = max_window_secs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.internal_adapters_primary_http_handler_backtest_settings_response_max_window_secs import (
            InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs,
        )

        d = dict(src_dict)
        max_tick_budget = d.pop("max_tick_budget", UNSET)

        _max_window_secs = d.pop("max_window_secs", UNSET)
        max_window_secs: (
            InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs
            | Unset
        )
        if isinstance(_max_window_secs, Unset):
            max_window_secs = UNSET
        else:
            max_window_secs = InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponseMaxWindowSecs.from_dict(
                _max_window_secs
            )

        internal_adapters_primary_http_handler_backtest_settings_response = cls(
            max_tick_budget=max_tick_budget,
            max_window_secs=max_window_secs,
        )

        internal_adapters_primary_http_handler_backtest_settings_response.additional_properties = d
        return internal_adapters_primary_http_handler_backtest_settings_response

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
