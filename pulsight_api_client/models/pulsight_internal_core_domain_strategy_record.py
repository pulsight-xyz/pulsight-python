from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
        PulsightInternalCoreDomainStrategyStrategyDef,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyRecord")


@_attrs_define
class PulsightInternalCoreDomainStrategyRecord:
    """
    Attributes:
        created_at (str | Unset):
        def_ (PulsightInternalCoreDomainStrategyStrategyDef | Unset):
        deleted_at (str | Unset):
        description (str | Unset):
        id (str | Unset):
        name (str | Unset):
        updated_at (str | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset = UNSET
    deleted_at: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        def_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.def_, Unset):
            def_ = self.def_.to_dict()

        deleted_at = self.deleted_at

        description = self.description

        id = self.id

        name = self.name

        updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if def_ is not UNSET:
            field_dict["def"] = def_
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
            PulsightInternalCoreDomainStrategyStrategyDef,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _def_ = d.pop("def", UNSET)
        def_: PulsightInternalCoreDomainStrategyStrategyDef | Unset
        if isinstance(_def_, Unset):
            def_ = UNSET
        else:
            def_ = PulsightInternalCoreDomainStrategyStrategyDef.from_dict(_def_)

        deleted_at = d.pop("deleted_at", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        pulsight_internal_core_domain_strategy_record = cls(
            created_at=created_at,
            def_=def_,
            deleted_at=deleted_at,
            description=description,
            id=id,
            name=name,
            updated_at=updated_at,
            user_id=user_id,
        )

        pulsight_internal_core_domain_strategy_record.additional_properties = d
        return pulsight_internal_core_domain_strategy_record

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
