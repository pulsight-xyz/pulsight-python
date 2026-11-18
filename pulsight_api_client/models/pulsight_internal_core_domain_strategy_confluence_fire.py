from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyConfluenceFire")


@_attrs_define
class PulsightInternalCoreDomainStrategyConfluenceFire:
    """
    Attributes:
        at (int | Unset): At is the instant, unix seconds.
        mint (str | Unset): Mint is the token's address.
        votes (int | Unset): Votes is how many wallets the condition counted then, after merging same-second buys.
    """

    at: int | Unset = UNSET
    mint: str | Unset = UNSET
    votes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at

        mint = self.mint

        votes = self.votes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if mint is not UNSET:
            field_dict["mint"] = mint
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = d.pop("at", UNSET)

        mint = d.pop("mint", UNSET)

        votes = d.pop("votes", UNSET)

        pulsight_internal_core_domain_strategy_confluence_fire = cls(
            at=at,
            mint=mint,
            votes=votes,
        )

        pulsight_internal_core_domain_strategy_confluence_fire.additional_properties = d
        return pulsight_internal_core_domain_strategy_confluence_fire

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
