from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorAuthorityStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorAuthorityStat:
    """
    Attributes:
        freeze (str | Unset):
        freeze_active (bool | Unset):
        mint (str | Unset):
        mint_active (bool | Unset):
        observed (bool | Unset):
    """

    freeze: str | Unset = UNSET
    freeze_active: bool | Unset = UNSET
    mint: str | Unset = UNSET
    mint_active: bool | Unset = UNSET
    observed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freeze = self.freeze

        freeze_active = self.freeze_active

        mint = self.mint

        mint_active = self.mint_active

        observed = self.observed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if freeze is not UNSET:
            field_dict["freeze"] = freeze
        if freeze_active is not UNSET:
            field_dict["freeze_active"] = freeze_active
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mint_active is not UNSET:
            field_dict["mint_active"] = mint_active
        if observed is not UNSET:
            field_dict["observed"] = observed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        freeze = d.pop("freeze", UNSET)

        freeze_active = d.pop("freeze_active", UNSET)

        mint = d.pop("mint", UNSET)

        mint_active = d.pop("mint_active", UNSET)

        observed = d.pop("observed", UNSET)

        pulsight_internal_core_domain_aggregator_authority_stat = cls(
            freeze=freeze,
            freeze_active=freeze_active,
            mint=mint,
            mint_active=mint_active,
            observed=observed,
        )

        pulsight_internal_core_domain_aggregator_authority_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_authority_stat

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
