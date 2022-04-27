# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import TextAnalyticsClientConfiguration
from ._operations_mixin import TextAnalyticsClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class TextAnalyticsClient(TextAnalyticsClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """The Text Analytics API is a suite of natural language processing (NLP) services built with best-in-class Microsoft machine learning algorithms.  The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection. Functionality for analysis of text specific to the healthcare domain and personal information are also available in the API. Further documentation can be found in :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview">https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview</a>`.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = 'v3.1'
    _PROFILE_TAG = "azure.ai.textanalytics.TextAnalyticsClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'analyze_text': '2022-03-01-preview',
            'analyze_text_job_status': '2022-03-01-preview',
            'begin_analyze_text_cancel_job': '2022-03-01-preview',
            'begin_analyze_text_submit_job': '2022-03-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        api_version: Optional[str] = None,
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if api_version == '2022-03-01-preview':
            base_url = '{Endpoint}/language'
        elif api_version == 'v3.0':
            base_url = '{Endpoint}/text/analytics/v3.0'
        elif api_version == 'v3.1':
            base_url = '{Endpoint}/text/analytics/v3.1'
        elif api_version == 'v3.2-preview.2':
            base_url = '{Endpoint}/text/analytics/v3.2-preview.2'
        else:
            raise ValueError("API version {} is not available".format(api_version))
        self._config = TextAnalyticsClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(TextAnalyticsClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2022-03-01-preview: :mod:`v2022_03_01_preview.models<azure.ai.textanalytics.v2022_03_01_preview.models>`
           * v3.0: :mod:`v3_0.models<azure.ai.textanalytics.v3_0.models>`
           * v3.1: :mod:`v3_1.models<azure.ai.textanalytics.v3_1.models>`
           * v3.2-preview.2: :mod:`v3_2_preview_2.models<azure.ai.textanalytics.v3_2_preview_2.models>`
        """
        if api_version == '2022-03-01-preview':
            from ..v2022_03_01_preview import models
            return models
        elif api_version == 'v3.0':
            from ..v3_0 import models
            return models
        elif api_version == 'v3.1':
            from ..v3_1 import models
            return models
        elif api_version == 'v3.2-preview.2':
            from ..v3_2_preview_2 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
