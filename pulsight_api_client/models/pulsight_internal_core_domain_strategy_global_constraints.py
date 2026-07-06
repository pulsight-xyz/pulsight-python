from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyGlobalConstraints")


@_attrs_define
class PulsightInternalCoreDomainStrategyGlobalConstraints:
    """
    Attributes:
        max_buy_sol (float | Unset):
        max_buys_per_open_position (int | Unset): MaxBuysPerOpenPosition is the max number of buys (initial open + adds)
            allowed within ONE open position. 0 ⇒ 1 — the historical single-buy-
            per-position behaviour; read it through EffectiveMaxBuysPerOpenPosition.
            Raise it above 1 to enable DCA / pyramiding.
        max_buys_per_token_per_hour (int | Unset):
        max_buys_per_token_per_minute (int | Unset):
        max_position_exposure_sol (float | Unset): MaxPositionExposureSol caps the cumulative cost basis (SOL spent) of
            a
            single open position. 0 ⇒ unlimited. An add that would push the open
            position's exposure over this cap is skipped.
        min_buy_sol (float | Unset):
    """

    max_buy_sol: float | Unset = UNSET
    max_buys_per_open_position: int | Unset = UNSET
    max_buys_per_token_per_hour: int | Unset = UNSET
    max_buys_per_token_per_minute: int | Unset = UNSET
    max_position_exposure_sol: float | Unset = UNSET
    min_buy_sol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_buy_sol = self.max_buy_sol

        max_buys_per_open_position = self.max_buys_per_open_position

        max_buys_per_token_per_hour = self.max_buys_per_token_per_hour

        max_buys_per_token_per_minute = self.max_buys_per_token_per_minute

        max_position_exposure_sol = self.max_position_exposure_sol

        min_buy_sol = self.min_buy_sol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_buy_sol is not UNSET:
            field_dict["max_buy_sol"] = max_buy_sol
        if max_buys_per_open_position is not UNSET:
            field_dict["max_buys_per_open_position"] = max_buys_per_open_position
        if max_buys_per_token_per_hour is not UNSET:
            field_dict["max_buys_per_token_per_hour"] = max_buys_per_token_per_hour
        if max_buys_per_token_per_minute is not UNSET:
            field_dict["max_buys_per_token_per_minute"] = max_buys_per_token_per_minute
        if max_position_exposure_sol is not UNSET:
            field_dict["max_position_exposure_sol"] = max_position_exposure_sol
        if min_buy_sol is not UNSET:
            field_dict["min_buy_sol"] = min_buy_sol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_buy_sol = d.pop("max_buy_sol", UNSET)

        max_buys_per_open_position = d.pop("max_buys_per_open_position", UNSET)

        max_buys_per_token_per_hour = d.pop("max_buys_per_token_per_hour", UNSET)

        max_buys_per_token_per_minute = d.pop("max_buys_per_token_per_minute", UNSET)

        max_position_exposure_sol = d.pop("max_position_exposure_sol", UNSET)

        min_buy_sol = d.pop("min_buy_sol", UNSET)

        pulsight_internal_core_domain_strategy_global_constraints = cls(
            max_buy_sol=max_buy_sol,
            max_buys_per_open_position=max_buys_per_open_position,
            max_buys_per_token_per_hour=max_buys_per_token_per_hour,
            max_buys_per_token_per_minute=max_buys_per_token_per_minute,
            max_position_exposure_sol=max_position_exposure_sol,
            min_buy_sol=min_buy_sol,
        )

        pulsight_internal_core_domain_strategy_global_constraints.additional_properties = d
        return pulsight_internal_core_domain_strategy_global_constraints

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
