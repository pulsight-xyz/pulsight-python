from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_edge import (
        PulsightInternalCoreDomainStrategyEdge,
    )
    from ..models.pulsight_internal_core_domain_strategy_node import (
        PulsightInternalCoreDomainStrategyNode,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategySubGraph")


@_attrs_define
class PulsightInternalCoreDomainStrategySubGraph:
    """
    Attributes:
        edges (list[PulsightInternalCoreDomainStrategyEdge] | Unset):
        nodes (list[PulsightInternalCoreDomainStrategyNode] | Unset):
    """

    edges: list[PulsightInternalCoreDomainStrategyEdge] | Unset = UNSET
    nodes: list[PulsightInternalCoreDomainStrategyNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_edge import (
            PulsightInternalCoreDomainStrategyEdge,
        )
        from ..models.pulsight_internal_core_domain_strategy_node import (
            PulsightInternalCoreDomainStrategyNode,
        )

        d = dict(src_dict)
        _edges = d.pop("edges", UNSET)
        edges: list[PulsightInternalCoreDomainStrategyEdge] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = PulsightInternalCoreDomainStrategyEdge.from_dict(
                    edges_item_data
                )

                edges.append(edges_item)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[PulsightInternalCoreDomainStrategyNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = PulsightInternalCoreDomainStrategyNode.from_dict(
                    nodes_item_data
                )

                nodes.append(nodes_item)

        pulsight_internal_core_domain_strategy_sub_graph = cls(
            edges=edges,
            nodes=nodes,
        )

        pulsight_internal_core_domain_strategy_sub_graph.additional_properties = d
        return pulsight_internal_core_domain_strategy_sub_graph

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
