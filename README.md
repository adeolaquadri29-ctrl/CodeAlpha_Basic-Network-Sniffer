# CodeAlpha_Basic-Network-Sniffer
A SOC-style network traffic analysis project using Python and Scapy to capture, inspect, and analyze live packets, demonstrating protocol behavior, traffic flow, and basic incident detection.


# 🛡️ CodeAlpha Basic Network Sniffer (Python + Scapy)

Python
Scapy
Status

---

## 📌 Project Overview

This project is a lightweight network packet sniffer built using Python and Scapy. It captures live network traffic and extracts critical packet information such as source IP, destination IP, protocol type, and payload data.

The project simulates basic SOC (Security Operations Center) monitoring by analyzing network activity in real-time.

---

## 🎯 Objectives

- Capture live network packets
- Analyze packet structure and protocol behavior
- Understand how data flows across networks
- Simulate basic traffic monitoring and detection

---

## ⚙️ Architecture

[ Network Traffic ]         ↓ [ Scapy Sniffer Engine ]         ↓ [ Packet Processing Function ]         ↓ [ Data Extraction ] (SRC IP | DST IP | Protocol | Payload)         ↓ [ Console Output / Analysis ]

---

## 🚀 Features

- Live packet capture
- Source & Destination IP extraction
- Protocol identification (TCP, UDP, ICMP)
- Payload inspection
- Real-time traffic monitoring

---

## 🧪 Attack Simulation / Traffic Scenarios

To generate traffic for analysis:

- ICMP Traffic:
    ping google.com  

- Web Traffic:
  Browse any website

- DNS Queries:
  Perform searches online

---

## 🔍 Detection & Analysis

During packet capture, the following indicators can be observed:

- High volume of ICMP packets → Possible ping flood (DoS)
- Repeated connections → Potential scanning activity
- Unknown payload patterns → Suspicious traffic

Example Output:
[+] SRC: 192.168.0.117 [+] DST: 192.168.0.1
[+] PROTOCOL: ICMP
[+] PAYLOAD: b'E\x00\x00T\x89\x990\x000\x01/I\xc0\xa8\x00u\xc0\xa8\x0
0\x01\x08\x00\xa8\xa0n\xa9\×00\x12tQ\xf01\x00\x00\x00\x00\xb3\x15\n\x00\x00\x
00\x00\x00\x10\x11\x12\x13\x14\x15°

---

## 🚨 Incident Response Insights

From analysis, the following actions can be considered:

- Identify suspicious IP addresses
- Monitor abnormal traffic spikes
- Filter malicious protocols
- Apply firewall rules if necessary

---

## 📚 Lessons Learned

- Understanding packet structure (IP, TCP, UDP, ICMP)
- How network traffic flows in real-time
- Basics of packet inspection and analysis
- Importance of monitoring for security

---

## 🧠 Skills Gained

- Network Traffic Analysis
- Packet Inspection
- Python for Cybersecurity
- Protocol Analysis
- Security Monitoring Fundamentals

---

## 🛠️ Tools Used

- Python 3
- Scapy
- Networking Concepts

---

## ⚙️ Setup Guide

1. Install dependencies:
      pip install -r requirements.txt   

1. Run the sniffer:
      sudo python3 sniffer.py   

1. Generate traffic:
      ping google.com   

---

## 📸 Screenshots

### Packet Capture
Packet Capture

### Live Traffic
Live Traffic

---

## ⚠️ Ethical Use Disclaimer

This project is intended strictly for educational purposes and authorized network monitoring only. Unauthorized packet sniffing is illegal.

---

## 👤 Author

Adeola Quadri  
Cybersecurity Enthusiast | SOC Analyst in Training
