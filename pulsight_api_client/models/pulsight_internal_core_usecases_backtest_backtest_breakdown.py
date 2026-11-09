from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_backtest_backtest_breakdown_declines_by_reason import (
        PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason,
    )
    from ..models.pulsight_internal_core_usecases_backtest_equity_curve import (
        PulsightInternalCoreUsecasesBacktestEquityCurve,
    )
    from ..models.pulsight_internal_core_usecases_backtest_mint_breakdown import (
        PulsightInternalCoreUsecasesBacktestMintBreakdown,
    )
    from ..models.pulsight_internal_core_usecases_backtest_target_mint_comparison import (
        PulsightInternalCoreUsecasesBacktestTargetMintComparison,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestBreakdown")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestBreakdown:
    """
    Attributes:
        backtest_id (str | Unset):
        declines_by_reason (PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason | Unset):
        equity (PulsightInternalCoreUsecasesBacktestEquityCurve | Unset):
        mints (list[PulsightInternalCoreUsecasesBacktestMintBreakdown] | Unset):
        target (list[PulsightInternalCoreUsecasesBacktestTargetMintComparison] | Unset):
        target_wallets (list[str] | Unset): TargetWallets are the mirrored wallets the target comparison reads.
    """

    backtest_id: str | Unset = UNSET
    declines_by_reason: (
        PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason | Unset
    ) = UNSET
    equity: PulsightInternalCoreUsecasesBacktestEquityCurve | Unset = UNSET
    mints: list[PulsightInternalCoreUsecasesBacktestMintBreakdown] | Unset = UNSET
    target: list[PulsightInternalCoreUsecasesBacktestTargetMintComparison] | Unset = (
        UNSET
    )
    target_wallets: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backtest_id = self.backtest_id

        declines_by_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.declines_by_reason, Unset):
            declines_by_reason = self.declines_by_reason.to_dict()

        equity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity, Unset):
            equity = self.equity.to_dict()

        mints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mints, Unset):
            mints = []
            for mints_item_data in self.mints:
                mints_item = mints_item_data.to_dict()
                mints.append(mints_item)

        target: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = []
            for target_item_data in self.target:
                target_item = target_item_data.to_dict()
                target.append(target_item)

        target_wallets: list[str] | Unset = UNSET
        if not isinstance(self.target_wallets, Unset):
            target_wallets = self.target_wallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backtest_id is not UNSET:
            field_dict["backtest_id"] = backtest_id
        if declines_by_reason is not UNSET:
            field_dict["declines_by_reason"] = declines_by_reason
        if equity is not UNSET:
            field_dict["equity"] = equity
        if mints is not UNSET:
            field_dict["mints"] = mints
        if target is not UNSET:
            field_dict["target"] = target
        if target_wallets is not UNSET:
            field_dict["target_wallets"] = target_wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_usecases_backtest_backtest_breakdown_declines_by_reason import (
            PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason,
        )
        from ..models.pulsight_internal_core_usecases_backtest_equity_curve import (
            PulsightInternalCoreUsecasesBacktestEquityCurve,
        )
        from ..models.pulsight_internal_core_usecases_backtest_mint_breakdown import (
            PulsightInternalCoreUsecasesBacktestMintBreakdown,
        )
        from ..models.pulsight_internal_core_usecases_backtest_target_mint_comparison import (
            PulsightInternalCoreUsecasesBacktestTargetMintComparison,
        )

        d = dict(src_dict)
        backtest_id = d.pop("backtest_id", UNSET)

        _declines_by_reason = d.pop("declines_by_reason", UNSET)
        declines_by_reason: (
            PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason
            | Unset
        )
        if isinstance(_declines_by_reason, Unset):
            declines_by_reason = UNSET
        else:
            declines_by_reason = PulsightInternalCoreUsecasesBacktestBacktestBreakdownDeclinesByReason.from_dict(
                _declines_by_reason
            )

        _equity = d.pop("equity", UNSET)
        equity: PulsightInternalCoreUsecasesBacktestEquityCurve | Unset
        if isinstance(_equity, Unset):
            equity = UNSET
        else:
            equity = PulsightInternalCoreUsecasesBacktestEquityCurve.from_dict(_equity)

        _mints = d.pop("mints", UNSET)
        mints: list[PulsightInternalCoreUsecasesBacktestMintBreakdown] | Unset = UNSET
        if _mints is not UNSET:
            mints = []
            for mints_item_data in _mints:
                mints_item = (
                    PulsightInternalCoreUsecasesBacktestMintBreakdown.from_dict(
                        mints_item_data
                    )
                )

                mints.append(mints_item)

        _target = d.pop("target", UNSET)
        target: (
            list[PulsightInternalCoreUsecasesBacktestTargetMintComparison] | Unset
        ) = UNSET
        if _target is not UNSET:
            target = []
            for target_item_data in _target:
                target_item = (
                    PulsightInternalCoreUsecasesBacktestTargetMintComparison.from_dict(
                        target_item_data
                    )
                )

                target.append(target_item)

        target_wallets = cast(list[str], d.pop("target_wallets", UNSET))

        pulsight_internal_core_usecases_backtest_backtest_breakdown = cls(
            backtest_id=backtest_id,
            declines_by_reason=declines_by_reason,
            equity=equity,
            mints=mints,
            target=target,
            target_wallets=target_wallets,
        )

        pulsight_internal_core_usecases_backtest_backtest_breakdown.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_breakdown

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
