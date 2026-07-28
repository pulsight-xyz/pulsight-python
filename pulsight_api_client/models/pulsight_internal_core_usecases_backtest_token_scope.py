from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_usecases_backtest_token_scope_kind import (
    PulsightInternalCoreUsecasesBacktestTokenScopeKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestTokenScope")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestTokenScope:
    """
    Attributes:
        kind (PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset):
        max_mints (int | Unset): MaxMints — on a Strategy scope this is STAMPED BY THE RUNNER at submit
            (from the def's Universe node / mirror default) so the tick-budget and
            credit math have a mint bound; requests don't set it. Legacy kinds
            carried it on the wire. (The other legacy payload fields — trader,
            window, include/exclude filters — were dropped 2026-07-28 with the
            standalone resolution path; unknown keys on old persisted rows are
            ignored on decode, so tolerant reads are unaffected.)
        mint (str | Unset): SingleMint
        mints (list[str] | Unset): Mints
        pool (str | Unset): Pool optionally pins a SingleMint run to one specific market (the AMM
            pool pubkey) of the mint. Empty ⇒ the candle source resolves the mint's
            dominant pool within the replay window (the historical default). Only
            valid on the SingleMint variant — a pool belongs to exactly one mint, so
            it is meaningless on a multi-mint / dynamic scope. Mirrors the preview's
            PreviewRequest.Pool so a pinned run replays the same market the builder
            previewed.
    """

    kind: PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset = UNSET
    max_mints: int | Unset = UNSET
    mint: str | Unset = UNSET
    mints: list[str] | Unset = UNSET
    pool: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        max_mints = self.max_mints

        mint = self.mint

        mints: list[str] | Unset = UNSET
        if not isinstance(self.mints, Unset):
            mints = self.mints

        pool = self.pool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if max_mints is not UNSET:
            field_dict["max_mints"] = max_mints
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mints is not UNSET:
            field_dict["mints"] = mints
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: PulsightInternalCoreUsecasesBacktestTokenScopeKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PulsightInternalCoreUsecasesBacktestTokenScopeKind(_kind)

        max_mints = d.pop("max_mints", UNSET)

        mint = d.pop("mint", UNSET)

        mints = cast(list[str], d.pop("mints", UNSET))

        pool = d.pop("pool", UNSET)

        pulsight_internal_core_usecases_backtest_token_scope = cls(
            kind=kind,
            max_mints=max_mints,
            mint=mint,
            mints=mints,
            pool=pool,
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
