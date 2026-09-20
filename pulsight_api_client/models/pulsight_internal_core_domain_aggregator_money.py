from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMoney")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMoney:
    """
    Attributes:
        sol (int | Unset):
        usd (int | Unset):
    """

    sol: int | Unset = UNSET
    usd: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sol = self.sol

        usd = self.usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sol is not UNSET:
            field_dict["sol"] = sol
        if usd is not UNSET:
            field_dict["usd"] = usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sol = d.pop("sol", UNSET)

        usd = d.pop("usd", UNSET)

        pulsight_internal_core_domain_aggregator_money = cls(
            sol=sol,
            usd=usd,
        )

        pulsight_internal_core_domain_aggregator_money.additional_properties = d
        return pulsight_internal_core_domain_aggregator_money

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
