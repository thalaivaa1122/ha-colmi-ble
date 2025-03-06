"""Sample API Client."""

from __future__ import annotations

import datetime
import socket
from typing import Any

import aiohttp
import async_timeout

from colmi_r02_client import client


class ColmiRingApiClientError(Exception):
    """Exception to indicate a general API error."""


class ColmiRingApiClientCommunicationError(
    ColmiRingApiClientError,
):
    """Exception to indicate a communication error."""


class ColmiRingApiClientAuthenticationError(
    ColmiRingApiClientError,
):
    """Exception to indicate an authentication error."""


def _verify_response_or_raise(response: aiohttp.ClientResponse) -> None:
    """Verify that the response is valid."""
    if response.status in (401, 403):
        msg = "Invalid credentials"
        raise ColmiRingApiClientAuthenticationError(
            msg,
        )
    response.raise_for_status()


class ColmiRingApiClient:
    """Sample API Client."""

    def __init__(self, ring_address: str) -> None:
        """Sample API Client."""
        self._ring_address = ring_address
        self._colmi_client = client.Client(self._ring_address)

    async def async_get_data(self) -> Any:
        """Get data from the API."""
        # TODO: think about making this something other than 1 hr
        end_time = datetime.datetime.now(datetime.timezone.utc)  # Current time in UTC
        start_time = end_time - datetime.timedelta(hours=1)  # One hour ago
        async with client.Client(self._ring_address) as ring_client:
            return await ring_client.get_full_data(start_time, end_time)

    async def async_set_time(self, value: datetime.datetime) -> Any:
        async with client.Client(self._ring_address) as ring_client:
            return await ring_client.set_time(value)

    async def async_blink_twice(self) -> Any:
        async with client.Client(self._ring_address) as ring_client:
            return await ring_client.blink_twice()

    async def reboot(self) -> Any:
        async with client.Client(self._ring_address) as ring_client:
            return await ring_client.reboot()
