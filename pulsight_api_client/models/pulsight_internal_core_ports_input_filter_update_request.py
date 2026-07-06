from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCorePortsInputFilterUpdateRequest")


@_attrs_define
class PulsightInternalCorePortsInputFilterUpdateRequest:
    """
    Attributes:
        filters (list[int] | Unset):
        is_default (bool | Unset):
        name (str | Unset):
    """

    filters: list[int] | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters: list[int] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters

        is_default = self.is_default

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filters = cast(list[int], d.pop("filters", UNSET))

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        pulsight_internal_core_ports_input_filter_update_request = cls(
            filters=filters,
            is_default=is_default,
            name=name,
        )

        pulsight_internal_core_ports_input_filter_update_request.additional_properties = d
        return pulsight_internal_core_ports_input_filter_update_request

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
