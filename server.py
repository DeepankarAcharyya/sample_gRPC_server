import grpc
from concurrent import futures
import time

import service_pb2
import service_pb2_grpc

class EchoService(service_pb2_grpc.EchoServiceServicer):

    def Echo(self, request, context):
        # Simply return the message received in the request
        return service_pb2.EchoResponse(message=request.message)

def serve():
    # Specify the server with which port to listen on
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_EchoServiceServicer_to_server(EchoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    try:
        # Keep the server running
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
