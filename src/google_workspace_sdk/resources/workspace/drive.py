# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workspace.drive_tree import DriveTree

__all__ = ["DriveResource", "AsyncDriveResource"]


class DriveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#accessing-raw-response-data-eg-headers
        """
        return DriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#with_streaming_response
        """
        return DriveResourceWithStreamingResponse(self)

    def retrieve_tree(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveTree:
        """
        Retrieve the complete folder structure of the workspace drive

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/workspace/{session_id}/drive/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriveTree,
        )


class AsyncDriveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#with_streaming_response
        """
        return AsyncDriveResourceWithStreamingResponse(self)

    async def retrieve_tree(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriveTree:
        """
        Retrieve the complete folder structure of the workspace drive

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/workspace/{session_id}/drive/tree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriveTree,
        )


class DriveResourceWithRawResponse:
    def __init__(self, drive: DriveResource) -> None:
        self._drive = drive

        self.retrieve_tree = to_raw_response_wrapper(
            drive.retrieve_tree,
        )


class AsyncDriveResourceWithRawResponse:
    def __init__(self, drive: AsyncDriveResource) -> None:
        self._drive = drive

        self.retrieve_tree = async_to_raw_response_wrapper(
            drive.retrieve_tree,
        )


class DriveResourceWithStreamingResponse:
    def __init__(self, drive: DriveResource) -> None:
        self._drive = drive

        self.retrieve_tree = to_streamed_response_wrapper(
            drive.retrieve_tree,
        )


class AsyncDriveResourceWithStreamingResponse:
    def __init__(self, drive: AsyncDriveResource) -> None:
        self._drive = drive

        self.retrieve_tree = async_to_streamed_response_wrapper(
            drive.retrieve_tree,
        )
