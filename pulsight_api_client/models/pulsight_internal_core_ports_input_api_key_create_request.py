from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_apikey_scope import (
    PulsightInternalCoreDomainApikeyScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCorePortsInputAPIKeyCreateRequest")


@_attrs_define
class PulsightInternalCorePortsInputAPIKeyCreateRequest:
    """
    Attributes:
        expires_at (str | Unset):
        name (str | Unset):
        scopes (list[PulsightInternalCoreDomainApikeyScope] | Unset):
    """

    expires_at: str | Unset = UNSET
    name: str | Unset = UNSET
    scopes: list[PulsightInternalCoreDomainApikeyScope] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        name = self.name

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        name = d.pop("name", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[PulsightInternalCoreDomainApikeyScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = PulsightInternalCoreDomainApikeyScope(scopes_item_data)

                scopes.append(scopes_item)

        pulsight_internal_core_ports_input_api_key_create_request = cls(
            expires_at=expires_at,
            name=name,
            scopes=scopes,
        )

        pulsight_internal_core_ports_input_api_key_create_request.additional_properties = d
        return pulsight_internal_core_ports_input_api_key_create_request

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
