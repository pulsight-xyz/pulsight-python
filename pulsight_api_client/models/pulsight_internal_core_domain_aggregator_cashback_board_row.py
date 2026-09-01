from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCashbackBoardRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCashbackBoardRow:
    """
    Attributes:
        cashback_volume_lamports (int | Unset): CashbackVolumeLamports over TotalVolumeLamports is VolumeShare — nil
            when the window moved no volume (no share, which is not a 0% share).
        censored (bool | Unset):
        claim_count (int | Unset):
        claimed_lamports (int | Unset): ClaimedLamports / ClaimCount are nil only before CA 000106 exists. On
            the lifetime window they are RETENTION-BOUNDED (the raw claim ledger
            carries a 75-day TTL) — they undercount once rows age out rather than
            inventing, the trader panel's lifetime_claimed precedent.
        earned_lamports (int | Unset): EarnedLamports — cashback accrued in the window TO THIS WALLET'S OWN
            accumulator (since classifier 0cb3f9c, executor-routed fills whose
            accumulator belongs to the filler are excluded); the board's primary
            measure (claiming is sporadic, earning is the smooth signal).
        first_seen_ms (int | Unset):
        last_active_ms (int | Unset):
        pump_image (str | Unset):
        pump_username (str | Unset): Pump.fun profile enrichment (server-side, cached): the wallet's pump
            username and avatar when it has a profile. Always nil on a censored
            row — enrichment runs only on rows whose identity ships.
        rank (int | Unset): Rank is 1-based within the requested window + filters (offset-aware).
        tags (list[str] | Unset): Tags are the derived classification tags (`deriveTags`), resolved for
            the whole page in one round trip so a row states what the wallet is
            without being expanded. Empty on a censored row, and nil when the
            enrichment query failed — best-effort by contract, never an error the
            board surfaces.
        total_volume_lamports (int | Unset):
        trader (str | Unset): Trader is empty on a censored landing row (Censored true): the figures
            stay real, the identity is withheld server-side.
        volume_share (float | Unset):
    """

    cashback_volume_lamports: int | Unset = UNSET
    censored: bool | Unset = UNSET
    claim_count: int | Unset = UNSET
    claimed_lamports: int | Unset = UNSET
    earned_lamports: int | Unset = UNSET
    first_seen_ms: int | Unset = UNSET
    last_active_ms: int | Unset = UNSET
    pump_image: str | Unset = UNSET
    pump_username: str | Unset = UNSET
    rank: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    total_volume_lamports: int | Unset = UNSET
    trader: str | Unset = UNSET
    volume_share: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cashback_volume_lamports = self.cashback_volume_lamports

        censored = self.censored

        claim_count = self.claim_count

        claimed_lamports = self.claimed_lamports

        earned_lamports = self.earned_lamports

        first_seen_ms = self.first_seen_ms

        last_active_ms = self.last_active_ms

        pump_image = self.pump_image

        pump_username = self.pump_username

        rank = self.rank

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        total_volume_lamports = self.total_volume_lamports

        trader = self.trader

        volume_share = self.volume_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cashback_volume_lamports is not UNSET:
            field_dict["cashback_volume_lamports"] = cashback_volume_lamports
        if censored is not UNSET:
            field_dict["censored"] = censored
        if claim_count is not UNSET:
            field_dict["claim_count"] = claim_count
        if claimed_lamports is not UNSET:
            field_dict["claimed_lamports"] = claimed_lamports
        if earned_lamports is not UNSET:
            field_dict["earned_lamports"] = earned_lamports
        if first_seen_ms is not UNSET:
            field_dict["first_seen_ms"] = first_seen_ms
        if last_active_ms is not UNSET:
            field_dict["last_active_ms"] = last_active_ms
        if pump_image is not UNSET:
            field_dict["pump_image"] = pump_image
        if pump_username is not UNSET:
            field_dict["pump_username"] = pump_username
        if rank is not UNSET:
            field_dict["rank"] = rank
        if tags is not UNSET:
            field_dict["tags"] = tags
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports
        if trader is not UNSET:
            field_dict["trader"] = trader
        if volume_share is not UNSET:
            field_dict["volume_share"] = volume_share

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cashback_volume_lamports = d.pop("cashback_volume_lamports", UNSET)

        censored = d.pop("censored", UNSET)

        claim_count = d.pop("claim_count", UNSET)

        claimed_lamports = d.pop("claimed_lamports", UNSET)

        earned_lamports = d.pop("earned_lamports", UNSET)

        first_seen_ms = d.pop("first_seen_ms", UNSET)

        last_active_ms = d.pop("last_active_ms", UNSET)

        pump_image = d.pop("pump_image", UNSET)

        pump_username = d.pop("pump_username", UNSET)

        rank = d.pop("rank", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        trader = d.pop("trader", UNSET)

        volume_share = d.pop("volume_share", UNSET)

        pulsight_internal_core_domain_aggregator_cashback_board_row = cls(
            cashback_volume_lamports=cashback_volume_lamports,
            censored=censored,
            claim_count=claim_count,
            claimed_lamports=claimed_lamports,
            earned_lamports=earned_lamports,
            first_seen_ms=first_seen_ms,
            last_active_ms=last_active_ms,
            pump_image=pump_image,
            pump_username=pump_username,
            rank=rank,
            tags=tags,
            total_volume_lamports=total_volume_lamports,
            trader=trader,
            volume_share=volume_share,
        )

        pulsight_internal_core_domain_aggregator_cashback_board_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cashback_board_row

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
