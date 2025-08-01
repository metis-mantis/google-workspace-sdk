# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workspace import slide_create_params
from ...types.workspace.slide_retrieve_response import SlideRetrieveResponse

__all__ = ["SlidesResource", "AsyncSlidesResource"]


class SlidesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#accessing-raw-response-data-eg-headers
        """
        return SlidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#with_streaming_response
        """
        return SlidesResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        name: str,
        content: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new Google Slides presentation in the workspace

        Args:
          name: Name of the presentation

          content: Initial content for the presentation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/workspace/{session_id}/slides",
            body=maybe_transform(
                {
                    "name": name,
                    "content": content,
                },
                slide_create_params.SlideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        slides_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlideRetrieveResponse:
        """
        Retrieve the content of a specific presentation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not slides_id:
            raise ValueError(f"Expected a non-empty value for `slides_id` but received {slides_id!r}")
        return self._get(
            f"/workspace/{session_id}/slides/{slides_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlideRetrieveResponse,
        )


class AsyncSlidesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSlidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metis-mantis/google-workspace-sdk#with_streaming_response
        """
        return AsyncSlidesResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        name: str,
        content: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create a new Google Slides presentation in the workspace

        Args:
          name: Name of the presentation

          content: Initial content for the presentation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/workspace/{session_id}/slides",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "content": content,
                },
                slide_create_params.SlideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        slides_id: str,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlideRetrieveResponse:
        """
        Retrieve the content of a specific presentation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not slides_id:
            raise ValueError(f"Expected a non-empty value for `slides_id` but received {slides_id!r}")
        return await self._get(
            f"/workspace/{session_id}/slides/{slides_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlideRetrieveResponse,
        )


class SlidesResourceWithRawResponse:
    def __init__(self, slides: SlidesResource) -> None:
        self._slides = slides

        self.create = to_raw_response_wrapper(
            slides.create,
        )
        self.retrieve = to_raw_response_wrapper(
            slides.retrieve,
        )


class AsyncSlidesResourceWithRawResponse:
    def __init__(self, slides: AsyncSlidesResource) -> None:
        self._slides = slides

        self.create = async_to_raw_response_wrapper(
            slides.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            slides.retrieve,
        )


class SlidesResourceWithStreamingResponse:
    def __init__(self, slides: SlidesResource) -> None:
        self._slides = slides

        self.create = to_streamed_response_wrapper(
            slides.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            slides.retrieve,
        )


class AsyncSlidesResourceWithStreamingResponse:
    def __init__(self, slides: AsyncSlidesResource) -> None:
        self._slides = slides

        self.create = async_to_streamed_response_wrapper(
            slides.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            slides.retrieve,
        )
