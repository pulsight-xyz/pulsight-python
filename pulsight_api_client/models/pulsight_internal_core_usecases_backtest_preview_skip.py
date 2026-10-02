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
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestPreviewSkip")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestPreviewSkip:
    """
    Attributes:
        reason (PulsightInternalCoreUsecasesBacktestDeclineReason | Unset):
        side (PulsightInternalCoreUsecasesBacktestSide | Unset):
        signature (str | Unset):
        ts (int | Unset):
    """

    reason: PulsightInternalCoreUsecasesBacktestDeclineReason | Unset = UNSET
    side: PulsightInternalCoreUsecasesBacktestSide | Unset = UNSET
    signature: str | Unset = UNSET
    ts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        signature = self.signature

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if side is not UNSET:
            field_dict["side"] = side
        if signature is not UNSET:
            field_dict["signature"] = signature
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _reason = d.pop("reason", UNSET)
        reason: PulsightInternalCoreUsecasesBacktestDeclineReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PulsightInternalCoreUsecasesBacktestDeclineReason(_reason)

        _side = d.pop("side", UNSET)
        side: PulsightInternalCoreUsecasesBacktestSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PulsightInternalCoreUsecasesBacktestSide(_side)

        signature = d.pop("signature", UNSET)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_usecases_backtest_preview_skip = cls(
            reason=reason,
            side=side,
            signature=signature,
            ts=ts,
        )

        pulsight_internal_core_usecases_backtest_preview_skip.additional_properties = d
        return pulsight_internal_core_usecases_backtest_preview_skip

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
