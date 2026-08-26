from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramWindowFigures")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramWindowFigures:
    """
    Attributes:
        failed_txs (int | Unset):
        non_swap_rate (float | Unset):
        primary_volume_lamports (int | Unset):
        revenue_lamports (int | Unset):
        spam_rate (float | Unset):
        success_rate (float | Unset):
        txs (int | Unset): Txs is the landed tx count (incl. no-CPI probes).
        unique_users (int | Unset):
        venue_volume_lamports (int | Unset):
    """

    failed_txs: int | Unset = UNSET
    non_swap_rate: float | Unset = UNSET
    primary_volume_lamports: int | Unset = UNSET
    revenue_lamports: int | Unset = UNSET
    spam_rate: float | Unset = UNSET
    success_rate: float | Unset = UNSET
    txs: int | Unset = UNSET
    unique_users: int | Unset = UNSET
    venue_volume_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_txs = self.failed_txs

        non_swap_rate = self.non_swap_rate

        primary_volume_lamports = self.primary_volume_lamports

        revenue_lamports = self.revenue_lamports

        spam_rate = self.spam_rate

        success_rate = self.success_rate

        txs = self.txs

        unique_users = self.unique_users

        venue_volume_lamports = self.venue_volume_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed_txs is not UNSET:
            field_dict["failed_txs"] = failed_txs
        if non_swap_rate is not UNSET:
            field_dict["non_swap_rate"] = non_swap_rate
        if primary_volume_lamports is not UNSET:
            field_dict["primary_volume_lamports"] = primary_volume_lamports
        if revenue_lamports is not UNSET:
            field_dict["revenue_lamports"] = revenue_lamports
        if spam_rate is not UNSET:
            field_dict["spam_rate"] = spam_rate
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if txs is not UNSET:
            field_dict["txs"] = txs
        if unique_users is not UNSET:
            field_dict["unique_users"] = unique_users
        if venue_volume_lamports is not UNSET:
            field_dict["venue_volume_lamports"] = venue_volume_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failed_txs = d.pop("failed_txs", UNSET)

        non_swap_rate = d.pop("non_swap_rate", UNSET)

        primary_volume_lamports = d.pop("primary_volume_lamports", UNSET)

        revenue_lamports = d.pop("revenue_lamports", UNSET)

        spam_rate = d.pop("spam_rate", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        txs = d.pop("txs", UNSET)

        unique_users = d.pop("unique_users", UNSET)

        venue_volume_lamports = d.pop("venue_volume_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_program_window_figures = cls(
            failed_txs=failed_txs,
            non_swap_rate=non_swap_rate,
            primary_volume_lamports=primary_volume_lamports,
            revenue_lamports=revenue_lamports,
            spam_rate=spam_rate,
            success_rate=success_rate,
            txs=txs,
            unique_users=unique_users,
            venue_volume_lamports=venue_volume_lamports,
        )

        pulsight_internal_core_domain_aggregator_program_window_figures.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_window_figures

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
