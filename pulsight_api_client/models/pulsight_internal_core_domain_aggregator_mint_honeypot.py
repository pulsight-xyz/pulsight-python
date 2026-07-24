from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintHoneypot")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintHoneypot:
    """
    Attributes:
        buy_count (int | Unset): BuyCount/SellCount/Buyers/Sellers back "buy_dominant": an all-time sell-trap
            (> buyDominanceMinBuyShare buys over > buyDominanceMinSwaps swaps).
            Buyers/Sellers are distinct wallets.
        buyers (int | Unset):
        duplicate_count (int | Unset): DuplicateCount backs "copycat": how many mints share this (symbol, name).
        freeze_count (int | Unset): FreezeCount/ThawCount back the "freezes_holders" reason.
        reasons (list[str] | Unset):
        sell_count (int | Unset):
        sellers (int | Unset):
        thaw_count (int | Unset):
    """

    buy_count: int | Unset = UNSET
    buyers: int | Unset = UNSET
    duplicate_count: int | Unset = UNSET
    freeze_count: int | Unset = UNSET
    reasons: list[str] | Unset = UNSET
    sell_count: int | Unset = UNSET
    sellers: int | Unset = UNSET
    thaw_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_count = self.buy_count

        buyers = self.buyers

        duplicate_count = self.duplicate_count

        freeze_count = self.freeze_count

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        sell_count = self.sell_count

        sellers = self.sellers

        thaw_count = self.thaw_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_count is not UNSET:
            field_dict["buy_count"] = buy_count
        if buyers is not UNSET:
            field_dict["buyers"] = buyers
        if duplicate_count is not UNSET:
            field_dict["duplicate_count"] = duplicate_count
        if freeze_count is not UNSET:
            field_dict["freeze_count"] = freeze_count
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if sell_count is not UNSET:
            field_dict["sell_count"] = sell_count
        if sellers is not UNSET:
            field_dict["sellers"] = sellers
        if thaw_count is not UNSET:
            field_dict["thaw_count"] = thaw_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        buy_count = d.pop("buy_count", UNSET)

        buyers = d.pop("buyers", UNSET)

        duplicate_count = d.pop("duplicate_count", UNSET)

        freeze_count = d.pop("freeze_count", UNSET)

        reasons = cast(list[str], d.pop("reasons", UNSET))

        sell_count = d.pop("sell_count", UNSET)

        sellers = d.pop("sellers", UNSET)

        thaw_count = d.pop("thaw_count", UNSET)

        pulsight_internal_core_domain_aggregator_mint_honeypot = cls(
            buy_count=buy_count,
            buyers=buyers,
            duplicate_count=duplicate_count,
            freeze_count=freeze_count,
            reasons=reasons,
            sell_count=sell_count,
            sellers=sellers,
            thaw_count=thaw_count,
        )

        pulsight_internal_core_domain_aggregator_mint_honeypot.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_honeypot

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
