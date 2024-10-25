from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.book_request_response_model import BookRequestResponseModel
from ...models.error_response_model import ErrorResponseModel
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    isbn: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/books/{isbn}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BookRequestResponseModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponseModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponseModel.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    isbn: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    """Get Book By Isbn

     Retrieve a book's data by ISBN.

    Args:
        isbn (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        isbn=isbn,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    isbn: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    """Get Book By Isbn

     Retrieve a book's data by ISBN.

    Args:
        isbn (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]
    """

    return sync_detailed(
        isbn=isbn,
        client=client,
    ).parsed


async def asyncio_detailed(
    isbn: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    """Get Book By Isbn

     Retrieve a book's data by ISBN.

    Args:
        isbn (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        isbn=isbn,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    isbn: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]]:
    """Get Book By Isbn

     Retrieve a book's data by ISBN.

    Args:
        isbn (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BookRequestResponseModel, ErrorResponseModel, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            isbn=isbn,
            client=client,
        )
    ).parsed
