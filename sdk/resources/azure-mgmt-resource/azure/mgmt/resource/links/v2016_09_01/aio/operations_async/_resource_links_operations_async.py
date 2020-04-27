# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ResourceLinksOperations:
    """ResourceLinksOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.links.v2016_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def delete(
        self,
        link_id: str,
        api_version: str,
        **kwargs
    ) -> None:
        """Deletes a resource link with the specified ID.

        :param link_id: The fully qualified ID of the resource link. Use the format,
         /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-
         namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink.
        :type link_id: str
        :param api_version: The API version to use for the operation.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'linkId': self._serialize.url("link_id", link_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/{linkId}'}  # type: ignore

    async def create_or_update(
        self,
        link_id: str,
        api_version: str,
        parameters: "models.ResourceLink",
        **kwargs
    ) -> "models.ResourceLink":
        """Creates or updates a resource link between the specified resources.

        :param link_id: The fully qualified ID of the resource link. Use the format,
         /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-
         namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink.
        :type link_id: str
        :param api_version: The API version to use for the operation.
        :type api_version: str
        :param parameters: Parameters for creating or updating a resource link.
        :type parameters: ~azure.mgmt.resource.links.v2016_09_01.models.ResourceLink
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceLink or the result of cls(response)
        :rtype: ~azure.mgmt.resource.links.v2016_09_01.models.ResourceLink
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ResourceLink"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'linkId': self._serialize.url("link_id", link_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ResourceLink')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ResourceLink', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ResourceLink', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/{linkId}'}  # type: ignore

    async def get(
        self,
        link_id: str,
        api_version: str,
        **kwargs
    ) -> "models.ResourceLink":
        """Gets a resource link with the specified ID.

        :param link_id: The fully qualified Id of the resource link. For example,
         /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink.
        :type link_id: str
        :param api_version: The API version to use for the operation.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceLink or the result of cls(response)
        :rtype: ~azure.mgmt.resource.links.v2016_09_01.models.ResourceLink
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ResourceLink"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'linkId': self._serialize.url("link_id", link_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ResourceLink', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{linkId}'}  # type: ignore

    def list_at_subscription(
        self,
        api_version: str,
        filter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.ResourceLinkResult"]:
        """Gets all the linked resources for the subscription.

        :param api_version: The API version to use for the operation.
        :type api_version: str
        :param filter: The filter to apply on the list resource links operation. The supported filter
     for list resource links is targetId. For example, $filter=targetId eq {value}.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ResourceLinkResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.links.v2016_09_01.models.ResourceLinkResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ResourceLinkResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_at_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ResourceLinkResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_at_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/links'}  # type: ignore

    def list_at_source_scope(
        self,
        scope: str,
        api_version: str,
        filter: Optional[str] = "atScope()",
        **kwargs
    ) -> AsyncIterable["models.ResourceLinkResult"]:
        """Gets a list of resource links at and below the specified source scope.

        :param scope: The fully qualified ID of the scope for getting the resource links. For example,
     to list resource links at and under a resource group, set the scope to
     /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.
        :type scope: str
        :param api_version: The API version to use for the operation.
        :type api_version: str
        :param filter: The filter to apply when getting resource links. To get links only at the
     specified scope (not below the scope), use Filter.atScope().
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of ResourceLinkResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.links.v2016_09_01.models.ResourceLinkResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ResourceLinkResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_at_source_scope.metadata['url']  # type: ignore
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ResourceLinkResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_at_source_scope.metadata = {'url': '/{scope}/providers/Microsoft.Resources/links'}  # type: ignore
