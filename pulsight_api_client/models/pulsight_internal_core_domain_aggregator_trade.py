from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_arb import (
        PulsightInternalCoreDomainAggregatorArb,
    )
    from ..models.pulsight_internal_core_domain_aggregator_costs import (
        PulsightInternalCoreDomainAggregatorCosts,
    )
    from ..models.pulsight_internal_core_domain_aggregator_hop import (
        PulsightInternalCoreDomainAggregatorHop,
    )
    from ..models.pulsight_internal_core_domain_aggregator_money import (
        PulsightInternalCoreDomainAggregatorMoney,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTrade")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTrade:
    """
    Attributes:
        arb (PulsightInternalCoreDomainAggregatorArb | Unset):
        attribution (str | Unset):
        carry_basis (PulsightInternalCoreDomainAggregatorMoney | Unset):
        carry_from_mint (str | Unset):
        carry_from_mint_id (int | Unset):
        carry_to_mint (str | Unset):
        carry_to_mint_id (int | Unset):
        cashback_accrued (PulsightInternalCoreDomainAggregatorMoney | Unset):
        costs (PulsightInternalCoreDomainAggregatorCosts | Unset):
        counter_amount (int | Unset):
        counter_decimals (int | Unset):
        counter_mint (str | Unset):
        counter_mint_id (int | Unset):
        counter_symbol (str | Unset):
        decimals (int | Unset):
        dex (str | Unset):
        fees (PulsightInternalCoreDomainAggregatorMoney | Unset):
        flags (int | Unset):
        is_arb (bool | Unset):
        key (str | Unset):
        kind (str | Unset):
        label (str | Unset):
        label_type (str | Unset):
        mint (str | Unset):
        mint_id (int | Unset):
        price_age_ms (int | Unset):
        price_source (str | Unset):
        primary_pool (str | Unset):
        primary_pool_id (int | Unset):
        primary_pool_quote_mint (str | Unset): PrimaryPoolQuoteMint is the primary pool's counter asset from this
            mint's side (its quote, or its base when the mint is the quote of a
            token-quoted pair) — the rule that decides whether a copy can
            execute there. REST decoration; absent when the catalog does not know
            the pool.
        qty (str | Unset):
        realized (PulsightInternalCoreDomainAggregatorMoney | Unset):
        route (list[PulsightInternalCoreDomainAggregatorHop] | Unset):
        signature (str | Unset):
        slot (int | Unset):
        sol_post_lamports (int | Unset):
        sol_usd (float | Unset):
        trader (str | Unset):
        ts_ms (int | Unset):
        tx_index (int | Unset):
        v_source (str | Unset):
        value (PulsightInternalCoreDomainAggregatorMoney | Unset):
        wsol_post_lamports (int | Unset):
    """

    arb: PulsightInternalCoreDomainAggregatorArb | Unset = UNSET
    attribution: str | Unset = UNSET
    carry_basis: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    carry_from_mint: str | Unset = UNSET
    carry_from_mint_id: int | Unset = UNSET
    carry_to_mint: str | Unset = UNSET
    carry_to_mint_id: int | Unset = UNSET
    cashback_accrued: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    costs: PulsightInternalCoreDomainAggregatorCosts | Unset = UNSET
    counter_amount: int | Unset = UNSET
    counter_decimals: int | Unset = UNSET
    counter_mint: str | Unset = UNSET
    counter_mint_id: int | Unset = UNSET
    counter_symbol: str | Unset = UNSET
    decimals: int | Unset = UNSET
    dex: str | Unset = UNSET
    fees: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    flags: int | Unset = UNSET
    is_arb: bool | Unset = UNSET
    key: str | Unset = UNSET
    kind: str | Unset = UNSET
    label: str | Unset = UNSET
    label_type: str | Unset = UNSET
    mint: str | Unset = UNSET
    mint_id: int | Unset = UNSET
    price_age_ms: int | Unset = UNSET
    price_source: str | Unset = UNSET
    primary_pool: str | Unset = UNSET
    primary_pool_id: int | Unset = UNSET
    primary_pool_quote_mint: str | Unset = UNSET
    qty: str | Unset = UNSET
    realized: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    route: list[PulsightInternalCoreDomainAggregatorHop] | Unset = UNSET
    signature: str | Unset = UNSET
    slot: int | Unset = UNSET
    sol_post_lamports: int | Unset = UNSET
    sol_usd: float | Unset = UNSET
    trader: str | Unset = UNSET
    ts_ms: int | Unset = UNSET
    tx_index: int | Unset = UNSET
    v_source: str | Unset = UNSET
    value: PulsightInternalCoreDomainAggregatorMoney | Unset = UNSET
    wsol_post_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arb, Unset):
            arb = self.arb.to_dict()

        attribution = self.attribution

        carry_basis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.carry_basis, Unset):
            carry_basis = self.carry_basis.to_dict()

        carry_from_mint = self.carry_from_mint

        carry_from_mint_id = self.carry_from_mint_id

        carry_to_mint = self.carry_to_mint

        carry_to_mint_id = self.carry_to_mint_id

        cashback_accrued: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cashback_accrued, Unset):
            cashback_accrued = self.cashback_accrued.to_dict()

        costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.costs, Unset):
            costs = self.costs.to_dict()

        counter_amount = self.counter_amount

        counter_decimals = self.counter_decimals

        counter_mint = self.counter_mint

        counter_mint_id = self.counter_mint_id

        counter_symbol = self.counter_symbol

        decimals = self.decimals

        dex = self.dex

        fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        flags = self.flags

        is_arb = self.is_arb

        key = self.key

        kind = self.kind

        label = self.label

        label_type = self.label_type

        mint = self.mint

        mint_id = self.mint_id

        price_age_ms = self.price_age_ms

        price_source = self.price_source

        primary_pool = self.primary_pool

        primary_pool_id = self.primary_pool_id

        primary_pool_quote_mint = self.primary_pool_quote_mint

        qty = self.qty

        realized: dict[str, Any] | Unset = UNSET
        if not isinstance(self.realized, Unset):
            realized = self.realized.to_dict()

        route: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = []
            for route_item_data in self.route:
                route_item = route_item_data.to_dict()
                route.append(route_item)

        signature = self.signature

        slot = self.slot

        sol_post_lamports = self.sol_post_lamports

        sol_usd = self.sol_usd

        trader = self.trader

        ts_ms = self.ts_ms

        tx_index = self.tx_index

        v_source = self.v_source

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        wsol_post_lamports = self.wsol_post_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb is not UNSET:
            field_dict["arb"] = arb
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if carry_basis is not UNSET:
            field_dict["carry_basis"] = carry_basis
        if carry_from_mint is not UNSET:
            field_dict["carry_from_mint"] = carry_from_mint
        if carry_from_mint_id is not UNSET:
            field_dict["carry_from_mint_id"] = carry_from_mint_id
        if carry_to_mint is not UNSET:
            field_dict["carry_to_mint"] = carry_to_mint
        if carry_to_mint_id is not UNSET:
            field_dict["carry_to_mint_id"] = carry_to_mint_id
        if cashback_accrued is not UNSET:
            field_dict["cashback_accrued"] = cashback_accrued
        if costs is not UNSET:
            field_dict["costs"] = costs
        if counter_amount is not UNSET:
            field_dict["counter_amount"] = counter_amount
        if counter_decimals is not UNSET:
            field_dict["counter_decimals"] = counter_decimals
        if counter_mint is not UNSET:
            field_dict["counter_mint"] = counter_mint
        if counter_mint_id is not UNSET:
            field_dict["counter_mint_id"] = counter_mint_id
        if counter_symbol is not UNSET:
            field_dict["counter_symbol"] = counter_symbol
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if dex is not UNSET:
            field_dict["dex"] = dex
        if fees is not UNSET:
            field_dict["fees"] = fees
        if flags is not UNSET:
            field_dict["flags"] = flags
        if is_arb is not UNSET:
            field_dict["is_arb"] = is_arb
        if key is not UNSET:
            field_dict["key"] = key
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mint_id is not UNSET:
            field_dict["mint_id"] = mint_id
        if price_age_ms is not UNSET:
            field_dict["price_age_ms"] = price_age_ms
        if price_source is not UNSET:
            field_dict["price_source"] = price_source
        if primary_pool is not UNSET:
            field_dict["primary_pool"] = primary_pool
        if primary_pool_id is not UNSET:
            field_dict["primary_pool_id"] = primary_pool_id
        if primary_pool_quote_mint is not UNSET:
            field_dict["primary_pool_quote_mint"] = primary_pool_quote_mint
        if qty is not UNSET:
            field_dict["qty"] = qty
        if realized is not UNSET:
            field_dict["realized"] = realized
        if route is not UNSET:
            field_dict["route"] = route
        if signature is not UNSET:
            field_dict["signature"] = signature
        if slot is not UNSET:
            field_dict["slot"] = slot
        if sol_post_lamports is not UNSET:
            field_dict["sol_post_lamports"] = sol_post_lamports
        if sol_usd is not UNSET:
            field_dict["sol_usd"] = sol_usd
        if trader is not UNSET:
            field_dict["trader"] = trader
        if ts_ms is not UNSET:
            field_dict["ts_ms"] = ts_ms
        if tx_index is not UNSET:
            field_dict["tx_index"] = tx_index
        if v_source is not UNSET:
            field_dict["v_source"] = v_source
        if value is not UNSET:
            field_dict["value"] = value
        if wsol_post_lamports is not UNSET:
            field_dict["wsol_post_lamports"] = wsol_post_lamports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_arb import (
            PulsightInternalCoreDomainAggregatorArb,
        )
        from ..models.pulsight_internal_core_domain_aggregator_costs import (
            PulsightInternalCoreDomainAggregatorCosts,
        )
        from ..models.pulsight_internal_core_domain_aggregator_hop import (
            PulsightInternalCoreDomainAggregatorHop,
        )
        from ..models.pulsight_internal_core_domain_aggregator_money import (
            PulsightInternalCoreDomainAggregatorMoney,
        )

        d = dict(src_dict)
        _arb = d.pop("arb", UNSET)
        arb: PulsightInternalCoreDomainAggregatorArb | Unset
        if isinstance(_arb, Unset):
            arb = UNSET
        else:
            arb = PulsightInternalCoreDomainAggregatorArb.from_dict(_arb)

        attribution = d.pop("attribution", UNSET)

        _carry_basis = d.pop("carry_basis", UNSET)
        carry_basis: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_carry_basis, Unset):
            carry_basis = UNSET
        else:
            carry_basis = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _carry_basis
            )

        carry_from_mint = d.pop("carry_from_mint", UNSET)

        carry_from_mint_id = d.pop("carry_from_mint_id", UNSET)

        carry_to_mint = d.pop("carry_to_mint", UNSET)

        carry_to_mint_id = d.pop("carry_to_mint_id", UNSET)

        _cashback_accrued = d.pop("cashback_accrued", UNSET)
        cashback_accrued: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_cashback_accrued, Unset):
            cashback_accrued = UNSET
        else:
            cashback_accrued = PulsightInternalCoreDomainAggregatorMoney.from_dict(
                _cashback_accrued
            )

        _costs = d.pop("costs", UNSET)
        costs: PulsightInternalCoreDomainAggregatorCosts | Unset
        if isinstance(_costs, Unset):
            costs = UNSET
        else:
            costs = PulsightInternalCoreDomainAggregatorCosts.from_dict(_costs)

        counter_amount = d.pop("counter_amount", UNSET)

        counter_decimals = d.pop("counter_decimals", UNSET)

        counter_mint = d.pop("counter_mint", UNSET)

        counter_mint_id = d.pop("counter_mint_id", UNSET)

        counter_symbol = d.pop("counter_symbol", UNSET)

        decimals = d.pop("decimals", UNSET)

        dex = d.pop("dex", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_fees, Unset):
            fees = UNSET
        else:
            fees = PulsightInternalCoreDomainAggregatorMoney.from_dict(_fees)

        flags = d.pop("flags", UNSET)

        is_arb = d.pop("is_arb", UNSET)

        key = d.pop("key", UNSET)

        kind = d.pop("kind", UNSET)

        label = d.pop("label", UNSET)

        label_type = d.pop("label_type", UNSET)

        mint = d.pop("mint", UNSET)

        mint_id = d.pop("mint_id", UNSET)

        price_age_ms = d.pop("price_age_ms", UNSET)

        price_source = d.pop("price_source", UNSET)

        primary_pool = d.pop("primary_pool", UNSET)

        primary_pool_id = d.pop("primary_pool_id", UNSET)

        primary_pool_quote_mint = d.pop("primary_pool_quote_mint", UNSET)

        qty = d.pop("qty", UNSET)

        _realized = d.pop("realized", UNSET)
        realized: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_realized, Unset):
            realized = UNSET
        else:
            realized = PulsightInternalCoreDomainAggregatorMoney.from_dict(_realized)

        _route = d.pop("route", UNSET)
        route: list[PulsightInternalCoreDomainAggregatorHop] | Unset = UNSET
        if _route is not UNSET:
            route = []
            for route_item_data in _route:
                route_item = PulsightInternalCoreDomainAggregatorHop.from_dict(
                    route_item_data
                )

                route.append(route_item)

        signature = d.pop("signature", UNSET)

        slot = d.pop("slot", UNSET)

        sol_post_lamports = d.pop("sol_post_lamports", UNSET)

        sol_usd = d.pop("sol_usd", UNSET)

        trader = d.pop("trader", UNSET)

        ts_ms = d.pop("ts_ms", UNSET)

        tx_index = d.pop("tx_index", UNSET)

        v_source = d.pop("v_source", UNSET)

        _value = d.pop("value", UNSET)
        value: PulsightInternalCoreDomainAggregatorMoney | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PulsightInternalCoreDomainAggregatorMoney.from_dict(_value)

        wsol_post_lamports = d.pop("wsol_post_lamports", UNSET)

        pulsight_internal_core_domain_aggregator_trade = cls(
            arb=arb,
            attribution=attribution,
            carry_basis=carry_basis,
            carry_from_mint=carry_from_mint,
            carry_from_mint_id=carry_from_mint_id,
            carry_to_mint=carry_to_mint,
            carry_to_mint_id=carry_to_mint_id,
            cashback_accrued=cashback_accrued,
            costs=costs,
            counter_amount=counter_amount,
            counter_decimals=counter_decimals,
            counter_mint=counter_mint,
            counter_mint_id=counter_mint_id,
            counter_symbol=counter_symbol,
            decimals=decimals,
            dex=dex,
            fees=fees,
            flags=flags,
            is_arb=is_arb,
            key=key,
            kind=kind,
            label=label,
            label_type=label_type,
            mint=mint,
            mint_id=mint_id,
            price_age_ms=price_age_ms,
            price_source=price_source,
            primary_pool=primary_pool,
            primary_pool_id=primary_pool_id,
            primary_pool_quote_mint=primary_pool_quote_mint,
            qty=qty,
            realized=realized,
            route=route,
            signature=signature,
            slot=slot,
            sol_post_lamports=sol_post_lamports,
            sol_usd=sol_usd,
            trader=trader,
            ts_ms=ts_ms,
            tx_index=tx_index,
            v_source=v_source,
            value=value,
            wsol_post_lamports=wsol_post_lamports,
        )

        pulsight_internal_core_domain_aggregator_trade.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trade

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
