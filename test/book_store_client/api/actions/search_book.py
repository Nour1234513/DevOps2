from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.book_request_response_model import BookRequestResponseModel
from ...models.error_response_model import ErrorResponseModel
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[None, Unset, str] = UNSET,
    author: Union[None, Unset, str] = UNSET,
    isbn: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_name: Union[None, Unset, str]
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_author: Union[None, Unset, str]
    if isinstance(author, Unset):
        json_author = UNSET
    else:
        json_author = author
    params["author"] = json_author

    json_isbn: Union[None, Unset, str]
    if isinstance(isbn, Unset):
        json_isbn = UNSET
    else:
        json_isbn = isbn
    params["isbn"] = json_isbn

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/books/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BookRequestResponseModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponseModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[None, Unset, str] = UNSET,
    author: Union[None, Unset, str] = UNSET,
    isbn: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    """Search Books

     Search for books using optional filters for name, author, and ISBN.

    Args:
        name (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        isbn (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseModel, HTTPValidationError, List['BookRequestResponseModel']]]
    """

    kwargs = _get_kwargs(
        name=name,
        author=author,
        isbn=isbn,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[None, Unset, str] = UNSET,
    author: Union[None, Unset, str] = UNSET,
    isbn: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    """Search Books

     Search for books using optional filters for name, author, and ISBN.

    Args:
        name (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        isbn (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseModel, HTTPValidationError, List['BookRequestResponseModel']]
    """

    return sync_detailed(
        client=client,
        name=name,
        author=author,
        isbn=isbn,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[None, Unset, str] = UNSET,
    author: Union[None, Unset, str] = UNSET,
    isbn: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    """Search Books

     Search for books using optional filters for name, author, and ISBN.

    Args:
        name (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        isbn (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponseModel, HTTPValidationError, List['BookRequestResponseModel']]]
    """

    kwargs = _get_kwargs(
        name=name,
        author=author,
        isbn=isbn,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[None, Unset, str] = UNSET,
    author: Union[None, Unset, str] = UNSET,
    isbn: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponseModel, HTTPValidationError, List["BookRequestResponseModel"]]]:
    """Search Books

     Search for books using optional filters for name, author, and ISBN.

    Args:
        name (Union[None, Unset, str]):
        author (Union[None, Unset, str]):
        isbn (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponseModel, HTTPValidationError, List['BookRequestResponseModel']]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            author=author,
            isbn=isbn,
        )
    ).parsed
