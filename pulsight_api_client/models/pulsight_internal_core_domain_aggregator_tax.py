from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_tax_swap_fee_source import (
    PulsightInternalCoreDomainAggregatorTaxSwapFeeSource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_tax_part import (
        PulsightInternalCoreDomainAggregatorTaxPart,
    )
    from ..models.pulsight_internal_core_domain_aggregator_tax_via import (
        PulsightInternalCoreDomainAggregatorTaxVia,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTax")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTax:
    """
    Attributes:
        buy_bps (int | Unset): BuyBps is the tax a buy pays, SwapFeeBps plus TransferFeeBps. Absent
            while either is unknown: the tax is then at least TransferFeeBps, plus
            SwapFeeMinBps when that is known.
        dex (str | Unset): Dex is Pool's venue slug, same vocabulary as `?dex=`.
        holder_rewards (bool | Unset): HolderRewards reports that the creator share inside SwapFeeBps is paid
            to the coin's holders: the mint is a pump.fun holder-rewards coin and
            the pool is its own pump.fun curve or PumpSwap pool. SwapFeeParts sizes
            the share as `holder_rewards` when the pool's configuration is known.
            Never set on a listing row, whose pool is not named.
        pool (str | Unset): Pool is the pool SwapFeeBps was read from: on the token page's row the
            mint's reference pool, the one its price is read from. Omitted on a
            listing row and on a market row, which is its own pool.
        sell_bps (int | Unset): SellBps is the tax a sell pays, on the same components as BuyBps.
        swap_fee_at (str | Unset): SwapFeeAt is the minute a recorded SwapFeeBps was recorded in. Omitted on
            a listing row and for a configured fee.
        swap_fee_bps (int | Unset): SwapFeeBps is the pool's swap fee, the venue's whole schedule (LP,
            protocol, creator and partner shares). Absent when it is unknown —
            never free.
        swap_fee_min_bps (int | Unset): SwapFeeMinBps is a lower bound on the pool's swap fee, set only while
            SwapFeeBps is unknown: the pool's configuration fixes a base fee and the
            venue adds a variable fee on top that no recorded trade has priced yet.
        swap_fee_parts (list[PulsightInternalCoreDomainAggregatorTaxPart] | Unset): SwapFeeParts splits SwapFeeBps into
            the shares the venue defines,
            summing to it: always for a configured fee, and for a recorded one where
            the venue defines its split as shares of whatever fee it charges.
            Absent when the swap fee is a lower bound or unknown, and on a listing
            row.
        swap_fee_source (PulsightInternalCoreDomainAggregatorTaxSwapFeeSource | Unset): SwapFeeSource says where the
            swap fee comes from: `recorded`, the highest
            fee the pool's trades recorded in the latest minute that recorded one;
            `configured`, the pool's fee configuration read from chain. The
            configuration stands while the trades record its total or one hop's share
            of it, and a recorded fee it does not explain wins. Omitted on a listing
            row.
        transfer_fee_bps (int | Unset): TransferFeeBps is the mint's Token-2022 transfer fee, the higher of its
            current and scheduled rate with its per-transfer cap not applied; 0 for
            a mint without one. Absent until the mint account has been read.
        via (PulsightInternalCoreDomainAggregatorTaxVia | Unset):
    """

    buy_bps: int | Unset = UNSET
    dex: str | Unset = UNSET
    holder_rewards: bool | Unset = UNSET
    pool: str | Unset = UNSET
    sell_bps: int | Unset = UNSET
    swap_fee_at: str | Unset = UNSET
    swap_fee_bps: int | Unset = UNSET
    swap_fee_min_bps: int | Unset = UNSET
    swap_fee_parts: list[PulsightInternalCoreDomainAggregatorTaxPart] | Unset = UNSET
    swap_fee_source: PulsightInternalCoreDomainAggregatorTaxSwapFeeSource | Unset = (
        UNSET
    )
    transfer_fee_bps: int | Unset = UNSET
    via: PulsightInternalCoreDomainAggregatorTaxVia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_bps = self.buy_bps

        dex = self.dex

        holder_rewards = self.holder_rewards

        pool = self.pool

        sell_bps = self.sell_bps

        swap_fee_at = self.swap_fee_at

        swap_fee_bps = self.swap_fee_bps

        swap_fee_min_bps = self.swap_fee_min_bps

        swap_fee_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.swap_fee_parts, Unset):
            swap_fee_parts = []
            for swap_fee_parts_item_data in self.swap_fee_parts:
                swap_fee_parts_item = swap_fee_parts_item_data.to_dict()
                swap_fee_parts.append(swap_fee_parts_item)

        swap_fee_source: str | Unset = UNSET
        if not isinstance(self.swap_fee_source, Unset):
            swap_fee_source = self.swap_fee_source.value

        transfer_fee_bps = self.transfer_fee_bps

        via: dict[str, Any] | Unset = UNSET
        if not isinstance(self.via, Unset):
            via = self.via.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_bps is not UNSET:
            field_dict["buy_bps"] = buy_bps
        if dex is not UNSET:
            field_dict["dex"] = dex
        if holder_rewards is not UNSET:
            field_dict["holder_rewards"] = holder_rewards
        if pool is not UNSET:
            field_dict["pool"] = pool
        if sell_bps is not UNSET:
            field_dict["sell_bps"] = sell_bps
        if swap_fee_at is not UNSET:
            field_dict["swap_fee_at"] = swap_fee_at
        if swap_fee_bps is not UNSET:
            field_dict["swap_fee_bps"] = swap_fee_bps
        if swap_fee_min_bps is not UNSET:
            field_dict["swap_fee_min_bps"] = swap_fee_min_bps
        if swap_fee_parts is not UNSET:
            field_dict["swap_fee_parts"] = swap_fee_parts
        if swap_fee_source is not UNSET:
            field_dict["swap_fee_source"] = swap_fee_source
        if transfer_fee_bps is not UNSET:
            field_dict["transfer_fee_bps"] = transfer_fee_bps
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_tax_part import (
            PulsightInternalCoreDomainAggregatorTaxPart,
        )
        from ..models.pulsight_internal_core_domain_aggregator_tax_via import (
            PulsightInternalCoreDomainAggregatorTaxVia,
        )

        d = dict(src_dict)
        buy_bps = d.pop("buy_bps", UNSET)

        dex = d.pop("dex", UNSET)

        holder_rewards = d.pop("holder_rewards", UNSET)

        pool = d.pop("pool", UNSET)

        sell_bps = d.pop("sell_bps", UNSET)

        swap_fee_at = d.pop("swap_fee_at", UNSET)

        swap_fee_bps = d.pop("swap_fee_bps", UNSET)

        swap_fee_min_bps = d.pop("swap_fee_min_bps", UNSET)

        _swap_fee_parts = d.pop("swap_fee_parts", UNSET)
        swap_fee_parts: list[PulsightInternalCoreDomainAggregatorTaxPart] | Unset = (
            UNSET
        )
        if _swap_fee_parts is not UNSET:
            swap_fee_parts = []
            for swap_fee_parts_item_data in _swap_fee_parts:
                swap_fee_parts_item = (
                    PulsightInternalCoreDomainAggregatorTaxPart.from_dict(
                        swap_fee_parts_item_data
                    )
                )

                swap_fee_parts.append(swap_fee_parts_item)

        _swap_fee_source = d.pop("swap_fee_source", UNSET)
        swap_fee_source: PulsightInternalCoreDomainAggregatorTaxSwapFeeSource | Unset
        if isinstance(_swap_fee_source, Unset):
            swap_fee_source = UNSET
        else:
            swap_fee_source = PulsightInternalCoreDomainAggregatorTaxSwapFeeSource(
                _swap_fee_source
            )

        transfer_fee_bps = d.pop("transfer_fee_bps", UNSET)

        _via = d.pop("via", UNSET)
        via: PulsightInternalCoreDomainAggregatorTaxVia | Unset
        if isinstance(_via, Unset):
            via = UNSET
        else:
            via = PulsightInternalCoreDomainAggregatorTaxVia.from_dict(_via)

        pulsight_internal_core_domain_aggregator_tax = cls(
            buy_bps=buy_bps,
            dex=dex,
            holder_rewards=holder_rewards,
            pool=pool,
            sell_bps=sell_bps,
            swap_fee_at=swap_fee_at,
            swap_fee_bps=swap_fee_bps,
            swap_fee_min_bps=swap_fee_min_bps,
            swap_fee_parts=swap_fee_parts,
            swap_fee_source=swap_fee_source,
            transfer_fee_bps=transfer_fee_bps,
            via=via,
        )

        pulsight_internal_core_domain_aggregator_tax.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tax

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
