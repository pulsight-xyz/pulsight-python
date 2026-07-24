from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_webhook_type import (
    PulsightInternalCoreDomainWebhookType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_webhook_notifier_webhook_extra import (
        PulsightInternalCoreDomainWebhookNotifierWebhookExtra,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainWebhookNotifier")


@_attrs_define
class PulsightInternalCoreDomainWebhookNotifier:
    """
    Attributes:
        created_at (str | Unset):
        filter_preset_id (str | Unset): Solana trader filter
        id (str | Unset):
        interval_hours (int | Unset):
        is_active (bool | Unset):
        last_sent_at (str | Unset):
        latest_activity_seconds (int | Unset): LatestActivitySeconds restricts delivery to traders whose most recent
            activity is within this many seconds (nil = off). Unlike the oldest-trade
            knob, it has no leaderboard-clause equivalent: the dispatch worker
            post-filters matched rows by last_active_timestamp.
        name (str | Unset):
        oldest_trade_op (str | Unset): ">", "<", ">=", "<="
        oldest_trade_seconds (int | Unset):
        updated_at (str | Unset):
        user_id (str | Unset):
        webhook_extra (PulsightInternalCoreDomainWebhookNotifierWebhookExtra | Unset): platform-specific config (e.g.
            channel ID)
        webhook_type (PulsightInternalCoreDomainWebhookType | Unset):
        webhook_url (str | Unset):
    """

    created_at: str | Unset = UNSET
    filter_preset_id: str | Unset = UNSET
    id: str | Unset = UNSET
    interval_hours: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_sent_at: str | Unset = UNSET
    latest_activity_seconds: int | Unset = UNSET
    name: str | Unset = UNSET
    oldest_trade_op: str | Unset = UNSET
    oldest_trade_seconds: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: str | Unset = UNSET
    webhook_extra: PulsightInternalCoreDomainWebhookNotifierWebhookExtra | Unset = UNSET
    webhook_type: PulsightInternalCoreDomainWebhookType | Unset = UNSET
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        filter_preset_id = self.filter_preset_id

        id = self.id

        interval_hours = self.interval_hours

        is_active = self.is_active

        last_sent_at = self.last_sent_at

        latest_activity_seconds = self.latest_activity_seconds

        name = self.name

        oldest_trade_op = self.oldest_trade_op

        oldest_trade_seconds = self.oldest_trade_seconds

        updated_at = self.updated_at

        user_id = self.user_id

        webhook_extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_extra, Unset):
            webhook_extra = self.webhook_extra.to_dict()

        webhook_type: str | Unset = UNSET
        if not isinstance(self.webhook_type, Unset):
            webhook_type = self.webhook_type.value

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if filter_preset_id is not UNSET:
            field_dict["filter_preset_id"] = filter_preset_id
        if id is not UNSET:
            field_dict["id"] = id
        if interval_hours is not UNSET:
            field_dict["interval_hours"] = interval_hours
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_sent_at is not UNSET:
            field_dict["last_sent_at"] = last_sent_at
        if latest_activity_seconds is not UNSET:
            field_dict["latest_activity_seconds"] = latest_activity_seconds
        if name is not UNSET:
            field_dict["name"] = name
        if oldest_trade_op is not UNSET:
            field_dict["oldest_trade_op"] = oldest_trade_op
        if oldest_trade_seconds is not UNSET:
            field_dict["oldest_trade_seconds"] = oldest_trade_seconds
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if webhook_extra is not UNSET:
            field_dict["webhook_extra"] = webhook_extra
        if webhook_type is not UNSET:
            field_dict["webhook_type"] = webhook_type
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_webhook_notifier_webhook_extra import (
            PulsightInternalCoreDomainWebhookNotifierWebhookExtra,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        filter_preset_id = d.pop("filter_preset_id", UNSET)

        id = d.pop("id", UNSET)

        interval_hours = d.pop("interval_hours", UNSET)

        is_active = d.pop("is_active", UNSET)

        last_sent_at = d.pop("last_sent_at", UNSET)

        latest_activity_seconds = d.pop("latest_activity_seconds", UNSET)

        name = d.pop("name", UNSET)

        oldest_trade_op = d.pop("oldest_trade_op", UNSET)

        oldest_trade_seconds = d.pop("oldest_trade_seconds", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        _webhook_extra = d.pop("webhook_extra", UNSET)
        webhook_extra: PulsightInternalCoreDomainWebhookNotifierWebhookExtra | Unset
        if isinstance(_webhook_extra, Unset):
            webhook_extra = UNSET
        else:
            webhook_extra = (
                PulsightInternalCoreDomainWebhookNotifierWebhookExtra.from_dict(
                    _webhook_extra
                )
            )

        _webhook_type = d.pop("webhook_type", UNSET)
        webhook_type: PulsightInternalCoreDomainWebhookType | Unset
        if isinstance(_webhook_type, Unset):
            webhook_type = UNSET
        else:
            webhook_type = PulsightInternalCoreDomainWebhookType(_webhook_type)

        webhook_url = d.pop("webhook_url", UNSET)

        pulsight_internal_core_domain_webhook_notifier = cls(
            created_at=created_at,
            filter_preset_id=filter_preset_id,
            id=id,
            interval_hours=interval_hours,
            is_active=is_active,
            last_sent_at=last_sent_at,
            latest_activity_seconds=latest_activity_seconds,
            name=name,
            oldest_trade_op=oldest_trade_op,
            oldest_trade_seconds=oldest_trade_seconds,
            updated_at=updated_at,
            user_id=user_id,
            webhook_extra=webhook_extra,
            webhook_type=webhook_type,
            webhook_url=webhook_url,
        )

        pulsight_internal_core_domain_webhook_notifier.additional_properties = d
        return pulsight_internal_core_domain_webhook_notifier

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
