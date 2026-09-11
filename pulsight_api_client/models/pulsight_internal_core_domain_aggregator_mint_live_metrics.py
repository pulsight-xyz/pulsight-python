from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintLiveMetrics")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintLiveMetrics:
    """
    Attributes:
        as_of (str | Unset):
        circulating_supply (float | Unset): CirculatingSupply is the supply MarketCapUsd was computed against, in
            WHOLE tokens (decimals already applied). It rides along so a client
            patching the price can carry the market cap with it on the server's own
            basis instead of re-deriving the figure from raw supply and decimals.
            nil when supply or decimals are unknown, exactly when MarketCapUsd is.
        market_cap_usd (float | Unset):
        mint (str | Unset):
        price_basis_pool (str | Unset): PriceBasisPool is the pool PriceUsd was read from: the mint's DOMINANT
            pool by 24h quote volume, which is the basis the whole price surface
            uses so a dust side-market's prints cannot move the displayed number.
            A client that patches the price from the live swap stream between reads
            must believe prints from THIS pool only — and gets the answer from the
            server precisely so it never has to resolve a dominant pool of its own.
            nil whenever PriceUsd is.
        price_usd (float | Unset): PriceUsd / MarketCapUsd carry MintRow.PriceUsd and MintRow.MarketCapUsd
            verbatim, including their nil conditions (no WSOL pool, unknown
            decimals, no SOL/USD reference, absent supply).
        unique_traders (int | Unset): UniqueTraders is MintRow.UniqueTraders read straight off the insert-time
            uniq plane, so it is as fresh as ingest rather than as fresh as the
            holder-fold refresh that stamps the identity row. nil without the plane:
            this route never falls back to the lifetime position-table fold, which is
            the read it exists to stop paying at poll cadence. A quote-registry mint
            has no rows on that plane and so never reports a count here.
    """

    as_of: str | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    market_cap_usd: float | Unset = UNSET
    mint: str | Unset = UNSET
    price_basis_pool: str | Unset = UNSET
    price_usd: float | Unset = UNSET
    unique_traders: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        circulating_supply = self.circulating_supply

        market_cap_usd = self.market_cap_usd

        mint = self.mint

        price_basis_pool = self.price_basis_pool

        price_usd = self.price_usd

        unique_traders = self.unique_traders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if circulating_supply is not UNSET:
            field_dict["circulating_supply"] = circulating_supply
        if market_cap_usd is not UNSET:
            field_dict["market_cap_usd"] = market_cap_usd
        if mint is not UNSET:
            field_dict["mint"] = mint
        if price_basis_pool is not UNSET:
            field_dict["price_basis_pool"] = price_basis_pool
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        as_of = d.pop("as_of", UNSET)

        circulating_supply = d.pop("circulating_supply", UNSET)

        market_cap_usd = d.pop("market_cap_usd", UNSET)

        mint = d.pop("mint", UNSET)

        price_basis_pool = d.pop("price_basis_pool", UNSET)

        price_usd = d.pop("price_usd", UNSET)

        unique_traders = d.pop("unique_traders", UNSET)

        pulsight_internal_core_domain_aggregator_mint_live_metrics = cls(
            as_of=as_of,
            circulating_supply=circulating_supply,
            market_cap_usd=market_cap_usd,
            mint=mint,
            price_basis_pool=price_basis_pool,
            price_usd=price_usd,
            unique_traders=unique_traders,
        )

        pulsight_internal_core_domain_aggregator_mint_live_metrics.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_live_metrics

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
