from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_window import (
    PulsightInternalCoreDomainAggregatorWindow,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_cashback_claim_row import (
        PulsightInternalCoreDomainAggregatorCashbackClaimRow,
    )
    from ..models.pulsight_internal_core_domain_aggregator_cashback_program_totals import (
        PulsightInternalCoreDomainAggregatorCashbackProgramTotals,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderCashbackStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderCashbackStats:
    """
    Attributes:
        avg_cashback_bps (float | Unset):
        cashback_volume_lamports (int | Unset): CashbackVolumeLamports — the window's quote-side volume on
            cashback-enabled coins; TotalVolumeLamports the window's whole
            quote-side volume (buy in + sell out). VolumeShare divides the two
            (nil when no volume); AvgCashbackBps = earned / cashback volume in
            basis points (nil when no cashback volume) — the effective rebate
            rate, which is per-coin on-chain (30 and 90 bps both live).
        claim_count (int | Unset): Claim cadence, lifetime, all quote denominations.
        claimable_lamports (int | Unset): ClaimableLamports is the unclaimed balance sitting in the wallet's
            accumulators: cashback accrued SINCE its last claim. A claim sweeps
            the accumulator in full, so the balance at that moment is 0 and
            everything after it is unclaimed — which makes this immune both to
            the claim ledger's TTL and to history that predates our ingest, since
            only a timestamp comes from the claim side. Wallets that never claimed
            report everything we have observed them earn. Reads LOW, never high
            (see cashbackAccruedSince for the two bounded undercounts).
        claimed_lamports (int | Unset): ClaimedLamports — WSOL cashback swept by claim_cashback in the window.
            This is the cash-basis component net PnL ADDS (page, series, board —
            all three fold the same claimed numbers, #c22).
        earned_lamports (int | Unset): EarnedLamports — cashback ACCRUED by the window's swaps (the exact
            per-swap amounts from the pump trade events, WSOL-quoted markets
            only). Informational: the net-PnL formulas fold CLAIMED, not this.
        last_claim_at (str | Unset):
        lifetime_claimed_lamports (int | Unset):
        lifetime_earned_lamports (int | Unset): LifetimeEarnedLamports is exact: it comes from `trader_stats.cashback`,
            which is untimed, WSOL-only by construction and rebuildable from
            `swaps`. LifetimeClaimedLamports is bounded by the raw claim ledger's
            75-day retention (CA 000098) — the same compromise reliability's "all"
            window makes, undercounting rather than inventing. ProgramTotals below
            carries the program's own all-time figures beside it.
        program_totals (list[PulsightInternalCoreDomainAggregatorCashbackProgramTotals] | Unset): ProgramTotals — the
            lifetime running totals the pump program itself
            stamped on the wallet's LATEST claim event, one row per program
            (pumpfun = bonding curve, pumpswap = AMM), read from
            `cashback_claim_anchors` so they outlive the raw ledger's TTL. They
            cover history from before our ingest and are surfaced verbatim as
            "program-reported" — DISPLAY ONLY. Never fold them into a lamport
            figure: the on-chain counter is one u64 per accumulator and cashback
            is not SOL-only (~7% of sampled claims carried a USDC quote), so
            whether it mixes denominations is not observable from the event.
            Empty array when the wallet never claimed.
        pubkey (str | Unset):
        recent_claims (list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset): RecentClaims — the wallet's
            latest claims, newest first (≤10).
            AmountLamports is in the claim's quote-mint base units — lamports for
            WSOL rows, which is nearly all of them.
        total_volume_lamports (int | Unset):
        volume_share (float | Unset):
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    avg_cashback_bps: float | Unset = UNSET
    cashback_volume_lamports: int | Unset = UNSET
    claim_count: int | Unset = UNSET
    claimable_lamports: int | Unset = UNSET
    claimed_lamports: int | Unset = UNSET
    earned_lamports: int | Unset = UNSET
    last_claim_at: str | Unset = UNSET
    lifetime_claimed_lamports: int | Unset = UNSET
    lifetime_earned_lamports: int | Unset = UNSET
    program_totals: (
        list[PulsightInternalCoreDomainAggregatorCashbackProgramTotals] | Unset
    ) = UNSET
    pubkey: str | Unset = UNSET
    recent_claims: (
        list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset
    ) = UNSET
    total_volume_lamports: int | Unset = UNSET
    volume_share: float | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_cashback_bps = self.avg_cashback_bps

        cashback_volume_lamports = self.cashback_volume_lamports

        claim_count = self.claim_count

        claimable_lamports = self.claimable_lamports

        claimed_lamports = self.claimed_lamports

        earned_lamports = self.earned_lamports

        last_claim_at = self.last_claim_at

        lifetime_claimed_lamports = self.lifetime_claimed_lamports

        lifetime_earned_lamports = self.lifetime_earned_lamports

        program_totals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.program_totals, Unset):
            program_totals = []
            for program_totals_item_data in self.program_totals:
                program_totals_item = program_totals_item_data.to_dict()
                program_totals.append(program_totals_item)

        pubkey = self.pubkey

        recent_claims: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_claims, Unset):
            recent_claims = []
            for recent_claims_item_data in self.recent_claims:
                recent_claims_item = recent_claims_item_data.to_dict()
                recent_claims.append(recent_claims_item)

        total_volume_lamports = self.total_volume_lamports

        volume_share = self.volume_share

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_cashback_bps is not UNSET:
            field_dict["avg_cashback_bps"] = avg_cashback_bps
        if cashback_volume_lamports is not UNSET:
            field_dict["cashback_volume_lamports"] = cashback_volume_lamports
        if claim_count is not UNSET:
            field_dict["claim_count"] = claim_count
        if claimable_lamports is not UNSET:
            field_dict["claimable_lamports"] = claimable_lamports
        if claimed_lamports is not UNSET:
            field_dict["claimed_lamports"] = claimed_lamports
        if earned_lamports is not UNSET:
            field_dict["earned_lamports"] = earned_lamports
        if last_claim_at is not UNSET:
            field_dict["last_claim_at"] = last_claim_at
        if lifetime_claimed_lamports is not UNSET:
            field_dict["lifetime_claimed_lamports"] = lifetime_claimed_lamports
        if lifetime_earned_lamports is not UNSET:
            field_dict["lifetime_earned_lamports"] = lifetime_earned_lamports
        if program_totals is not UNSET:
            field_dict["program_totals"] = program_totals
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if recent_claims is not UNSET:
            field_dict["recent_claims"] = recent_claims
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports
        if volume_share is not UNSET:
            field_dict["volume_share"] = volume_share
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_cashback_claim_row import (
            PulsightInternalCoreDomainAggregatorCashbackClaimRow,
        )
        from ..models.pulsight_internal_core_domain_aggregator_cashback_program_totals import (
            PulsightInternalCoreDomainAggregatorCashbackProgramTotals,
        )

        d = dict(src_dict)
        avg_cashback_bps = d.pop("avg_cashback_bps", UNSET)

        cashback_volume_lamports = d.pop("cashback_volume_lamports", UNSET)

        claim_count = d.pop("claim_count", UNSET)

        claimable_lamports = d.pop("claimable_lamports", UNSET)

        claimed_lamports = d.pop("claimed_lamports", UNSET)

        earned_lamports = d.pop("earned_lamports", UNSET)

        last_claim_at = d.pop("last_claim_at", UNSET)

        lifetime_claimed_lamports = d.pop("lifetime_claimed_lamports", UNSET)

        lifetime_earned_lamports = d.pop("lifetime_earned_lamports", UNSET)

        _program_totals = d.pop("program_totals", UNSET)
        program_totals: (
            list[PulsightInternalCoreDomainAggregatorCashbackProgramTotals] | Unset
        ) = UNSET
        if _program_totals is not UNSET:
            program_totals = []
            for program_totals_item_data in _program_totals:
                program_totals_item = (
                    PulsightInternalCoreDomainAggregatorCashbackProgramTotals.from_dict(
                        program_totals_item_data
                    )
                )

                program_totals.append(program_totals_item)

        pubkey = d.pop("pubkey", UNSET)

        _recent_claims = d.pop("recent_claims", UNSET)
        recent_claims: (
            list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset
        ) = UNSET
        if _recent_claims is not UNSET:
            recent_claims = []
            for recent_claims_item_data in _recent_claims:
                recent_claims_item = (
                    PulsightInternalCoreDomainAggregatorCashbackClaimRow.from_dict(
                        recent_claims_item_data
                    )
                )

                recent_claims.append(recent_claims_item)

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        volume_share = d.pop("volume_share", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_trader_cashback_stats = cls(
            avg_cashback_bps=avg_cashback_bps,
            cashback_volume_lamports=cashback_volume_lamports,
            claim_count=claim_count,
            claimable_lamports=claimable_lamports,
            claimed_lamports=claimed_lamports,
            earned_lamports=earned_lamports,
            last_claim_at=last_claim_at,
            lifetime_claimed_lamports=lifetime_claimed_lamports,
            lifetime_earned_lamports=lifetime_earned_lamports,
            program_totals=program_totals,
            pubkey=pubkey,
            recent_claims=recent_claims,
            total_volume_lamports=total_volume_lamports,
            volume_share=volume_share,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_trader_cashback_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trader_cashback_stats

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
