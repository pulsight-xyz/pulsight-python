from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_window import (
    PulsightInternalCoreDomainAggregatorWindow,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderReliabilityStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderReliabilityStats:
    """
    Attributes:
        failed_arbs (int | Unset):
        failed_fee_lamports (int | Unset): Lamports burned on failed txs (base + priority fee) vs on landed
            no-CPI probes, plus tips the probes paid.
        failed_other (int | Unset):
        failed_swaps (int | Unset):
        failed_txs (int | Unset): = FailedSwaps + FailedArbs + FailedOther
        landed_txs (int | Unset): LandedTxs is uniqExact(signature) over the wallet's `swaps` rows in
            the window — successful swap TRANSACTIONS, not legs or trades.
        no_cpi_fee_lamports (int | Unset):
        no_cpi_tip_lamports (int | Unset):
        no_cpi_txs (int | Unset):
        pubkey (str | Unset):
        spam_rate (float | Unset):
        success_rate (float | Unset): SuccessRate = LandedTxs / (LandedTxs + FailedTxs); SpamRate =
            (FailedTxs + NoCpiTxs) / (LandedTxs + FailedTxs + NoCpiTxs).
            POINTERS: nil when the denominator is 0 — a wallet with no activity
            has no rate, and that must not read as 0%.
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    failed_arbs: int | Unset = UNSET
    failed_fee_lamports: int | Unset = UNSET
    failed_other: int | Unset = UNSET
    failed_swaps: int | Unset = UNSET
    failed_txs: int | Unset = UNSET
    landed_txs: int | Unset = UNSET
    no_cpi_fee_lamports: int | Unset = UNSET
    no_cpi_tip_lamports: int | Unset = UNSET
    no_cpi_txs: int | Unset = UNSET
    pubkey: str | Unset = UNSET
    spam_rate: float | Unset = UNSET
    success_rate: float | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_arbs = self.failed_arbs

        failed_fee_lamports = self.failed_fee_lamports

        failed_other = self.failed_other

        failed_swaps = self.failed_swaps

        failed_txs = self.failed_txs

        landed_txs = self.landed_txs

        no_cpi_fee_lamports = self.no_cpi_fee_lamports

        no_cpi_tip_lamports = self.no_cpi_tip_lamports

        no_cpi_txs = self.no_cpi_txs

        pubkey = self.pubkey

        spam_rate = self.spam_rate

        success_rate = self.success_rate

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed_arbs is not UNSET:
            field_dict["failed_arbs"] = failed_arbs
        if failed_fee_lamports is not UNSET:
            field_dict["failed_fee_lamports"] = failed_fee_lamports
        if failed_other is not UNSET:
            field_dict["failed_other"] = failed_other
        if failed_swaps is not UNSET:
            field_dict["failed_swaps"] = failed_swaps
        if failed_txs is not UNSET:
            field_dict["failed_txs"] = failed_txs
        if landed_txs is not UNSET:
            field_dict["landed_txs"] = landed_txs
        if no_cpi_fee_lamports is not UNSET:
            field_dict["no_cpi_fee_lamports"] = no_cpi_fee_lamports
        if no_cpi_tip_lamports is not UNSET:
            field_dict["no_cpi_tip_lamports"] = no_cpi_tip_lamports
        if no_cpi_txs is not UNSET:
            field_dict["no_cpi_txs"] = no_cpi_txs
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if spam_rate is not UNSET:
            field_dict["spam_rate"] = spam_rate
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failed_arbs = d.pop("failed_arbs", UNSET)

        failed_fee_lamports = d.pop("failed_fee_lamports", UNSET)

        failed_other = d.pop("failed_other", UNSET)

        failed_swaps = d.pop("failed_swaps", UNSET)

        failed_txs = d.pop("failed_txs", UNSET)

        landed_txs = d.pop("landed_txs", UNSET)

        no_cpi_fee_lamports = d.pop("no_cpi_fee_lamports", UNSET)

        no_cpi_tip_lamports = d.pop("no_cpi_tip_lamports", UNSET)

        no_cpi_txs = d.pop("no_cpi_txs", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        spam_rate = d.pop("spam_rate", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_trader_reliability_stats = cls(
            failed_arbs=failed_arbs,
            failed_fee_lamports=failed_fee_lamports,
            failed_other=failed_other,
            failed_swaps=failed_swaps,
            failed_txs=failed_txs,
            landed_txs=landed_txs,
            no_cpi_fee_lamports=no_cpi_fee_lamports,
            no_cpi_tip_lamports=no_cpi_tip_lamports,
            no_cpi_txs=no_cpi_txs,
            pubkey=pubkey,
            spam_rate=spam_rate,
            success_rate=success_rate,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_trader_reliability_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trader_reliability_stats

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
