from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_confluence_fire import (
        PulsightInternalCoreDomainStrategyConfluenceFire,
    )
    from ..models.pulsight_internal_core_domain_strategy_same_operator_pair import (
        PulsightInternalCoreDomainStrategySameOperatorPair,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyConfluencePreview")


@_attrs_define
class PulsightInternalCoreDomainStrategyConfluencePreview:
    """
    Attributes:
        capped (bool | Unset): Capped is true when the wallets' trades exceeded what one preview reads; the counts are
            then lower bounds.
        fires (list[PulsightInternalCoreDomainStrategyConfluenceFire] | Unset): Fires lists the 50 most recent of those
            instants, newest first.
        fires_7d (int | Unset): Fires7d counts the instants the condition became true inside the window, across every
            token.
        same_operator (list[PulsightInternalCoreDomainStrategySameOperatorPair] | Unset): SameOperator lists up to 20
            wallet pairs that bought the same tokens within 1 second of each other, highest rate first.
        tokens_7d (int | Unset): Tokens7d counts the tokens on which it became true at least once.
        window_from (int | Unset): WindowFrom is the start of the 7-day window, unix seconds.
        window_to (int | Unset): WindowTo is the end of the window (now), unix seconds.
    """

    capped: bool | Unset = UNSET
    fires: list[PulsightInternalCoreDomainStrategyConfluenceFire] | Unset = UNSET
    fires_7d: int | Unset = UNSET
    same_operator: list[PulsightInternalCoreDomainStrategySameOperatorPair] | Unset = (
        UNSET
    )
    tokens_7d: int | Unset = UNSET
    window_from: int | Unset = UNSET
    window_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capped = self.capped

        fires: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fires, Unset):
            fires = []
            for fires_item_data in self.fires:
                fires_item = fires_item_data.to_dict()
                fires.append(fires_item)

        fires_7d = self.fires_7d

        same_operator: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.same_operator, Unset):
            same_operator = []
            for same_operator_item_data in self.same_operator:
                same_operator_item = same_operator_item_data.to_dict()
                same_operator.append(same_operator_item)

        tokens_7d = self.tokens_7d

        window_from = self.window_from

        window_to = self.window_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capped is not UNSET:
            field_dict["capped"] = capped
        if fires is not UNSET:
            field_dict["fires"] = fires
        if fires_7d is not UNSET:
            field_dict["fires_7d"] = fires_7d
        if same_operator is not UNSET:
            field_dict["same_operator"] = same_operator
        if tokens_7d is not UNSET:
            field_dict["tokens_7d"] = tokens_7d
        if window_from is not UNSET:
            field_dict["window_from"] = window_from
        if window_to is not UNSET:
            field_dict["window_to"] = window_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_strategy_confluence_fire import (
            PulsightInternalCoreDomainStrategyConfluenceFire,
        )
        from ..models.pulsight_internal_core_domain_strategy_same_operator_pair import (
            PulsightInternalCoreDomainStrategySameOperatorPair,
        )

        d = dict(src_dict)
        capped = d.pop("capped", UNSET)

        _fires = d.pop("fires", UNSET)
        fires: list[PulsightInternalCoreDomainStrategyConfluenceFire] | Unset = UNSET
        if _fires is not UNSET:
            fires = []
            for fires_item_data in _fires:
                fires_item = PulsightInternalCoreDomainStrategyConfluenceFire.from_dict(
                    fires_item_data
                )

                fires.append(fires_item)

        fires_7d = d.pop("fires_7d", UNSET)

        _same_operator = d.pop("same_operator", UNSET)
        same_operator: (
            list[PulsightInternalCoreDomainStrategySameOperatorPair] | Unset
        ) = UNSET
        if _same_operator is not UNSET:
            same_operator = []
            for same_operator_item_data in _same_operator:
                same_operator_item = (
                    PulsightInternalCoreDomainStrategySameOperatorPair.from_dict(
                        same_operator_item_data
                    )
                )

                same_operator.append(same_operator_item)

        tokens_7d = d.pop("tokens_7d", UNSET)

        window_from = d.pop("window_from", UNSET)

        window_to = d.pop("window_to", UNSET)

        pulsight_internal_core_domain_strategy_confluence_preview = cls(
            capped=capped,
            fires=fires,
            fires_7d=fires_7d,
            same_operator=same_operator,
            tokens_7d=tokens_7d,
            window_from=window_from,
            window_to=window_to,
        )

        pulsight_internal_core_domain_strategy_confluence_preview.additional_properties = d
        return pulsight_internal_core_domain_strategy_confluence_preview

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
