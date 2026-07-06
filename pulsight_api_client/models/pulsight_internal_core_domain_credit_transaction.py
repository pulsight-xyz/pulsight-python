from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_credit_pool import (
    PulsightInternalCoreDomainCreditPool,
)
from ..models.pulsight_internal_core_domain_credit_reason import (
    PulsightInternalCoreDomainCreditReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainCreditTransaction")


@_attrs_define
class PulsightInternalCoreDomainCreditTransaction:
    """
    Attributes:
        created_at (str | Unset):
        delta (int | Unset):
        id (str | Unset):
        pool (PulsightInternalCoreDomainCreditPool | Unset):
        reason (PulsightInternalCoreDomainCreditReason | Unset):
        ref (str | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    delta: int | Unset = UNSET
    id: str | Unset = UNSET
    pool: PulsightInternalCoreDomainCreditPool | Unset = UNSET
    reason: PulsightInternalCoreDomainCreditReason | Unset = UNSET
    ref: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        delta = self.delta

        id = self.id

        pool: str | Unset = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.value

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        ref = self.ref

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delta is not UNSET:
            field_dict["delta"] = delta
        if id is not UNSET:
            field_dict["id"] = id
        if pool is not UNSET:
            field_dict["pool"] = pool
        if reason is not UNSET:
            field_dict["reason"] = reason
        if ref is not UNSET:
            field_dict["ref"] = ref
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        delta = d.pop("delta", UNSET)

        id = d.pop("id", UNSET)

        _pool = d.pop("pool", UNSET)
        pool: PulsightInternalCoreDomainCreditPool | Unset
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = PulsightInternalCoreDomainCreditPool(_pool)

        _reason = d.pop("reason", UNSET)
        reason: PulsightInternalCoreDomainCreditReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PulsightInternalCoreDomainCreditReason(_reason)

        ref = d.pop("ref", UNSET)

        user_id = d.pop("user_id", UNSET)

        pulsight_internal_core_domain_credit_transaction = cls(
            created_at=created_at,
            delta=delta,
            id=id,
            pool=pool,
            reason=reason,
            ref=ref,
            user_id=user_id,
        )

        pulsight_internal_core_domain_credit_transaction.additional_properties = d
        return pulsight_internal_core_domain_credit_transaction

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
