from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCashbackClaimRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCashbackClaimRow:
    """
    Attributes:
        amount (int | Unset): Amount is the raw payout in QuoteMint's base units, and Priced says
            whether AmountLamports carries a SOL valuation of it. Both are zero on
            a claim, whose AmountLamports is already lamports.
        amount_lamports (int | Unset):
        kind (str | Unset): Kind is "cashback_claim" or "holder_reward".
        mint (str | Unset): Mint is the coin that paid a holder reward; empty on a claim, which is
            per-accumulator rather than per-coin.
        priced (bool | Unset):
        program (str | Unset):
        quote_mint (str | Unset):
        signature (str | Unset):
        timestamp (str | Unset):
    """

    amount: int | Unset = UNSET
    amount_lamports: int | Unset = UNSET
    kind: str | Unset = UNSET
    mint: str | Unset = UNSET
    priced: bool | Unset = UNSET
    program: str | Unset = UNSET
    quote_mint: str | Unset = UNSET
    signature: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_lamports = self.amount_lamports

        kind = self.kind

        mint = self.mint

        priced = self.priced

        program = self.program

        quote_mint = self.quote_mint

        signature = self.signature

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_lamports is not UNSET:
            field_dict["amount_lamports"] = amount_lamports
        if kind is not UNSET:
            field_dict["kind"] = kind
        if mint is not UNSET:
            field_dict["mint"] = mint
        if priced is not UNSET:
            field_dict["priced"] = priced
        if program is not UNSET:
            field_dict["program"] = program
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if signature is not UNSET:
            field_dict["signature"] = signature
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        amount_lamports = d.pop("amount_lamports", UNSET)

        kind = d.pop("kind", UNSET)

        mint = d.pop("mint", UNSET)

        priced = d.pop("priced", UNSET)

        program = d.pop("program", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        signature = d.pop("signature", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        pulsight_internal_core_domain_aggregator_cashback_claim_row = cls(
            amount=amount,
            amount_lamports=amount_lamports,
            kind=kind,
            mint=mint,
            priced=priced,
            program=program,
            quote_mint=quote_mint,
            signature=signature,
            timestamp=timestamp,
        )

        pulsight_internal_core_domain_aggregator_cashback_claim_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cashback_claim_row

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
