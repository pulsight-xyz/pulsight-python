from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerSolPriceResponse")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerSolPriceResponse:
    """
    Attributes:
        sol_usd (float | Unset):
    """

    sol_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sol_usd = self.sol_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sol_usd is not UNSET:
            field_dict["sol_usd"] = sol_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sol_usd = d.pop("sol_usd", UNSET)

        internal_adapters_primary_http_handler_sol_price_response = cls(
            sol_usd=sol_usd,
        )

        internal_adapters_primary_http_handler_sol_price_response.additional_properties = d
        return internal_adapters_primary_http_handler_sol_price_response

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
