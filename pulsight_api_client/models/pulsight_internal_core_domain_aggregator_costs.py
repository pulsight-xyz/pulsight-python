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


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCosts")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCosts:
    """
    Attributes:
        base_fee (PulsightInternalCoreDomainAggregatorMoney | Unset):
        cashback_on_top (PulsightInternalCoreDomainAggregatorMoney | Unset):
        dex_fee (PulsightInternalCoreDomainAggregatorMoney | Unset):
        payer (str | Unset):
        platform (str | Unset):
        platform_fee (PulsightInternalCoreDomainAggregatorMoney | Unset):
        priority_fee (PulsightInternalCoreDomainAggregatorMoney | Unset):
        rent_paid (PulsightInternalCoreDomainAggregatorMoney | Unset):
        rent_refunded (PulsightInternalCoreDomainAggregatorMoney | Unset):
        tip (PulsightInternalCoreDomainAggregatorMoney | Unset):
        tip_service (str | Unset):
    """

    base_fee: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    cashback_on_top: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    dex_fee: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    payer: str | Unset = UNSET
    platform: str | Unset = UNSET
    platform_fee: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    priority_fee: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    rent_paid: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    rent_refunded: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    tip: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    tip_service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_fee, Unset):
            base_fee = self.base_fee.to_dict()

        cashback_on_top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cashback_on_top, Unset):
            cashback_on_top = self.cashback_on_top.to_dict()

        dex_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dex_fee, Unset):
            dex_fee = self.dex_fee.to_dict()

        payer = self.payer

        platform = self.platform

        platform_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_fee, Unset):
            platform_fee = self.platform_fee.to_dict()

        priority_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority_fee, Unset):
            priority_fee = self.priority_fee.to_dict()

        rent_paid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rent_paid, Unset):
            rent_paid = self.rent_paid.to_dict()

        rent_refunded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rent_refunded, Unset):
            rent_refunded = self.rent_refunded.to_dict()

        tip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tip, Unset):
            tip = self.tip.to_dict()

        tip_service = self.tip_service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_fee is not UNSET:
            field_dict["base_fee"] = base_fee
        if cashback_on_top is not UNSET:
            field_dict["cashback_on_top"] = cashback_on_top
        if dex_fee is not UNSET:
            field_dict["dex_fee"] = dex_fee
        if payer is not UNSET:
            field_dict["payer"] = payer
        if platform is not UNSET:
            field_dict["platform"] = platform
        if platform_fee is not UNSET:
            field_dict["platform_fee"] = platform_fee
        if priority_fee is not UNSET:
            field_dict["priority_fee"] = priority_fee
        if rent_paid is not UNSET:
            field_dict["rent_paid"] = rent_paid
        if rent_refunded is not UNSET:
            field_dict["rent_refunded"] = rent_refunded
        if tip is not UNSET:
            field_dict["tip"] = tip
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_money import (
            PulsightInternalCoreDomainAggregatorMoney,
        )

        d = dict(src_dict)
        _base_fee = d.pop("base_fee", UNSET)
        base_fee: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_base_fee, Unset):
            base_fee = UNSET
        else:
            base_fee = PulsightInternalCoreDomainAggregatorMoney.from_dict(_base_fee)

        _cashback_on_top = d.pop("cashback_on_top", UNSET)
        cashback_on_top: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_cashback_on_top, Unset):
            cashback_on_top = UNSET
        else:
            cashback_on_top = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _cashback_on_top
            )

        _dex_fee = d.pop("dex_fee", UNSET)
        dex_fee: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_dex_fee, Unset):
            dex_fee = UNSET
        else:
            dex_fee = PulsightInternalCoreDomainAggregatorMoney.from_dict(_dex_fee)

        payer = d.pop("payer", UNSET)

        platform = d.pop("platform", UNSET)

        _platform_fee = d.pop("platform_fee", UNSET)
        platform_fee: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_platform_fee, Unset):
            platform_fee = UNSET
        else:
            platform_fee = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _platform_fee
            )

        _priority_fee = d.pop("priority_fee", UNSET)
        priority_fee: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_priority_fee, Unset):
            priority_fee = UNSET
        else:
            priority_fee = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _priority_fee
            )

        _rent_paid = d.pop("rent_paid", UNSET)
        rent_paid: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_rent_paid, Unset):
            rent_paid = UNSET
        else:
            rent_paid = PulsightInternalCoreDomainAggregatorMoney.from_dict(_rent_paid)

        _rent_refunded = d.pop("rent_refunded", UNSET)
        rent_refunded: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_rent_refunded, Unset):
            rent_refunded = UNSET
        else:
            rent_refunded = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _rent_refunded
            )

        _tip = d.pop("tip", UNSET)
        tip: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_tip, Unset):
            tip = UNSET
        else:
            tip = PulsightInternalCoreDomainAggregatorMoney.from_dict(_tip)

        tip_service = d.pop("tip_service", UNSET)

        pulsight_internal_core_domain_aggregator_costs = cls(
            base_fee=base_fee,
            cashback_on_top=cashback_on_top,
            dex_fee=dex_fee,
            payer=payer,
            platform=platform,
            platform_fee=platform_fee,
            priority_fee=priority_fee,
            rent_paid=rent_paid,
            rent_refunded=rent_refunded,
            tip=tip,
            tip_service=tip_service,
        )

        pulsight_internal_core_domain_aggregator_costs.additional_properties = d
        return pulsight_internal_core_domain_aggregator_costs

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
