from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramDayStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramDayStat:
    """
    Attributes:
        arb_no_cpi_txs (int | Unset):
        arb_revenue_lamports (int | Unset):
        arb_txs (int | Unset):
        day (str | Unset): "2026-08-23" (UTC)
        failed_arb_txs (int | Unset):
        failed_fee_lamports (int | Unset):
        failed_other_txs (int | Unset):
        failed_swap_txs (int | Unset):
        fee_revenue_lamports (int | Unset):
        other_txs (int | Unset):
        primary_volume_lamports (int | Unset):
        swap_txs (int | Unset):
        txs (int | Unset):
        users (int | Unset):
        venue_volume_lamports (int | Unset):
    """

    arb_no_cpi_txs: int | Unset = UNSET
    arb_revenue_lamports: int | Unset = UNSET
    arb_txs: int | Unset = UNSET
    day: str | Unset = UNSET
    failed_arb_txs: int | Unset = UNSET
    failed_fee_lamports: int | Unset = UNSET
    failed_other_txs: int | Unset = UNSET
    failed_swap_txs: int | Unset = UNSET
    fee_revenue_lamports: int | Unset = UNSET
    other_txs: int | Unset = UNSET
    primary_volume_lamports: int | Unset = UNSET
    swap_txs: int | Unset = UNSET
    txs: int | Unset = UNSET
    users: int | Unset = UNSET
    venue_volume_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_no_cpi_txs = self.arb_no_cpi_txs

        arb_revenue_lamports = self.arb_revenue_lamports

        arb_txs = self.arb_txs

        day = self.day

        failed_arb_txs = self.failed_arb_txs

        failed_fee_lamports = self.failed_fee_lamports

        failed_other_txs = self.failed_other_txs

        failed_swap_txs = self.failed_swap_txs

        fee_revenue_lamports = self.fee_revenue_lamports

        other_txs = self.other_txs

        primary_volume_lamports = self.primary_volume_lamports

        swap_txs = self.swap_txs

        txs = self.txs

        users = self.users

        venue_volume_lamports = self.venue_volume_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_no_cpi_txs is not UNSET:
            field_dict["arb_no_cpi_txs"] = arb_no_cpi_txs
        if arb_revenue_lamports is not UNSET:
            field_dict["arb_revenue_lamports"] = arb_revenue_lamports
        if arb_txs is not UNSET:
            field_dict["arb_txs"] = arb_txs
        if day is not UNSET:
            field_dict["day"] = day
        if failed_arb_txs is not UNSET:
            field_dict["failed_arb_txs"] = failed_arb_txs
        if failed_fee_lamports is not UNSET:
            field_dict["failed_fee_lamports"] = failed_fee_lamports
        if failed_other_txs is not UNSET:
            field_dict["failed_other_txs"] = failed_other_txs
        if failed_swap_txs is not UNSET:
            field_dict["failed_swap_txs"] = failed_swap_txs
        if fee_revenue_lamports is not UNSET:
            field_dict["fee_revenue_lamports"] = fee_revenue_lamports
        if other_txs is not UNSET:
            field_dict["other_txs"] = other_txs
        if primary_volume_lamports is not UNSET:
            field_dict["primary_volume_lamports"] = primary_volume_lamports
        if swap_txs is not UNSET:
            field_dict["swap_txs"] = swap_txs
        if txs is not UNSET:
            field_dict["txs"] = txs
        if users is not UNSET:
            field_dict["users"] = users
        if venue_volume_lamports is not UNSET:
            field_dict["venue_volume_lamports"] = venue_volume_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arb_no_cpi_txs = d.pop("arb_no_cpi_txs", UNSET)

        arb_revenue_lamports = d.pop("arb_revenue_lamports", UNSET)

        arb_txs = d.pop("arb_txs", UNSET)

        day = d.pop("day", UNSET)

        failed_arb_txs = d.pop("failed_arb_txs", UNSET)

        failed_fee_lamports = d.pop("failed_fee_lamports", UNSET)

        failed_other_txs = d.pop("failed_other_txs", UNSET)

        failed_swap_txs = d.pop("failed_swap_txs", UNSET)

        fee_revenue_lamports = d.pop("fee_revenue_lamports", UNSET)

        other_txs = d.pop("other_txs", UNSET)

        primary_volume_lamports = d.pop("primary_volume_lamports", UNSET)

        swap_txs = d.pop("swap_txs", UNSET)

        txs = d.pop("txs", UNSET)

        users = d.pop("users", UNSET)

        venue_volume_lamports = d.pop("venue_volume_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_program_day_stat = cls(
            arb_no_cpi_txs=arb_no_cpi_txs,
            arb_revenue_lamports=arb_revenue_lamports,
            arb_txs=arb_txs,
            day=day,
            failed_arb_txs=failed_arb_txs,
            failed_fee_lamports=failed_fee_lamports,
            failed_other_txs=failed_other_txs,
            failed_swap_txs=failed_swap_txs,
            fee_revenue_lamports=fee_revenue_lamports,
            other_txs=other_txs,
            primary_volume_lamports=primary_volume_lamports,
            swap_txs=swap_txs,
            txs=txs,
            users=users,
            venue_volume_lamports=venue_volume_lamports,
        )

        pulsight_internal_core_domain_aggregator_program_day_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_day_stat

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
