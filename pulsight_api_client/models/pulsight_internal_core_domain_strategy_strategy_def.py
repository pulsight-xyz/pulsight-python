from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_global_constraints import (
        PulsightInternalCoreDomainStrategyGlobalConstraints,
    )
    from ..models.pulsight_internal_core_domain_strategy_sub_graph import (
        PulsightInternalCoreDomainStrategySubGraph,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyStrategyDef")


@_attrs_define
class PulsightInternalCoreDomainStrategyStrategyDef:
    """
    Attributes:
        constraints (PulsightInternalCoreDomainStrategyGlobalConstraints | Unset):
        entry (PulsightInternalCoreDomainStrategySubGraph | Unset):
        exit_ (PulsightInternalCoreDomainStrategySubGraph | Unset):
    """

    constraints: PulsightInternalCoreDomainStrategyGlobalConstraints | Unset = UNSET
    entry: PulsightInternalCoreDomainStrategySubGraph | Unset = UNSET
    exit_: PulsightInternalCoreDomainStrategySubGraph | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constraints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = self.constraints.to_dict()

        entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        exit_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_, Unset):
            exit_ = self.exit_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if entry is not UNSET:
            field_dict["entry"] = entry
        if exit_ is not UNSET:
            field_dict["exit"] = exit_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_global_constraints import (
            PulsightInternalCoreDomainStrategyGlobalConstraints,
        )
        from ..models.pulsight_internal_core_domain_strategy_sub_graph import (
            PulsightInternalCoreDomainStrategySubGraph,
        )

        d = dict(src_dict)
        _constraints = d.pop("constraints", UNSET)
        constraints: PulsightInternalCoreDomainStrategyGlobalConstraints | Unset
        if isinstance(_constraints, Unset):
            constraints = UNSET
        else:
            constraints = PulsightInternalCoreDomainStrategyGlobalConstraints.from_dict(
                _constraints
            )

        _entry = d.pop("entry", UNSET)
        entry: PulsightInternalCoreDomainStrategySubGraph | Unset
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = PulsightInternalCoreDomainStrategySubGraph.from_dict(_entry)

        _exit_ = d.pop("exit", UNSET)
        exit_: PulsightInternalCoreDomainStrategySubGraph | Unset
        if isinstance(_exit_, Unset):
            exit_ = UNSET
        else:
            exit_ = PulsightInternalCoreDomainStrategySubGraph.from_dict(_exit_)

        pulsight_internal_core_domain_strategy_strategy_def = cls(
            constraints=constraints,
            entry=entry,
            exit_=exit_,
        )

        pulsight_internal_core_domain_strategy_strategy_def.additional_properties = d
        return pulsight_internal_core_domain_strategy_strategy_def

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
