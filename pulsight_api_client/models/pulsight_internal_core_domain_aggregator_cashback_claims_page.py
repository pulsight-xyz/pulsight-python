from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_cashback_claim_row import (
        PulsightInternalCoreDomainAggregatorCashbackClaimRow,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCashbackClaimsPage")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCashbackClaimsPage:
    """
    Attributes:
        items (list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset):
        limit (int | Unset):
        offset (int | Unset):
        pubkey (str | Unset):
        total (int | Unset):
    """

    items: list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    pubkey: str | Unset = UNSET
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

        pubkey = self.pubkey

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
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_cashback_claim_row import (
            PulsightInternalCoreDomainAggregatorCashbackClaimRow,
        )

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[PulsightInternalCoreDomainAggregatorCashbackClaimRow] | Unset = (
            UNSET
        )
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = (
                    PulsightInternalCoreDomainAggregatorCashbackClaimRow.from_dict(
                        items_item_data
                    )
                )

                items.append(items_item)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        total = d.pop("total", UNSET)

        pulsight_internal_core_domain_aggregator_cashback_claims_page = cls(
            items=items,
            limit=limit,
            offset=offset,
            pubkey=pubkey,
            total=total,
        )

        pulsight_internal_core_domain_aggregator_cashback_claims_page.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cashback_claims_page

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
