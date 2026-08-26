from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCashbackProgramTotals")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCashbackProgramTotals:
    """
    Attributes:
        program (str | Unset): "pumpfun" | "pumpswap"
        total_claimed_lamports (int | Unset):
        total_earned_lamports (int | Unset):
    """

    program: str | Unset = UNSET
    total_claimed_lamports: int | Unset = UNSET
    total_earned_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program = self.program

        total_claimed_lamports = self.total_claimed_lamports

        total_earned_lamports = self.total_earned_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if program is not UNSET:
            field_dict["program"] = program
        if total_claimed_lamports is not UNSET:
            field_dict["total_claimed_lamports"] = total_claimed_lamports
        if total_earned_lamports is not UNSET:
            field_dict["total_earned_lamports"] = total_earned_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        program = d.pop("program", UNSET)

        total_claimed_lamports = d.pop("total_claimed_lamports", UNSET)

        total_earned_lamports = d.pop("total_earned_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_cashback_program_totals = cls(
            program=program,
            total_claimed_lamports=total_claimed_lamports,
            total_earned_lamports=total_earned_lamports,
        )

        pulsight_internal_core_domain_aggregator_cashback_program_totals.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cashback_program_totals

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
