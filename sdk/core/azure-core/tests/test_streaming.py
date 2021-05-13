# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# --------------------------------------------------------------------------
import os
from azure.core import PipelineClient

def test_decompress_plain_no_header():
    # expect plain text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test.txt".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=True)
    content = b"".join(list(data))
    decoded = content.decode('utf-8')
    assert decoded == "test"

def test_compress_plain_no_header():
    # expect plain text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test.txt".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=False)
    content = b"".join(list(data))
    decoded = content.decode('utf-8')
    assert decoded == "test"

def test_decompress_compressed_no_header():
    # expect compressed text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test.tar.gz".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=True)
    content = b"".join(list(data))
    try:
        decoded = content.decode('utf-8')
        assert False
    except UnicodeDecodeError:
        pass

def test_compress_compressed_no_header():
    # expect compressed text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test.tar.gz".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=False)
    content = b"".join(list(data))
    try:
        decoded = content.decode('utf-8')
        assert False
    except UnicodeDecodeError:
        pass

def test_decompress_plain_header():
    # expect error
    import requests
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test_with_header.txt".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=True)
    try:
        content = b"".join(list(data))
        assert False
    except requests.exceptions.ContentDecodingError:
        pass

def test_compress_plain_header():
    # expect plain text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test_with_header.txt".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=False)
    content = b"".join(list(data))
    decoded = content.decode('utf-8')
    assert decoded == "test"

def test_decompress_compressed_header():
    # expect plain text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test_with_header.tar.gz".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=True)
    content = b"".join(list(data))
    decoded = content.decode('utf-8')
    assert decoded == "test"

def test_compress_compressed_header():
    # expect compressed text
    account_name = "coretests"
    account_url = "https://{}.blob.core.windows.net".format(account_name)
    url = "https://{}.blob.core.windows.net/tests/test_with_header.tar.gz".format(account_name)
    client = PipelineClient(account_url)
    request = client.get(url)
    pipeline_response = client._pipeline.run(request, stream=True)
    response = pipeline_response.http_response
    data = response.stream_download(client._pipeline, decompress=False)
    content = b"".join(list(data))
    try:
        decoded = content.decode('utf-8')
        assert False
    except UnicodeDecodeError:
        pass
