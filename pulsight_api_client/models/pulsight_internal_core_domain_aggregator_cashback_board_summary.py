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

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCashbackBoardSummary")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCashbackBoardSummary:
    """
    Attributes:
        claim_count (int | Unset):
        claimed_lamports (int | Unset): ClaimedLamports / ClaimCount: on the lifetime window these are
            RETENTION-BOUNDED sums over the 75-day claim ledger (undercount, never
            invented).
        earned_lamports (int | Unset):
        earners (int | Unset): Earners / EarnedLamports — wallets with any earned cashback in the
            window, and their summed earnings (the "% of pool" denominator).
        median_earned_lamports (int | Unset): Population marks.
        rank1_earned_lamports (int | Unset):
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    claim_count: int | Unset = UNSET
    claimed_lamports: int | Unset = UNSET
    earned_lamports: int | Unset = UNSET
    earners: int | Unset = UNSET
    median_earned_lamports: int | Unset = UNSET
    rank1_earned_lamports: int | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim_count = self.claim_count

        claimed_lamports = self.claimed_lamports

        earned_lamports = self.earned_lamports

        earners = self.earners

        median_earned_lamports = self.median_earned_lamports

        rank1_earned_lamports = self.rank1_earned_lamports

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim_count is not UNSET:
            field_dict["claim_count"] = claim_count
        if claimed_lamports is not UNSET:
            field_dict["claimed_lamports"] = claimed_lamports
        if earned_lamports is not UNSET:
            field_dict["earned_lamports"] = earned_lamports
        if earners is not UNSET:
            field_dict["earners"] = earners
        if median_earned_lamports is not UNSET:
            field_dict["median_earned_lamports"] = median_earned_lamports
        if rank1_earned_lamports is not UNSET:
            field_dict["rank1_earned_lamports"] = rank1_earned_lamports
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        claim_count = d.pop("claim_count", UNSET)

        claimed_lamports = d.pop("claimed_lamports", UNSET)

        earned_lamports = d.pop("earned_lamports", UNSET)

        earners = d.pop("earners", UNSET)

        median_earned_lamports = d.pop("median_earned_lamports", UNSET)

        rank1_earned_lamports = d.pop("rank1_earned_lamports", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_cashback_board_summary = cls(
            claim_count=claim_count,
            claimed_lamports=claimed_lamports,
            earned_lamports=earned_lamports,
            earners=earners,
            median_earned_lamports=median_earned_lamports,
            rank1_earned_lamports=rank1_earned_lamports,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_cashback_board_summary.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cashback_board_summary

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
