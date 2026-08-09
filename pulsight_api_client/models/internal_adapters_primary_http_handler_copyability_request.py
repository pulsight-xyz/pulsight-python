from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerCopyabilityRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerCopyabilityRequest:
    """
    Attributes:
        delays_slots (list[int] | Unset): Simulated latencies in SLOTS (blocks) behind the target. Omitted ⇒ the
            default ladder. Blocks rather than milliseconds because the stored swap
            timestamp resolves only to whole seconds, so a sub-second ladder cannot
            be answered — see domain/trader/copyability.go.
        from_ (str | Unset):
        size_lamports (int | Unset): OPTIONAL copier trade size in lamports. Supplying it attaches the
            execution half — what slippage band each fill needed, and what each
            widening step buys. Optional because a band is a threshold for a
            concrete size against a concrete depth, while the price-transfer curve
            above is deliberately unit-free; both come from one read either way.
        to (str | Unset):
        wallets (list[str] | Unset):
    """

    delays_slots: list[int] | Unset = UNSET
    from_: str | Unset = UNSET
    size_lamports: int | Unset = UNSET
    to: str | Unset = UNSET
    wallets: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delays_slots: list[int] | Unset = UNSET
        if not isinstance(self.delays_slots, Unset):
            delays_slots = self.delays_slots

        from_ = self.from_

        size_lamports = self.size_lamports

        to = self.to

        wallets: list[str] | Unset = UNSET
        if not isinstance(self.wallets, Unset):
            wallets = self.wallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delays_slots is not UNSET:
            field_dict["delays_slots"] = delays_slots
        if from_ is not UNSET:
            field_dict["from"] = from_
        if size_lamports is not UNSET:
            field_dict["size_lamports"] = size_lamports
        if to is not UNSET:
            field_dict["to"] = to
        if wallets is not UNSET:
            field_dict["wallets"] = wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delays_slots = cast(list[int], d.pop("delays_slots", UNSET))

        from_ = d.pop("from", UNSET)

        size_lamports = d.pop("size_lamports", UNSET)

        to = d.pop("to", UNSET)

        wallets = cast(list[str], d.pop("wallets", UNSET))

        internal_adapters_primary_http_handler_copyability_request = cls(
            delays_slots=delays_slots,
            from_=from_,
            size_lamports=size_lamports,
            to=to,
            wallets=wallets,
        )

        internal_adapters_primary_http_handler_copyability_request.additional_properties = d
        return internal_adapters_primary_http_handler_copyability_request

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
