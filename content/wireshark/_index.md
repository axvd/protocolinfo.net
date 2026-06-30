---
title: "Wireshark Guide"
description: "Wireshark filters, packet analysis examples, and troubleshooting workflows."
weight: 30
---

# Wireshark Guide

This section provides packet analysis references and troubleshooting examples.

## Topics

- Display filters
- Capture filters
- TCP analysis
- DNS analysis
- TLS handshake analysis
- MTU troubleshooting
- Retransmission analysis
- Duplicate ACK analysis
- Zero window analysis

## Example Filters

```text
tcp
udp
dns
icmp
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.window_size == 0
```
