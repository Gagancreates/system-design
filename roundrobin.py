class RR:
    def __init__(self, servers):
        if not servers:
            raise ValueError("NO SERVERS IN THE INPUT")
        self.server=servers
        self.server_index=0

    def get_server(self):
        server=self.server[self.server_index]
        self.server_index=(self.server_index+1)%(len(self.server))

        return server

if __name__ == "__main__":
    # Define a list of backend servers.
    backend_servers = [
        "http://server-a.api",
        "http://server-b.api",
        "http://server-c.api",
    ]

    # Create an instance of the load balancer.
    load_balancer = RR(backend_servers)

    print("Simulating 10 requests to the load balancer:")
    print("-" * 40)

    # Simulate 10 requests and see which server each request is routed to.
    for i in range(1, 11):
        # Get the next server from the load balancer.
        next_server = load_balancer.get_server()
        print(f"Request {i:2}: Routed to -> {next_server}")

    print("\nDemonstrating the next-server method directly:")
    print("-" * 40)
    # The iterator state is maintained, so the next call will continue from where it left off.
    print(f"Next server is: {load_balancer.get_server()}")
    print(f"Next server is: {load_balancer.get_server()}")
