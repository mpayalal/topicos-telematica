# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.clientStreaming = channel.stream_unary(
                '/sendfile.ProductService/clientStreaming',
                request_serializer=Service__pb2.Request.SerializeToString,
                response_deserializer=Service__pb2.Response.FromString,
                )
        self.clientSingle = channel.unary_unary(
                '/sendfile.ProductService/clientSingle',
                request_serializer=Service__pb2.RequestSimple.SerializeToString,
                response_deserializer=Service__pb2.ResponseSimple.FromString,
                )
        self.open = channel.unary_unary(
                '/sendfile.ProductService/open',
                request_serializer=Service__pb2.openRequest.SerializeToString,
                response_deserializer=Service__pb2.openResponse.FromString,
                )
        self.read = channel.unary_unary(
                '/sendfile.ProductService/read',
                request_serializer=Service__pb2.readRequest.SerializeToString,
                response_deserializer=Service__pb2.readResponse.FromString,
                )
        self.write = channel.unary_unary(
                '/sendfile.ProductService/write',
                request_serializer=Service__pb2.writeRequest.SerializeToString,
                response_deserializer=Service__pb2.writeResponse.FromString,
                )
        self.sendFile = channel.unary_unary(
                '/sendfile.ProductService/sendFile',
                request_serializer=Service__pb2.fileRequest.SerializeToString,
                response_deserializer=Service__pb2.fileResponse.FromString,
                )
        self.copyPart = channel.unary_unary(
                '/sendfile.ProductService/copyPart',
                request_serializer=Service__pb2.copyRequest.SerializeToString,
                response_deserializer=Service__pb2.copyResponse.FromString,
                )
        self.distributeFiles = channel.unary_unary(
                '/sendfile.ProductService/distributeFiles',
                request_serializer=Service__pb2.distributeFilesRequest.SerializeToString,
                response_deserializer=Service__pb2.distributeFilesResponse.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def clientStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def clientSingle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def open(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def copyPart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def distributeFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'clientStreaming': grpc.stream_unary_rpc_method_handler(
                    servicer.clientStreaming,
                    request_deserializer=Service__pb2.Request.FromString,
                    response_serializer=Service__pb2.Response.SerializeToString,
            ),
            'clientSingle': grpc.unary_unary_rpc_method_handler(
                    servicer.clientSingle,
                    request_deserializer=Service__pb2.RequestSimple.FromString,
                    response_serializer=Service__pb2.ResponseSimple.SerializeToString,
            ),
            'open': grpc.unary_unary_rpc_method_handler(
                    servicer.open,
                    request_deserializer=Service__pb2.openRequest.FromString,
                    response_serializer=Service__pb2.openResponse.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=Service__pb2.readRequest.FromString,
                    response_serializer=Service__pb2.readResponse.SerializeToString,
            ),
            'write': grpc.unary_unary_rpc_method_handler(
                    servicer.write,
                    request_deserializer=Service__pb2.writeRequest.FromString,
                    response_serializer=Service__pb2.writeResponse.SerializeToString,
            ),
            'sendFile': grpc.unary_unary_rpc_method_handler(
                    servicer.sendFile,
                    request_deserializer=Service__pb2.fileRequest.FromString,
                    response_serializer=Service__pb2.fileResponse.SerializeToString,
            ),
            'copyPart': grpc.unary_unary_rpc_method_handler(
                    servicer.copyPart,
                    request_deserializer=Service__pb2.copyRequest.FromString,
                    response_serializer=Service__pb2.copyResponse.SerializeToString,
            ),
            'distributeFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.distributeFiles,
                    request_deserializer=Service__pb2.distributeFilesRequest.FromString,
                    response_serializer=Service__pb2.distributeFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sendfile.ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def clientStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/sendfile.ProductService/clientStreaming',
            Service__pb2.Request.SerializeToString,
            Service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def clientSingle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/clientSingle',
            Service__pb2.RequestSimple.SerializeToString,
            Service__pb2.ResponseSimple.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/open',
            Service__pb2.openRequest.SerializeToString,
            Service__pb2.openResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/read',
            Service__pb2.readRequest.SerializeToString,
            Service__pb2.readResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/write',
            Service__pb2.writeRequest.SerializeToString,
            Service__pb2.writeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/sendFile',
            Service__pb2.fileRequest.SerializeToString,
            Service__pb2.fileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def copyPart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/copyPart',
            Service__pb2.copyRequest.SerializeToString,
            Service__pb2.copyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def distributeFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendfile.ProductService/distributeFiles',
            Service__pb2.distributeFilesRequest.SerializeToString,
            Service__pb2.distributeFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
