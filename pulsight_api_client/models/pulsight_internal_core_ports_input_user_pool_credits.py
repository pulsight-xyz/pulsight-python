from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_credit_pool import (
    PulsightInternalCoreDomainCreditPool,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCorePortsInputUserPoolCredits")


@_attrs_define
class PulsightInternalCorePortsInputUserPoolCredits:
    """
    Attributes:
        allowance (int | Unset): tier grant per cycle (the limit)
        balance (int | Unset): total remaining = cycle balance + gift
        gifted (int | Unset): Gifted is the persistent admin-gift reserve still available. It is
            spent down before the cycle allowance and survives tier changes.
            Cycle tier balance remaining = Balance − Gifted.
        period_end (str | Unset):
        period_start (str | Unset):
        pool (PulsightInternalCoreDomainCreditPool | Unset):
        used (int | Unset): Used is the real consumption this cycle (positive), summed from the
            ledger — not allowance−balance, which breaks once credits are gifted.
    """

    allowance: int | Unset = UNSET
    balance: int | Unset = UNSET
    gifted: int | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    pool: PulsightInternalCoreDomainCreditPool | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowance = self.allowance

        balance = self.balance

        gifted = self.gifted

        period_end = self.period_end

        period_start = self.period_start

        pool: str | Unset = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.value

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowance is not UNSET:
            field_dict["allowance"] = allowance
        if balance is not UNSET:
            field_dict["balance"] = balance
        if gifted is not UNSET:
            field_dict["gifted"] = gifted
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if pool is not UNSET:
            field_dict["pool"] = pool
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowance = d.pop("allowance", UNSET)

        balance = d.pop("balance", UNSET)

        gifted = d.pop("gifted", UNSET)

        period_end = d.pop("period_end", UNSET)

        period_start = d.pop("period_start", UNSET)

        _pool = d.pop("pool", UNSET)
        pool: PulsightInternalCoreDomainCreditPool | Unset
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = PulsightInternalCoreDomainCreditPool(_pool)

        used = d.pop("used", UNSET)

        pulsight_internal_core_ports_input_user_pool_credits = cls(
            allowance=allowance,
            balance=balance,
            gifted=gifted,
            period_end=period_end,
            period_start=period_start,
            pool=pool,
            used=used,
        )

        pulsight_internal_core_ports_input_user_pool_credits.additional_properties = d
        return pulsight_internal_core_ports_input_user_pool_credits

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
