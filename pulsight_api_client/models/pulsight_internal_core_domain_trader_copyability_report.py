from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_copy_delay_point import (
        PulsightInternalCoreDomainTraderCopyDelayPoint,
    )
    from ..models.pulsight_internal_core_domain_trader_copy_execution_summary import (
        PulsightInternalCoreDomainTraderCopyExecutionSummary,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyabilityReport")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyabilityReport:
    """
    Attributes:
        delays (list[PulsightInternalCoreDomainTraderCopyDelayPoint] | Unset): Never nil on the wire: an empty ladder is
            [], not null.
        execution_summary (PulsightInternalCoreDomainTraderCopyExecutionSummary | Unset):
        fee_per_tx_lamports (int | Unset): The wallet's median transaction fee plus tip, lamports, charged to the
            copier on every mirrored transaction.
        positions (int | Unset): Positions the wallet opened in the window that the replay sampled: the
            most recent ones, bounded per wallet.
        positions_closed (int | Unset): Positions the wallet had sold in full by the end of the window; the
            rest are valued at the last price seen.
        round_trip_mints (int | Unset): Positions with at least one sell in the window.
        sample_from_ts (int | Unset): Earliest position open in the sample, Unix seconds; 0 when nothing was
            sampled.
        size_lamports (int | Unset): Size of each mirrored buy, lamports.
        txs_per_position (float | Unset): Mean number of transactions, buys plus sells, per sampled position.
        wallet (str | Unset):
    """

    delays: list[PulsightInternalCoreDomainTraderCopyDelayPoint] | Unset = UNSET
    execution_summary: PulsightInternalCoreDomainTraderCopyExecutionSummary | Unset = (
        UNSET
    )
    fee_per_tx_lamports: int | Unset = UNSET
    positions: int | Unset = UNSET
    positions_closed: int | Unset = UNSET
    round_trip_mints: int | Unset = UNSET
    sample_from_ts: int | Unset = UNSET
    size_lamports: int | Unset = UNSET
    txs_per_position: float | Unset = UNSET
    wallet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delays: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delays, Unset):
            delays = []
            for delays_item_data in self.delays:
                delays_item = delays_item_data.to_dict()
                delays.append(delays_item)

        execution_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_summary, Unset):
            execution_summary = self.execution_summary.to_dict()

        fee_per_tx_lamports = self.fee_per_tx_lamports

        positions = self.positions

        positions_closed = self.positions_closed

        round_trip_mints = self.round_trip_mints

        sample_from_ts = self.sample_from_ts

        size_lamports = self.size_lamports

        txs_per_position = self.txs_per_position

        wallet = self.wallet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delays is not UNSET:
            field_dict["delays"] = delays
        if execution_summary is not UNSET:
            field_dict["execution_summary"] = execution_summary
        if fee_per_tx_lamports is not UNSET:
            field_dict["fee_per_tx_lamports"] = fee_per_tx_lamports
        if positions is not UNSET:
            field_dict["positions"] = positions
        if positions_closed is not UNSET:
            field_dict["positions_closed"] = positions_closed
        if round_trip_mints is not UNSET:
            field_dict["round_trip_mints"] = round_trip_mints
        if sample_from_ts is not UNSET:
            field_dict["sample_from_ts"] = sample_from_ts
        if size_lamports is not UNSET:
            field_dict["size_lamports"] = size_lamports
        if txs_per_position is not UNSET:
            field_dict["txs_per_position"] = txs_per_position
        if wallet is not UNSET:
            field_dict["wallet"] = wallet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_trader_copy_delay_point import (
            PulsightInternalCoreDomainTraderCopyDelayPoint,
        )
        from ..models.pulsight_internal_core_domain_trader_copy_execution_summary import (
            PulsightInternalCoreDomainTraderCopyExecutionSummary,
        )

        d = dict(src_dict)
        _delays = d.pop("delays", UNSET)
        delays: list[PulsightInternalCoreDomainTraderCopyDelayPoint] | Unset = UNSET
        if _delays is not UNSET:
            delays = []
            for delays_item_data in _delays:
                delays_item = PulsightInternalCoreDomainTraderCopyDelayPoint.from_dict(
                    delays_item_data
                )

                delays.append(delays_item)

        _execution_summary = d.pop("execution_summary", UNSET)
        execution_summary: PulsightInternalCoreDomainTraderCopyExecutionSummary | Unset
        if isinstance(_execution_summary, Unset):
            execution_summary = UNSET
        else:
            execution_summary = (
                PulsightInternalCoreDomainTraderCopyExecutionSummary.from_dict(
                    _execution_summary
                )
            )

        fee_per_tx_lamports = d.pop("fee_per_tx_lamports", UNSET)

        positions = d.pop("positions", UNSET)

        positions_closed = d.pop("positions_closed", UNSET)

        round_trip_mints = d.pop("round_trip_mints", UNSET)

        sample_from_ts = d.pop("sample_from_ts", UNSET)

        size_lamports = d.pop("size_lamports", UNSET)

        txs_per_position = d.pop("txs_per_position", UNSET)

        wallet = d.pop("wallet", UNSET)

        pulsight_internal_core_domain_trader_copyability_report = cls(
            delays=delays,
            execution_summary=execution_summary,
            fee_per_tx_lamports=fee_per_tx_lamports,
            positions=positions,
            positions_closed=positions_closed,
            round_trip_mints=round_trip_mints,
            sample_from_ts=sample_from_ts,
            size_lamports=size_lamports,
            txs_per_position=txs_per_position,
            wallet=wallet,
        )

        pulsight_internal_core_domain_trader_copyability_report.additional_properties = d
        return pulsight_internal_core_domain_trader_copyability_report

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
