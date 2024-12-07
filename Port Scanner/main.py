import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning host: {host}")
    print("-" * 50)
    
    for port in range(start_port, end_port + 1):
        try:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Set timeout for faster scanning
                result = s.connect_ex((host, port))  # Attempt to connect to the port
                
                # If port=open
                if result == 0:
                    print(f"Port: {port}\tState: open")
                else:
                    print(f"Port: {port}\tState: closed")
        
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    print("-" * 50)
    print("Scan complete.")

if __name__ == "__main__":
    target_host = input("Enter the target host (e.g., 127.0.0.1): ").strip()
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 1024): "))    
    scan_ports(target_host, start_port, end_port)