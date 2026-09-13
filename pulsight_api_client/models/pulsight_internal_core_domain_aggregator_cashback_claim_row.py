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
        amount_gross (int | Unset): AmountGross is a cashback claim's RAW swept amount before the part the
            wallet immediately re-parked; AmountLamports is what it KEPT. They differ
            on a park-resweep, where kept is legitimately zero and only the gross
            shows a claim happened at all. Zero on a payout, which cannot be parked.
        amount_lamports (int | Unset):
        kind (str | Unset): Kind is RewardKindCashbackClaim or RewardKindHolderReward.
        logo_uri (str | Unset):
        mint (str | Unset): Mint is the coin that paid a holder reward; empty on a claim, which is
            per-accumulator rather than per-coin.
        name (str | Unset):
        price_basis (str | Unset): PriceBasis says HOW AmountLamports was arrived at: "exact" when the
            payout was already in SOL, "market" when it was valued through the
            quote's own SOL market at that minute, "unpriced" when no value could
            be stated. A market figure moves with the quote; an exact one is the
            amount received. Empty on a cashback claim.
        priced (bool | Unset):
        program (str | Unset):
        quote_decimals (int | Unset):
        quote_logo_uri (str | Unset):
        quote_mint (str | Unset):
        quote_name (str | Unset):
        quote_symbol (str | Unset): QuoteSymbol / QuoteName / QuoteLogoURI name QuoteMint — the token the
            reward was actually paid in, which on a holder-rewards coin is its
            pool's quote and only rarely WSOL. QuoteDecimals scales Amount into
            whole tokens and is -1 when unknown; it is per-token (PUMP 6, ZEC 8,
            XMR 12), so a reader must not assume a default.
        signature (str | Unset):
        symbol (str | Unset): Symbol / Name / LogoURI name the paying coin so a payout renders as a
            token rather than a raw address. Empty on a claim, and on a coin whose
            metadata has not been fetched yet.
        timestamp (str | Unset):
    """

    amount: int | Unset = UNSET
    amount_gross: int | Unset = UNSET
    amount_lamports: int | Unset = UNSET
    kind: str | Unset = UNSET
    logo_uri: str | Unset = UNSET
    mint: str | Unset = UNSET
    name: str | Unset = UNSET
    price_basis: str | Unset = UNSET
    priced: bool | Unset = UNSET
    program: str | Unset = UNSET
    quote_decimals: int | Unset = UNSET
    quote_logo_uri: str | Unset = UNSET
    quote_mint: str | Unset = UNSET
    quote_name: str | Unset = UNSET
    quote_symbol: str | Unset = UNSET
    signature: str | Unset = UNSET
    symbol: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_gross = self.amount_gross

        amount_lamports = self.amount_lamports

        kind = self.kind

        logo_uri = self.logo_uri

        mint = self.mint

        name = self.name

        price_basis = self.price_basis

        priced = self.priced

        program = self.program

        quote_decimals = self.quote_decimals

        quote_logo_uri = self.quote_logo_uri

        quote_mint = self.quote_mint

        quote_name = self.quote_name

        quote_symbol = self.quote_symbol

        signature = self.signature

        symbol = self.symbol

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_gross is not UNSET:
            field_dict["amount_gross"] = amount_gross
        if amount_lamports is not UNSET:
            field_dict["amount_lamports"] = amount_lamports
        if kind is not UNSET:
            field_dict["kind"] = kind
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if mint is not UNSET:
            field_dict["mint"] = mint
        if name is not UNSET:
            field_dict["name"] = name
        if price_basis is not UNSET:
            field_dict["price_basis"] = price_basis
        if priced is not UNSET:
            field_dict["priced"] = priced
        if program is not UNSET:
            field_dict["program"] = program
        if quote_decimals is not UNSET:
            field_dict["quote_decimals"] = quote_decimals
        if quote_logo_uri is not UNSET:
            field_dict["quote_logo_uri"] = quote_logo_uri
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if quote_name is not UNSET:
            field_dict["quote_name"] = quote_name
        if quote_symbol is not UNSET:
            field_dict["quote_symbol"] = quote_symbol
        if signature is not UNSET:
            field_dict["signature"] = signature
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        amount_gross = d.pop("amount_gross", UNSET)

        amount_lamports = d.pop("amount_lamports", UNSET)

        kind = d.pop("kind", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        mint = d.pop("mint", UNSET)

        name = d.pop("name", UNSET)

        price_basis = d.pop("price_basis", UNSET)

        priced = d.pop("priced", UNSET)

        program = d.pop("program", UNSET)

        quote_decimals = d.pop("quote_decimals", UNSET)

        quote_logo_uri = d.pop("quote_logo_uri", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        quote_name = d.pop("quote_name", UNSET)

        quote_symbol = d.pop("quote_symbol", UNSET)

        signature = d.pop("signature", UNSET)

        symbol = d.pop("symbol", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        pulsight_internal_core_domain_aggregator_cashback_claim_row = cls(
            amount=amount,
            amount_gross=amount_gross,
            amount_lamports=amount_lamports,
            kind=kind,
            logo_uri=logo_uri,
            mint=mint,
            name=name,
            price_basis=price_basis,
            priced=priced,
            program=program,
            quote_decimals=quote_decimals,
            quote_logo_uri=quote_logo_uri,
            quote_mint=quote_mint,
            quote_name=quote_name,
            quote_symbol=quote_symbol,
            signature=signature,
            symbol=symbol,
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
