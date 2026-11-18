from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_wallet_confluence_condition import (
        PulsightInternalCoreDomainStrategyWalletConfluenceCondition,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerConfluencePreviewRequest")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerConfluencePreviewRequest:
    """
    Attributes:
        node (PulsightInternalCoreDomainStrategyWalletConfluenceCondition | Unset):
    """

    node: PulsightInternalCoreDomainStrategyWalletConfluenceCondition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_strategy_wallet_confluence_condition import (
            PulsightInternalCoreDomainStrategyWalletConfluenceCondition,
        )

        d = dict(src_dict)
        _node = d.pop("node", UNSET)
        node: PulsightInternalCoreDomainStrategyWalletConfluenceCondition | Unset
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = (
                PulsightInternalCoreDomainStrategyWalletConfluenceCondition.from_dict(
                    _node
                )
            )

        internal_adapters_primary_http_handler_confluence_preview_request = cls(
            node=node,
        )

        internal_adapters_primary_http_handler_confluence_preview_request.additional_properties = d
        return internal_adapters_primary_http_handler_confluence_preview_request

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
