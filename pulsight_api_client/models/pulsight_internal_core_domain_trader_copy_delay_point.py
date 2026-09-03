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
        deployed_lamports (int | Unset): The copier's outcome at the requested size: one order of size_lamports
            mirrored on each of the wallet's buys, every sell mirrored in proportion,
            unsold tokens valued at the pool's last price in the window.
        entry_cost_bps (float | Unset): What copying costs, in order: buying after the wallet at the copier's
            size, selling after it, and transaction fees plus tips on every
            mirrored transaction.
        entry_slippage_bps (float | Unset): Price drift alone, independent of size: the pool's worst price in the
            landing block against the price the wallet's own trade left, averaged
            over positions. Positive is always worse for the copier.
        execution (PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset):
        exit_cost_bps (float | Unset):
        exit_slippage_bps (float | Unset):
        fees_bps (float | Unset):
        measured_fills (int | Unset):
        pnl_lamports (int | Unset):
        positions (int | Unset): Positions the replay could price at this latency, and how they ended
            for the copier after fees.
        positions_lost (int | Unset):
        positions_won (int | Unset):
        return_bps (float | Unset):
        target_return_bps (float | Unset): What the wallet itself made on the same positions, at its own fills.
        unmeasurable_fills (int | Unset): Swap legs with and without a pool state to execute into.
    """

    delay_slots: int | Unset = UNSET
    deployed_lamports: int | Unset = UNSET
    entry_cost_bps: float | Unset = UNSET
    entry_slippage_bps: float | Unset = UNSET
    execution: PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset = UNSET
    exit_cost_bps: float | Unset = UNSET
    exit_slippage_bps: float | Unset = UNSET
    fees_bps: float | Unset = UNSET
    measured_fills: int | Unset = UNSET
    pnl_lamports: int | Unset = UNSET
    positions: int | Unset = UNSET
    positions_lost: int | Unset = UNSET
    positions_won: int | Unset = UNSET
    return_bps: float | Unset = UNSET
    target_return_bps: float | Unset = UNSET
    unmeasurable_fills: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_slots = self.delay_slots

        deployed_lamports = self.deployed_lamports

        entry_cost_bps = self.entry_cost_bps

        entry_slippage_bps = self.entry_slippage_bps

        execution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution, Unset):
            execution = self.execution.to_dict()

        exit_cost_bps = self.exit_cost_bps

        exit_slippage_bps = self.exit_slippage_bps

        fees_bps = self.fees_bps

        measured_fills = self.measured_fills

        pnl_lamports = self.pnl_lamports

        positions = self.positions

        positions_lost = self.positions_lost

        positions_won = self.positions_won

        return_bps = self.return_bps

        target_return_bps = self.target_return_bps

        unmeasurable_fills = self.unmeasurable_fills

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay_slots is not UNSET:
            field_dict["delay_slots"] = delay_slots
        if deployed_lamports is not UNSET:
            field_dict["deployed_lamports"] = deployed_lamports
        if entry_cost_bps is not UNSET:
            field_dict["entry_cost_bps"] = entry_cost_bps
        if entry_slippage_bps is not UNSET:
            field_dict["entry_slippage_bps"] = entry_slippage_bps
        if execution is not UNSET:
            field_dict["execution"] = execution
        if exit_cost_bps is not UNSET:
            field_dict["exit_cost_bps"] = exit_cost_bps
        if exit_slippage_bps is not UNSET:
            field_dict["exit_slippage_bps"] = exit_slippage_bps
        if fees_bps is not UNSET:
            field_dict["fees_bps"] = fees_bps
        if measured_fills is not UNSET:
            field_dict["measured_fills"] = measured_fills
        if pnl_lamports is not UNSET:
            field_dict["pnl_lamports"] = pnl_lamports
        if positions is not UNSET:
            field_dict["positions"] = positions
        if positions_lost is not UNSET:
            field_dict["positions_lost"] = positions_lost
        if positions_won is not UNSET:
            field_dict["positions_won"] = positions_won
        if return_bps is not UNSET:
            field_dict["return_bps"] = return_bps
        if target_return_bps is not UNSET:
            field_dict["target_return_bps"] = target_return_bps
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

        deployed_lamports = d.pop("deployed_lamports", UNSET)

        entry_cost_bps = d.pop("entry_cost_bps", UNSET)

        entry_slippage_bps = d.pop("entry_slippage_bps", UNSET)

        _execution = d.pop("execution", UNSET)
        execution: PulsightInternalCoreDomainTraderCopyExecutionAtDelay | Unset
        if isinstance(_execution, Unset):
            execution = UNSET
        else:
            execution = PulsightInternalCoreDomainTraderCopyExecutionAtDelay.from_dict(
                _execution
            )

        exit_cost_bps = d.pop("exit_cost_bps", UNSET)

        exit_slippage_bps = d.pop("exit_slippage_bps", UNSET)

        fees_bps = d.pop("fees_bps", UNSET)

        measured_fills = d.pop("measured_fills", UNSET)

        pnl_lamports = d.pop("pnl_lamports", UNSET)

        positions = d.pop("positions", UNSET)

        positions_lost = d.pop("positions_lost", UNSET)

        positions_won = d.pop("positions_won", UNSET)

        return_bps = d.pop("return_bps", UNSET)

        target_return_bps = d.pop("target_return_bps", UNSET)

        unmeasurable_fills = d.pop("unmeasurable_fills", UNSET)

        pulsight_internal_core_domain_trader_copy_delay_point = cls(
            delay_slots=delay_slots,
            deployed_lamports=deployed_lamports,
            entry_cost_bps=entry_cost_bps,
            entry_slippage_bps=entry_slippage_bps,
            execution=execution,
            exit_cost_bps=exit_cost_bps,
            exit_slippage_bps=exit_slippage_bps,
            fees_bps=fees_bps,
            measured_fills=measured_fills,
            pnl_lamports=pnl_lamports,
            positions=positions,
            positions_lost=positions_lost,
            positions_won=positions_won,
            return_bps=return_bps,
            target_return_bps=target_return_bps,
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
