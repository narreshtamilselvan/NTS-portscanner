import socket
import threading
from queue import Queue
from datetime import datetime

print("=== Advanced Python Port Scanner ===")

target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
thread_count = int(input("Enter number of threads (50-200 recommended): "))

print(f"\nScanning {target} from port {start_port} to {end_port}")
print("Scan started at:", datetime.now())
print("-" * 50)

queue = Queue()
open_ports = []

# Banner grabbing function
def grab_banner(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return "No Banner"

# Port scanning function
def scan():
    while not queue.empty():
        port = queue.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"

                banner = grab_banner(sock)

                print(f"\033[92m[OPEN]\033[0m Port {port} | Service: {service} | Banner: {banner}")
                open_ports.append(port)

            sock.close()
        except:
            pass

        queue.task_done()


# Fill queue with ports
for port in range(start_port, end_port + 1):
    queue.put(port)

# Create thread pool
for _ in range(thread_count):
    t = threading.Thread(target=scan)
    t.daemon = True
    t.start()

queue.join()

print("-" * 50)
print("Scan completed at:", datetime.now())
print("Total open ports found:", len(open_ports))

# Save results to file
with open("scan_results.txt", "w") as file:
    file.write(f"Scan results for {target}\n")
    file.write(f"Open Ports: {open_ports}\n")

print("Results saved to scan_results.txt")
