import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # faster scanning
        result = s.connect_ex((host, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"
            print(f"Port {port} is OPEN  --> Service: {service}")
            open_ports.append((port, service))
        s.close()

        if not open_ports:
            print("\nNo open ports found.")
        else:
            print("\nOpen ports and services:")
            for port, service in open_ports:
                print(f"  Port {port} : {service}")

# Example usage:
target_host = input("Enter IP Address: ")  # Change this to any IP
scan_ports(target_host, 20, 500) # Change this to desire Port Number Range
