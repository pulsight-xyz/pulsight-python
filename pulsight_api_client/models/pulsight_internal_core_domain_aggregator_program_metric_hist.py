from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorProgramMetricHist")


@_attrs_define
class PulsightInternalCoreDomainAggregatorProgramMetricHist:
    """
    Attributes:
        bins (list[int] | Unset):
        hi (float | Unset):
        lo (float | Unset):
        log (bool | Unset):
    """

    bins: list[int] | Unset = UNSET
    hi: float | Unset = UNSET
    lo: float | Unset = UNSET
    log: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bins: list[int] | Unset = UNSET
        if not isinstance(self.bins, Unset):
            bins = self.bins

        hi = self.hi

        lo = self.lo

        log = self.log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bins is not UNSET:
            field_dict["bins"] = bins
        if hi is not UNSET:
            field_dict["hi"] = hi
        if lo is not UNSET:
            field_dict["lo"] = lo
        if log is not UNSET:
            field_dict["log"] = log

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bins = cast(list[int], d.pop("bins", UNSET))

        hi = d.pop("hi", UNSET)

        lo = d.pop("lo", UNSET)

        log = d.pop("log", UNSET)

        pulsight_internal_core_domain_aggregator_program_metric_hist = cls(
            bins=bins,
            hi=hi,
            lo=lo,
            log=log,
        )

        pulsight_internal_core_domain_aggregator_program_metric_hist.additional_properties = d
        return pulsight_internal_core_domain_aggregator_program_metric_hist

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
