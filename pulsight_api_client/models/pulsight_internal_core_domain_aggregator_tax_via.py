from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTaxVia")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTaxVia:
    """
    Attributes:
        bps (int | Unset): Bps is the most the hop adds: SwapFeeBps plus TransferFeeBps, what a SOL
            trade pays when it swaps through Pool as a hop of its own. Absent while
            either is unknown. A router that prices the two hops together can charge
            less; see PumpRouted.
        dex (str | Unset): Dex is Pool's venue slug.
        pool (str | Unset): Pool is the hop's pool: the quote token's deepest pool paired with SOL,
            else its reference pool.
        ppm (int | Unset): Ppm is Bps in millionths of the traded value, exactly.
        pump_routed (bool | Unset): PumpRouted reports that pump's own router (`multi_hop_swap`) serves this
            route: Pool is a PumpSwap pool and the token's pool is a pump pool.
            Through that router the hop adds nothing: pump charges the far pool's
            protocol share on the hop instead of on the far pool, so a buyer it
            routes pays the token's own tax alone.
        quote_mint (str | Unset): QuoteMint is the quote token the hop swaps through.
        quote_symbol (str | Unset): QuoteSymbol is QuoteMint's symbol, empty when unknown.
        swap_fee_bps (int | Unset): SwapFeeBps is the swap fee of the hop's pool, on the basis of
            Tax.SwapFeeBps; absent when unknown.
        swap_fee_min_bps (int | Unset): SwapFeeMinBps is a lower bound on that swap fee, set only while
            SwapFeeBps is unknown.
        swap_fee_min_ppm (int | Unset): SwapFeeMinPpm is SwapFeeMinBps in millionths, exactly.
        swap_fee_ppm (int | Unset): SwapFeePpm is SwapFeeBps in millionths, exactly.
        transfer_fee_bps (int | Unset): TransferFeeBps is the quote token's Token-2022 transfer fee; absent
            until its mint account has been read.
    """

    bps: int | Unset = UNSET
    dex: str | Unset = UNSET
    pool: str | Unset = UNSET
    ppm: int | Unset = UNSET
    pump_routed: bool | Unset = UNSET
    quote_mint: str | Unset = UNSET
    quote_symbol: str | Unset = UNSET
    swap_fee_bps: int | Unset = UNSET
    swap_fee_min_bps: int | Unset = UNSET
    swap_fee_min_ppm: int | Unset = UNSET
    swap_fee_ppm: int | Unset = UNSET
    transfer_fee_bps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bps = self.bps

        dex = self.dex

        pool = self.pool

        ppm = self.ppm

        pump_routed = self.pump_routed

        quote_mint = self.quote_mint

        quote_symbol = self.quote_symbol

        swap_fee_bps = self.swap_fee_bps

        swap_fee_min_bps = self.swap_fee_min_bps

        swap_fee_min_ppm = self.swap_fee_min_ppm

        swap_fee_ppm = self.swap_fee_ppm

        transfer_fee_bps = self.transfer_fee_bps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bps is not UNSET:
            field_dict["bps"] = bps
        if dex is not UNSET:
            field_dict["dex"] = dex
        if pool is not UNSET:
            field_dict["pool"] = pool
        if ppm is not UNSET:
            field_dict["ppm"] = ppm
        if pump_routed is not UNSET:
            field_dict["pump_routed"] = pump_routed
        if quote_mint is not UNSET:
            field_dict["quote_mint"] = quote_mint
        if quote_symbol is not UNSET:
            field_dict["quote_symbol"] = quote_symbol
        if swap_fee_bps is not UNSET:
            field_dict["swap_fee_bps"] = swap_fee_bps
        if swap_fee_min_bps is not UNSET:
            field_dict["swap_fee_min_bps"] = swap_fee_min_bps
        if swap_fee_min_ppm is not UNSET:
            field_dict["swap_fee_min_ppm"] = swap_fee_min_ppm
        if swap_fee_ppm is not UNSET:
            field_dict["swap_fee_ppm"] = swap_fee_ppm
        if transfer_fee_bps is not UNSET:
            field_dict["transfer_fee_bps"] = transfer_fee_bps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bps = d.pop("bps", UNSET)

        dex = d.pop("dex", UNSET)

        pool = d.pop("pool", UNSET)

        ppm = d.pop("ppm", UNSET)

        pump_routed = d.pop("pump_routed", UNSET)

        quote_mint = d.pop("quote_mint", UNSET)

        quote_symbol = d.pop("quote_symbol", UNSET)

        swap_fee_bps = d.pop("swap_fee_bps", UNSET)

        swap_fee_min_bps = d.pop("swap_fee_min_bps", UNSET)

        swap_fee_min_ppm = d.pop("swap_fee_min_ppm", UNSET)

        swap_fee_ppm = d.pop("swap_fee_ppm", UNSET)

        transfer_fee_bps = d.pop("transfer_fee_bps", UNSET)

        pulsight_internal_core_domain_aggregator_tax_via = cls(
            bps=bps,
            dex=dex,
            pool=pool,
            ppm=ppm,
            pump_routed=pump_routed,
            quote_mint=quote_mint,
            quote_symbol=quote_symbol,
            swap_fee_bps=swap_fee_bps,
            swap_fee_min_bps=swap_fee_min_bps,
            swap_fee_min_ppm=swap_fee_min_ppm,
            swap_fee_ppm=swap_fee_ppm,
            transfer_fee_bps=transfer_fee_bps,
        )

        pulsight_internal_core_domain_aggregator_tax_via.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tax_via

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
