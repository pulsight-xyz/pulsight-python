from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorDevStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorDevStat:
    """
    Attributes:
        creator (str | Unset):
        pct_of_supply (float | Unset):
        sold (bool | Unset):
    """

    creator: str | Unset = UNSET
    pct_of_supply: float | Unset = UNSET
    sold: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator = self.creator

        pct_of_supply = self.pct_of_supply

        sold = self.sold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if pct_of_supply is not UNSET:
            field_dict["pct_of_supply"] = pct_of_supply
        if sold is not UNSET:
            field_dict["sold"] = sold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        creator = d.pop("creator", UNSET)

        pct_of_supply = d.pop("pct_of_supply", UNSET)

        sold = d.pop("sold", UNSET)

        pulsight_internal_core_domain_aggregator_dev_stat = cls(
            creator=creator,
            pct_of_supply=pct_of_supply,
            sold=sold,
        )

        pulsight_internal_core_domain_aggregator_dev_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_dev_stat

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
