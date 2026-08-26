from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow")


@_attrs_define
class PulsightInternalCoreUsecasesTraderTraderPnlDistributionRow:
    """
    Attributes:
        pnl_0x_2x (int | Unset):
        pnl_2x_5x (int | Unset):
        pnl_gt_5x (int | Unset):
        pnl_lt_nd5 (int | Unset):
        pnl_nd5_0x (int | Unset):
        trader (str | Unset):
        window_label (str | Unset):
    """

    pnl_0x_2x: int | Unset = UNSET
    pnl_2x_5x: int | Unset = UNSET
    pnl_gt_5x: int | Unset = UNSET
    pnl_lt_nd5: int | Unset = UNSET
    pnl_nd5_0x: int | Unset = UNSET
    trader: str | Unset = UNSET
    window_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pnl_0x_2x = self.pnl_0x_2x

        pnl_2x_5x = self.pnl_2x_5x

        pnl_gt_5x = self.pnl_gt_5x

        pnl_lt_nd5 = self.pnl_lt_nd5

        pnl_nd5_0x = self.pnl_nd5_0x

        trader = self.trader

        window_label = self.window_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pnl_0x_2x is not UNSET:
            field_dict["pnl_0x_2x"] = pnl_0x_2x
        if pnl_2x_5x is not UNSET:
            field_dict["pnl_2x_5x"] = pnl_2x_5x
        if pnl_gt_5x is not UNSET:
            field_dict["pnl_gt_5x"] = pnl_gt_5x
        if pnl_lt_nd5 is not UNSET:
            field_dict["pnl_lt_nd5"] = pnl_lt_nd5
        if pnl_nd5_0x is not UNSET:
            field_dict["pnl_nd5_0x"] = pnl_nd5_0x
        if trader is not UNSET:
            field_dict["trader"] = trader
        if window_label is not UNSET:
            field_dict["window_label"] = window_label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pnl_0x_2x = d.pop("pnl_0x_2x", UNSET)

        pnl_2x_5x = d.pop("pnl_2x_5x", UNSET)

        pnl_gt_5x = d.pop("pnl_gt_5x", UNSET)

        pnl_lt_nd5 = d.pop("pnl_lt_nd5", UNSET)

        pnl_nd5_0x = d.pop("pnl_nd5_0x", UNSET)

        trader = d.pop("trader", UNSET)

        window_label = d.pop("window_label", UNSET)

        pulsight_internal_core_usecases_trader_trader_pnl_distribution_row = cls(
            pnl_0x_2x=pnl_0x_2x,
            pnl_2x_5x=pnl_2x_5x,
            pnl_gt_5x=pnl_gt_5x,
            pnl_lt_nd5=pnl_lt_nd5,
            pnl_nd5_0x=pnl_nd5_0x,
            trader=trader,
            window_label=window_label,
        )

        pulsight_internal_core_usecases_trader_trader_pnl_distribution_row.additional_properties = d
        return pulsight_internal_core_usecases_trader_trader_pnl_distribution_row

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
