from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramBoardRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramBoardRow:
    """
    Attributes:
        arb_txs (int | Unset):
        category (str | Unset): Category is the RESOLVED category: admin identity > embedded
            program seed > 7d auto-arb rule > "unknown".
        censored (bool | Unset):
        failed_txs (int | Unset):
        first_seen_ms (int | Unset):
        hidden (bool | Unset): Hidden mirrors the admin identity's hide flag. Hidden rows never
            reach the public board (dropped before ranking) — only the admin
            listing serves them.
        last_seen_ms (int | Unset):
        logo_uri (str | Unset): LogoURI is the admin-assigned identity logo, falling back to the
            embedded seed's self-hosted mirror path (/program-logos/…); empty
            when the program has none.
        name (str | Unset): Name is the admin-assigned identity name, falling back to the
            embedded seed name; empty when unnamed.
        non_swap_rate (float | Unset):
        program_id (str | Unset):
        rank (int | Unset):
        revenue_lamports (int | Unset): RevenueLamports is category-gated (ProgramRevenueLamports): net arb
            extraction for arbitrage programs (can be negative — an unprofitable
            bot), decoded venue fees for amm/dex programs, and 0 ("not measured")
            for routers, unknowns and every other category.
        spam_rate (float | Unset):
        spark (list[int] | Unset): Spark is the program's daily volume over the trailing 7 days
            (lamports, oldest first; role-matched like VolumeLamports). Only
            populated on the rows a page actually returns.
        success_rate (float | Unset):
        txs (int | Unset): Txs is the landed tx count (incl. no-CPI probes).
        unique_users (int | Unset):
        volume_lamports (int | Unset): VolumeLamports is venue-executed volume for amm/dex-category
            programs (true venue volume incl. routed flow) and tx-level primary
            volume for everything else. WSOL-projected lamports; unpriced
            quote flow is excluded, never guessed.
    """

    arb_txs: int | Unset = UNSET
    category: str | Unset = UNSET
    censored: bool | Unset = UNSET
    failed_txs: int | Unset = UNSET
    first_seen_ms: int | Unset = UNSET
    hidden: bool | Unset = UNSET
    last_seen_ms: int | Unset = UNSET
    logo_uri: str | Unset = UNSET
    name: str | Unset = UNSET
    non_swap_rate: float | Unset = UNSET
    program_id: str | Unset = UNSET
    rank: int | Unset = UNSET
    revenue_lamports: int | Unset = UNSET
    spam_rate: float | Unset = UNSET
    spark: list[int] | Unset = UNSET
    success_rate: float | Unset = UNSET
    txs: int | Unset = UNSET
    unique_users: int | Unset = UNSET
    volume_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_txs = self.arb_txs

        category = self.category

        censored = self.censored

        failed_txs = self.failed_txs

        first_seen_ms = self.first_seen_ms

        hidden = self.hidden

        last_seen_ms = self.last_seen_ms

        logo_uri = self.logo_uri

        name = self.name

        non_swap_rate = self.non_swap_rate

        program_id = self.program_id

        rank = self.rank

        revenue_lamports = self.revenue_lamports

        spam_rate = self.spam_rate

        spark: list[int] | Unset = UNSET
        if not isinstance(self.spark, Unset):
            spark = self.spark

        success_rate = self.success_rate

        txs = self.txs

        unique_users = self.unique_users

        volume_lamports = self.volume_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_txs is not UNSET:
            field_dict["arb_txs"] = arb_txs
        if category is not UNSET:
            field_dict["category"] = category
        if censored is not UNSET:
            field_dict["censored"] = censored
        if failed_txs is not UNSET:
            field_dict["failed_txs"] = failed_txs
        if first_seen_ms is not UNSET:
            field_dict["first_seen_ms"] = first_seen_ms
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if last_seen_ms is not UNSET:
            field_dict["last_seen_ms"] = last_seen_ms
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if name is not UNSET:
            field_dict["name"] = name
        if non_swap_rate is not UNSET:
            field_dict["non_swap_rate"] = non_swap_rate
        if program_id is not UNSET:
            field_dict["program_id"] = program_id
        if rank is not UNSET:
            field_dict["rank"] = rank
        if revenue_lamports is not UNSET:
            field_dict["revenue_lamports"] = revenue_lamports
        if spam_rate is not UNSET:
            field_dict["spam_rate"] = spam_rate
        if spark is not UNSET:
            field_dict["spark"] = spark
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if txs is not UNSET:
            field_dict["txs"] = txs
        if unique_users is not UNSET:
            field_dict["unique_users"] = unique_users
        if volume_lamports is not UNSET:
            field_dict["volume_lamports"] = volume_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arb_txs = d.pop("arb_txs", UNSET)

        category = d.pop("category", UNSET)

        censored = d.pop("censored", UNSET)

        failed_txs = d.pop("failed_txs", UNSET)

        first_seen_ms = d.pop("first_seen_ms", UNSET)

        hidden = d.pop("hidden", UNSET)

        last_seen_ms = d.pop("last_seen_ms", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        name = d.pop("name", UNSET)

        non_swap_rate = d.pop("non_swap_rate", UNSET)

        program_id = d.pop("program_id", UNSET)

        rank = d.pop("rank", UNSET)

        revenue_lamports = d.pop("revenue_lamports", UNSET)

        spam_rate = d.pop("spam_rate", UNSET)

        spark = cast(list[int], d.pop("spark", UNSET))

        success_rate = d.pop("success_rate", UNSET)

        txs = d.pop("txs", UNSET)

        unique_users = d.pop("unique_users", UNSET)

        volume_lamports = d.pop("volume_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_program_board_row = cls(
            arb_txs=arb_txs,
            category=category,
            censored=censored,
            failed_txs=failed_txs,
            first_seen_ms=first_seen_ms,
            hidden=hidden,
            last_seen_ms=last_seen_ms,
            logo_uri=logo_uri,
            name=name,
            non_swap_rate=non_swap_rate,
            program_id=program_id,
            rank=rank,
            revenue_lamports=revenue_lamports,
            spam_rate=spam_rate,
            spark=spark,
            success_rate=success_rate,
            txs=txs,
            unique_users=unique_users,
            volume_lamports=volume_lamports,
        )

        pulsight_internal_core_domain_aggregator_program_board_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_board_row

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
