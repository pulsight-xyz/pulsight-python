from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_trader_daily_profit_list_item import (
        PulsightInternalCoreUsecasesTraderDailyProfitListItem,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderDailyProfitsResult")


@_attrs_define
class PulsightInternalCoreUsecasesTraderDailyProfitsResult:
    """
    Attributes:
        items (list[PulsightInternalCoreUsecasesTraderDailyProfitListItem] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        total (int | Unset):
    """

    items: list[PulsightInternalCoreUsecasesTraderDailyProfitListItem] | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        limit = self.limit

        offset = self.offset

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_trader_daily_profit_list_item import (
            PulsightInternalCoreUsecasesTraderDailyProfitListItem,
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[PulsightInternalCoreUsecasesTraderDailyProfitListItem] | Unset = (
            UNSET
        )
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = (
                    PulsightInternalCoreUsecasesTraderDailyProfitListItem.from_dict(
                        items_item_data
                    )
                )

                items.append(items_item)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        total = d.pop("total", UNSET)

        pulsight_internal_core_usecases_trader_daily_profits_result = cls(
            items=items,
            limit=limit,
            offset=offset,
            total=total,
        )

        pulsight_internal_core_usecases_trader_daily_profits_result.additional_properties = d
        return pulsight_internal_core_usecases_trader_daily_profits_result

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
