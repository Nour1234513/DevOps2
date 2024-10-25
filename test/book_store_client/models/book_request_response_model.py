from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BookRequestResponseModel")


@_attrs_define
class BookRequestResponseModel:
    """
    Attributes:
        name (str):
        author (str):
        isbn (str):
        price (float):
        copies (int):
    """

    name: str
    author: str
    isbn: str
    price: float
    copies: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        author = self.author

        isbn = self.isbn

        price = self.price

        copies = self.copies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "author": author,
                "isbn": isbn,
                "price": price,
                "copies": copies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        author = d.pop("author")

        isbn = d.pop("isbn")

        price = d.pop("price")

        copies = d.pop("copies")

        book_request_response_model = cls(
            name=name,
            author=author,
            isbn=isbn,
            price=price,
            copies=copies,
        )

        book_request_response_model.additional_properties = d
        return book_request_response_model

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
