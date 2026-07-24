from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_authority_stat import (
        PulsightInternalCoreDomainAggregatorAuthorityStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_bundler_stat import (
        PulsightInternalCoreDomainAggregatorBundlerStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_cohort_stat import (
        PulsightInternalCoreDomainAggregatorCohortStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_dev_stat import (
        PulsightInternalCoreDomainAggregatorDevStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
        PulsightInternalCoreDomainAggregatorHolderEntry,
    )
    from ..models.pulsight_internal_core_domain_aggregator_lp_stat import (
        PulsightInternalCoreDomainAggregatorLpStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_market_stat import (
        PulsightInternalCoreDomainAggregatorMarketStat,
    )
    from ..models.pulsight_internal_core_domain_aggregator_risk_item import (
        PulsightInternalCoreDomainAggregatorRiskItem,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorRiskReport")


@_attrs_define
class PulsightInternalCoreDomainAggregatorRiskReport:
    """
    Attributes:
        authorities (PulsightInternalCoreDomainAggregatorAuthorityStat | Unset):
        bundlers (PulsightInternalCoreDomainAggregatorBundlerStat | Unset):
        dev (PulsightInternalCoreDomainAggregatorDevStat | Unset):
        holder_count (int | Unset):
        holders (list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset): top few (summary)
        insiders (PulsightInternalCoreDomainAggregatorCohortStat | Unset):
        lp (PulsightInternalCoreDomainAggregatorLpStat | Unset):
        markets (PulsightInternalCoreDomainAggregatorMarketStat | Unset):
        mint (str | Unset):
        risks (list[PulsightInternalCoreDomainAggregatorRiskItem] | Unset):
        rugged (bool | Unset):
        score (int | Unset):
        score_normalised (int | Unset): 0..100
        snipers (PulsightInternalCoreDomainAggregatorCohortStat | Unset):
        supply_known (bool | Unset):
        top10 (float | Unset): % of circulating
        verdict (str | Unset): low|caution|high|critical
    """

    authorities: PulsightInternalCoreDomainAggregatorAuthorityStat | Unset = UNSET
    bundlers: PulsightInternalCoreDomainAggregatorBundlerStat | Unset = UNSET
    dev: PulsightInternalCoreDomainAggregatorDevStat | Unset = UNSET
    holder_count: int | Unset = UNSET
    holders: list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset = UNSET
    insiders: PulsightInternalCoreDomainAggregatorCohortStat | Unset = UNSET
    lp: PulsightInternalCoreDomainAggregatorLpStat | Unset = UNSET
    markets: PulsightInternalCoreDomainAggregatorMarketStat | Unset = UNSET
    mint: str | Unset = UNSET
    risks: list[PulsightInternalCoreDomainAggregatorRiskItem] | Unset = UNSET
    rugged: bool | Unset = UNSET
    score: int | Unset = UNSET
    score_normalised: int | Unset = UNSET
    snipers: PulsightInternalCoreDomainAggregatorCohortStat | Unset = UNSET
    supply_known: bool | Unset = UNSET
    top10: float | Unset = UNSET
    verdict: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = self.authorities.to_dict()

        bundlers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bundlers, Unset):
            bundlers = self.bundlers.to_dict()

        dev: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev, Unset):
            dev = self.dev.to_dict()

        holder_count = self.holder_count

        holders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.holders, Unset):
            holders = []
            for holders_item_data in self.holders:
                holders_item = holders_item_data.to_dict()
                holders.append(holders_item)

        insiders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insiders, Unset):
            insiders = self.insiders.to_dict()

        lp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lp, Unset):
            lp = self.lp.to_dict()

        markets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.markets, Unset):
            markets = self.markets.to_dict()

        mint = self.mint

        risks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.risks, Unset):
            risks = []
            for risks_item_data in self.risks:
                risks_item = risks_item_data.to_dict()
                risks.append(risks_item)

        rugged = self.rugged

        score = self.score

        score_normalised = self.score_normalised

        snipers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snipers, Unset):
            snipers = self.snipers.to_dict()

        supply_known = self.supply_known

        top10 = self.top10

        verdict = self.verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if bundlers is not UNSET:
            field_dict["bundlers"] = bundlers
        if dev is not UNSET:
            field_dict["dev"] = dev
        if holder_count is not UNSET:
            field_dict["holder_count"] = holder_count
        if holders is not UNSET:
            field_dict["holders"] = holders
        if insiders is not UNSET:
            field_dict["insiders"] = insiders
        if lp is not UNSET:
            field_dict["lp"] = lp
        if markets is not UNSET:
            field_dict["markets"] = markets
        if mint is not UNSET:
            field_dict["mint"] = mint
        if risks is not UNSET:
            field_dict["risks"] = risks
        if rugged is not UNSET:
            field_dict["rugged"] = rugged
        if score is not UNSET:
            field_dict["score"] = score
        if score_normalised is not UNSET:
            field_dict["score_normalised"] = score_normalised
        if snipers is not UNSET:
            field_dict["snipers"] = snipers
        if supply_known is not UNSET:
            field_dict["supply_known"] = supply_known
        if top10 is not UNSET:
            field_dict["top10"] = top10
        if verdict is not UNSET:
            field_dict["verdict"] = verdict

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_authority_stat import (
            PulsightInternalCoreDomainAggregatorAuthorityStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_bundler_stat import (
            PulsightInternalCoreDomainAggregatorBundlerStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_cohort_stat import (
            PulsightInternalCoreDomainAggregatorCohortStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_dev_stat import (
            PulsightInternalCoreDomainAggregatorDevStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
            PulsightInternalCoreDomainAggregatorHolderEntry,
        )
        from ..models.pulsight_internal_core_domain_aggregator_lp_stat import (
            PulsightInternalCoreDomainAggregatorLpStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_market_stat import (
            PulsightInternalCoreDomainAggregatorMarketStat,
        )
        from ..models.pulsight_internal_core_domain_aggregator_risk_item import (
            PulsightInternalCoreDomainAggregatorRiskItem,
        )

        d = dict(src_dict)
        _authorities = d.pop("authorities", UNSET)
        authorities: PulsightInternalCoreDomainAggregatorAuthorityStat | Unset
        if isinstance(_authorities, Unset):
            authorities = UNSET
        else:
            authorities = PulsightInternalCoreDomainAggregatorAuthorityStat.from_dict(
                _authorities
            )

        _bundlers = d.pop("bundlers", UNSET)
        bundlers: PulsightInternalCoreDomainAggregatorBundlerStat | Unset
        if isinstance(_bundlers, Unset):
            bundlers = UNSET
        else:
            bundlers = PulsightInternalCoreDomainAggregatorBundlerStat.from_dict(
                _bundlers
            )

        _dev = d.pop("dev", UNSET)
        dev: PulsightInternalCoreDomainAggregatorDevStat | Unset
        if isinstance(_dev, Unset):
            dev = UNSET
        else:
            dev = PulsightInternalCoreDomainAggregatorDevStat.from_dict(_dev)

        holder_count = d.pop("holder_count", UNSET)

        _holders = d.pop("holders", UNSET)
        holders: list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset = UNSET
        if _holders is not UNSET:
            holders = []
            for holders_item_data in _holders:
                holders_item = (
                    PulsightInternalCoreDomainAggregatorHolderEntry.from_dict(
                        holders_item_data
                    )
                )

                holders.append(holders_item)

        _insiders = d.pop("insiders", UNSET)
        insiders: PulsightInternalCoreDomainAggregatorCohortStat | Unset
        if isinstance(_insiders, Unset):
            insiders = UNSET
        else:
            insiders = PulsightInternalCoreDomainAggregatorCohortStat.from_dict(
                _insiders
            )

        _lp = d.pop("lp", UNSET)
        lp: PulsightInternalCoreDomainAggregatorLpStat | Unset
        if isinstance(_lp, Unset):
            lp = UNSET
        else:
            lp = PulsightInternalCoreDomainAggregatorLpStat.from_dict(_lp)

        _markets = d.pop("markets", UNSET)
        markets: PulsightInternalCoreDomainAggregatorMarketStat | Unset
        if isinstance(_markets, Unset):
            markets = UNSET
        else:
            markets = PulsightInternalCoreDomainAggregatorMarketStat.from_dict(_markets)

        mint = d.pop("mint", UNSET)

        _risks = d.pop("risks", UNSET)
        risks: list[PulsightInternalCoreDomainAggregatorRiskItem] | Unset = UNSET
        if _risks is not UNSET:
            risks = []
            for risks_item_data in _risks:
                risks_item = PulsightInternalCoreDomainAggregatorRiskItem.from_dict(
                    risks_item_data
                )

                risks.append(risks_item)

        rugged = d.pop("rugged", UNSET)

        score = d.pop("score", UNSET)

        score_normalised = d.pop("score_normalised", UNSET)

        _snipers = d.pop("snipers", UNSET)
        snipers: PulsightInternalCoreDomainAggregatorCohortStat | Unset
        if isinstance(_snipers, Unset):
            snipers = UNSET
        else:
            snipers = PulsightInternalCoreDomainAggregatorCohortStat.from_dict(_snipers)

        supply_known = d.pop("supply_known", UNSET)

        top10 = d.pop("top10", UNSET)

        verdict = d.pop("verdict", UNSET)

        pulsight_internal_core_domain_aggregator_risk_report = cls(
            authorities=authorities,
            bundlers=bundlers,
            dev=dev,
            holder_count=holder_count,
            holders=holders,
            insiders=insiders,
            lp=lp,
            markets=markets,
            mint=mint,
            risks=risks,
            rugged=rugged,
            score=score,
            score_normalised=score_normalised,
            snipers=snipers,
            supply_known=supply_known,
            top10=top10,
            verdict=verdict,
        )

        pulsight_internal_core_domain_aggregator_risk_report.additional_properties = d
        return pulsight_internal_core_domain_aggregator_risk_report

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
