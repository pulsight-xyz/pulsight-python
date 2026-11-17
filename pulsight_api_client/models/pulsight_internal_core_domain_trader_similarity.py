from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_trader_similarity_label import (
    PulsightInternalCoreDomainTraderSimilarityLabel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_money_trait_value import (
        PulsightInternalCoreDomainTraderMoneyTraitValue,
    )
    from ..models.pulsight_internal_core_domain_trader_tags_trait import (
        PulsightInternalCoreDomainTraderTagsTrait,
    )
    from ..models.pulsight_internal_core_domain_trader_trades_per_token_trait import (
        PulsightInternalCoreDomainTraderTradesPerTokenTrait,
    )
    from ..models.pulsight_internal_core_domain_trader_trait_value import (
        PulsightInternalCoreDomainTraderTraitValue,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderSimilarity")


@_attrs_define
class PulsightInternalCoreDomainTraderSimilarity:
    """
    Attributes:
        buy_size (PulsightInternalCoreDomainTraderMoneyTraitValue | Unset):
        label (PulsightInternalCoreDomainTraderSimilarityLabel | Unset):
        median_hold_secs (PulsightInternalCoreDomainTraderTraitValue | Unset):
        score (int | Unset): Score is the similarity, 0–100, and the page's sort value rounded; null
            when fewer than three traits are measured on both wallets.
        tags (PulsightInternalCoreDomainTraderTagsTrait | Unset):
        tokens_traded (PulsightInternalCoreDomainTraderTraitValue | Unset):
        trades_per_token (PulsightInternalCoreDomainTraderTradesPerTokenTrait | Unset):
        traits_total (int | Unset): TraitsTotal counts the traits the window carries: 6, or 5 at lifetime,
            which has no token count.
        traits_used (int | Unset): TraitsUsed counts the traits measured on both wallets.
        volume (float | Unset): Volume is the window's bought plus sold value in lamports, with its USD
            twin (micro-USD). It is shown beside the score, never part of it.
        volume_usd (float | Unset):
        window (str | Unset): Window is the window the windowed traits are read at (the page's).
        winrate (PulsightInternalCoreDomainTraderTraitValue | Unset):
    """

    buy_size: PulsightInternalCoreDomainTraderMoneyTraitValue | Unset = UNSET
    label: PulsightInternalCoreDomainTraderSimilarityLabel | Unset = UNSET
    median_hold_secs: PulsightInternalCoreDomainTraderTraitValue | Unset = UNSET
    score: int | Unset = UNSET
    tags: PulsightInternalCoreDomainTraderTagsTrait | Unset = UNSET
    tokens_traded: PulsightInternalCoreDomainTraderTraitValue | Unset = UNSET
    trades_per_token: PulsightInternalCoreDomainTraderTradesPerTokenTrait | Unset = (
        UNSET
    )
    traits_total: int | Unset = UNSET
    traits_used: int | Unset = UNSET
    volume: float | Unset = UNSET
    volume_usd: float | Unset = UNSET
    window: str | Unset = UNSET
    winrate: PulsightInternalCoreDomainTraderTraitValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_size, Unset):
            buy_size = self.buy_size.to_dict()

        label: str | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.value

        median_hold_secs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.median_hold_secs, Unset):
            median_hold_secs = self.median_hold_secs.to_dict()

        score = self.score

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        tokens_traded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tokens_traded, Unset):
            tokens_traded = self.tokens_traded.to_dict()

        trades_per_token: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trades_per_token, Unset):
            trades_per_token = self.trades_per_token.to_dict()

        traits_total = self.traits_total

        traits_used = self.traits_used

        volume = self.volume

        volume_usd = self.volume_usd

        window = self.window

        winrate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.winrate, Unset):
            winrate = self.winrate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_size is not UNSET:
            field_dict["buy_size"] = buy_size
        if label is not UNSET:
            field_dict["label"] = label
        if median_hold_secs is not UNSET:
            field_dict["median_hold_secs"] = median_hold_secs
        if score is not UNSET:
            field_dict["score"] = score
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tokens_traded is not UNSET:
            field_dict["tokens_traded"] = tokens_traded
        if trades_per_token is not UNSET:
            field_dict["trades_per_token"] = trades_per_token
        if traits_total is not UNSET:
            field_dict["traits_total"] = traits_total
        if traits_used is not UNSET:
            field_dict["traits_used"] = traits_used
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_usd is not UNSET:
            field_dict["volume_usd"] = volume_usd
        if window is not UNSET:
            field_dict["window"] = window
        if winrate is not UNSET:
            field_dict["winrate"] = winrate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_trader_money_trait_value import (
            PulsightInternalCoreDomainTraderMoneyTraitValue,
        )
        from ..models.pulsight_internal_core_domain_trader_tags_trait import (
            PulsightInternalCoreDomainTraderTagsTrait,
        )
        from ..models.pulsight_internal_core_domain_trader_trades_per_token_trait import (
            PulsightInternalCoreDomainTraderTradesPerTokenTrait,
        )
        from ..models.pulsight_internal_core_domain_trader_trait_value import (
            PulsightInternalCoreDomainTraderTraitValue,
        )

        d = dict(src_dict)
        _buy_size = d.pop("buy_size", UNSET)
        buy_size: PulsightInternalCoreDomainTraderMoneyTraitValue | Unset
        if isinstance(_buy_size, Unset):
            buy_size = UNSET
        else:
            buy_size = PulsightInternalCoreDomainTraderMoneyTraitValue.from_dict(
                _buy_size
            )

        _label = d.pop("label", UNSET)
        label: PulsightInternalCoreDomainTraderSimilarityLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = PulsightInternalCoreDomainTraderSimilarityLabel(_label)

        _median_hold_secs = d.pop("median_hold_secs", UNSET)
        median_hold_secs: PulsightInternalCoreDomainTraderTraitValue | Unset
        if isinstance(_median_hold_secs, Unset):
            median_hold_secs = UNSET
        else:
            median_hold_secs = PulsightInternalCoreDomainTraderTraitValue.from_dict(
                _median_hold_secs
            )

        score = d.pop("score", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: PulsightInternalCoreDomainTraderTagsTrait | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PulsightInternalCoreDomainTraderTagsTrait.from_dict(_tags)

        _tokens_traded = d.pop("tokens_traded", UNSET)
        tokens_traded: PulsightInternalCoreDomainTraderTraitValue | Unset
        if isinstance(_tokens_traded, Unset):
            tokens_traded = UNSET
        else:
            tokens_traded = PulsightInternalCoreDomainTraderTraitValue.from_dict(
                _tokens_traded
            )

        _trades_per_token = d.pop("trades_per_token", UNSET)
        trades_per_token: PulsightInternalCoreDomainTraderTradesPerTokenTrait | Unset
        if isinstance(_trades_per_token, Unset):
            trades_per_token = UNSET
        else:
            trades_per_token = (
                PulsightInternalCoreDomainTraderTradesPerTokenTrait.from_dict(
                    _trades_per_token
                )
            )

        traits_total = d.pop("traits_total", UNSET)

        traits_used = d.pop("traits_used", UNSET)

        volume = d.pop("volume", UNSET)

        volume_usd = d.pop("volume_usd", UNSET)

        window = d.pop("window", UNSET)

        _winrate = d.pop("winrate", UNSET)
        winrate: PulsightInternalCoreDomainTraderTraitValue | Unset
        if isinstance(_winrate, Unset):
            winrate = UNSET
        else:
            winrate = PulsightInternalCoreDomainTraderTraitValue.from_dict(_winrate)

        pulsight_internal_core_domain_trader_similarity = cls(
            buy_size=buy_size,
            label=label,
            median_hold_secs=median_hold_secs,
            score=score,
            tags=tags,
            tokens_traded=tokens_traded,
            trades_per_token=trades_per_token,
            traits_total=traits_total,
            traits_used=traits_used,
            volume=volume,
            volume_usd=volume_usd,
            window=window,
            winrate=winrate,
        )

        pulsight_internal_core_domain_trader_similarity.additional_properties = d
        return pulsight_internal_core_domain_trader_similarity

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
