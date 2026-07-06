from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerServiceLoyaltyRow")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerServiceLoyaltyRow:
    """
    Attributes:
        share_pct (float | Unset):
        swap_count (int | Unset):
        tip_service (str | Unset):
        tip_sum_lamports (int | Unset):
    """

    share_pct: float | Unset = UNSET
    swap_count: int | Unset = UNSET
    tip_service: str | Unset = UNSET
    tip_sum_lamports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_pct = self.share_pct

        swap_count = self.swap_count

        tip_service = self.tip_service

        tip_sum_lamports = self.tip_sum_lamports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_pct is not UNSET:
            field_dict["share_pct"] = share_pct
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if tip_service is not UNSET:
            field_dict["tip_service"] = tip_service
        if tip_sum_lamports is not UNSET:
            field_dict["tip_sum_lamports"] = tip_sum_lamports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        share_pct = d.pop("share_pct", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        tip_service = d.pop("tip_service", UNSET)

        tip_sum_lamports = d.pop("tip_sum_lamports", UNSET)

        internal_adapters_primary_http_handler_service_loyalty_row = cls(
            share_pct=share_pct,
            swap_count=swap_count,
            tip_service=tip_service,
            tip_sum_lamports=tip_sum_lamports,
        )

        internal_adapters_primary_http_handler_service_loyalty_row.additional_properties = d
        return internal_adapters_primary_http_handler_service_loyalty_row

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
