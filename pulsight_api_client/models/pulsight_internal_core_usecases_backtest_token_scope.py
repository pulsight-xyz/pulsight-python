from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_usecases_backtest_token_scope_kind import (
    PulsightInternalCoreUsecasesBacktestTokenScopeKind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_selection_filter import (
        PulsightInternalCoreUsecasesBacktestSelectionFilter,
    )
    from ..models.pulsight_internal_core_usecases_backtest_time_range import (
        PulsightInternalCoreUsecasesBacktestTimeRange,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestTokenScope")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestTokenScope:
    """
    Attributes:
        exclude (PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset):
        include (PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset):
        kind (PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset):
        max_mints (int | Unset): MirrorsTraded + TraderTraded + Standalone (cap on selected mints).
        mint (str | Unset): SingleMint
        mints (list[str] | Unset): Mints
        trader (str | Unset): TraderTraded only.
        window (PulsightInternalCoreUsecasesBacktestTimeRange | Unset):
    """

    exclude: PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset = UNSET
    include: PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset = UNSET
    kind: PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset = UNSET
    max_mints: int | Unset = UNSET
    mint: str | Unset = UNSET
    mints: list[str] | Unset = UNSET
    trader: str | Unset = UNSET
    window: PulsightInternalCoreUsecasesBacktestTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude.to_dict()

        include: dict[str, Any] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = self.include.to_dict()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        max_mints = self.max_mints

        mint = self.mint

        mints: list[str] | Unset = UNSET
        if not isinstance(self.mints, Unset):
            mints = self.mints

        trader = self.trader

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if include is not UNSET:
            field_dict["include"] = include
        if kind is not UNSET:
            field_dict["kind"] = kind
        if max_mints is not UNSET:
            field_dict["max_mints"] = max_mints
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mints is not UNSET:
            field_dict["mints"] = mints
        if trader is not UNSET:
            field_dict["trader"] = trader
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_backtest_selection_filter import (
            PulsightInternalCoreUsecasesBacktestSelectionFilter,
        )
        from ..models.pulsight_internal_core_usecases_backtest_time_range import (
            PulsightInternalCoreUsecasesBacktestTimeRange,
        )

        d = dict(src_dict)
        _exclude = d.pop("exclude", UNSET)
        exclude: PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset
        if isinstance(_exclude, Unset):
            exclude = UNSET
        else:
            exclude = PulsightInternalCoreUsecasesBacktestSelectionFilter.from_dict(
                _exclude
            )

        _include = d.pop("include", UNSET)
        include: PulsightInternalCoreUsecasesBacktestSelectionFilter | Unset
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = PulsightInternalCoreUsecasesBacktestSelectionFilter.from_dict(
                _include
            )

        _kind = d.pop("kind", UNSET)
        kind: PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PulsightInternalCoreUsecasesBacktestTokenScopeKind(_kind)

        max_mints = d.pop("max_mints", UNSET)

        mint = d.pop("mint", UNSET)

        mints = cast(list[str], d.pop("mints", UNSET))

        trader = d.pop("trader", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreUsecasesBacktestTimeRange | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreUsecasesBacktestTimeRange.from_dict(_window)

        pulsight_internal_core_usecases_backtest_token_scope = cls(
            exclude=exclude,
            include=include,
            kind=kind,
            max_mints=max_mints,
            mint=mint,
            mints=mints,
            trader=trader,
            window=window,
        )

        pulsight_internal_core_usecases_backtest_token_scope.additional_properties = d
        return pulsight_internal_core_usecases_backtest_token_scope

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
