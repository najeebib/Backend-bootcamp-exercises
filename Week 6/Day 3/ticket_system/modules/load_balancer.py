from .request_stream import RequestGenerator
from .request import Request
from .server import Server
import time
import threading
class LoadBalancer:
    def __init__(self, request_generator: RequestGenerator):
        self.request_generator = request_generator
        self.servers = []
        self.num_of_servers = 0
        self.last_server_index = 0

    def add_server(self, server: Server):
        self.servers.append(server)
        self.num_of_servers += 1
        
    def process_events(self):
        for request in self.request_generator.generate_requests():
            self.handle_event(request)

    def handle_event(self, request: Request):
        # assign server to process the request using round robin
        ### ok chice - remember to thing what are the upsides and downsides
        server = self.servers[self.last_server_index]
        status = server.process_request(request)
        while True:
            try:
                status = server.process_request(request)
                if not status:
                    self.request_generator.remove_event(request.get_event())
                break  # break out of the retry loop if process_request succeeds
            except Exception as e:# when exception is raised cuz server cant handle more requestrs
                ### better is to seperate or specify the exact exception
                print(f"An error occurred: {e}. Retrying in 5 seconds...")
                time.sleep(1)# wait intill one of the servers are available
                continue  # retry process_request

        self.last_server_index = (self.last_server_index + 1) % self.num_of_servers

        print("Received event:", request)
        print(f"Event processed by server {server}")
