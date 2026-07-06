from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerSnapshotRow")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerSnapshotRow:
    """
    Attributes:
        avg_buys_per_token (float | Unset):
        avg_hold_secs (float | Unset):
        avg_reactivity_secs (float | Unset):
        avg_rp_30d (float | Unset): lamports
        avg_rp_7d (float | Unset): lamports
        avg_sells_per_token (float | Unset):
        holding_pnl_lamports (float | Unset):
        med_buys_per_token (float | Unset):
        med_hold_secs (float | Unset):
        med_reactivity_secs (float | Unset):
        med_rp_30d (float | Unset): lamports
        med_rp_7d (float | Unset): lamports
        med_sells_per_token (float | Unset):
        oldest_trade_at (str | Unset):
        pnl_distribution (list[int] | Unset):
        pnl_sparkline_7d (list[float] | Unset): lamports per day
        tags (list[str] | Unset):
        tokens_created (int | Unset): lifetime mints created
        tokens_graduated (int | Unset): subset that graduated
        trader (str | Unset):
    """

    avg_buys_per_token: float | Unset = UNSET
    avg_hold_secs: float | Unset = UNSET
    avg_reactivity_secs: float | Unset = UNSET
    avg_rp_30d: float | Unset = UNSET
    avg_rp_7d: float | Unset = UNSET
    avg_sells_per_token: float | Unset = UNSET
    holding_pnl_lamports: float | Unset = UNSET
    med_buys_per_token: float | Unset = UNSET
    med_hold_secs: float | Unset = UNSET
    med_reactivity_secs: float | Unset = UNSET
    med_rp_30d: float | Unset = UNSET
    med_rp_7d: float | Unset = UNSET
    med_sells_per_token: float | Unset = UNSET
    oldest_trade_at: str | Unset = UNSET
    pnl_distribution: list[int] | Unset = UNSET
    pnl_sparkline_7d: list[float] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    tokens_created: int | Unset = UNSET
    tokens_graduated: int | Unset = UNSET
    trader: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_buys_per_token = self.avg_buys_per_token

        avg_hold_secs = self.avg_hold_secs

        avg_reactivity_secs = self.avg_reactivity_secs

        avg_rp_30d = self.avg_rp_30d

        avg_rp_7d = self.avg_rp_7d

        avg_sells_per_token = self.avg_sells_per_token

        holding_pnl_lamports = self.holding_pnl_lamports

        med_buys_per_token = self.med_buys_per_token

        med_hold_secs = self.med_hold_secs

        med_reactivity_secs = self.med_reactivity_secs

        med_rp_30d = self.med_rp_30d

        med_rp_7d = self.med_rp_7d

        med_sells_per_token = self.med_sells_per_token

        oldest_trade_at = self.oldest_trade_at

        pnl_distribution: list[int] | Unset = UNSET
        if not isinstance(self.pnl_distribution, Unset):
            pnl_distribution = self.pnl_distribution

        pnl_sparkline_7d: list[float] | Unset = UNSET
        if not isinstance(self.pnl_sparkline_7d, Unset):
            pnl_sparkline_7d = self.pnl_sparkline_7d

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        tokens_created = self.tokens_created

        tokens_graduated = self.tokens_graduated

        trader = self.trader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_buys_per_token is not UNSET:
            field_dict["avg_buys_per_token"] = avg_buys_per_token
        if avg_hold_secs is not UNSET:
            field_dict["avg_hold_secs"] = avg_hold_secs
        if avg_reactivity_secs is not UNSET:
            field_dict["avg_reactivity_secs"] = avg_reactivity_secs
        if avg_rp_30d is not UNSET:
            field_dict["avg_rp_30d"] = avg_rp_30d
        if avg_rp_7d is not UNSET:
            field_dict["avg_rp_7d"] = avg_rp_7d
        if avg_sells_per_token is not UNSET:
            field_dict["avg_sells_per_token"] = avg_sells_per_token
        if holding_pnl_lamports is not UNSET:
            field_dict["holding_pnl_lamports"] = holding_pnl_lamports
        if med_buys_per_token is not UNSET:
            field_dict["med_buys_per_token"] = med_buys_per_token
        if med_hold_secs is not UNSET:
            field_dict["med_hold_secs"] = med_hold_secs
        if med_reactivity_secs is not UNSET:
            field_dict["med_reactivity_secs"] = med_reactivity_secs
        if med_rp_30d is not UNSET:
            field_dict["med_rp_30d"] = med_rp_30d
        if med_rp_7d is not UNSET:
            field_dict["med_rp_7d"] = med_rp_7d
        if med_sells_per_token is not UNSET:
            field_dict["med_sells_per_token"] = med_sells_per_token
        if oldest_trade_at is not UNSET:
            field_dict["oldest_trade_at"] = oldest_trade_at
        if pnl_distribution is not UNSET:
            field_dict["pnl_distribution"] = pnl_distribution
        if pnl_sparkline_7d is not UNSET:
            field_dict["pnl_sparkline_7d"] = pnl_sparkline_7d
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tokens_created is not UNSET:
            field_dict["tokens_created"] = tokens_created
        if tokens_graduated is not UNSET:
            field_dict["tokens_graduated"] = tokens_graduated
        if trader is not UNSET:
            field_dict["trader"] = trader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_buys_per_token = d.pop("avg_buys_per_token", UNSET)

        avg_hold_secs = d.pop("avg_hold_secs", UNSET)

        avg_reactivity_secs = d.pop("avg_reactivity_secs", UNSET)

        avg_rp_30d = d.pop("avg_rp_30d", UNSET)

        avg_rp_7d = d.pop("avg_rp_7d", UNSET)

        avg_sells_per_token = d.pop("avg_sells_per_token", UNSET)

        holding_pnl_lamports = d.pop("holding_pnl_lamports", UNSET)

        med_buys_per_token = d.pop("med_buys_per_token", UNSET)

        med_hold_secs = d.pop("med_hold_secs", UNSET)

        med_reactivity_secs = d.pop("med_reactivity_secs", UNSET)

        med_rp_30d = d.pop("med_rp_30d", UNSET)

        med_rp_7d = d.pop("med_rp_7d", UNSET)

        med_sells_per_token = d.pop("med_sells_per_token", UNSET)

        oldest_trade_at = d.pop("oldest_trade_at", UNSET)

        pnl_distribution = cast(list[int], d.pop("pnl_distribution", UNSET))

        pnl_sparkline_7d = cast(list[float], d.pop("pnl_sparkline_7d", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        tokens_created = d.pop("tokens_created", UNSET)

        tokens_graduated = d.pop("tokens_graduated", UNSET)

        trader = d.pop("trader", UNSET)

        internal_adapters_primary_http_handler_snapshot_row = cls(
            avg_buys_per_token=avg_buys_per_token,
            avg_hold_secs=avg_hold_secs,
            avg_reactivity_secs=avg_reactivity_secs,
            avg_rp_30d=avg_rp_30d,
            avg_rp_7d=avg_rp_7d,
            avg_sells_per_token=avg_sells_per_token,
            holding_pnl_lamports=holding_pnl_lamports,
            med_buys_per_token=med_buys_per_token,
            med_hold_secs=med_hold_secs,
            med_reactivity_secs=med_reactivity_secs,
            med_rp_30d=med_rp_30d,
            med_rp_7d=med_rp_7d,
            med_sells_per_token=med_sells_per_token,
            oldest_trade_at=oldest_trade_at,
            pnl_distribution=pnl_distribution,
            pnl_sparkline_7d=pnl_sparkline_7d,
            tags=tags,
            tokens_created=tokens_created,
            tokens_graduated=tokens_graduated,
            trader=trader,
        )

        internal_adapters_primary_http_handler_snapshot_row.additional_properties = d
        return internal_adapters_primary_http_handler_snapshot_row

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
