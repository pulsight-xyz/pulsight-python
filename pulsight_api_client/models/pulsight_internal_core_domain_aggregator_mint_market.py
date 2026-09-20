from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintMarket")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintMarket:
    """
    Attributes:
        base_mint (str | Unset): BaseMint is the pool's base side as the aggregator oriented it — the
            page's own mint except on a money mint's page, where the mint may be
            the quote of the pools listed. BaseSymbol is its symbol, empty when
            unknown.
        base_symbol (str | Unset):
        dex (str | Unset):
        is_default (bool | Unset): IsDefault marks the mint's default market — the pool an unpinned
            /api/ohlcv chart resolves to (lifetime-dominant, recency-aware; one
            definition, server-side: defaultMarketPool). Resolved independently
            of the requested window, so a listing may carry no flagged row when
            the default market is idle in a short window. Resolve defaults from
            `window=all`.
        last_swap_ts (str | Unset):
        pool (str | Unset):
        quote_decimals (int | Unset):
        quote_mint (str | Unset): QuoteMint is the pool's quote side as the aggregator oriented it: a
            registry quote when one side is one (USDC > USDT > USD1 > WSOL), else
            the pool's own quote token. This market's native candle prices and
            quote amounts are denominated in it, and the live chart folds only
            ticks that carry the same quote.
        quote_symbol (str | Unset): QuoteSymbol and QuoteDecimals describe the quote mint; the decimals are
            omitted when the mint is unknown.
        sol_volume_lamports (int | Unset):
        sol_volume_share (float | Unset):
        swap_count (int | Unset):
    """

    base_mint: str | Unset = UNSET
    base_symbol: str | Unset = UNSET
    dex: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    last_swap_ts: str | Unset = UNSET
    pool: str | Unset = UNSET
    quote_decimals: int | Unset = UNSET
    quote_mint: str | Unset = UNSET
    quote_symbol: str | Unset = UNSET
    sol_volume_lamports: int | Unset = UNSET
    sol_volume_share: float | Unset = UNSET
    swap_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_mint = self.base_mint

        base_symbol = self.base_symbol

        dex = self.dex

        is_default = self.is_default

        last_swap_ts = self.last_swap_ts

        pool = self.pool

        quote_decimals = self.quote_decimals

        quote_mint = self.quote_mint

        quote_symbol = self.quote_symbol

        sol_volume_lamports = self.sol_volume_lamports

        sol_volume_share = self.sol_volume_share

        swap_count = self.swap_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_mint is not UNSET:
            field_dict["base_mint"] = base_mint
        if base_symbol is not UNSET:
            field_dict["base_symbol"] = base_symbol
        if dex is not UNSET:
            field_dict["dex"] = dex
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if last_swap_ts is not UNSET:
            field_dict["last_swap_ts"] = last_swap_ts
        if pool is not UNSET:
            field_dict["pool"] = pool
        if quote_decimals is not UNSET:
            field_dict["quote_decimals"] = quote_decimals
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if quote_symbol is not UNSET:
            field_dict["quote_symbol"] = quote_symbol
        if sol_volume_lamports is not UNSET:
            field_dict["sol_volume_lamports"] = sol_volume_lamports
        if sol_volume_share is not UNSET:
            field_dict["sol_volume_share"] = sol_volume_share
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_mint = d.pop("base_mint", UNSET)

        base_symbol = d.pop("base_symbol", UNSET)

        dex = d.pop("dex", UNSET)

        is_default = d.pop("is_default", UNSET)

        last_swap_ts = d.pop("last_swap_ts", UNSET)

        pool = d.pop("pool", UNSET)

        quote_decimals = d.pop("quote_decimals", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        quote_symbol = d.pop("quote_symbol", UNSET)

        sol_volume_lamports = d.pop("sol_volume_lamports", UNSET)

        sol_volume_share = d.pop("sol_volume_share", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        pulsight_internal_core_domain_aggregator_mint_market = cls(
            base_mint=base_mint,
            base_symbol=base_symbol,
            dex=dex,
            is_default=is_default,
            last_swap_ts=last_swap_ts,
            pool=pool,
            quote_decimals=quote_decimals,
            quote_mint=quote_mint,
            quote_symbol=quote_symbol,
            sol_volume_lamports=sol_volume_lamports,
            sol_volume_share=sol_volume_share,
            swap_count=swap_count,
        )

        pulsight_internal_core_domain_aggregator_mint_market.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_market

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
