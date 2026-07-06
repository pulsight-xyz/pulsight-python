from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorJitoEfficiencyRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorJitoEfficiencyRow:
    """
    Attributes:
        efficiency_score (float | Unset):
        tip_swaps (int | Unset):
        total_tip_sum (int | Unset):
        total_volume_in (int | Unset):
        trader (str | Unset):
    """

    efficiency_score: float | Unset = UNSET
    tip_swaps: int | Unset = UNSET
    total_tip_sum: int | Unset = UNSET
    total_volume_in: int | Unset = UNSET
    trader: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        efficiency_score = self.efficiency_score

        tip_swaps = self.tip_swaps

        total_tip_sum = self.total_tip_sum

        total_volume_in = self.total_volume_in

        trader = self.trader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if efficiency_score is not UNSET:
            field_dict["efficiency_score"] = efficiency_score
        if tip_swaps is not UNSET:
            field_dict["tip_swaps"] = tip_swaps
        if total_tip_sum is not UNSET:
            field_dict["total_tip_sum"] = total_tip_sum
        if total_volume_in is not UNSET:
            field_dict["total_volume_in"] = total_volume_in
        if trader is not UNSET:
            field_dict["trader"] = trader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        efficiency_score = d.pop("efficiency_score", UNSET)

        tip_swaps = d.pop("tip_swaps", UNSET)

        total_tip_sum = d.pop("total_tip_sum", UNSET)

        total_volume_in = d.pop("total_volume_in", UNSET)

        trader = d.pop("trader", UNSET)

        pulsight_internal_core_domain_aggregator_jito_efficiency_row = cls(
            efficiency_score=efficiency_score,
            tip_swaps=tip_swaps,
            total_tip_sum=total_tip_sum,
            total_volume_in=total_volume_in,
            trader=trader,
        )

        pulsight_internal_core_domain_aggregator_jito_efficiency_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_jito_efficiency_row

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
