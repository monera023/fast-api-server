A fastApi server which acts as a client for a grpc server and a FastApi rest server.

The idea of having 2 similar servers is to a get comparative analysis while building same features in both. 

**Pre setup**

Create virtual env:
python3 -m venv venv; source venv/bin/activate

Install dependencies:
pip3 install -r requirements.txt

Generate Proto files:
cd fastApiServer
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. chatMessage.proto

cd grpcServer
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. chatMessage.proto

**Steps to start all servers**

FastApi Client Server:
This received http calls. And then based on endpoint passes it to either grpc server or rest server
Runs on port: 8080
Command to run server: uvicorn main:app --host 0.0.0.0 --port 8080

Grpc server:
Receives grpc requests.
Runs on port: 50052
Command to run server: python3 grpcServer/gprc_server.py 

FastApi Rest Server:
Recevies http requests.
Runs on port: 8081
Command to run server: uvicorn restMain:app --host 0.0.0.0 --port 8081


Steps for Docker:

docker build -t fastapi-app .

docker run -p 8080:8080 fastapi-app
