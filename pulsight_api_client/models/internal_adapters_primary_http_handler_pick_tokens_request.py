from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_time_range import (
        PulsightInternalCoreUsecasesBacktestTimeRange,
    )
    from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
        PulsightInternalCoreUsecasesBacktestTokenScope,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerPickTokensRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerPickTokensRequest:
    """
    Attributes:
        scope (PulsightInternalCoreUsecasesBacktestTokenScope | Unset):
        time_range (PulsightInternalCoreUsecasesBacktestTimeRange | Unset):
    """

    scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset = UNSET
    time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if time_range is not UNSET:
            field_dict["time_range"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_usecases_backtest_time_range import (
            PulsightInternalCoreUsecasesBacktestTimeRange,
        )
        from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
            PulsightInternalCoreUsecasesBacktestTokenScope,
        )

        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PulsightInternalCoreUsecasesBacktestTokenScope.from_dict(_scope)

        _time_range = d.pop("time_range", UNSET)
        time_range: PulsightInternalCoreUsecasesBacktestTimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = PulsightInternalCoreUsecasesBacktestTimeRange.from_dict(
                _time_range
            )

        internal_adapters_primary_http_handler_pick_tokens_request = cls(
            scope=scope,
            time_range=time_range,
        )

        internal_adapters_primary_http_handler_pick_tokens_request.additional_properties = d
        return internal_adapters_primary_http_handler_pick_tokens_request

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
