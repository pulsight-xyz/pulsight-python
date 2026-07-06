from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintMarket")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintMarket:
    """
    Attributes:
        dex (str | Unset):
        last_swap_ts (str | Unset):
        pool (str | Unset):
        sol_volume_lamports (int | Unset):
        sol_volume_share (float | Unset):
        swap_count (int | Unset):
    """

    dex: str | Unset = UNSET
    last_swap_ts: str | Unset = UNSET
    pool: str | Unset = UNSET
    sol_volume_lamports: int | Unset = UNSET
    sol_volume_share: float | Unset = UNSET
    swap_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dex = self.dex

        last_swap_ts = self.last_swap_ts

        pool = self.pool

        sol_volume_lamports = self.sol_volume_lamports

        sol_volume_share = self.sol_volume_share

        swap_count = self.swap_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dex is not UNSET:
            field_dict["dex"] = dex
        if last_swap_ts is not UNSET:
            field_dict["last_swap_ts"] = last_swap_ts
        if pool is not UNSET:
            field_dict["pool"] = pool
        if sol_volume_lamports is not UNSET:
            field_dict["sol_volume_lamports"] = sol_volume_lamports
        if sol_volume_share is not UNSET:
            field_dict["sol_volume_share"] = sol_volume_share
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dex = d.pop("dex", UNSET)

        last_swap_ts = d.pop("last_swap_ts", UNSET)

        pool = d.pop("pool", UNSET)

        sol_volume_lamports = d.pop("sol_volume_lamports", UNSET)

        sol_volume_share = d.pop("sol_volume_share", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        pulsight_internal_core_domain_aggregator_mint_market = cls(
            dex=dex,
            last_swap_ts=last_swap_ts,
            pool=pool,
            sol_volume_lamports=sol_volume_lamports,
            sol_volume_share=sol_volume_share,
            swap_count=swap_count,
        )

        pulsight_internal_core_domain_aggregator_mint_market.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_market

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
