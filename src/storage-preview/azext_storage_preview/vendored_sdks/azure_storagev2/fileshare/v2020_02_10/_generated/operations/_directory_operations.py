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

from azure.core.exceptions import map_error

from .. import models


class DirectoryOperations(object):
    """DirectoryOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar restype: . Constant value: "directory".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.restype = "directory"

    def create(self, file_attributes="none", file_creation_time="now", file_last_write_time="now", timeout=None, metadata=None, file_permission="inherit", file_permission_key=None, cls=None, **kwargs):
        """Creates a new directory under the specified share or parent directory.

        :param file_attributes: If specified, the provided file attributes
         shall be set. Default value: ‘Archive’ for file and ‘Directory’ for
         directory. ‘None’ can also be specified as default.
        :type file_attributes: str
        :param file_creation_time: Creation time for the file/directory.
         Default value: Now.
        :type file_creation_time: str
        :param file_last_write_time: Last write time for the file/directory.
         Default value: Now.
        :type file_last_write_time: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param metadata: A name-value pair to associate with a file storage
         object.
        :type metadata: str
        :param file_permission: If specified the permission (security
         descriptor) shall be set for the directory/file. This header can be
         used if Permission size is <= 8KB, else x-ms-file-permission-key
         header shall be used. Default value: Inherit. If SDDL is specified as
         input, it must have owner, group and dacl. Note: Only one of the
         x-ms-file-permission or x-ms-file-permission-key should be specified.
        :type file_permission: str
        :param file_permission_key: Key of the permission to be set for the
         directory/file. Note: Only one of the x-ms-file-permission or
         x-ms-file-permission-key should be specified.
        :type file_permission_key: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if file_permission is not None:
            header_parameters['x-ms-file-permission'] = self._serialize.header("file_permission", file_permission, 'str')
        if file_permission_key is not None:
            header_parameters['x-ms-file-permission-key'] = self._serialize.header("file_permission_key", file_permission_key, 'str')
        header_parameters['x-ms-file-attributes'] = self._serialize.header("file_attributes", file_attributes, 'str')
        header_parameters['x-ms-file-creation-time'] = self._serialize.header("file_creation_time", file_creation_time, 'str')
        header_parameters['x-ms-file-last-write-time'] = self._serialize.header("file_last_write_time", file_last_write_time, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-request-server-encrypted': self._deserialize('bool', response.headers.get('x-ms-request-server-encrypted')),
                'x-ms-file-permission-key': self._deserialize('str', response.headers.get('x-ms-file-permission-key')),
                'x-ms-file-attributes': self._deserialize('str', response.headers.get('x-ms-file-attributes')),
                'x-ms-file-creation-time': self._deserialize('str', response.headers.get('x-ms-file-creation-time')),
                'x-ms-file-last-write-time': self._deserialize('str', response.headers.get('x-ms-file-last-write-time')),
                'x-ms-file-change-time': self._deserialize('str', response.headers.get('x-ms-file-change-time')),
                'x-ms-file-id': self._deserialize('str', response.headers.get('x-ms-file-id')),
                'x-ms-file-parent-id': self._deserialize('str', response.headers.get('x-ms-file-parent-id')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    create.metadata = {'url': '/{shareName}/{directory}'}

    def get_properties(self, sharesnapshot=None, timeout=None, cls=None, **kwargs):
        """Returns all system properties for the specified directory, and can also
        be used to check the existence of a directory. The data returned does
        not include the files in the directory or any subdirectories.

        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-meta': self._deserialize('{str}', response.headers.get('x-ms-meta')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-server-encrypted': self._deserialize('bool', response.headers.get('x-ms-server-encrypted')),
                'x-ms-file-attributes': self._deserialize('str', response.headers.get('x-ms-file-attributes')),
                'x-ms-file-creation-time': self._deserialize('str', response.headers.get('x-ms-file-creation-time')),
                'x-ms-file-last-write-time': self._deserialize('str', response.headers.get('x-ms-file-last-write-time')),
                'x-ms-file-change-time': self._deserialize('str', response.headers.get('x-ms-file-change-time')),
                'x-ms-file-permission-key': self._deserialize('str', response.headers.get('x-ms-file-permission-key')),
                'x-ms-file-id': self._deserialize('str', response.headers.get('x-ms-file-id')),
                'x-ms-file-parent-id': self._deserialize('str', response.headers.get('x-ms-file-parent-id')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    get_properties.metadata = {'url': '/{shareName}/{directory}'}

    def delete(self, timeout=None, cls=None, **kwargs):
        """Removes the specified empty directory. Note that the directory must be
        empty before it can be deleted.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    delete.metadata = {'url': '/{shareName}/{directory}'}

    def set_properties(self, file_attributes="none", file_creation_time="now", file_last_write_time="now", timeout=None, file_permission="inherit", file_permission_key=None, cls=None, **kwargs):
        """Sets properties on the directory.

        :param file_attributes: If specified, the provided file attributes
         shall be set. Default value: ‘Archive’ for file and ‘Directory’ for
         directory. ‘None’ can also be specified as default.
        :type file_attributes: str
        :param file_creation_time: Creation time for the file/directory.
         Default value: Now.
        :type file_creation_time: str
        :param file_last_write_time: Last write time for the file/directory.
         Default value: Now.
        :type file_last_write_time: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param file_permission: If specified the permission (security
         descriptor) shall be set for the directory/file. This header can be
         used if Permission size is <= 8KB, else x-ms-file-permission-key
         header shall be used. Default value: Inherit. If SDDL is specified as
         input, it must have owner, group and dacl. Note: Only one of the
         x-ms-file-permission or x-ms-file-permission-key should be specified.
        :type file_permission: str
        :param file_permission_key: Key of the permission to be set for the
         directory/file. Note: Only one of the x-ms-file-permission or
         x-ms-file-permission-key should be specified.
        :type file_permission_key: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "properties"

        # Construct URL
        url = self.set_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if file_permission is not None:
            header_parameters['x-ms-file-permission'] = self._serialize.header("file_permission", file_permission, 'str')
        if file_permission_key is not None:
            header_parameters['x-ms-file-permission-key'] = self._serialize.header("file_permission_key", file_permission_key, 'str')
        header_parameters['x-ms-file-attributes'] = self._serialize.header("file_attributes", file_attributes, 'str')
        header_parameters['x-ms-file-creation-time'] = self._serialize.header("file_creation_time", file_creation_time, 'str')
        header_parameters['x-ms-file-last-write-time'] = self._serialize.header("file_last_write_time", file_last_write_time, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-request-server-encrypted': self._deserialize('bool', response.headers.get('x-ms-request-server-encrypted')),
                'x-ms-file-permission-key': self._deserialize('str', response.headers.get('x-ms-file-permission-key')),
                'x-ms-file-attributes': self._deserialize('str', response.headers.get('x-ms-file-attributes')),
                'x-ms-file-creation-time': self._deserialize('str', response.headers.get('x-ms-file-creation-time')),
                'x-ms-file-last-write-time': self._deserialize('str', response.headers.get('x-ms-file-last-write-time')),
                'x-ms-file-change-time': self._deserialize('str', response.headers.get('x-ms-file-change-time')),
                'x-ms-file-id': self._deserialize('str', response.headers.get('x-ms-file-id')),
                'x-ms-file-parent-id': self._deserialize('str', response.headers.get('x-ms-file-parent-id')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_properties.metadata = {'url': '/{shareName}/{directory}'}

    def set_metadata(self, timeout=None, metadata=None, cls=None, **kwargs):
        """Updates user defined metadata for the specified directory.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param metadata: A name-value pair to associate with a file storage
         object.
        :type metadata: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "metadata"

        # Construct URL
        url = self.set_metadata.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-request-server-encrypted': self._deserialize('bool', response.headers.get('x-ms-request-server-encrypted')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_metadata.metadata = {'url': '/{shareName}/{directory}'}

    def list_files_and_directories_segment(self, prefix=None, sharesnapshot=None, marker=None, maxresults=None, timeout=None, cls=None, **kwargs):
        """Returns a list of files or directories under the specified share or
        directory. It lists the contents only for a single level of the
        directory hierarchy.

        :param prefix: Filters the results to return only entries whose name
         begins with the specified prefix.
        :type prefix: str
        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param marker: A string value that identifies the portion of the list
         to be returned with the next list operation. The operation returns a
         marker value within the response body if the list returned was not
         complete. The marker value may then be used in a subsequent call to
         request the next set of list items. The marker value is opaque to the
         client.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return.
         If the request does not specify maxresults, or specifies a value
         greater than 5,000, the server will return up to 5,000 items.
        :type maxresults: int
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: ListFilesAndDirectoriesSegmentResponse or the result of
         cls(response)
        :rtype:
         ~azure.storage.fileshare.models.ListFilesAndDirectoriesSegmentResponse
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "list"

        # Construct URL
        url = self.list_files_and_directories_segment.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if prefix is not None:
            query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if maxresults is not None:
            query_parameters['maxresults'] = self._serialize.query("maxresults", maxresults, 'int', minimum=1)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ListFilesAndDirectoriesSegmentResponse', response)
            header_dict = {
                'Content-Type': self._deserialize('str', response.headers.get('Content-Type')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    list_files_and_directories_segment.metadata = {'url': '/{shareName}/{directory}'}

    def list_handles(self, marker=None, maxresults=None, timeout=None, sharesnapshot=None, recursive=None, cls=None, **kwargs):
        """Lists handles for directory.

        :param marker: A string value that identifies the portion of the list
         to be returned with the next list operation. The operation returns a
         marker value within the response body if the list returned was not
         complete. The marker value may then be used in a subsequent call to
         request the next set of list items. The marker value is opaque to the
         client.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return.
         If the request does not specify maxresults, or specifies a value
         greater than 5,000, the server will return up to 5,000 items.
        :type maxresults: int
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param recursive: Specifies operation should apply to the directory
         specified in the URI, its files, its subdirectories and their files.
        :type recursive: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: ListHandlesResponse or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListHandlesResponse
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "listhandles"

        # Construct URL
        url = self.list_handles.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if maxresults is not None:
            query_parameters['maxresults'] = self._serialize.query("maxresults", maxresults, 'int', minimum=1)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        if recursive is not None:
            header_parameters['x-ms-recursive'] = self._serialize.header("recursive", recursive, 'bool')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ListHandlesResponse', response)
            header_dict = {
                'Content-Type': self._deserialize('str', response.headers.get('Content-Type')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    list_handles.metadata = {'url': '/{shareName}/{directory}'}

    def force_close_handles(self, handle_id, timeout=None, marker=None, sharesnapshot=None, recursive=None, cls=None, **kwargs):
        """Closes all handles open for given directory.

        :param handle_id: Specifies handle ID opened on the file or directory
         to be closed. Asterisk (‘*’) is a wildcard that specifies all handles.
        :type handle_id: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param marker: A string value that identifies the portion of the list
         to be returned with the next list operation. The operation returns a
         marker value within the response body if the list returned was not
         complete. The marker value may then be used in a subsequent call to
         request the next set of list items. The marker value is opaque to the
         client.
        :type marker: str
        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param recursive: Specifies operation should apply to the directory
         specified in the URI, its files, its subdirectories and their files.
        :type recursive: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.fileshare.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "forceclosehandles"

        # Construct URL
        url = self.force_close_handles.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-handle-id'] = self._serialize.header("handle_id", handle_id, 'str')
        if recursive is not None:
            header_parameters['x-ms-recursive'] = self._serialize.header("recursive", recursive, 'bool')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-marker': self._deserialize('str', response.headers.get('x-ms-marker')),
                'x-ms-number-of-handles-closed': self._deserialize('int', response.headers.get('x-ms-number-of-handles-closed')),
                'x-ms-number-of-handles-failed': self._deserialize('int', response.headers.get('x-ms-number-of-handles-failed')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    force_close_handles.metadata = {'url': '/{shareName}/{directory}'}
