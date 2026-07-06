from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_usecases_trader_trader_list_item import (
        PulsightInternalCoreUsecasesTraderTraderListItem,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderTraderListResult")


@_attrs_define
class PulsightInternalCoreUsecasesTraderTraderListResult:
    """
    Attributes:
        items (list[PulsightInternalCoreUsecasesTraderTraderListItem] | Unset):
        limit (int | Unset):
        next_cursor_pubkey (str | Unset):
        next_cursor_value (float | Unset):
        offset (int | Unset):
        total (int | Unset):
    """

    items: list[PulsightInternalCoreUsecasesTraderTraderListItem] | Unset = UNSET
    limit: int | Unset = UNSET
    next_cursor_pubkey: str | Unset = UNSET
    next_cursor_value: float | Unset = UNSET
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

        next_cursor_pubkey = self.next_cursor_pubkey

        next_cursor_value = self.next_cursor_value

        offset = self.offset

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if limit is not UNSET:
            field_dict["limit"] = limit
        if next_cursor_pubkey is not UNSET:
            field_dict["next_cursor_pubkey"] = next_cursor_pubkey
        if next_cursor_value is not UNSET:
            field_dict["next_cursor_value"] = next_cursor_value
        if offset is not UNSET:
            field_dict["offset"] = offset
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_usecases_trader_trader_list_item import (
            PulsightInternalCoreUsecasesTraderTraderListItem,
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[PulsightInternalCoreUsecasesTraderTraderListItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = PulsightInternalCoreUsecasesTraderTraderListItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        limit = d.pop("limit", UNSET)

        next_cursor_pubkey = d.pop("next_cursor_pubkey", UNSET)

        next_cursor_value = d.pop("next_cursor_value", UNSET)

        offset = d.pop("offset", UNSET)

        total = d.pop("total", UNSET)

        pulsight_internal_core_usecases_trader_trader_list_result = cls(
            items=items,
            limit=limit,
            next_cursor_pubkey=next_cursor_pubkey,
            next_cursor_value=next_cursor_value,
            offset=offset,
            total=total,
        )

        pulsight_internal_core_usecases_trader_trader_list_result.additional_properties = d
        return pulsight_internal_core_usecases_trader_trader_list_result

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
