from concurrent import futures
import grpc
import chatMessage_pb2_grpc
import chatMessage_pb2
import time

class ChatServerServicer(chatMessage_pb2_grpc.ChatServerServicer):
    def Create(self, request,  context):
        print(request)
        return chatMessage_pb2.ChatCreateResponse(success=True)

    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatMessage_pb2_grpc.add_ChatServerServicer_to_server(ChatServerServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Started grpc server at 50052...")

    try:
        while True:
            time.sleep(86500)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()