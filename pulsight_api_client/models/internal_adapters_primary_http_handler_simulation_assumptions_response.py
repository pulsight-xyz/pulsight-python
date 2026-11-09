from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="InternalAdaptersPrimaryHttpHandlerSimulationAssumptionsResponse"
)


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerSimulationAssumptionsResponse:
    """
    Attributes:
        simulation_assumptions (list[str] | Unset): SimulationAssumptions is the list every run's
            summary.simulation_assumptions and every preview carry.
    """

    simulation_assumptions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        simulation_assumptions: list[str] | Unset = UNSET
        if not isinstance(self.simulation_assumptions, Unset):
            simulation_assumptions = self.simulation_assumptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if simulation_assumptions is not UNSET:
            field_dict["simulation_assumptions"] = simulation_assumptions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        simulation_assumptions = cast(list[str], d.pop("simulation_assumptions", UNSET))

        internal_adapters_primary_http_handler_simulation_assumptions_response = cls(
            simulation_assumptions=simulation_assumptions,
        )

        internal_adapters_primary_http_handler_simulation_assumptions_response.additional_properties = d
        return internal_adapters_primary_http_handler_simulation_assumptions_response

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
