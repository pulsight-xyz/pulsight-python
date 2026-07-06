from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorServiceDominanceRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorServiceDominanceRow:
    """
    Attributes:
        share_pct (float | Unset):
        tip_service (str | Unset):
        tip_sum_lamports (int | Unset):
        tipped_count (int | Unset):
    """

    share_pct: float | Unset = UNSET
    tip_service: str | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    tipped_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_pct = self.share_pct

        tip_service = self.tip_service

        tip_sum_lamports = self.tip_sum_lamports

        tipped_count = self.tipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_pct is not UNSET:
            field_dict["share_pct"] = share_pct
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports
        if tipped_count is not UNSET:
            field_dict["tipped_count"] = tipped_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        share_pct = d.pop("share_pct", UNSET)

        tip_service = d.pop("tip_service", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        tipped_count = d.pop("tipped_count", UNSET)

        pulsight_internal_core_domain_aggregator_service_dominance_row = cls(
            share_pct=share_pct,
            tip_service=tip_service,
            tip_sum_lamports=tip_sum_lamports,
            tipped_count=tipped_count,
        )

        pulsight_internal_core_domain_aggregator_service_dominance_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_service_dominance_row

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
