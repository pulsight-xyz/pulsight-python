from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_apikey_scope import (
    PulsightInternalCoreDomainApikeyScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainApikeyKey")


@_attrs_define
class PulsightInternalCoreDomainApikeyKey:
    """
    Attributes:
        created_at (str | Unset):
        expires_at (str | Unset):
        id (str | Unset):
        last_used_at (str | Unset):
        name (str | Unset):
        prefix (str | Unset):
        revoked_at (str | Unset):
        scopes (list[PulsightInternalCoreDomainApikeyScope] | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: str | Unset = UNSET
    last_used_at: str | Unset = UNSET
    name: str | Unset = UNSET
    prefix: str | Unset = UNSET
    revoked_at: str | Unset = UNSET
    scopes: list[PulsightInternalCoreDomainApikeyScope] | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        expires_at = self.expires_at

        id = self.id

        last_used_at = self.last_used_at

        name = self.name

        prefix = self.prefix

        revoked_at = self.revoked_at

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        revoked_at = d.pop("revoked_at", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[PulsightInternalCoreDomainApikeyScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = PulsightInternalCoreDomainApikeyScope(scopes_item_data)

                scopes.append(scopes_item)

        user_id = d.pop("user_id", UNSET)

        pulsight_internal_core_domain_apikey_key = cls(
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            last_used_at=last_used_at,
            name=name,
            prefix=prefix,
            revoked_at=revoked_at,
            scopes=scopes,
            user_id=user_id,
        )

        pulsight_internal_core_domain_apikey_key.additional_properties = d
        return pulsight_internal_core_domain_apikey_key

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
