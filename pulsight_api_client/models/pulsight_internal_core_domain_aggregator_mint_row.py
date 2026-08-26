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
        buy_count (int | Unset): BuyCount/SellCount: buy- vs sell-side swap counts over the `?hours`
            activity window (countIf(is_buy)). Populated on the list path; 0 on
            the detail path.
        creator (str | Unset):
        decimals (int | Unset):
        dev_holdings (PulsightInternalCoreDomainAggregatorDevHoldings | Unset):
        fetch_status (str | Unset):
        first_seen_ts (str | Unset):
        freeze_authority (str | Unset):
        holder_count (int | Unset): ── GMGN-style discovery enrichment (list path only, best-effort). ──
            HolderCount is the number of distinct wallets currently holding a
            positive balance of this mint (uniqExact over trader_token_stats).
            nil when the holders batch is unavailable. Best-effort: a holders
            hiccup decorates fewer rows, it never fails the listing.
        honeypot (PulsightInternalCoreDomainAggregatorMintHoneypot | Unset):
        insiders (PulsightInternalCoreDomainAggregatorMintInsiders | Unset):
        is_mayhem_mode (bool | Unset): IsMayhemMode flags a Pump.fun "Mayhem"-mode token (its trades route
            through the Mayhem custody program). Populated on BOTH list and detail
            from the mint_mayhem table; omitted when false.
        last_trade_ts (str | Unset):
        logo_uri (str | Unset):
        lp_burned (bool | Unset): LpBurned reports whether ANY LP burn is on file for the mint — the same
            `lp_events(op='burn')` set the `lp_burned=1` listing filter uses, so the
            audit glyph and the filter can never disagree. Page-scoped, so it is a
            definite true/false for every returned row (never nil on the list path);
            nil on the detail path, where the batch does not run.
        market_cap_usd (float | Unset): MarketCapUsd is PriceUsd × circulating supply. Equivalently
            close_sol × supply_raw × sol_usd / 1e6 (token decimals cancel), so
            it's populated even when decimals are unknown (unlike PriceUsd). nil
            when the WSOL close, supply, or SOL/USD ref is missing.
        markets_count (int | Unset):
        metadata_uri (str | Unset): MetadataURI/FetchStatus are detail-only identity fields the
            frontend's TokenIdentityCard renders (off-chain JSON link + enrich
            status). nil on list rows.
        mint (str | Unset):
        mint_authority (str | Unset): MintAuthority/FreezeAuthority: non-nil = active authority pubkey;
            nil with AuthoritiesObservedAt set = renounced; nil with
            AuthoritiesObservedAt nil = unknown (not yet observed).
        name (str | Unset):
        price_sparkline (list[float] | Unset): PriceSparkline is the mint's last-24h price shape: WSOL-quoted per-minute
            closes of the mint's DOMINANT pool (highest 24h quote volume — one pool,
            never a merge, so a dust side-market's prints can't flatten the line),
            oldest→newest, at most priceSparklineMaxPoints values. A mint that
            traded through the whole window is sampled evenly down to that cap
            (so the series still spans 24h, just coarser); one that traded for an
            hour carries all of it. It rides the SAME scan as PriceUsd, so it
            carries the same denomination caveat: WSOL-quoted only, which is why a
            USDC-only mint has none rather than a series in another unit (mixing
            quotes would draw a step that never happened). Values are raw SOL per
            whole token, rounded to 6 significant digits — the client normalises to
            its own min/max, so the unit only has to be CONSISTENT within the
            series, and this is a SHAPE, not a price read (use PriceUsd for that).
            Only minutes that actually traded appear, so the x axis is trade
            sequence, not wall clock. Omitted below 2 points — but a mint younger
            than ~10 minutes gets its points from 1-SECOND candles instead, so a
            fresh row draws a line as soon as it has two seconds of trading.
        price_usd (float | Unset): PriceUsd is the latest price per WHOLE token in USD, derived from the
            dominant WSOL-quoted OHLCV close × the SOL/USD reference rate. nil
            when there's no WSOL pool, decimals are unknown, or no SOL/USD ref.
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
        supply (str | Unset): Supply is the on-chain total supply (NUMERIC → decimal string, raw
            smallest units); nil until the enricher has decoded the mint account.
            Populated on the list path to back the market-cap column.
        swap_count (int | Unset): Window-bound activity aggregates over the `?hours` lookback,
            derived from hourly_mint_trader_activity + hourly_mint_pool_activity.
            All non-pointer because GROUP BY in the LATERAL produces a row even
            for zero swaps (we go through the activity gate first, so anything
            returned has at least one). SwapCount, TraderCount and MarketsCount
            default to 0 if the LATERAL came up empty; the frontend's `formatNum`
            renders 0 cleanly.
        symbol (str | Unset):
        top10_pct (float | Unset): Top10Pct is the top-10 holder concentration as a PERCENT of circulating
            supply (0..100). Already read per page by top10ConcentrationBatch to
            score the row — emitting it costs nothing extra and is what the listing's
            Distribution column leads with. nil when the accumulator has no row for
            the mint (fresh token, or holder balances not yet folded).
        top_dex (str | Unset): TopDex is the venue slug of the mint's DOMINANT pool over the activity
            window — the pool with the most quote volume, i.e. the venue the token
            actually trades on. Same vocabulary as `?dex=` and `swaps.dex`; look up
            the display label via DEX_LABEL. Rides fillMarketsCount's existing scan
            (same GROUP BY, one more aggregate), so it is free. nil when the mint had
            no dex_swaps row in the window.
        total_fees_sol (int | Unset): TotalFeesSol — LIFETIME network fees paid trading the mint, in
            lamports: tx fees (base + priority) plus MEV tips summed over its
            swaps (CA 000137 on mint_activity_totals; the 000064 sawtooth basis —
            lifetime between stats rebuilds, re-synced to the swaps 3-month
            retention at each healer finalize). Unlike the counts above it is NOT
            hours-window-bound. nil until the migration is applied or when the
            page decoration read fails.
        total_tx_count (int | Unset): TotalTxCount — LIFETIME swap count for the mint, from the same
            mint_activity_totals seek as TotalFeesSol (and on its same sawtooth
            basis). It is the fee figure's denominator: the bot-fee-pattern risk
            rule scores fees PER transaction, so the two must share a basis —
            the hours-window SwapCount would not. nil whenever TotalFeesSol is.
        trader_count (int | Unset):
        trader_quality (PulsightInternalCoreDomainAggregatorMintTraderQuality | Unset):
        unique_traders (int | Unset): UniqueTraders is the number of distinct wallets that have EVER traded
            this mint (all-time count() over trader_token_stats, the same
            projection-served source as HolderCount). Distinct from TraderCount
            (which is a WINDOWED, HLL-approximate count over the `?hours` gate and
            is set on the list path only): UniqueTraders is exact and lifetime, so
            the list column and the /api/mints/:pubkey detail render the same value.
            Populated on BOTH paths, best-effort: nil when the trader_token_stats
            read is unavailable.
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
