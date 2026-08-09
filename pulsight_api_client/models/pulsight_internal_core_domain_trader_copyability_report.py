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
        delays (list[PulsightInternalCoreDomainTraderCopyDelayPoint] | Unset): Never nil on the wire: an empty curve is
            [], not null.
        execution_summary (PulsightInternalCoreDomainTraderCopyExecutionSummary | Unset):
        round_trip_mints (int | Unset): Positions (mints) that had BOTH a buy and a sell in the window — the
            only ones a round-trip cost can be measured on.
        wallet (str | Unset):
    """

    delays: list[PulsightInternalCoreDomainTraderCopyDelayPoint] | Unset = UNSET
    execution_summary: PulsightInternalCoreDomainTraderCopyExecutionSummary | Unset = (
        UNSET
    )
    round_trip_mints: int | Unset = UNSET
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

        round_trip_mints = self.round_trip_mints

        wallet = self.wallet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delays is not UNSET:
            field_dict["delays"] = delays
        if execution_summary is not UNSET:
            field_dict["execution_summary"] = execution_summary
        if round_trip_mints is not UNSET:
            field_dict["round_trip_mints"] = round_trip_mints
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

        round_trip_mints = d.pop("round_trip_mints", UNSET)

        wallet = d.pop("wallet", UNSET)

        pulsight_internal_core_domain_trader_copyability_report = cls(
            delays=delays,
            execution_summary=execution_summary,
            round_trip_mints=round_trip_mints,
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
