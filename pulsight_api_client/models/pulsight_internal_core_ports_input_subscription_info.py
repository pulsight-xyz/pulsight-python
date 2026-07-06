from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_subscription_subscription_tier import (
    PulsightInternalCoreDomainSubscriptionSubscriptionTier,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_ports_input_plan_limits_read import (
        PulsightInternalCorePortsInputPlanLimitsRead,
    )
    from ..models.pulsight_internal_core_ports_input_usage_counts import (
        PulsightInternalCorePortsInputUsageCounts,
    )


T = TypeVar("T", bound="PulsightInternalCorePortsInputSubscriptionInfo")


@_attrs_define
class PulsightInternalCorePortsInputSubscriptionInfo:
    """
    Attributes:
        expires_at (str | Unset):
        interval (str | Unset):
        is_active (bool | Unset):
        label (str | Unset): Label/PriceUSD/Interval describe a bespoke ENTERPRISE plan; populated
            only for an active TierEnterprise user (from their custom entitlement)
            so the plan page can render the negotiated plan instead of a tier card.
        limits (PulsightInternalCorePortsInputPlanLimitsRead | Unset):
        price_usd (float | Unset):
        provider (str | Unset):
        started_at (str | Unset):
        status (str | Unset):
        tier (PulsightInternalCoreDomainSubscriptionSubscriptionTier | Unset):
        usage (PulsightInternalCorePortsInputUsageCounts | Unset):
    """

    expires_at: str | Unset = UNSET
    interval: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    label: str | Unset = UNSET
    limits: PulsightInternalCorePortsInputPlanLimitsRead | Unset = UNSET
    price_usd: float | Unset = UNSET
    provider: str | Unset = UNSET
    started_at: str | Unset = UNSET
    status: str | Unset = UNSET
    tier: PulsightInternalCoreDomainSubscriptionSubscriptionTier | Unset = UNSET
    usage: PulsightInternalCorePortsInputUsageCounts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        interval = self.interval

        is_active = self.is_active

        label = self.label

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        price_usd = self.price_usd

        provider = self.provider

        started_at = self.started_at

        status = self.status

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if interval is not UNSET:
            field_dict["interval"] = interval
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if label is not UNSET:
            field_dict["label"] = label
        if limits is not UNSET:
            field_dict["limits"] = limits
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if provider is not UNSET:
            field_dict["provider"] = provider
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if tier is not UNSET:
            field_dict["tier"] = tier
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_ports_input_plan_limits_read import (
            PulsightInternalCorePortsInputPlanLimitsRead,
        )
        from ..models.pulsight_internal_core_ports_input_usage_counts import (
            PulsightInternalCorePortsInputUsageCounts,
        )

        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        interval = d.pop("interval", UNSET)

        is_active = d.pop("is_active", UNSET)

        label = d.pop("label", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: PulsightInternalCorePortsInputPlanLimitsRead | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = PulsightInternalCorePortsInputPlanLimitsRead.from_dict(_limits)

        price_usd = d.pop("price_usd", UNSET)

        provider = d.pop("provider", UNSET)

        started_at = d.pop("started_at", UNSET)

        status = d.pop("status", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: PulsightInternalCoreDomainSubscriptionSubscriptionTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = PulsightInternalCoreDomainSubscriptionSubscriptionTier(_tier)

        _usage = d.pop("usage", UNSET)
        usage: PulsightInternalCorePortsInputUsageCounts | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = PulsightInternalCorePortsInputUsageCounts.from_dict(_usage)

        pulsight_internal_core_ports_input_subscription_info = cls(
            expires_at=expires_at,
            interval=interval,
            is_active=is_active,
            label=label,
            limits=limits,
            price_usd=price_usd,
            provider=provider,
            started_at=started_at,
            status=status,
            tier=tier,
            usage=usage,
        )

        pulsight_internal_core_ports_input_subscription_info.additional_properties = d
        return pulsight_internal_core_ports_input_subscription_info

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
