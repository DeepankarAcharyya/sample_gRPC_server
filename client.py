import grpc

import service_pb2
import service_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = service_pb2_grpc.EchoServiceStub(channel)
        
        # Create an EchoRequest object
        response = stub.Echo(service_pb2.EchoRequest(message="Hello World!"))
        
        # Print the response from the server
        print("Echo response received: " + response.message)

if __name__ == '__main__':
    run()