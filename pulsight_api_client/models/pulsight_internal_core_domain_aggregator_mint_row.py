from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_bonding_curve_state import (
        PulsightInternalCoreDomainAggregatorBondingCurveState,
    )
    from ..models.pulsight_internal_core_domain_aggregator_dev_holdings import (
        PulsightInternalCoreDomainAggregatorDevHoldings,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_bundled import (
        PulsightInternalCoreDomainAggregatorMintBundled,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_honeypot import (
        PulsightInternalCoreDomainAggregatorMintHoneypot,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_insiders import (
        PulsightInternalCoreDomainAggregatorMintInsiders,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_matched_pool import (
        PulsightInternalCoreDomainAggregatorMintMatchedPool,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
        PulsightInternalCoreDomainAggregatorMintStatsByWindow,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_trader_quality import (
        PulsightInternalCoreDomainAggregatorMintTraderQuality,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintRow:
    """
    Attributes:
        authorities_observed_at (str | Unset):
        bonding_curve (PulsightInternalCoreDomainAggregatorBondingCurveState | Unset):
        bundled (PulsightInternalCoreDomainAggregatorMintBundled | Unset):
        buy_count (int | Unset):
        creator (str | Unset):
        decimals (int | Unset):
        dev_holdings (PulsightInternalCoreDomainAggregatorDevHoldings | Unset):
        dust_float (bool | Unset): DustFloat reports that the holders' circulating float is under 0.1 % of
            total supply: Top10Pct and the insiders' share measure dust, and the
            risk score's concentration rules did not fire on them.
        fetch_status (str | Unset):
        first_seen_ts (str | Unset):
        freeze_authority (str | Unset):
        holder_count (int | Unset): HolderCount is the number of wallets holding a positive balance of
            this mint, off the sealed holder-stats family of the mint's row (pool
            inventory excluded by token account); nil until the family is sealed.
        honeypot (PulsightInternalCoreDomainAggregatorMintHoneypot | Unset):
        insiders (PulsightInternalCoreDomainAggregatorMintInsiders | Unset):
        is_mayhem_mode (bool | Unset): IsMayhemMode flags a Pump.fun "Mayhem"-mode token (its trades route
            through the Mayhem custody program). Populated on BOTH list and detail;
            omitted when false.
        last_trade_ts (str | Unset):
        logo_uri (str | Unset):
        lp_burned (bool | Unset): LpBurned reports whether ANY LP burn is on file for the mint — the same
            flag the `lp_burned=1` listing filter uses, so the audit glyph and the
            filter can never disagree.
        market_cap_usd (float | Unset): MarketCapUsd is the stored latest price × supply, in USD; nil when
            either is unknown.
        markets_count (int | Unset):
        matched_pool (PulsightInternalCoreDomainAggregatorMintMatchedPool | Unset):
        metadata_uri (str | Unset): MetadataURI/FetchStatus are detail-only identity fields the
            frontend's TokenIdentityCard renders (off-chain JSON link + enrich
            status). nil on list rows.
        mint (str | Unset):
        mint_authority (str | Unset): MintAuthority/FreezeAuthority: non-nil = active authority pubkey;
            nil with AuthoritiesObservedAt set = renounced; nil with
            AuthoritiesObservedAt nil = unknown (not yet observed).
        name (str | Unset):
        price_sparkline (list[float] | Unset): PriceSparkline is the mint's last-24h price shape: the USD closes of
            its dominant pool at 15-minute buckets, oldest→newest, at most
            priceSparklineMaxPoints values rounded to 6 significant digits. Only
            buckets that traded appear. It is a SHAPE (the client normalises to
            its own min/max), not a price read. Omitted below 2 points.
        price_usd (float | Unset): PriceUsd is the stored latest price per WHOLE token in USD (the
            reference pool's per-raw-unit stamp scaled by the mint's decimals);
            nil when the mint has no priced reference pool or unknown decimals.
        risk_score (int | Unset): RiskScore/RiskVerdict are a fast at-a-glance risk score (0..100 +
            low|caution|high|critical) computed from the signals already on this row
            (authorities, honeypot/copycat/sell-trap, dev %, bundle, top-10
            concentration, lifetime fees per tx, trader quality) via the same
            domain ScoreRisk as the per-mint risk card. The listing omits the inputs
            that need per-mint queries (snipers, insider %, liquidity), so this is a
            LOWER BOUND of the card's full score — the token page is authoritative.
            nil only if scoring was skipped.
        risk_verdict (str | Unset):
        sell_count (int | Unset):
        stats (PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset):
        supply (str | Unset): Supply is the on-chain total supply (decimal string, raw
            smallest units); nil until the enricher has decoded the mint account.
            Populated on the list path to back the market-cap column.
        swap_count (int | Unset): Activity counts. On the listing they count the `?hours` gate the page
            was filtered on, off the board row's gate counters; on the detail page
            SwapCount, BuyCount and SellCount are lifetime and TraderCount is 0.
            MarketsCount is the number of pools the mint trades in.
        symbol (str | Unset):
        top10_pct (float | Unset): Top10Pct is the top-10 holder concentration as a PERCENT of circulating
            supply (0..100), off the mint's holder-stats plane — the figure the
            listing's Distribution column leads with. nil until the plane has
            folded the mint's holders.
        top_dex (str | Unset): TopDex is the venue slug the token actually trades on: on the listing
            the mint's dominant pool's venue, on the detail page its graduation
            target or else its launchpad. Same vocabulary as `?dex=`; look up the
            display label via DEX_LABEL. nil when unknown.
        total_fees_sol (int | Unset): TotalFeesSol — LIFETIME network fees paid trading the mint, in
            lamports: tx fees (base + priority) plus MEV tips over its trades.
            Unlike the listing's counts above it is NOT hours-window-bound. nil
            when the mint has no trades on file.
        total_fees_usd (int | Unset): TotalFeesUsd is the same figure on the USD stamps (micro-USD).
        total_tx_count (int | Unset): TotalTxCount — LIFETIME trade count for the mint, on the same basis as
            TotalFeesSol. It is the fee figure's denominator: the bot-fee-pattern
            risk rule scores fees PER transaction, so the two must share a basis —
            the hours-window SwapCount would not. nil whenever TotalFeesSol is.
        trader_count (int | Unset):
        trader_quality (PulsightInternalCoreDomainAggregatorMintTraderQuality | Unset):
        unique_traders (int | Unset): UniqueTraders is the LIFETIME number of distinct wallets that traded
            this mint (the insert-time `mint_traders` plane on the detail path, the
            holder-stats traders on the list path), as opposed to TraderCount, the
            count over the `?hours` gate; nil when unavailable.
        verified (bool | Unset): Verified marks a mint on the curated verified token list (Jupiter's,
            refreshed hourly by the jupverified registry). Also the copycat
            CANONICAL exemption: a verified member of a name-dupe farm keeps its
            listing spot and loses the copycat badge while the clones stay
            flagged. Omitted when false or when no registry is wired.
    """

    authorities_observed_at: str | Unset = UNSET
    bonding_curve: PulsightInternalCoreDomainAggregatorBondingCurveState | Unset = UNSET
    bundled: PulsightInternalCoreDomainAggregatorMintBundled | Unset = UNSET
    buy_count: int | Unset = UNSET
    creator: str | Unset = UNSET
    decimals: int | Unset = UNSET
    dev_holdings: PulsightInternalCoreDomainAggregatorDevHoldings | Unset = UNSET
    dust_float: bool | Unset = UNSET
    fetch_status: str | Unset = UNSET
    first_seen_ts: str | Unset = UNSET
    freeze_authority: str | Unset = UNSET
    holder_count: int | Unset = UNSET
    honeypot: PulsightInternalCoreDomainAggregatorMintHoneypot | Unset = UNSET
    insiders: PulsightInternalCoreDomainAggregatorMintInsiders | Unset = UNSET
    is_mayhem_mode: bool | Unset = UNSET
    last_trade_ts: str | Unset = UNSET
    logo_uri: str | Unset = UNSET
    lp_burned: bool | Unset = UNSET
    market_cap_usd: float | Unset = UNSET
    markets_count: int | Unset = UNSET
    matched_pool: PulsightInternalCoreDomainAggregatorMintMatchedPool | Unset = UNSET
    metadata_uri: str | Unset = UNSET
    mint: str | Unset = UNSET
    mint_authority: str | Unset = UNSET
    name: str | Unset = UNSET
    price_sparkline: list[float] | Unset = UNSET
    price_usd: float | Unset = UNSET
    risk_score: int | Unset = UNSET
    risk_verdict: str | Unset = UNSET
    sell_count: int | Unset = UNSET
    stats: PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset = UNSET
    supply: str | Unset = UNSET
    swap_count: int | Unset = UNSET
    symbol: str | Unset = UNSET
    top10_pct: float | Unset = UNSET
    top_dex: str | Unset = UNSET
    total_fees_sol: int | Unset = UNSET
    total_fees_usd: int | Unset = UNSET
    total_tx_count: int | Unset = UNSET
    trader_count: int | Unset = UNSET
    trader_quality: PulsightInternalCoreDomainAggregatorMintTraderQuality | Unset = (
        UNSET
    )
    unique_traders: int | Unset = UNSET
    verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorities_observed_at = self.authorities_observed_at

        bonding_curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bonding_curve, Unset):
            bonding_curve = self.bonding_curve.to_dict()

        bundled: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bundled, Unset):
            bundled = self.bundled.to_dict()

        buy_count = self.buy_count

        creator = self.creator

        decimals = self.decimals

        dev_holdings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_holdings, Unset):
            dev_holdings = self.dev_holdings.to_dict()

        dust_float = self.dust_float

        fetch_status = self.fetch_status

        first_seen_ts = self.first_seen_ts

        freeze_authority = self.freeze_authority

        holder_count = self.holder_count

        honeypot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.honeypot, Unset):
            honeypot = self.honeypot.to_dict()

        insiders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insiders, Unset):
            insiders = self.insiders.to_dict()

        is_mayhem_mode = self.is_mayhem_mode

        last_trade_ts = self.last_trade_ts

        logo_uri = self.logo_uri

        lp_burned = self.lp_burned

        market_cap_usd = self.market_cap_usd

        markets_count = self.markets_count

        matched_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matched_pool, Unset):
            matched_pool = self.matched_pool.to_dict()

        metadata_uri = self.metadata_uri

        mint = self.mint

        mint_authority = self.mint_authority

        name = self.name

        price_sparkline: list[float] | Unset = UNSET
        if not isinstance(self.price_sparkline, Unset):
            price_sparkline = self.price_sparkline

        price_usd = self.price_usd

        risk_score = self.risk_score

        risk_verdict = self.risk_verdict

        sell_count = self.sell_count

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        supply = self.supply

        swap_count = self.swap_count

        symbol = self.symbol

        top10_pct = self.top10_pct

        top_dex = self.top_dex

        total_fees_sol = self.total_fees_sol

        total_fees_usd = self.total_fees_usd

        total_tx_count = self.total_tx_count

        trader_count = self.trader_count

        trader_quality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trader_quality, Unset):
            trader_quality = self.trader_quality.to_dict()

        unique_traders = self.unique_traders

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorities_observed_at is not UNSET:
            field_dict["authorities_observed_at"] = authorities_observed_at
        if bonding_curve is not UNSET:
            field_dict["bonding_curve"] = bonding_curve
        if bundled is not UNSET:
            field_dict["bundled"] = bundled
        if buy_count is not UNSET:
            field_dict["buy_count"] = buy_count
        if creator is not UNSET:
            field_dict["creator"] = creator
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if dev_holdings is not UNSET:
            field_dict["dev_holdings"] = dev_holdings
        if dust_float is not UNSET:
            field_dict["dust_float"] = dust_float
        if fetch_status is not UNSET:
            field_dict["fetch_status"] = fetch_status
        if first_seen_ts is not UNSET:
            field_dict["first_seen_ts"] = first_seen_ts
        if freeze_authority is not UNSET:
            field_dict["freeze_authority"] = freeze_authority
        if holder_count is not UNSET:
            field_dict["holder_count"] = holder_count
        if honeypot is not UNSET:
            field_dict["honeypot"] = honeypot
        if insiders is not UNSET:
            field_dict["insiders"] = insiders
        if is_mayhem_mode is not UNSET:
            field_dict["is_mayhem_mode"] = is_mayhem_mode
        if last_trade_ts is not UNSET:
            field_dict["last_trade_ts"] = last_trade_ts
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if lp_burned is not UNSET:
            field_dict["lp_burned"] = lp_burned
        if market_cap_usd is not UNSET:
            field_dict["market_cap_usd"] = market_cap_usd
        if markets_count is not UNSET:
            field_dict["markets_count"] = markets_count
        if matched_pool is not UNSET:
            field_dict["matched_pool"] = matched_pool
        if metadata_uri is not UNSET:
            field_dict["metadata_uri"] = metadata_uri
        if mint is not UNSET:
            field_dict["mint"] = mint
        if mint_authority is not UNSET:
            field_dict["mint_authority"] = mint_authority
        if name is not UNSET:
            field_dict["name"] = name
        if price_sparkline is not UNSET:
            field_dict["price_sparkline"] = price_sparkline
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if risk_score is not UNSET:
            field_dict["risk_score"] = risk_score
        if risk_verdict is not UNSET:
            field_dict["risk_verdict"] = risk_verdict
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
        if top10_pct is not UNSET:
            field_dict["top10_pct"] = top10_pct
        if top_dex is not UNSET:
            field_dict["top_dex"] = top_dex
        if total_fees_sol is not UNSET:
            field_dict["total_fees_sol"] = total_fees_sol
        if total_fees_usd is not UNSET:
            field_dict["total_fees_usd"] = total_fees_usd
        if total_tx_count is not UNSET:
            field_dict["total_tx_count"] = total_tx_count
        if trader_count is not UNSET:
            field_dict["trader_count"] = trader_count
        if trader_quality is not UNSET:
            field_dict["trader_quality"] = trader_quality
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_bonding_curve_state import (
            PulsightInternalCoreDomainAggregatorBondingCurveState,
        )
        from ..models.pulsight_internal_core_domain_aggregator_dev_holdings import (
            PulsightInternalCoreDomainAggregatorDevHoldings,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_bundled import (
            PulsightInternalCoreDomainAggregatorMintBundled,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_honeypot import (
            PulsightInternalCoreDomainAggregatorMintHoneypot,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_insiders import (
            PulsightInternalCoreDomainAggregatorMintInsiders,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_matched_pool import (
            PulsightInternalCoreDomainAggregatorMintMatchedPool,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
            PulsightInternalCoreDomainAggregatorMintStatsByWindow,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_trader_quality import (
            PulsightInternalCoreDomainAggregatorMintTraderQuality,
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

        _bundled = d.pop("bundled", UNSET)
        bundled: PulsightInternalCoreDomainAggregatorMintBundled | Unset
        if isinstance(_bundled, Unset):
            bundled = UNSET
        else:
            bundled = PulsightInternalCoreDomainAggregatorMintBundled.from_dict(
                _bundled
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

        dust_float = d.pop("dust_float", UNSET)

        fetch_status = d.pop("fetch_status", UNSET)

        first_seen_ts = d.pop("first_seen_ts", UNSET)

        freeze_authority = d.pop("freeze_authority", UNSET)

        holder_count = d.pop("holder_count", UNSET)

        _honeypot = d.pop("honeypot", UNSET)
        honeypot: PulsightInternalCoreDomainAggregatorMintHoneypot | Unset
        if isinstance(_honeypot, Unset):
            honeypot = UNSET
        else:
            honeypot = PulsightInternalCoreDomainAggregatorMintHoneypot.from_dict(
                _honeypot
            )

        _insiders = d.pop("insiders", UNSET)
        insiders: PulsightInternalCoreDomainAggregatorMintInsiders | Unset
        if isinstance(_insiders, Unset):
            insiders = UNSET
        else:
            insiders = PulsightInternalCoreDomainAggregatorMintInsiders.from_dict(
                _insiders
            )

        is_mayhem_mode = d.pop("is_mayhem_mode", UNSET)

        last_trade_ts = d.pop("last_trade_ts", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        lp_burned = d.pop("lp_burned", UNSET)

        market_cap_usd = d.pop("market_cap_usd", UNSET)

        markets_count = d.pop("markets_count", UNSET)

        _matched_pool = d.pop("matched_pool", UNSET)
        matched_pool: PulsightInternalCoreDomainAggregatorMintMatchedPool | Unset
        if isinstance(_matched_pool, Unset):
            matched_pool = UNSET
        else:
            matched_pool = (
                PulsightInternalCoreDomainAggregatorMintMatchedPool.from_dict(
                    _matched_pool
                )
            )

        metadata_uri = d.pop("metadata_uri", UNSET)

        mint = d.pop("mint", UNSET)

        mint_authority = d.pop("mint_authority", UNSET)

        name = d.pop("name", UNSET)

        price_sparkline = cast(list[float], d.pop("price_sparkline", UNSET))

        price_usd = d.pop("price_usd", UNSET)

        risk_score = d.pop("risk_score", UNSET)

        risk_verdict = d.pop("risk_verdict", UNSET)

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

        top10_pct = d.pop("top10_pct", UNSET)

        top_dex = d.pop("top_dex", UNSET)

        total_fees_sol = d.pop("total_fees_sol", UNSET)

        total_fees_usd = d.pop("total_fees_usd", UNSET)

        total_tx_count = d.pop("total_tx_count", UNSET)

        trader_count = d.pop("trader_count", UNSET)

        _trader_quality = d.pop("trader_quality", UNSET)
        trader_quality: PulsightInternalCoreDomainAggregatorMintTraderQuality | Unset
        if isinstance(_trader_quality, Unset):
            trader_quality = UNSET
        else:
            trader_quality = (
                PulsightInternalCoreDomainAggregatorMintTraderQuality.from_dict(
                    _trader_quality
                )
            )

        unique_traders = d.pop("unique_traders", UNSET)

        verified = d.pop("verified", UNSET)

        pulsight_internal_core_domain_aggregator_mint_row = cls(
            authorities_observed_at=authorities_observed_at,
            bonding_curve=bonding_curve,
            bundled=bundled,
            buy_count=buy_count,
            creator=creator,
            decimals=decimals,
            dev_holdings=dev_holdings,
            dust_float=dust_float,
            fetch_status=fetch_status,
            first_seen_ts=first_seen_ts,
            freeze_authority=freeze_authority,
            holder_count=holder_count,
            honeypot=honeypot,
            insiders=insiders,
            is_mayhem_mode=is_mayhem_mode,
            last_trade_ts=last_trade_ts,
            logo_uri=logo_uri,
            lp_burned=lp_burned,
            market_cap_usd=market_cap_usd,
            markets_count=markets_count,
            matched_pool=matched_pool,
            metadata_uri=metadata_uri,
            mint=mint,
            mint_authority=mint_authority,
            name=name,
            price_sparkline=price_sparkline,
            price_usd=price_usd,
            risk_score=risk_score,
            risk_verdict=risk_verdict,
            sell_count=sell_count,
            stats=stats,
            supply=supply,
            swap_count=swap_count,
            symbol=symbol,
            top10_pct=top10_pct,
            top_dex=top_dex,
            total_fees_sol=total_fees_sol,
            total_fees_usd=total_fees_usd,
            total_tx_count=total_tx_count,
            trader_count=trader_count,
            trader_quality=trader_quality,
            unique_traders=unique_traders,
            verified=verified,
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
