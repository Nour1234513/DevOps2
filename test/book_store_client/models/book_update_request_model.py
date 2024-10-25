from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookUpdateRequestModel")


@_attrs_define
class BookUpdateRequestModel:
    """
    Attributes:
        name (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        isbn (Union[None, Unset, str]):
        price (Union[None, Unset, float]):
        copies (Union[None, Unset, int]):
    """

    name: Union[None, Unset, str] = UNSET
    author: Union[None, Unset, str] = UNSET
    isbn: Union[None, Unset, str] = UNSET
    price: Union[None, Unset, float] = UNSET
    copies: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        author: Union[None, Unset, str]
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        isbn: Union[None, Unset, str]
        if isinstance(self.isbn, Unset):
            isbn = UNSET
        else:
            isbn = self.isbn

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        copies: Union[None, Unset, int]
        if isinstance(self.copies, Unset):
            copies = UNSET
        else:
            copies = self.copies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if author is not UNSET:
            field_dict["author"] = author
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if price is not UNSET:
            field_dict["price"] = price
        if copies is not UNSET:
            field_dict["copies"] = copies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_isbn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        isbn = _parse_isbn(d.pop("isbn", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_copies(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        copies = _parse_copies(d.pop("copies", UNSET))

        book_update_request_model = cls(
            name=name,
            author=author,
            isbn=isbn,
            price=price,
            copies=copies,
        )

        book_update_request_model.additional_properties = d
        return book_update_request_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
