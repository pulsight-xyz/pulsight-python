from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_strategy_venue_id import (
    PulsightInternalCoreDomainStrategyVenueID,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
        PulsightInternalCoreDomainStrategyStrategyDef,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerValidateStrategyRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerValidateStrategyRequest:
    """
    Attributes:
        def_ (PulsightInternalCoreDomainStrategyStrategyDef | Unset):
        venue (PulsightInternalCoreDomainStrategyVenueID | Unset):
    """

    def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset = UNSET
    venue: PulsightInternalCoreDomainStrategyVenueID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        def_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.def_, Unset):
            def_ = self.def_.to_dict()

        venue: str | Unset = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if def_ is not UNSET:
            field_dict["def"] = def_
        if venue is not UNSET:
            field_dict["venue"] = venue

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
            PulsightInternalCoreDomainStrategyStrategyDef,
        )

        d = dict(src_dict)
        _def_ = d.pop("def", UNSET)
        def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset
        if isinstance(_def_, Unset):
            def_ = UNSET
        else:
            def_ = PulsightInternalCoreDomainStrategyStrategyDef.from_dict(_def_)

        _venue = d.pop("venue", UNSET)
        venue: PulsightInternalCoreDomainStrategyVenueID | Unset
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = PulsightInternalCoreDomainStrategyVenueID(_venue)

        internal_adapters_primary_http_handler_validate_strategy_request = cls(
            def_=def_,
            venue=venue,
        )

        internal_adapters_primary_http_handler_validate_strategy_request.additional_properties = d
        return internal_adapters_primary_http_handler_validate_strategy_request

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
