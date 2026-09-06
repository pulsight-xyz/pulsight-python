from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_usecases_backtest_decline_reason import (
    PulsightInternalCoreUsecasesBacktestDeclineReason,
)
from ..models.pulsight_internal_core_usecases_backtest_side import (
    PulsightInternalCoreUsecasesBacktestSide,
)
from ..models.pulsight_internal_core_usecases_backtest_trade_source import (
    PulsightInternalCoreUsecasesBacktestTradeSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestDecline")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestDecline:
    """
    Attributes:
        backtest_id (str | Unset):
        detail (str | Unset): Detail is a short human-readable specific for the reason (the cap
            that was full, the drift that tripped the gate, …).
        fee_sol (float | Unset): FeeSol + TipSol are non-zero only on `reverted`: the priority fee and
            tip the failed tx still paid (already inside the summary's totals).
        idx (int | Unset):
        landing_drift_bps (float | Unset): LandingDriftBps is the adverse-signed drift that tripped a `reverted`
            fill's slippage gate. Nil otherwise.
        mint (str | Unset):
        pool (str | Unset): Pool is the market the triggering swap executed in.
        reason (PulsightInternalCoreUsecasesBacktestDeclineReason | Unset):
        requested_sol (float | Unset): RequestedSol is the SOL the buy would have spent, or the SOL the sell
            would have realised, had it filled. 0 when sizing itself failed.
        side (PulsightInternalCoreUsecasesBacktestSide | Unset):
        source (PulsightInternalCoreUsecasesBacktestTradeSource | Unset):
        tip_sol (float | Unset):
        triggering_swap_sig (str | Unset):
        ts (str | Unset):
    """

    backtest_id: str | Unset = UNSET
    detail: str | Unset = UNSET
    fee_sol: float | Unset = UNSET
    idx: int | Unset = UNSET
    landing_drift_bps: float | Unset = UNSET
    mint: str | Unset = UNSET
    pool: str | Unset = UNSET
    reason: PulsightInternalCoreUsecasesBacktestDeclineReason | Unset = UNSET
    requested_sol: float | Unset = UNSET
    side: PulsightInternalCoreUsecasesBacktestSide | Unset = UNSET
    source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset = UNSET
    tip_sol: float | Unset = UNSET
    triggering_swap_sig: str | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backtest_id = self.backtest_id

        detail = self.detail

        fee_sol = self.fee_sol

        idx = self.idx

        landing_drift_bps = self.landing_drift_bps

        mint = self.mint

        pool = self.pool

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        requested_sol = self.requested_sol

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        tip_sol = self.tip_sol

        triggering_swap_sig = self.triggering_swap_sig

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backtest_id is not UNSET:
            field_dict["backtest_id"] = backtest_id
        if detail is not UNSET:
            field_dict["detail"] = detail
        if fee_sol is not UNSET:
            field_dict["fee_sol"] = fee_sol
        if idx is not UNSET:
            field_dict["idx"] = idx
        if landing_drift_bps is not UNSET:
            field_dict["landing_drift_bps"] = landing_drift_bps
        if mint is not UNSET:
            field_dict["mint"] = mint
        if pool is not UNSET:
            field_dict["pool"] = pool
        if reason is not UNSET:
            field_dict["reason"] = reason
        if requested_sol is not UNSET:
            field_dict["requested_sol"] = requested_sol
        if side is not UNSET:
            field_dict["side"] = side
        if source is not UNSET:
            field_dict["source"] = source
        if tip_sol is not UNSET:
            field_dict["tip_sol"] = tip_sol
        if triggering_swap_sig is not UNSET:
            field_dict["triggering_swap_sig"] = triggering_swap_sig
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backtest_id = d.pop("backtest_id", UNSET)

        detail = d.pop("detail", UNSET)

        fee_sol = d.pop("fee_sol", UNSET)

        idx = d.pop("idx", UNSET)

        landing_drift_bps = d.pop("landing_drift_bps", UNSET)

        mint = d.pop("mint", UNSET)

        pool = d.pop("pool", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: PulsightInternalCoreUsecasesBacktestDeclineReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PulsightInternalCoreUsecasesBacktestDeclineReason(_reason)

        requested_sol = d.pop("requested_sol", UNSET)

        _side = d.pop("side", UNSET)
        side: PulsightInternalCoreUsecasesBacktestSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PulsightInternalCoreUsecasesBacktestSide(_side)

        _source = d.pop("source", UNSET)
        source: PulsightInternalCoreUsecasesBacktestTradeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PulsightInternalCoreUsecasesBacktestTradeSource(_source)

        tip_sol = d.pop("tip_sol", UNSET)

        triggering_swap_sig = d.pop("triggering_swap_sig", UNSET)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_decline = cls(
            backtest_id=backtest_id,
            detail=detail,
            fee_sol=fee_sol,
            idx=idx,
            landing_drift_bps=landing_drift_bps,
            mint=mint,
            pool=pool,
            reason=reason,
            requested_sol=requested_sol,
            side=side,
            source=source,
            tip_sol=tip_sol,
            triggering_swap_sig=triggering_swap_sig,
            ts=ts,
        )

        pulsight_internal_core_usecases_backtest_backtest_decline.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_decline

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
