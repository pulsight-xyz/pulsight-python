from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCorePortsInputPlanLimitsRead")


@_attrs_define
class PulsightInternalCorePortsInputPlanLimitsRead:
    """
    Attributes:
        can_use_tag_event_filters (bool | Unset):
        can_view_full_data (bool | Unset):
        max_filters (int | Unset):
        max_webhooks (int | Unset):
    """

    can_use_tag_event_filters: bool | Unset = UNSET
    can_view_full_data: bool | Unset = UNSET
    max_filters: int | Unset = UNSET
    max_webhooks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_use_tag_event_filters = self.can_use_tag_event_filters

        can_view_full_data = self.can_view_full_data

        max_filters = self.max_filters

        max_webhooks = self.max_webhooks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_use_tag_event_filters is not UNSET:
            field_dict["can_use_tag_event_filters"] = can_use_tag_event_filters
        if can_view_full_data is not UNSET:
            field_dict["can_view_full_data"] = can_view_full_data
        if max_filters is not UNSET:
            field_dict["max_filters"] = max_filters
        if max_webhooks is not UNSET:
            field_dict["max_webhooks"] = max_webhooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_use_tag_event_filters = d.pop("can_use_tag_event_filters", UNSET)

        can_view_full_data = d.pop("can_view_full_data", UNSET)

        max_filters = d.pop("max_filters", UNSET)

        max_webhooks = d.pop("max_webhooks", UNSET)

        pulsight_internal_core_ports_input_plan_limits_read = cls(
            can_use_tag_event_filters=can_use_tag_event_filters,
            can_view_full_data=can_view_full_data,
            max_filters=max_filters,
            max_webhooks=max_webhooks,
        )

        pulsight_internal_core_ports_input_plan_limits_read.additional_properties = d
        return pulsight_internal_core_ports_input_plan_limits_read

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
