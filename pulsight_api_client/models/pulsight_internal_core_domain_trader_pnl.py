from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderPnl")


@_attrs_define
class PulsightInternalCoreDomainTraderPnl:
    """
    Attributes:
        balance (float | Unset): Position
        buy_tx_count (int | Unset): Activity
        created_at (str | Unset):
        id (str | Unset):
        last_active_timestamp (int | Unset):
        open_timestamp (int | Unset): Timing
        realized_profit (float | Unset):
        sell_tx_count (int | Unset):
        start_holding_at (int | Unset):
        token_address (str | Unset): Token info
        token_logo (str | Unset):
        token_name (str | Unset):
        token_price (float | Unset):
        token_symbol (str | Unset):
        total_profit (float | Unset):
        total_profit_pnl (float | Unset):
        trader_id (str | Unset):
        unrealized_profit (float | Unset):
        updated_at (str | Unset):
        usd_value (float | Unset):
    """

    balance: float | Unset = UNSET
    buy_tx_count: int | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    last_active_timestamp: int | Unset = UNSET
    open_timestamp: int | Unset = UNSET
    realized_profit: float | Unset = UNSET
    sell_tx_count: int | Unset = UNSET
    start_holding_at: int | Unset = UNSET
    token_address: str | Unset = UNSET
    token_logo: str | Unset = UNSET
    token_name: str | Unset = UNSET
    token_price: float | Unset = UNSET
    token_symbol: str | Unset = UNSET
    total_profit: float | Unset = UNSET
    total_profit_pnl: float | Unset = UNSET
    trader_id: str | Unset = UNSET
    unrealized_profit: float | Unset = UNSET
    updated_at: str | Unset = UNSET
    usd_value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        buy_tx_count = self.buy_tx_count

        created_at = self.created_at

        id = self.id

        last_active_timestamp = self.last_active_timestamp

        open_timestamp = self.open_timestamp

        realized_profit = self.realized_profit

        sell_tx_count = self.sell_tx_count

        start_holding_at = self.start_holding_at

        token_address = self.token_address

        token_logo = self.token_logo

        token_name = self.token_name

        token_price = self.token_price

        token_symbol = self.token_symbol

        total_profit = self.total_profit

        total_profit_pnl = self.total_profit_pnl

        trader_id = self.trader_id

        unrealized_profit = self.unrealized_profit

        updated_at = self.updated_at

        usd_value = self.usd_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if buy_tx_count is not UNSET:
            field_dict["buy_tx_count"] = buy_tx_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if last_active_timestamp is not UNSET:
            field_dict["last_active_timestamp"] = last_active_timestamp
        if open_timestamp is not UNSET:
            field_dict["open_timestamp"] = open_timestamp
        if realized_profit is not UNSET:
            field_dict["realized_profit"] = realized_profit
        if sell_tx_count is not UNSET:
            field_dict["sell_tx_count"] = sell_tx_count
        if start_holding_at is not UNSET:
            field_dict["start_holding_at"] = start_holding_at
        if token_address is not UNSET:
            field_dict["token_address"] = token_address
        if token_logo is not UNSET:
            field_dict["token_logo"] = token_logo
        if token_name is not UNSET:
            field_dict["token_name"] = token_name
        if token_price is not UNSET:
            field_dict["token_price"] = token_price
        if token_symbol is not UNSET:
            field_dict["token_symbol"] = token_symbol
        if total_profit is not UNSET:
            field_dict["total_profit"] = total_profit
        if total_profit_pnl is not UNSET:
            field_dict["total_profit_pnl"] = total_profit_pnl
        if trader_id is not UNSET:
            field_dict["trader_id"] = trader_id
        if unrealized_profit is not UNSET:
            field_dict["unrealized_profit"] = unrealized_profit
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if usd_value is not UNSET:
            field_dict["usd_value"] = usd_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        buy_tx_count = d.pop("buy_tx_count", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        last_active_timestamp = d.pop("last_active_timestamp", UNSET)

        open_timestamp = d.pop("open_timestamp", UNSET)

        realized_profit = d.pop("realized_profit", UNSET)

        sell_tx_count = d.pop("sell_tx_count", UNSET)

        start_holding_at = d.pop("start_holding_at", UNSET)

        token_address = d.pop("token_address", UNSET)

        token_logo = d.pop("token_logo", UNSET)

        token_name = d.pop("token_name", UNSET)

        token_price = d.pop("token_price", UNSET)

        token_symbol = d.pop("token_symbol", UNSET)

        total_profit = d.pop("total_profit", UNSET)

        total_profit_pnl = d.pop("total_profit_pnl", UNSET)

        trader_id = d.pop("trader_id", UNSET)

        unrealized_profit = d.pop("unrealized_profit", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        usd_value = d.pop("usd_value", UNSET)

        pulsight_internal_core_domain_trader_pnl = cls(
            balance=balance,
            buy_tx_count=buy_tx_count,
            created_at=created_at,
            id=id,
            last_active_timestamp=last_active_timestamp,
            open_timestamp=open_timestamp,
            realized_profit=realized_profit,
            sell_tx_count=sell_tx_count,
            start_holding_at=start_holding_at,
            token_address=token_address,
            token_logo=token_logo,
            token_name=token_name,
            token_price=token_price,
            token_symbol=token_symbol,
            total_profit=total_profit,
            total_profit_pnl=total_profit_pnl,
            trader_id=trader_id,
            unrealized_profit=unrealized_profit,
            updated_at=updated_at,
            usd_value=usd_value,
        )

        pulsight_internal_core_domain_trader_pnl.additional_properties = d
        return pulsight_internal_core_domain_trader_pnl

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
