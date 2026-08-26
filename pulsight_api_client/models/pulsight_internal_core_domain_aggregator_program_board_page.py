from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_window import (
    PulsightInternalCoreDomainAggregatorWindow,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_program_board_row import (
        PulsightInternalCoreDomainAggregatorProgramBoardRow,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramBoardPage")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramBoardPage:
    """
    Attributes:
        board (str | Unset):
        categories (list[str] | Unset):
        items (list[PulsightInternalCoreDomainAggregatorProgramBoardRow] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        total (int | Unset):
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    board: str | Unset = UNSET
    categories: list[str] | Unset = UNSET
    items: list[PulsightInternalCoreDomainAggregatorProgramBoardRow] | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    total: int | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board = self.board

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        limit = self.limit

        offset = self.offset

        total = self.total

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if board is not UNSET:
            field_dict["board"] = board
        if categories is not UNSET:
            field_dict["categories"] = categories
        if items is not UNSET:
            field_dict["items"] = items
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if total is not UNSET:
            field_dict["total"] = total
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_program_board_row import (
            PulsightInternalCoreDomainAggregatorProgramBoardRow,
        )

        d = dict(src_dict)
        board = d.pop("board", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        _items = d.pop("items", UNSET)
        items: list[PulsightInternalCoreDomainAggregatorProgramBoardRow] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = (
                    PulsightInternalCoreDomainAggregatorProgramBoardRow.from_dict(
                        items_item_data
                    )
                )

                items.append(items_item)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        total = d.pop("total", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_program_board_page = cls(
            board=board,
            categories=categories,
            items=items,
            limit=limit,
            offset=offset,
            total=total,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_program_board_page.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_board_page

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
