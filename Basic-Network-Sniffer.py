from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0

def process_packet(packet):
    global packet_count
    packet_count += 1

    print("\n" + "="*60)
    print(f"[+] Packet Number : {packet_count}")
    print(f"[+] Timestamp     : {datetime.now()}")

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"[+] Source IP     : {src_ip}")
        print(f"[+] Destination IP: {dst_ip}")

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "OTHER"

        print(f"[+] Protocol      : {protocol}")

        # Extract payload safely
        try:
            payload = bytes(packet.payload)
            print(f"[+] Payload       : {payload[:100]}")
        except:
            print("[+] Payload       : Not readable")

print("[*] Starting Network Sniffer...")
print("[*] Press CTRL+C to stop.\n")

sniff(prn=process_packet, store=False)
