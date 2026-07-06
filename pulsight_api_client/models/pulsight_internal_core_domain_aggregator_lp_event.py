from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorLpEvent")


@_attrs_define
class PulsightInternalCoreDomainAggregatorLpEvent:
    """
    Attributes:
        base_amount (str | Unset):
        base_mint (str | Unset):
        dex (str | Unset):
        ix_index (int | Unset):
        lp_mint (str | Unset): LpMint is the LP-token mint; "" when unknown.
        lp_token_amount (str | Unset):
        op (str | Unset): Op ∈ {add, remove, burn}.
        pool (str | Unset):
        quote_amount (str | Unset):
        quote_mint (str | Unset):
        signature (str | Unset):
        signer (str | Unset):
        slot (int | Unset):
        timestamp (str | Unset):
    """

    base_amount: str | Unset = UNSET
    base_mint: str | Unset = UNSET
    dex: str | Unset = UNSET
    ix_index: int | Unset = UNSET
    lp_mint: str | Unset = UNSET
    lp_token_amount: str | Unset = UNSET
    op: str | Unset = UNSET
    pool: str | Unset = UNSET
    quote_amount: str | Unset = UNSET
    quote_mint: str | Unset = UNSET
    signature: str | Unset = UNSET
    signer: str | Unset = UNSET
    slot: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_amount = self.base_amount

        base_mint = self.base_mint

        dex = self.dex

        ix_index = self.ix_index

        lp_mint = self.lp_mint

        lp_token_amount = self.lp_token_amount

        op = self.op

        pool = self.pool

        quote_amount = self.quote_amount

        quote_mint = self.quote_mint

        signature = self.signature

        signer = self.signer

        slot = self.slot

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_amount is not UNSET:
            field_dict["base_amount"] = base_amount
        if base_mint is not UNSET:
            field_dict["base_mint"] = base_mint
        if dex is not UNSET:
            field_dict["dex"] = dex
        if ix_index is not UNSET:
            field_dict["ix_index"] = ix_index
        if lp_mint is not UNSET:
            field_dict["lp_mint"] = lp_mint
        if lp_token_amount is not UNSET:
            field_dict["lp_token_amount"] = lp_token_amount
        if op is not UNSET:
            field_dict["op"] = op
        if pool is not UNSET:
            field_dict["pool"] = pool
        if quote_amount is not UNSET:
            field_dict["quote_amount"] = quote_amount
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if signature is not UNSET:
            field_dict["signature"] = signature
        if signer is not UNSET:
            field_dict["signer"] = signer
        if slot is not UNSET:
            field_dict["slot"] = slot
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_amount = d.pop("base_amount", UNSET)

        base_mint = d.pop("base_mint", UNSET)

        dex = d.pop("dex", UNSET)

        ix_index = d.pop("ix_index", UNSET)

        lp_mint = d.pop("lp_mint", UNSET)

        lp_token_amount = d.pop("lp_token_amount", UNSET)

        op = d.pop("op", UNSET)

        pool = d.pop("pool", UNSET)

        quote_amount = d.pop("quote_amount", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        signature = d.pop("signature", UNSET)

        signer = d.pop("signer", UNSET)

        slot = d.pop("slot", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        pulsight_internal_core_domain_aggregator_lp_event = cls(
            base_amount=base_amount,
            base_mint=base_mint,
            dex=dex,
            ix_index=ix_index,
            lp_mint=lp_mint,
            lp_token_amount=lp_token_amount,
            op=op,
            pool=pool,
            quote_amount=quote_amount,
            quote_mint=quote_mint,
            signature=signature,
            signer=signer,
            slot=slot,
            timestamp=timestamp,
        )

        pulsight_internal_core_domain_aggregator_lp_event.additional_properties = d
        return pulsight_internal_core_domain_aggregator_lp_event

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
