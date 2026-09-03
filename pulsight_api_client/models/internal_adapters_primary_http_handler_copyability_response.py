from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_copyability_report import (
        PulsightInternalCoreDomainTraderCopyabilityReport,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerCopyabilityResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerCopyabilityResponse:
    """
    Attributes:
        bands_bps (list[int] | Unset):
        delays_slots (list[int] | Unset):
        from_ts (int | Unset):
        reports (list[PulsightInternalCoreDomainTraderCopyabilityReport] | Unset):
        size_lamports (int | Unset): The mirrored buy size the reports were replayed at, and the slippage
            ladder their execution profile was evaluated on.
        to_ts (int | Unset):
    """

    bands_bps: list[int] | Unset = UNSET
    delays_slots: list[int] | Unset = UNSET
    from_ts: int | Unset = UNSET
    reports: list[PulsightInternalCoreDomainTraderCopyabilityReport] | Unset = UNSET
    size_lamports: int | Unset = UNSET
    to_ts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bands_bps: list[int] | Unset = UNSET
        if not isinstance(self.bands_bps, Unset):
            bands_bps = self.bands_bps

        delays_slots: list[int] | Unset = UNSET
        if not isinstance(self.delays_slots, Unset):
            delays_slots = self.delays_slots

        from_ts = self.from_ts

        reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        size_lamports = self.size_lamports

        to_ts = self.to_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bands_bps is not UNSET:
            field_dict["bands_bps"] = bands_bps
        if delays_slots is not UNSET:
            field_dict["delays_slots"] = delays_slots
        if from_ts is not UNSET:
            field_dict["from_ts"] = from_ts
        if reports is not UNSET:
            field_dict["reports"] = reports
        if size_lamports is not UNSET:
            field_dict["size_lamports"] = size_lamports
        if to_ts is not UNSET:
            field_dict["to_ts"] = to_ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_trader_copyability_report import (
            PulsightInternalCoreDomainTraderCopyabilityReport,
        )

        d = dict(src_dict)
        bands_bps = cast(list[int], d.pop("bands_bps", UNSET))

        delays_slots = cast(list[int], d.pop("delays_slots", UNSET))

        from_ts = d.pop("from_ts", UNSET)

        _reports = d.pop("reports", UNSET)
        reports: list[PulsightInternalCoreDomainTraderCopyabilityReport] | Unset = UNSET
        if _reports is not UNSET:
            reports = []
            for reports_item_data in _reports:
                reports_item = (
                    PulsightInternalCoreDomainTraderCopyabilityReport.from_dict(
                        reports_item_data
                    )
                )

                reports.append(reports_item)

        size_lamports = d.pop("size_lamports", UNSET)

        to_ts = d.pop("to_ts", UNSET)

        internal_adapters_primary_http_handler_copyability_response = cls(
            bands_bps=bands_bps,
            delays_slots=delays_slots,
            from_ts=from_ts,
            reports=reports,
            size_lamports=size_lamports,
            to_ts=to_ts,
        )

        internal_adapters_primary_http_handler_copyability_response.additional_properties = d
        return internal_adapters_primary_http_handler_copyability_response

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
