from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_money import (
        PulsightInternalCoreDomainAggregatorMoney,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorArb")


@_attrs_define
class PulsightInternalCoreDomainAggregatorArb:
    """
    Attributes:
        funding (PulsightInternalCoreDomainAggregatorMoney | Unset):
        gross (PulsightInternalCoreDomainAggregatorMoney | Unset):
        kind (str | Unset):
        notional (PulsightInternalCoreDomainAggregatorMoney | Unset):
        pools (int | Unset):
        priced (bool | Unset):
        take_home (PulsightInternalCoreDomainAggregatorMoney | Unset):
    """

    funding: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    gross: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    kind: str | Unset = UNSET
    notional: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    pools: int | Unset = UNSET
    priced: bool | Unset = UNSET
    take_home: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funding, Unset):
            funding = self.funding.to_dict()

        gross: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gross, Unset):
            gross = self.gross.to_dict()

        kind = self.kind

        notional: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notional, Unset):
            notional = self.notional.to_dict()

        pools = self.pools

        priced = self.priced

        take_home: dict[str, Any] | Unset = UNSET
        if not isinstance(self.take_home, Unset):
            take_home = self.take_home.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if funding is not UNSET:
            field_dict["funding"] = funding
        if gross is not UNSET:
            field_dict["gross"] = gross
        if kind is not UNSET:
            field_dict["kind"] = kind
        if notional is not UNSET:
            field_dict["notional"] = notional
        if pools is not UNSET:
            field_dict["pools"] = pools
        if priced is not UNSET:
            field_dict["priced"] = priced
        if take_home is not UNSET:
            field_dict["take_home"] = take_home

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_money import (
            PulsightInternalCoreDomainAggregatorMoney,
        )

        d = dict(src_dict)
        _funding = d.pop("funding", UNSET)
        funding: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_funding, Unset):
            funding = UNSET
        else:
            funding = PulsightInternalCoreDomainAggregatorMoney.from_dict(_funding)

        _gross = d.pop("gross", UNSET)
        gross: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_gross, Unset):
            gross = UNSET
        else:
            gross = PulsightInternalCoreDomainAggregatorMoney.from_dict(_gross)

        kind = d.pop("kind", UNSET)

        _notional = d.pop("notional", UNSET)
        notional: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_notional, Unset):
            notional = UNSET
        else:
            notional = PulsightInternalCoreDomainAggregatorMoney.from_dict(_notional)

        pools = d.pop("pools", UNSET)

        priced = d.pop("priced", UNSET)

        _take_home = d.pop("take_home", UNSET)
        take_home: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_take_home, Unset):
            take_home = UNSET
        else:
            take_home = PulsightInternalCoreDomainAggregatorMoney.from_dict(_take_home)

        pulsight_internal_core_domain_aggregator_arb = cls(
            funding=funding,
            gross=gross,
            kind=kind,
            notional=notional,
            pools=pools,
            priced=priced,
            take_home=take_home,
        )

        pulsight_internal_core_domain_aggregator_arb.additional_properties = d
        return pulsight_internal_core_domain_aggregator_arb

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
