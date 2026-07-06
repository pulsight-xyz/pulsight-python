from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_strategy_event_kind import (
    PulsightInternalCoreDomainStrategyEventKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestEventPredicate")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestEventPredicate:
    """
    Attributes:
        event (PulsightInternalCoreDomainStrategyEventKind | Unset):
        negate (bool | Unset):
    """

    event: PulsightInternalCoreDomainStrategyEventKind | Unset = UNSET
    negate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: str | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        negate = self.negate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if negate is not UNSET:
            field_dict["negate"] = negate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: PulsightInternalCoreDomainStrategyEventKind | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = PulsightInternalCoreDomainStrategyEventKind(_event)

        negate = d.pop("negate", UNSET)

        pulsight_internal_core_usecases_backtest_event_predicate = cls(
            event=event,
            negate=negate,
        )

        pulsight_internal_core_usecases_backtest_event_predicate.additional_properties = d
        return pulsight_internal_core_usecases_backtest_event_predicate

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
