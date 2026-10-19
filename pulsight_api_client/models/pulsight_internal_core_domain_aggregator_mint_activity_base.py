from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintActivityBase")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintActivityBase:
    """
    Attributes:
        fees_lamports (int | Unset):
        fees_micro_usd (int | Unset):
        swaps (int | Unset):
        tip_trades (int | Unset): TipTrades is a point's tip_trades over everything before the range.
            Served with the `tips` field.
        tipped_trades (int | Unset): TippedTrades is a point's tipped_trades over everything before the
            range. Served with the `tips` field.
        traders (str | Unset): Traders packs the key of every wallet with a buy or sell row before the
            range, as a point's traders. Served with the `trader_base` field.
    """

    fees_lamports: int | Unset = UNSET
    fees_micro_usd: int | Unset = UNSET
    swaps: int | Unset = UNSET
    tip_trades: int | Unset = UNSET
    tipped_trades: int | Unset = UNSET
    traders: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fees_lamports = self.fees_lamports

        fees_micro_usd = self.fees_micro_usd

        swaps = self.swaps

        tip_trades = self.tip_trades

        tipped_trades = self.tipped_trades

        traders = self.traders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fees_lamports is not UNSET:
            field_dict["fees_lamports"] = fees_lamports
        if fees_micro_usd is not UNSET:
            field_dict["fees_micro_usd"] = fees_micro_usd
        if swaps is not UNSET:
            field_dict["swaps"] = swaps
        if tip_trades is not UNSET:
            field_dict["tip_trades"] = tip_trades
        if tipped_trades is not UNSET:
            field_dict["tipped_trades"] = tipped_trades
        if traders is not UNSET:
            field_dict["traders"] = traders

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fees_lamports = d.pop("fees_lamports", UNSET)

        fees_micro_usd = d.pop("fees_micro_usd", UNSET)

        swaps = d.pop("swaps", UNSET)

        tip_trades = d.pop("tip_trades", UNSET)

        tipped_trades = d.pop("tipped_trades", UNSET)

        traders = d.pop("traders", UNSET)

        pulsight_internal_core_domain_aggregator_mint_activity_base = cls(
            fees_lamports=fees_lamports,
            fees_micro_usd=fees_micro_usd,
            swaps=swaps,
            tip_trades=tip_trades,
            tipped_trades=tipped_trades,
            traders=traders,
        )

        pulsight_internal_core_domain_aggregator_mint_activity_base.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_activity_base

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
