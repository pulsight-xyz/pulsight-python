from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_trader_copy_band_point import (
        PulsightInternalCoreDomainTraderCopyBandPoint,
    )
    from ..models.pulsight_internal_core_domain_trader_copy_band_quantiles import (
        PulsightInternalCoreDomainTraderCopyBandQuantiles,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainTraderCopyExecutionAtDelay")


@_attrs_define
class PulsightInternalCoreDomainTraderCopyExecutionAtDelay:
    """
    Attributes:
        bands (list[PulsightInternalCoreDomainTraderCopyBandPoint] | Unset):
        in_block_move_bps (float | Unset): Where the adverse move comes from. `InBlockSharePct` is the share of the
            total move that had already happened by the end of the target's OWN
            block — i.e. from the copy wave the target's trade set off, not from
            latency. Only populated when the ladder includes slot 0.
        in_block_share_pct (float | Unset):
        measured_fills (int | Unset):
        required (PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset):
        required_follow_on (PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset):
        required_signal_buy (PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset):
        total_move_bps (float | Unset):
        unmeasurable_fills (int | Unset):
    """

    bands: list[PulsightInternalCoreDomainTraderCopyBandPoint] | Unset = UNSET
    in_block_move_bps: float | Unset = UNSET
    in_block_share_pct: float | Unset = UNSET
    measured_fills: int | Unset = UNSET
    required: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset = UNSET
    required_follow_on: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset = (
        UNSET
    )
    required_signal_buy: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset = (
        UNSET
    )
    total_move_bps: float | Unset = UNSET
    unmeasurable_fills: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = []
            for bands_item_data in self.bands:
                bands_item = bands_item_data.to_dict()
                bands.append(bands_item)

        in_block_move_bps = self.in_block_move_bps

        in_block_share_pct = self.in_block_share_pct

        measured_fills = self.measured_fills

        required: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required.to_dict()

        required_follow_on: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_follow_on, Unset):
            required_follow_on = self.required_follow_on.to_dict()

        required_signal_buy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_signal_buy, Unset):
            required_signal_buy = self.required_signal_buy.to_dict()

        total_move_bps = self.total_move_bps

        unmeasurable_fills = self.unmeasurable_fills

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bands is not UNSET:
            field_dict["bands"] = bands
        if in_block_move_bps is not UNSET:
            field_dict["in_block_move_bps"] = in_block_move_bps
        if in_block_share_pct is not UNSET:
            field_dict["in_block_share_pct"] = in_block_share_pct
        if measured_fills is not UNSET:
            field_dict["measured_fills"] = measured_fills
        if required is not UNSET:
            field_dict["required"] = required
        if required_follow_on is not UNSET:
            field_dict["required_follow_on"] = required_follow_on
        if required_signal_buy is not UNSET:
            field_dict["required_signal_buy"] = required_signal_buy
        if total_move_bps is not UNSET:
            field_dict["total_move_bps"] = total_move_bps
        if unmeasurable_fills is not UNSET:
            field_dict["unmeasurable_fills"] = unmeasurable_fills

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_trader_copy_band_point import (
            PulsightInternalCoreDomainTraderCopyBandPoint,
        )
        from ..models.pulsight_internal_core_domain_trader_copy_band_quantiles import (
            PulsightInternalCoreDomainTraderCopyBandQuantiles,
        )

        d = dict(src_dict)
        _bands = d.pop("bands", UNSET)
        bands: list[PulsightInternalCoreDomainTraderCopyBandPoint] | Unset = UNSET
        if _bands is not UNSET:
            bands = []
            for bands_item_data in _bands:
                bands_item = PulsightInternalCoreDomainTraderCopyBandPoint.from_dict(
                    bands_item_data
                )

                bands.append(bands_item)

        in_block_move_bps = d.pop("in_block_move_bps", UNSET)

        in_block_share_pct = d.pop("in_block_share_pct", UNSET)

        measured_fills = d.pop("measured_fills", UNSET)

        _required = d.pop("required", UNSET)
        required: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset
        if isinstance(_required, Unset):
            required = UNSET
        else:
            required = PulsightInternalCoreDomainTraderCopyBandQuantiles.from_dict(
                _required
            )

        _required_follow_on = d.pop("required_follow_on", UNSET)
        required_follow_on: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset
        if isinstance(_required_follow_on, Unset):
            required_follow_on = UNSET
        else:
            required_follow_on = (
                PulsightInternalCoreDomainTraderCopyBandQuantiles.from_dict(
                    _required_follow_on
                )
            )

        _required_signal_buy = d.pop("required_signal_buy", UNSET)
        required_signal_buy: PulsightInternalCoreDomainTraderCopyBandQuantiles | Unset
        if isinstance(_required_signal_buy, Unset):
            required_signal_buy = UNSET
        else:
            required_signal_buy = (
                PulsightInternalCoreDomainTraderCopyBandQuantiles.from_dict(
                    _required_signal_buy
                )
            )

        total_move_bps = d.pop("total_move_bps", UNSET)

        unmeasurable_fills = d.pop("unmeasurable_fills", UNSET)

        pulsight_internal_core_domain_trader_copy_execution_at_delay = cls(
            bands=bands,
            in_block_move_bps=in_block_move_bps,
            in_block_share_pct=in_block_share_pct,
            measured_fills=measured_fills,
            required=required,
            required_follow_on=required_follow_on,
            required_signal_buy=required_signal_buy,
            total_move_bps=total_move_bps,
            unmeasurable_fills=unmeasurable_fills,
        )

        pulsight_internal_core_domain_trader_copy_execution_at_delay.additional_properties = d
        return pulsight_internal_core_domain_trader_copy_execution_at_delay

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
