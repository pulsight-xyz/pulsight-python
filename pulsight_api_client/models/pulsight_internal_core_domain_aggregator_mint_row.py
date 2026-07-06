from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_bonding_curve_state import (
        PulsightInternalCoreDomainAggregatorBondingCurveState,
    )
    from ..models.pulsight_internal_core_domain_aggregator_dev_holdings import (
        PulsightInternalCoreDomainAggregatorDevHoldings,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
        PulsightInternalCoreDomainAggregatorMintStatsByWindow,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintRow:
    """
    Attributes:
        authorities_observed_at (str | Unset):
        bonding_curve (PulsightInternalCoreDomainAggregatorBondingCurveState | Unset):
        buy_count (int | Unset): BuyCount/SellCount: buy- vs sell-side swap counts over the `?hours`
            activity window (countIf(is_buy)). Populated on the list path; 0 on
            the detail path.
        creator (str | Unset):
        decimals (int | Unset):
        dev_holdings (PulsightInternalCoreDomainAggregatorDevHoldings | Unset):
        fetch_status (str | Unset):
        first_seen_ts (str | Unset):
        freeze_authority (str | Unset):
        is_mayhem_mode (bool | Unset): IsMayhemMode flags a Pump.fun "Mayhem"-mode token (its trades route
            through the Mayhem custody program). Populated on BOTH list and detail
            from the mint_mayhem table; omitted when false.
        last_trade_ts (str | Unset):
        logo_uri (str | Unset):
        markets_count (int | Unset):
        metadata_uri (str | Unset): MetadataURI/FetchStatus are detail-only identity fields the
            frontend's TokenIdentityCard renders (off-chain JSON link + enrich
            status). nil on list rows.
        mint (str | Unset):
        mint_authority (str | Unset): MintAuthority/FreezeAuthority: non-nil = active authority pubkey;
            nil with AuthoritiesObservedAt set = renounced; nil with
            AuthoritiesObservedAt nil = unknown (not yet observed).
        name (str | Unset):
        sell_count (int | Unset):
        stats (PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset):
        supply (str | Unset): Supply is the on-chain total supply (NUMERIC → decimal string);
            nil until the enricher has decoded the mint account.
        swap_count (int | Unset): Window-bound activity aggregates over the `?hours` lookback,
            derived from hourly_mint_trader_activity + hourly_mint_pool_activity.
            All non-pointer because GROUP BY in the LATERAL produces a row even
            for zero swaps (we go through the activity gate first, so anything
            returned has at least one). SwapCount, TraderCount and MarketsCount
            default to 0 if the LATERAL came up empty; the frontend's `formatNum`
            renders 0 cleanly.
        symbol (str | Unset):
        trader_count (int | Unset):
    """

    authorities_observed_at: str | Unset = UNSET
    bonding_curve: PulsightInternalCoreDomainAggregatorBondingCurveState | Unset = UNSET
    buy_count: int | Unset = UNSET
    creator: str | Unset = UNSET
    decimals: int | Unset = UNSET
    dev_holdings: PulsightInternalCoreDomainAggregatorDevHoldings | Unset = UNSET
    fetch_status: str | Unset = UNSET
    first_seen_ts: str | Unset = UNSET
    freeze_authority: str | Unset = UNSET
    is_mayhem_mode: bool | Unset = UNSET
    last_trade_ts: str | Unset = UNSET
    logo_uri: str | Unset = UNSET
    markets_count: int | Unset = UNSET
    metadata_uri: str | Unset = UNSET
    mint: str | Unset = UNSET
    mint_authority: str | Unset = UNSET
    name: str | Unset = UNSET
    sell_count: int | Unset = UNSET
    stats: PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset = UNSET
    supply: str | Unset = UNSET
    swap_count: int | Unset = UNSET
    symbol: str | Unset = UNSET
    trader_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorities_observed_at = self.authorities_observed_at

        bonding_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bonding_curve, Unset):
            bonding_curve = self.bonding_curve.to_dict()

        buy_count = self.buy_count

        creator = self.creator

        decimals = self.decimals

        dev_holdings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_holdings, Unset):
            dev_holdings = self.dev_holdings.to_dict()

        fetch_status = self.fetch_status

        first_seen_ts = self.first_seen_ts

        freeze_authority = self.freeze_authority

        is_mayhem_mode = self.is_mayhem_mode

        last_trade_ts = self.last_trade_ts

        logo_uri = self.logo_uri

        markets_count = self.markets_count

        metadata_uri = self.metadata_uri

        mint = self.mint

        mint_authority = self.mint_authority

        name = self.name

        sell_count = self.sell_count

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        supply = self.supply

        swap_count = self.swap_count

        symbol = self.symbol

        trader_count = self.trader_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorities_observed_at is not UNSET:
            field_dict["authorities_observed_at"] = authorities_observed_at
        if bonding_curve is not UNSET:
            field_dict["bonding_curve"] = bonding_curve
        if buy_count is not UNSET:
            field_dict["buy_count"] = buy_count
        if creator is not UNSET:
            field_dict["creator"] = creator
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if dev_holdings is not UNSET:
            field_dict["dev_holdings"] = dev_holdings
        if fetch_status is not UNSET:
            field_dict["fetch_status"] = fetch_status
        if first_seen_ts is not UNSET:
            field_dict["first_seen_ts"] = first_seen_ts
        if freeze_authority is not UNSET:
            field_dict["freeze_authority"] = freeze_authority
        if is_mayhem_mode is not UNSET:
            field_dict["is_mayhem_mode"] = is_mayhem_mode
        if last_trade_ts is not UNSET:
            field_dict["last_trade_ts"] = last_trade_ts
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if markets_count is not UNSET:
            field_dict["markets_count"] = markets_count
        if metadata_uri is not UNSET:
            field_dict["metadata_uri"] = metadata_uri
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mint_authority is not UNSET:
            field_dict["mint_authority"] = mint_authority
        if name is not UNSET:
            field_dict["name"] = name
        if sell_count is not UNSET:
            field_dict["sell_count"] = sell_count
        if stats is not UNSET:
            field_dict["stats"] = stats
        if supply is not UNSET:
            field_dict["supply"] = supply
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if trader_count is not UNSET:
            field_dict["trader_count"] = trader_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_aggregator_bonding_curve_state import (
            PulsightInternalCoreDomainAggregatorBondingCurveState,
        )
        from ..models.pulsight_internal_core_domain_aggregator_dev_holdings import (
            PulsightInternalCoreDomainAggregatorDevHoldings,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
            PulsightInternalCoreDomainAggregatorMintStatsByWindow,
        )

        d = dict(src_dict)
        authorities_observed_at = d.pop("authorities_observed_at", UNSET)

        _bonding_curve = d.pop("bonding_curve", UNSET)
        bonding_curve: PulsightInternalCoreDomainAggregatorBondingCurveState | Unset
        if isinstance(_bonding_curve, Unset):
            bonding_curve = UNSET
        else:
            bonding_curve = (
                PulsightInternalCoreDomainAggregatorBondingCurveState.from_dict(
                    _bonding_curve
                )
            )

        buy_count = d.pop("buy_count", UNSET)

        creator = d.pop("creator", UNSET)

        decimals = d.pop("decimals", UNSET)

        _dev_holdings = d.pop("dev_holdings", UNSET)
        dev_holdings: PulsightInternalCoreDomainAggregatorDevHoldings | Unset
        if isinstance(_dev_holdings, Unset):
            dev_holdings = UNSET
        else:
            dev_holdings = PulsightInternalCoreDomainAggregatorDevHoldings.from_dict(
                _dev_holdings
            )

        fetch_status = d.pop("fetch_status", UNSET)

        first_seen_ts = d.pop("first_seen_ts", UNSET)

        freeze_authority = d.pop("freeze_authority", UNSET)

        is_mayhem_mode = d.pop("is_mayhem_mode", UNSET)

        last_trade_ts = d.pop("last_trade_ts", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        markets_count = d.pop("markets_count", UNSET)

        metadata_uri = d.pop("metadata_uri", UNSET)

        mint = d.pop("mint", UNSET)

        mint_authority = d.pop("mint_authority", UNSET)

        name = d.pop("name", UNSET)

        sell_count = d.pop("sell_count", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = PulsightInternalCoreDomainAggregatorMintStatsByWindow.from_dict(
                _stats
            )

        supply = d.pop("supply", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        symbol = d.pop("symbol", UNSET)

        trader_count = d.pop("trader_count", UNSET)

        pulsight_internal_core_domain_aggregator_mint_row = cls(
            authorities_observed_at=authorities_observed_at,
            bonding_curve=bonding_curve,
            buy_count=buy_count,
            creator=creator,
            decimals=decimals,
            dev_holdings=dev_holdings,
            fetch_status=fetch_status,
            first_seen_ts=first_seen_ts,
            freeze_authority=freeze_authority,
            is_mayhem_mode=is_mayhem_mode,
            last_trade_ts=last_trade_ts,
            logo_uri=logo_uri,
            markets_count=markets_count,
            metadata_uri=metadata_uri,
            mint=mint,
            mint_authority=mint_authority,
            name=name,
            sell_count=sell_count,
            stats=stats,
            supply=supply,
            swap_count=swap_count,
            symbol=symbol,
            trader_count=trader_count,
        )

        pulsight_internal_core_domain_aggregator_mint_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_row

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
