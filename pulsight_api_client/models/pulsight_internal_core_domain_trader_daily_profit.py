from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainTraderDailyProfit")


@_attrs_define
class PulsightInternalCoreDomainTraderDailyProfit:
    """
    Attributes:
        buy_amount_usd (float | Unset):
        created_at (str | Unset):
        date (str | Unset):
        id (str | Unset):
        loss_profit (float | Unset):
        loss_sells (int | Unset):
        sell_amount_usd (float | Unset):
        total_buys (int | Unset):
        total_profit (float | Unset):
        total_sells (int | Unset):
        trader_id (str | Unset):
        win_profit (float | Unset):
        win_sells (int | Unset):
    """

    buy_amount_usd: float | Unset = UNSET
    created_at: str | Unset = UNSET
    date: str | Unset = UNSET
    id: str | Unset = UNSET
    loss_profit: float | Unset = UNSET
    loss_sells: int | Unset = UNSET
    sell_amount_usd: float | Unset = UNSET
    total_buys: int | Unset = UNSET
    total_profit: float | Unset = UNSET
    total_sells: int | Unset = UNSET
    trader_id: str | Unset = UNSET
    win_profit: float | Unset = UNSET
    win_sells: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_amount_usd = self.buy_amount_usd

        created_at = self.created_at

        date = self.date

        id = self.id

        loss_profit = self.loss_profit

        loss_sells = self.loss_sells

        sell_amount_usd = self.sell_amount_usd

        total_buys = self.total_buys

        total_profit = self.total_profit

        total_sells = self.total_sells

        trader_id = self.trader_id

        win_profit = self.win_profit

        win_sells = self.win_sells

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_amount_usd is not UNSET:
            field_dict["buy_amount_usd"] = buy_amount_usd
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if loss_profit is not UNSET:
            field_dict["loss_profit"] = loss_profit
        if loss_sells is not UNSET:
            field_dict["loss_sells"] = loss_sells
        if sell_amount_usd is not UNSET:
            field_dict["sell_amount_usd"] = sell_amount_usd
        if total_buys is not UNSET:
            field_dict["total_buys"] = total_buys
        if total_profit is not UNSET:
            field_dict["total_profit"] = total_profit
        if total_sells is not UNSET:
            field_dict["total_sells"] = total_sells
        if trader_id is not UNSET:
            field_dict["trader_id"] = trader_id
        if win_profit is not UNSET:
            field_dict["win_profit"] = win_profit
        if win_sells is not UNSET:
            field_dict["win_sells"] = win_sells

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buy_amount_usd = d.pop("buy_amount_usd", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        id = d.pop("id", UNSET)

        loss_profit = d.pop("loss_profit", UNSET)

        loss_sells = d.pop("loss_sells", UNSET)

        sell_amount_usd = d.pop("sell_amount_usd", UNSET)

        total_buys = d.pop("total_buys", UNSET)

        total_profit = d.pop("total_profit", UNSET)

        total_sells = d.pop("total_sells", UNSET)

        trader_id = d.pop("trader_id", UNSET)

        win_profit = d.pop("win_profit", UNSET)

        win_sells = d.pop("win_sells", UNSET)

        pulsight_internal_core_domain_trader_daily_profit = cls(
            buy_amount_usd=buy_amount_usd,
            created_at=created_at,
            date=date,
            id=id,
            loss_profit=loss_profit,
            loss_sells=loss_sells,
            sell_amount_usd=sell_amount_usd,
            total_buys=total_buys,
            total_profit=total_profit,
            total_sells=total_sells,
            trader_id=trader_id,
            win_profit=win_profit,
            win_sells=win_sells,
        )

        pulsight_internal_core_domain_trader_daily_profit.additional_properties = d
        return pulsight_internal_core_domain_trader_daily_profit

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
