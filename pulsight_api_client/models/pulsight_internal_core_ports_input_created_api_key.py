from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_apikey_key import (
        PulsightInternalCoreDomainApikeyKey,
    )


T = TypeVar("T", bound="PulsightInternalCorePortsInputCreatedAPIKey")


@_attrs_define
class PulsightInternalCorePortsInputCreatedAPIKey:
    """
    Attributes:
        key (PulsightInternalCoreDomainApikeyKey | Unset):
        plaintext (str | Unset):
    """

    key: PulsightInternalCoreDomainApikeyKey | Unset = UNSET
    plaintext: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        plaintext = self.plaintext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if plaintext is not UNSET:
            field_dict["plaintext"] = plaintext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_apikey_key import (
            PulsightInternalCoreDomainApikeyKey,
        )

        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: PulsightInternalCoreDomainApikeyKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = PulsightInternalCoreDomainApikeyKey.from_dict(_key)

        plaintext = d.pop("plaintext", UNSET)

        pulsight_internal_core_ports_input_created_api_key = cls(
            key=key,
            plaintext=plaintext,
        )

        pulsight_internal_core_ports_input_created_api_key.additional_properties = d
        return pulsight_internal_core_ports_input_created_api_key

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
