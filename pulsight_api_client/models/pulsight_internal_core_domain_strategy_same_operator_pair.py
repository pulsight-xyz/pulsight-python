from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainStrategySameOperatorPair")


@_attrs_define
class PulsightInternalCoreDomainStrategySameOperatorPair:
    """
    Attributes:
        a (str | Unset): A is the first wallet, in the order of the set.
        b (str | Unset): B is the second wallet.
        co_bought_tokens (int | Unset): CoBoughtTokens counts the tokens both entered within 1 second of each other.
        co_buy_rate (float | Unset): CoBuyRate is CoBoughtTokens divided by SmallerTokens.
        shared_tokens (int | Unset): SharedTokens counts the tokens both wallets entered in the window.
        smaller_tokens (int | Unset): SmallerTokens is the smaller of the two wallets' counts of tokens entered.
    """

    a: str | Unset = UNSET
    b: str | Unset = UNSET
    co_bought_tokens: int | Unset = UNSET
    co_buy_rate: float | Unset = UNSET
    shared_tokens: int | Unset = UNSET
    smaller_tokens: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a = self.a

        b = self.b

        co_bought_tokens = self.co_bought_tokens

        co_buy_rate = self.co_buy_rate

        shared_tokens = self.shared_tokens

        smaller_tokens = self.smaller_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if co_bought_tokens is not UNSET:
            field_dict["co_bought_tokens"] = co_bought_tokens
        if co_buy_rate is not UNSET:
            field_dict["co_buy_rate"] = co_buy_rate
        if shared_tokens is not UNSET:
            field_dict["shared_tokens"] = shared_tokens
        if smaller_tokens is not UNSET:
            field_dict["smaller_tokens"] = smaller_tokens

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        co_bought_tokens = d.pop("co_bought_tokens", UNSET)

        co_buy_rate = d.pop("co_buy_rate", UNSET)

        shared_tokens = d.pop("shared_tokens", UNSET)

        smaller_tokens = d.pop("smaller_tokens", UNSET)

        pulsight_internal_core_domain_strategy_same_operator_pair = cls(
            a=a,
            b=b,
            co_bought_tokens=co_bought_tokens,
            co_buy_rate=co_buy_rate,
            shared_tokens=shared_tokens,
            smaller_tokens=smaller_tokens,
        )

        pulsight_internal_core_domain_strategy_same_operator_pair.additional_properties = d
        return pulsight_internal_core_domain_strategy_same_operator_pair

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
