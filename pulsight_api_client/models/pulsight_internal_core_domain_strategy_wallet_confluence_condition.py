from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_strategy_comparison_op import (
    PulsightInternalCoreDomainStrategyComparisonOp,
)
from ..models.pulsight_internal_core_domain_strategy_confluence_count import (
    PulsightInternalCoreDomainStrategyConfluenceCount,
)
from ..models.pulsight_internal_core_domain_strategy_confluence_metric import (
    PulsightInternalCoreDomainStrategyConfluenceMetric,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_confluence_source import (
        PulsightInternalCoreDomainStrategyConfluenceSource,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyWalletConfluenceCondition")


@_attrs_define
class PulsightInternalCoreDomainStrategyWalletConfluenceCondition:
    """
    Attributes:
        count (PulsightInternalCoreDomainStrategyConfluenceCount | Unset):
        dedup_secs (int | Unset): DedupSecs merges wallets whose trades are within this many seconds of each other into
            one; absent is 1, 0 turns it off.
        max_premium_pct (float | Unset): MaxPremiumPct caps how far the price may sit above the counted wallets' average
            entry, in percent; holders and buyers only.
        metric (PulsightInternalCoreDomainStrategyConfluenceMetric | Unset):
        min_buy_sol (float | Unset): MinBuySol is the SOL a wallet must have bought over its position to count; absent
            is no floor.
        min_sell_pct (float | Unset): MinSellPct is the share of its position a wallet must have sold to count, required
            with sellers only.
        op (PulsightInternalCoreDomainStrategyComparisonOp | Unset):
        sources (list[PulsightInternalCoreDomainStrategyConfluenceSource] | Unset): Sources records the favorites groups
            the wallets came from; nothing evaluates it.
        value (int | Unset): Value is the threshold: 1 to the set size with gte, 0 to one less than the set size with
            lte.
        wallets (list[str] | Unset): Wallets is the set, 2 to 50 distinct addresses.
        window_secs (int | Unset): WindowSecs is the window in seconds, 10 to 604800.
    """

    count: PulsightInternalCoreDomainStrategyConfluenceCount | Unset = UNSET
    dedup_secs: int | Unset = UNSET
    max_premium_pct: float | Unset = UNSET
    metric: PulsightInternalCoreDomainStrategyConfluenceMetric | Unset = UNSET
    min_buy_sol: float | Unset = UNSET
    min_sell_pct: float | Unset = UNSET
    op: PulsightInternalCoreDomainStrategyComparisonOp | Unset = UNSET
    sources: list[PulsightInternalCoreDomainStrategyConfluenceSource] | Unset = UNSET
    value: int | Unset = UNSET
    wallets: list[str] | Unset = UNSET
    window_secs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count: str | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.value

        dedup_secs = self.dedup_secs

        max_premium_pct = self.max_premium_pct

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        min_buy_sol = self.min_buy_sol

        min_sell_pct = self.min_sell_pct

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        value = self.value

        wallets: list[str] | Unset = UNSET
        if not isinstance(self.wallets, Unset):
            wallets = self.wallets

        window_secs = self.window_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if dedup_secs is not UNSET:
            field_dict["dedup_secs"] = dedup_secs
        if max_premium_pct is not UNSET:
            field_dict["max_premium_pct"] = max_premium_pct
        if metric is not UNSET:
            field_dict["metric"] = metric
        if min_buy_sol is not UNSET:
            field_dict["min_buy_sol"] = min_buy_sol
        if min_sell_pct is not UNSET:
            field_dict["min_sell_pct"] = min_sell_pct
        if op is not UNSET:
            field_dict["op"] = op
        if sources is not UNSET:
            field_dict["sources"] = sources
        if value is not UNSET:
            field_dict["value"] = value
        if wallets is not UNSET:
            field_dict["wallets"] = wallets
        if window_secs is not UNSET:
            field_dict["window_secs"] = window_secs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_strategy_confluence_source import (
            PulsightInternalCoreDomainStrategyConfluenceSource,
        )

        d = dict(src_dict)
        _count = d.pop("count", UNSET)
        count: PulsightInternalCoreDomainStrategyConfluenceCount | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = PulsightInternalCoreDomainStrategyConfluenceCount(_count)

        dedup_secs = d.pop("dedup_secs", UNSET)

        max_premium_pct = d.pop("max_premium_pct", UNSET)

        _metric = d.pop("metric", UNSET)
        metric: PulsightInternalCoreDomainStrategyConfluenceMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = PulsightInternalCoreDomainStrategyConfluenceMetric(_metric)

        min_buy_sol = d.pop("min_buy_sol", UNSET)

        min_sell_pct = d.pop("min_sell_pct", UNSET)

        _op = d.pop("op", UNSET)
        op: PulsightInternalCoreDomainStrategyComparisonOp | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = PulsightInternalCoreDomainStrategyComparisonOp(_op)

        _sources = d.pop("sources", UNSET)
        sources: list[PulsightInternalCoreDomainStrategyConfluenceSource] | Unset = (
            UNSET
        )
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = (
                    PulsightInternalCoreDomainStrategyConfluenceSource.from_dict(
                        sources_item_data
                    )
                )

                sources.append(sources_item)

        value = d.pop("value", UNSET)

        wallets = cast(list[str], d.pop("wallets", UNSET))

        window_secs = d.pop("window_secs", UNSET)

        pulsight_internal_core_domain_strategy_wallet_confluence_condition = cls(
            count=count,
            dedup_secs=dedup_secs,
            max_premium_pct=max_premium_pct,
            metric=metric,
            min_buy_sol=min_buy_sol,
            min_sell_pct=min_sell_pct,
            op=op,
            sources=sources,
            value=value,
            wallets=wallets,
            window_secs=window_secs,
        )

        pulsight_internal_core_domain_strategy_wallet_confluence_condition.additional_properties = d
        return pulsight_internal_core_domain_strategy_wallet_confluence_condition

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
