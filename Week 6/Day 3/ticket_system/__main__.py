from modules.request_stream import RequestGenerator
from modules.load_balancer import LoadBalancer
from modules.server import Server
from modules.tickets_generator import TicketsGenerator


if __name__ == "__main__":
    ticket_generator = TicketsGenerator()
    ticket_generator.genrate_500_tickets()
    request_generator = RequestGenerator()
    load_balancer = LoadBalancer(request_generator)
    server = Server("./data/tickets.json", requests_threshold_delay=1, max_concurrent_requests=2)
    server2 = Server("./data/tickets.json", requests_threshold_delay=1, max_concurrent_requests=2)
    load_balancer.add_server(server)
    load_balancer.add_server(server2)

    load_balancer.process_events()
