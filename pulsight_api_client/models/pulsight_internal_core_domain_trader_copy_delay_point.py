from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_copy_execution_at_delay import (
        PulsightInternalCoreDomainTraderCopyExecutionAtDelay,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyDelayPoint")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyDelayPoint:
    """
    Attributes:
        delay_slots (int | Unset):
        edge_retained_pct (float | Unset): Share of the target's edge left after paying the round-trip cost.
            NULL when the target's edge is not positive: you cannot "retain" a
            share of an edge that is not there, and reporting 0% would read as
            "latency destroyed it" when latency was never the problem.
        entry_slippage_bps (float | Unset): Positive is ALWAYS worse for the copier, on both sides: a buy filled
            higher than the target's, a sell filled lower.
        execution (PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset):
        exit_slippage_bps (float | Unset):
        measured_fills (int | Unset):
        round_trip_cost_bps (float | Unset):
        target_edge_bps (float | Unset): The target's own gross round-trip return over the same fills, so the
            comparison below is self-consistent — one price source, one window.
        unmeasurable_fills (int | Unset): Fills with no trade to copy into at this latency.
    """

    delay_slots: int | Unset = UNSET
    edge_retained_pct: float | Unset = UNSET
    entry_slippage_bps: float | Unset = UNSET
    execution: PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset = UNSET
    exit_slippage_bps: float | Unset = UNSET
    measured_fills: int | Unset = UNSET
    round_trip_cost_bps: float | Unset = UNSET
    target_edge_bps: float | Unset = UNSET
    unmeasurable_fills: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_slots = self.delay_slots

        edge_retained_pct = self.edge_retained_pct

        entry_slippage_bps = self.entry_slippage_bps

        execution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution, Unset):
            execution = self.execution.to_dict()

        exit_slippage_bps = self.exit_slippage_bps

        measured_fills = self.measured_fills

        round_trip_cost_bps = self.round_trip_cost_bps

        target_edge_bps = self.target_edge_bps

        unmeasurable_fills = self.unmeasurable_fills

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_slots is not UNSET:
            field_dict["delay_slots"] = delay_slots
        if edge_retained_pct is not UNSET:
            field_dict["edge_retained_pct"] = edge_retained_pct
        if entry_slippage_bps is not UNSET:
            field_dict["entry_slippage_bps"] = entry_slippage_bps
        if execution is not UNSET:
            field_dict["execution"] = execution
        if exit_slippage_bps is not UNSET:
            field_dict["exit_slippage_bps"] = exit_slippage_bps
        if measured_fills is not UNSET:
            field_dict["measured_fills"] = measured_fills
        if round_trip_cost_bps is not UNSET:
            field_dict["round_trip_cost_bps"] = round_trip_cost_bps
        if target_edge_bps is not UNSET:
            field_dict["target_edge_bps"] = target_edge_bps
        if unmeasurable_fills is not UNSET:
            field_dict["unmeasurable_fills"] = unmeasurable_fills

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_trader_copy_execution_at_delay import (
            PulsightInternalCoreDomainTraderCopyExecutionAtDelay,
        )

        d = dict(src_dict)
        delay_slots = d.pop("delay_slots", UNSET)

        edge_retained_pct = d.pop("edge_retained_pct", UNSET)

        entry_slippage_bps = d.pop("entry_slippage_bps", UNSET)

        _execution = d.pop("execution", UNSET)
        execution: PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset
        if isinstance(_execution, Unset):
            execution = UNSET
        else:
            execution = PulsightInternalCoreDomainTraderCopyExecutionAtDelay.from_dict(
                _execution
            )

        exit_slippage_bps = d.pop("exit_slippage_bps", UNSET)

        measured_fills = d.pop("measured_fills", UNSET)

        round_trip_cost_bps = d.pop("round_trip_cost_bps", UNSET)

        target_edge_bps = d.pop("target_edge_bps", UNSET)

        unmeasurable_fills = d.pop("unmeasurable_fills", UNSET)

        pulsight_internal_core_domain_trader_copy_delay_point = cls(
            delay_slots=delay_slots,
            edge_retained_pct=edge_retained_pct,
            entry_slippage_bps=entry_slippage_bps,
            execution=execution,
            exit_slippage_bps=exit_slippage_bps,
            measured_fills=measured_fills,
            round_trip_cost_bps=round_trip_cost_bps,
            target_edge_bps=target_edge_bps,
            unmeasurable_fills=unmeasurable_fills,
        )

        pulsight_internal_core_domain_trader_copy_delay_point.additional_properties = d
        return pulsight_internal_core_domain_trader_copy_delay_point

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
