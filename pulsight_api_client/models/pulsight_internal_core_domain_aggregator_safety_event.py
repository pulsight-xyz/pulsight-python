from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorSafetyEvent")


@_attrs_define
class PulsightInternalCoreDomainAggregatorSafetyEvent:
    """
    Attributes:
        account_target (str | Unset): AccountTarget is the affected token account; set for freeze/thaw.
        amount (str | Unset): Amount is a decimal token-amount string; set for burn/mint_to.
        authority_type (str | Unset): AuthorityType ∈ {mint, freeze, account_owner, close_account};
            set only for kind=authority_change.
        ix_index (int | Unset):
        kind (str | Unset): Kind ∈ {burn, mint_to, freeze, thaw, authority_change}.
        mint (str | Unset):
        new_authority (str | Unset): NewAuthority is the new authority pubkey (nil = revoked / empty);
            set only for kind=authority_change.
        signature (str | Unset):
        signer (str | Unset):
        slot (int | Unset):
        timestamp (str | Unset):
    """

    account_target: str | Unset = UNSET
    amount: str | Unset = UNSET
    authority_type: str | Unset = UNSET
    ix_index: int | Unset = UNSET
    kind: str | Unset = UNSET
    mint: str | Unset = UNSET
    new_authority: str | Unset = UNSET
    signature: str | Unset = UNSET
    signer: str | Unset = UNSET
    slot: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_target = self.account_target

        amount = self.amount

        authority_type = self.authority_type

        ix_index = self.ix_index

        kind = self.kind

        mint = self.mint

        new_authority = self.new_authority

        signature = self.signature

        signer = self.signer

        slot = self.slot

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_target is not UNSET:
            field_dict["account_target"] = account_target
        if amount is not UNSET:
            field_dict["amount"] = amount
        if authority_type is not UNSET:
            field_dict["authority_type"] = authority_type
        if ix_index is not UNSET:
            field_dict["ix_index"] = ix_index
        if kind is not UNSET:
            field_dict["kind"] = kind
        if mint is not UNSET:
            field_dict["mint"] = mint
        if new_authority is not UNSET:
            field_dict["new_authority"] = new_authority
        if signature is not UNSET:
            field_dict["signature"] = signature
        if signer is not UNSET:
            field_dict["signer"] = signer
        if slot is not UNSET:
            field_dict["slot"] = slot
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_target = d.pop("account_target", UNSET)

        amount = d.pop("amount", UNSET)

        authority_type = d.pop("authority_type", UNSET)

        ix_index = d.pop("ix_index", UNSET)

        kind = d.pop("kind", UNSET)

        mint = d.pop("mint", UNSET)

        new_authority = d.pop("new_authority", UNSET)

        signature = d.pop("signature", UNSET)

        signer = d.pop("signer", UNSET)

        slot = d.pop("slot", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        pulsight_internal_core_domain_aggregator_safety_event = cls(
            account_target=account_target,
            amount=amount,
            authority_type=authority_type,
            ix_index=ix_index,
            kind=kind,
            mint=mint,
            new_authority=new_authority,
            signature=signature,
            signer=signer,
            slot=slot,
            timestamp=timestamp,
        )

        pulsight_internal_core_domain_aggregator_safety_event.additional_properties = d
        return pulsight_internal_core_domain_aggregator_safety_event

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
