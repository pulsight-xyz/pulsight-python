from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_strategy_stats import (
        InternalAdaptersPrimaryHttpHandlerStrategyStats,
    )
    from ..models.pulsight_internal_core_domain_strategy_record import (
        PulsightInternalCoreDomainStrategyRecord,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerStrategyListItem")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerStrategyListItem:
    """
    Attributes:
        record (PulsightInternalCoreDomainStrategyRecord | Unset):
        stats (InternalAdaptersPrimaryHttpHandlerStrategyStats | Unset):
    """

    record: PulsightInternalCoreDomainStrategyRecord | Unset = UNSET
    stats: InternalAdaptersPrimaryHttpHandlerStrategyStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record is not UNSET:
            field_dict["record"] = record
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_adapters_primary_http_handler_strategy_stats import (
            InternalAdaptersPrimaryHttpHandlerStrategyStats,
        )
        from ..models.pulsight_internal_core_domain_strategy_record import (
            PulsightInternalCoreDomainStrategyRecord,
        )

        d = dict(src_dict)
        _record = d.pop("record", UNSET)
        record: PulsightInternalCoreDomainStrategyRecord | Unset
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = PulsightInternalCoreDomainStrategyRecord.from_dict(_record)

        _stats = d.pop("stats", UNSET)
        stats: InternalAdaptersPrimaryHttpHandlerStrategyStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = InternalAdaptersPrimaryHttpHandlerStrategyStats.from_dict(_stats)

        internal_adapters_primary_http_handler_strategy_list_item = cls(
            record=record,
            stats=stats,
        )

        internal_adapters_primary_http_handler_strategy_list_item.additional_properties = d
        return internal_adapters_primary_http_handler_strategy_list_item

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
