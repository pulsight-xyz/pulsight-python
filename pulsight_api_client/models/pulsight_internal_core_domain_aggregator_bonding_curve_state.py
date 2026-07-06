from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorBondingCurveState")


@_attrs_define
class PulsightInternalCoreDomainAggregatorBondingCurveState:
    """
    Attributes:
        graduated (bool | Unset): True iff mint_migrations carries any graduation row for this mint.
        graduation_target_dex (str | Unset): Destination dex of the graduation; nil when not graduated.
        launchpad (str | Unset): Launchpad slug — pumpfun_amm | raydium_launchpad | meteora_dbc.
        progress_pct (float | Unset): Curve progress 0..=100. nil for Raydium Launchpad / Meteora DBC
            (per-pool config not persisted); always set for PumpFun.
        virtual_sol_lamports (int | Unset): Most recent observed virtual_sol (= dex_swaps.quote_reserves)
            snapshot on the launchpad dex, in lamports. 0 for pre-feature
            graduations with no curve swap on file.
        virtual_token (str | Unset): Most recent observed virtual_token (NUMERIC → decimal string for
            JSON safety). "0" when no curve swap is on file.
    """

    graduated: bool | Unset = UNSET
    graduation_target_dex: str | Unset = UNSET
    launchpad: str | Unset = UNSET
    progress_pct: float | Unset = UNSET
    virtual_sol_lamports: int | Unset = UNSET
    virtual_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graduated = self.graduated

        graduation_target_dex = self.graduation_target_dex

        launchpad = self.launchpad

        progress_pct = self.progress_pct

        virtual_sol_lamports = self.virtual_sol_lamports

        virtual_token = self.virtual_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if graduated is not UNSET:
            field_dict["graduated"] = graduated
        if graduation_target_dex is not UNSET:
            field_dict["graduation_target_dex"] = graduation_target_dex
        if launchpad is not UNSET:
            field_dict["launchpad"] = launchpad
        if progress_pct is not UNSET:
            field_dict["progress_pct"] = progress_pct
        if virtual_sol_lamports is not UNSET:
            field_dict["virtual_sol_lamports"] = virtual_sol_lamports
        if virtual_token is not UNSET:
            field_dict["virtual_token"] = virtual_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        graduated = d.pop("graduated", UNSET)

        graduation_target_dex = d.pop("graduation_target_dex", UNSET)

        launchpad = d.pop("launchpad", UNSET)

        progress_pct = d.pop("progress_pct", UNSET)

        virtual_sol_lamports = d.pop("virtual_sol_lamports", UNSET)

        virtual_token = d.pop("virtual_token", UNSET)

        pulsight_internal_core_domain_aggregator_bonding_curve_state = cls(
            graduated=graduated,
            graduation_target_dex=graduation_target_dex,
            launchpad=launchpad,
            progress_pct=progress_pct,
            virtual_sol_lamports=virtual_sol_lamports,
            virtual_token=virtual_token,
        )

        pulsight_internal_core_domain_aggregator_bonding_curve_state.additional_properties = d
        return pulsight_internal_core_domain_aggregator_bonding_curve_state

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
