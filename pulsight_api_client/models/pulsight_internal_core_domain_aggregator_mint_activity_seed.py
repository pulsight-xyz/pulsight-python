from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_mint_activity_base import (
        PulsightInternalCoreDomainAggregatorMintActivityBase,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_activity_point import (
        PulsightInternalCoreDomainAggregatorMintActivityPoint,
    )
    from ..models.pulsight_internal_core_domain_aggregator_mint_launch_bundle import (
        PulsightInternalCoreDomainAggregatorMintLaunchBundle,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintActivitySeed")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintActivitySeed:
    """
    Attributes:
        base (PulsightInternalCoreDomainAggregatorMintActivityBase | Unset):
        fields (list[str] | Unset): Fields names the opt-in parts the response carries, in the request's
            vocabulary.
        first_trade_ts (int | Unset): FirstTradeTS is the mint's first trade, unix seconds, absent when it
            has none. Served with the `launch` field.
        from_ (int | Unset):
        launch (PulsightInternalCoreDomainAggregatorMintLaunchBundle | Unset):
        mint (str | Unset):
        points (list[PulsightInternalCoreDomainAggregatorMintActivityPoint] | Unset):
        to (int | Unset):
    """

    base: PulsightInternalCoreDomainAggregatorMintActivityBase | Unset = UNSET
    fields: list[str] | Unset = UNSET
    first_trade_ts: int | Unset = UNSET
    from_: int | Unset = UNSET
    launch: PulsightInternalCoreDomainAggregatorMintLaunchBundle | Unset = UNSET
    mint: str | Unset = UNSET
    points: list[PulsightInternalCoreDomainAggregatorMintActivityPoint] | Unset = UNSET
    to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        first_trade_ts = self.first_trade_ts

        from_ = self.from_

        launch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        mint = self.mint

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if fields is not UNSET:
            field_dict["fields"] = fields
        if first_trade_ts is not UNSET:
            field_dict["first_trade_ts"] = first_trade_ts
        if from_ is not UNSET:
            field_dict["from"] = from_
        if launch is not UNSET:
            field_dict["launch"] = launch
        if mint is not UNSET:
            field_dict["mint"] = mint
        if points is not UNSET:
            field_dict["points"] = points
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_mint_activity_base import (
            PulsightInternalCoreDomainAggregatorMintActivityBase,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_activity_point import (
            PulsightInternalCoreDomainAggregatorMintActivityPoint,
        )
        from ..models.pulsight_internal_core_domain_aggregator_mint_launch_bundle import (
            PulsightInternalCoreDomainAggregatorMintLaunchBundle,
        )

        d = dict(src_dict)
        _base = d.pop("base", UNSET)
        base: PulsightInternalCoreDomainAggregatorMintActivityBase | Unset
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = PulsightInternalCoreDomainAggregatorMintActivityBase.from_dict(_base)

        fields = cast(list[str], d.pop("fields", UNSET))

        first_trade_ts = d.pop("first_trade_ts", UNSET)

        from_ = d.pop("from", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: PulsightInternalCoreDomainAggregatorMintLaunchBundle | Unset
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = PulsightInternalCoreDomainAggregatorMintLaunchBundle.from_dict(
                _launch
            )

        mint = d.pop("mint", UNSET)

        _points = d.pop("points", UNSET)
        points: list[PulsightInternalCoreDomainAggregatorMintActivityPoint] | Unset = (
            UNSET
        )
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = (
                    PulsightInternalCoreDomainAggregatorMintActivityPoint.from_dict(
                        points_item_data
                    )
                )

                points.append(points_item)

        to = d.pop("to", UNSET)

        pulsight_internal_core_domain_aggregator_mint_activity_seed = cls(
            base=base,
            fields=fields,
            first_trade_ts=first_trade_ts,
            from_=from_,
            launch=launch,
            mint=mint,
            points=points,
            to=to,
        )

        pulsight_internal_core_domain_aggregator_mint_activity_seed.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_activity_seed

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
