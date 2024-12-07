from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    print("=" * 50)
    print("Packet Captured:")
    
    
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP       : {src_ip}")
        print(f"Destination IP  : {dst_ip}")
        print(f"Protocol        : {protocol}")

    # Check for TCP, UDP, or ICMP protocols
    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"TCP Source Port : {src_port}")
        print(f"TCP Dest. Port  : {dst_port}")
    elif UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        print(f"UDP Source Port : {src_port}")
        print(f"UDP Dest. Port  : {dst_port}")
    elif ICMP in packet:
        icmp_type = packet[ICMP].type
        icmp_code = packet[ICMP].code
        print(f"ICMP Type       : {icmp_type}")
        print(f"ICMP Code       : {icmp_code}")
    
    print("=" * 50)

# sniffing packets
print("Starting packet sniffing...")
sniff(prn=process_packet)
