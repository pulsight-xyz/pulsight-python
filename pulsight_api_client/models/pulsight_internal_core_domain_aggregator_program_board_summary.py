from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_window import (
    PulsightInternalCoreDomainAggregatorWindow,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_program_board_counts import (
        PulsightInternalCoreDomainAggregatorProgramBoardCounts,
    )
    from ..models.pulsight_internal_core_domain_aggregator_program_board_summary_filters import (
        PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramBoardSummary")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramBoardSummary:
    """
    Attributes:
        board (str | Unset):
        counts (PulsightInternalCoreDomainAggregatorProgramBoardCounts | Unset):
        earners (int | Unset):
        failed_total (int | Unset):
        filters (PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters | Unset):
        negative_rev (int | Unset):
        new_today (int | Unset):
        programs_total (int | Unset):
        rank2_volume_lamports (int | Unset): Rank2 volume anchors the table's magnitude-bar axis — the bar scale
            breaks at #2 when #1 is an outlier. Zero below 2 programs.
        revenue_total_lamports (int | Unset):
        txs_total (int | Unset):
        volume_total_lamports (int | Unset):
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    board: str | Unset = UNSET
    counts: PulsightInternalCoreDomainAggregatorProgramBoardCounts | Unset = UNSET
    earners: int | Unset = UNSET
    failed_total: int | Unset = UNSET
    filters: PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters | Unset = (
        UNSET
    )
    negative_rev: int | Unset = UNSET
    new_today: int | Unset = UNSET
    programs_total: int | Unset = UNSET
    rank2_volume_lamports: int | Unset = UNSET
    revenue_total_lamports: int | Unset = UNSET
    txs_total: int | Unset = UNSET
    volume_total_lamports: int | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board = self.board

        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        earners = self.earners

        failed_total = self.failed_total

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        negative_rev = self.negative_rev

        new_today = self.new_today

        programs_total = self.programs_total

        rank2_volume_lamports = self.rank2_volume_lamports

        revenue_total_lamports = self.revenue_total_lamports

        txs_total = self.txs_total

        volume_total_lamports = self.volume_total_lamports

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if board is not UNSET:
            field_dict["board"] = board
        if counts is not UNSET:
            field_dict["counts"] = counts
        if earners is not UNSET:
            field_dict["earners"] = earners
        if failed_total is not UNSET:
            field_dict["failed_total"] = failed_total
        if filters is not UNSET:
            field_dict["filters"] = filters
        if negative_rev is not UNSET:
            field_dict["negative_rev"] = negative_rev
        if new_today is not UNSET:
            field_dict["new_today"] = new_today
        if programs_total is not UNSET:
            field_dict["programs_total"] = programs_total
        if rank2_volume_lamports is not UNSET:
            field_dict["rank2_volume_lamports"] = rank2_volume_lamports
        if revenue_total_lamports is not UNSET:
            field_dict["revenue_total_lamports"] = revenue_total_lamports
        if txs_total is not UNSET:
            field_dict["txs_total"] = txs_total
        if volume_total_lamports is not UNSET:
            field_dict["volume_total_lamports"] = volume_total_lamports
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_program_board_counts import (
            PulsightInternalCoreDomainAggregatorProgramBoardCounts,
        )
        from ..models.pulsight_internal_core_domain_aggregator_program_board_summary_filters import (
            PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters,
        )

        d = dict(src_dict)
        board = d.pop("board", UNSET)

        _counts = d.pop("counts", UNSET)
        counts: PulsightInternalCoreDomainAggregatorProgramBoardCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = PulsightInternalCoreDomainAggregatorProgramBoardCounts.from_dict(
                _counts
            )

        earners = d.pop("earners", UNSET)

        failed_total = d.pop("failed_total", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = PulsightInternalCoreDomainAggregatorProgramBoardSummaryFilters.from_dict(
                _filters
            )

        negative_rev = d.pop("negative_rev", UNSET)

        new_today = d.pop("new_today", UNSET)

        programs_total = d.pop("programs_total", UNSET)

        rank2_volume_lamports = d.pop("rank2_volume_lamports", UNSET)

        revenue_total_lamports = d.pop("revenue_total_lamports", UNSET)

        txs_total = d.pop("txs_total", UNSET)

        volume_total_lamports = d.pop("volume_total_lamports", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_program_board_summary = cls(
            board=board,
            counts=counts,
            earners=earners,
            failed_total=failed_total,
            filters=filters,
            negative_rev=negative_rev,
            new_today=new_today,
            programs_total=programs_total,
            rank2_volume_lamports=rank2_volume_lamports,
            revenue_total_lamports=revenue_total_lamports,
            txs_total=txs_total,
            volume_total_lamports=volume_total_lamports,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_program_board_summary.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_board_summary

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
