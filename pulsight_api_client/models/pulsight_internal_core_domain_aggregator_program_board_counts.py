from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramBoardCounts")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramBoardCounts:
    """
    Attributes:
        all_ (int | Unset):
        amm (int | Unset):
        arbitrage (int | Unset):
        router (int | Unset):
        unknown (int | Unset):
    """

    all_: int | Unset = UNSET
    amm: int | Unset = UNSET
    arbitrage: int | Unset = UNSET
    router: int | Unset = UNSET
    unknown: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        amm = self.amm

        arbitrage = self.arbitrage

        router = self.router

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if amm is not UNSET:
            field_dict["amm"] = amm
        if arbitrage is not UNSET:
            field_dict["arbitrage"] = arbitrage
        if router is not UNSET:
            field_dict["router"] = router
        if unknown is not UNSET:
            field_dict["unknown"] = unknown

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        amm = d.pop("amm", UNSET)

        arbitrage = d.pop("arbitrage", UNSET)

        router = d.pop("router", UNSET)

        unknown = d.pop("unknown", UNSET)

        pulsight_internal_core_domain_aggregator_program_board_counts = cls(
            all_=all_,
            amm=amm,
            arbitrage=arbitrage,
            router=router,
            unknown=unknown,
        )

        pulsight_internal_core_domain_aggregator_program_board_counts.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_board_counts

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
