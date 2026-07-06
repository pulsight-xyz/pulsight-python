from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
        PulsightInternalCoreDomainStrategyStrategyDef,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerStrategyUpdateRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerStrategyUpdateRequest:
    """
    Attributes:
        def_ (PulsightInternalCoreDomainStrategyStrategyDef | Unset):
        description (str | Unset):
        name (str | Unset):
    """

    def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        def_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.def_, Unset):
            def_ = self.def_.to_dict()

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if def_ is not UNSET:
            field_dict["def"] = def_
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        internal_adapters_primary_http_handler_strategy_update_request = cls(
            def_=def_,
            description=description,
            name=name,
        )

        internal_adapters_primary_http_handler_strategy_update_request.additional_properties = d
        return internal_adapters_primary_http_handler_strategy_update_request

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
