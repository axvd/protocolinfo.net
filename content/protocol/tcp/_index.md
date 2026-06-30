---
title: "Transmission Control Protocol"
description: "Transmission Control Protocol article page with ProtocolInfo.net TCP header reference placed at the top."
weight: 10
source_url: "https://en.wikipedia.org/wiki/Transmission_Control_Protocol"
source_name: "Wikipedia: Transmission Control Protocol"
license_note: "The source article is licensed under Creative Commons Attribution-ShareAlike. Keep attribution when importing or updating content."
---

# Transmission Control Protocol

## ProtocolInfo TCP Header Reference

The TCP header is arranged in 32-bit rows. The first row contains the source and destination ports. The next two rows carry the sequence and acknowledgment numbers. The following rows contain header length, control flags, flow-control information, checksum, urgent pointer, options, padding, and payload data.

```text
 0                   15 16                  31
+---------------------+---------------------+
| Source Port         | Destination Port    |
+---------------------+---------------------+
| Sequence Number                           |
+-------------------------------------------+
| Acknowledgment Number                     |
+----+------+----------+--------------------+
|Off |Resvd | Flags    | Window             |
+----+------+----------+--------------------+
| Checksum            | Urgent Pointer      |
+---------------------+---------------------+
| Options and Padding                       |
+-------------------------------------------+
| Data                                      |
+-------------------------------------------+
```

### Header Field Summary

| Field | Size | Description |
|---|---:|---|
| Source Port | 16 bits | Identifies the sending application port. |
| Destination Port | 16 bits | Identifies the receiving application port. |
| Sequence Number | 32 bits | Identifies the sequence number of the first data byte in this segment. |
| Acknowledgment Number | 32 bits | Indicates the next sequence number expected by the sender of the acknowledgment. |
| Data Offset | 4 bits | Indicates the TCP header length in 32-bit words. |
| Reserved | Variable | Reserved for future use. |
| Flags | Variable | TCP control bits such as SYN, ACK, FIN, RST, PSH, and URG. |
| Window | 16 bits | Indicates the receive window size. |
| Checksum | 16 bits | Provides error detection for the TCP header and payload. |
| Urgent Pointer | 16 bits | Points to urgent data when the URG flag is set. |
| Options and Padding | Variable | Carries optional TCP parameters such as MSS, SACK, timestamps, and window scaling. |
| Data | Variable | Application payload carried by TCP. |

---

## Article Body

Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. It provides reliable, ordered, and error-checked delivery of a byte stream between applications running on hosts communicating through an IP network.

TCP is connection-oriented. Before application data is exchanged, the endpoints establish a connection using a three-way handshake. This connection model supports reliable delivery, retransmission, flow control, and congestion control.

Major Internet applications such as web browsing, email, remote administration, file transfer, and secure communication commonly rely on TCP.

## Historical Origin

TCP originated from early work on packet-switched internetworking and the original Transmission Control Program. The architecture later separated the functions of TCP and IP, producing the TCP/IP model used by the Internet.

## Network Function

TCP provides a reliable byte-stream service between applications. IP may deliver packets out of order, lose packets, duplicate packets, or delay packets. TCP hides many of these network-layer behaviors from applications by using sequence numbers, acknowledgments, retransmission, checksums, and ordering.

## TCP Segment Structure

A TCP segment contains a TCP header and optional data. The TCP header includes port numbers, sequence and acknowledgment numbers, header length, flags, window size, checksum, urgent pointer, and optional parameters.

## Protocol Operation

### Connection Establishment

TCP commonly establishes connections through a three-way handshake:

```text
Client                                      Server
  |                                           |
  |  SYN                                      |
  |------------------------------------------>|
  |                                           |
  |  SYN, ACK                                 |
  |<------------------------------------------|
  |                                           |
  |  ACK                                      |
  |------------------------------------------>|
  |                                           |
```

### Connection Termination

TCP connections are usually closed using FIN and ACK segments.

```text
Host A                                      Host B
  |                                           |
  |  FIN                                      |
  |------------------------------------------>|
  |                                           |
  |  ACK                                      |
  |<------------------------------------------|
  |                                           |
  |  FIN                                      |
  |<------------------------------------------|
  |                                           |
  |  ACK                                      |
  |------------------------------------------>|
```

### Data Transfer

TCP uses sequence numbers and acknowledgments to provide reliable ordered delivery. Missing data can be retransmitted, and out-of-order data can be reordered before being delivered to the application.

### Error Detection

TCP uses a checksum to detect corruption in the TCP header and payload.

### Flow Control

TCP uses a receive window to prevent a sender from overwhelming the receiver.

### Congestion Control

TCP congestion control reduces transmission rate when the network appears congested.

## TCP Ports

TCP uses port numbers to identify application endpoints. A TCP connection is commonly identified by source IP address, source port, destination IP address, destination port, and protocol.

| Port | Common Use |
|---:|---|
| 22 | SSH |
| 25 | SMTP |
| 80 | HTTP |
| 443 | HTTPS |
| 993 | IMAPS |

## Vulnerabilities

TCP can be affected by denial-of-service attacks, connection hijacking, spoofed reset packets, and resource exhaustion. Common mitigations include SYN cookies, randomized initial sequence numbers, firewall filtering, and rate limiting.

## Wireshark Filters

```text
tcp
tcp.port == 443
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.flags.reset == 1
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.window_size == 0
```

## Related RFCs

| RFC | Description |
|---|---|
| RFC 9293 | Current TCP specification |
| RFC 793 | Original TCP specification |
| RFC 1122 | Requirements for Internet Hosts |
| RFC 2018 | TCP Selective Acknowledgment Options |
| RFC 5681 | TCP Congestion Control |
| RFC 6298 | TCP Retransmission Timer |
| RFC 7323 | TCP Extensions for High Performance |

## Related Protocols

- IPv4
- IPv6
- UDP
- TLS
- HTTP
- QUIC
- SCTP

## Source and Attribution

This page is based on the English Wikipedia article:

- Source: <https://en.wikipedia.org/wiki/Transmission_Control_Protocol>
- License: Creative Commons Attribution-ShareAlike

ProtocolInfo.net adds the TCP header diagram, field summary, Wireshark filters, RFC mapping, and operational reference sections.
