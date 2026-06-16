# Pillar 2 — Networking

> *"Every HTTP request is a negotiation between machines that don't trust each other, across a medium that drops packets, in a protocol stack built from four decades of engineering compromise."*

---

## Table of Contents

1. [The Internet](#1-the-internet)
2. [Network Models — OSI and TCP/IP](#2-network-models)
3. [IP Addresses](#3-ip-addresses)
4. [MAC Addresses](#4-mac-addresses)
5. [DNS](#5-dns)
6. [Ports](#6-ports)
7. [TCP](#7-tcp)
8. [UDP](#8-udp)
9. [HTTP](#9-http)
10. [HTTPS and TLS](#10-https-and-tls)
11. [The Full Request Lifecycle](#11-the-full-request-lifecycle)
12. [Cookies](#12-cookies)
13. [HTTP Headers](#13-http-headers)
14. [CORS](#14-cors)
15. [Load Balancers](#15-load-balancers)
16. [Proxies and Reverse Proxies](#16-proxies-and-reverse-proxies)
17. [CDNs](#17-cdns)
18. [WebSockets](#18-websockets)
19. [Server-Sent Events (SSE)](#19-server-sent-events)

---

## 1. The Internet

### Definition

The Internet is a global system of interconnected computer networks that communicate using a standardized protocol suite (TCP/IP). It is not one network — it is a **network of networks**: ISPs, universities, corporations, data centers, and home routers all maintain independent networks, and the Internet is the agreements and infrastructure that lets them route packets between each other.

### Historical Context

The Internet's direct ancestor is **ARPANET** (1969), funded by the US Defense Advanced Research Projects Agency. ARPANET's design goal was a communications network that could survive partial failures — if nodes were destroyed, packets would find alternate routes. This design principle — **decentralized, packet-switched routing** — is the Internet's DNA.

Key milestones:
- 1969: ARPANET first message (UCLA → Stanford — the system crashed after "LO" of "LOGIN")
- 1973: TCP/IP conceptualized by Vint Cerf and Bob Kahn
- 1983: ARPANET migrates to TCP/IP ("flag day")
- 1991: Tim Berners-Lee invents the World Wide Web (HTTP + HTML + URLs) at CERN
- 1993: Mosaic web browser — mass adoption begins
- 1994: Netscape, SSL encryption for the web
- 2000: Internet backbone privatized; dot-com infrastructure largely in place

### Packet Switching vs. Circuit Switching

The telephone network used **circuit switching**: before a call, a dedicated physical circuit is established end-to-end. Resources are reserved for the entire call duration. If one node fails, the call drops.

The Internet uses **packet switching**: data is broken into packets. Each packet carries a destination address. Each router independently decides where to forward each packet. Packets from the same "connection" may take different routes through the network. If one node fails, packets route around it.

```
Circuit Switching (telephone):
  Sender ──[dedicated wire]──────────────────── Receiver
  One reserved path, no sharing, cannot reroute

Packet Switching (Internet):
  Sender → [Router A] → [Router C] → [Router E] → Receiver
              ↓                          ↑
           [Router B] ──────────────────
  
  Packets may take different paths.
  No single path reserved.
  Routers forward based on best available path.
```

### Autonomous Systems and BGP

The Internet is organized into **Autonomous Systems (AS)** — independently managed networks, each identified by an AS Number (ASN). Google's network is AS15169. Cloudflare is AS13335. Comcast is AS7922.

**BGP (Border Gateway Protocol)** is the routing protocol that lets ASes advertise which IP prefixes they can reach to neighboring ASes. It is the Internet's "postal system" directory — routers use BGP tables to decide which direction to forward packets.

BGP route hijacking (accidentally advertising another AS's IP prefixes) has caused major Internet outages. Pakistan Telecom accidentally hijacked YouTube's IP space in 2008, making YouTube unreachable globally for two hours.

---

## 2. Network Models

### The OSI Model (Theoretical Reference)

The OSI (Open Systems Interconnection) model is a conceptual framework for understanding network communication. It defines 7 layers, each with a specific responsibility:

```
+---+--------------------+-------------------------------------------+
| 7 | Application        | HTTP, SMTP, DNS, FTP                      |
|   |                    | What the user/application sends           |
+---+--------------------+-------------------------------------------+
| 6 | Presentation       | Encoding, encryption, compression         |
|   |                    | TLS lives here (conceptually)             |
+---+--------------------+-------------------------------------------+
| 5 | Session            | Session management, reconnection          |
+---+--------------------+-------------------------------------------+
| 4 | Transport          | TCP, UDP                                  |
|   |                    | Port numbers, reliability, flow control   |
+---+--------------------+-------------------------------------------+
| 3 | Network            | IP, ICMP, routing                         |
|   |                    | IP addresses, routers, packet forwarding  |
+---+--------------------+-------------------------------------------+
| 2 | Data Link          | Ethernet, Wi-Fi (802.11)                  |
|   |                    | MAC addresses, frames, switches           |
+---+--------------------+-------------------------------------------+
| 1 | Physical           | Electrical signals, fiber optics, radio   |
|   |                    | Bits on wire                              |
+---+--------------------+-------------------------------------------+
```

### The TCP/IP Model (Practical)

In practice, networks use the TCP/IP model (4 layers):

```
+--------------------+-------------------------------------------+
| Application        | HTTP, HTTPS, DNS, SMTP, SSH, FTP, WebSocket|
+--------------------+-------------------------------------------+
| Transport          | TCP, UDP                                   |
+--------------------+-------------------------------------------+
| Internet           | IP (IPv4, IPv6), ICMP, ARP                |
+--------------------+-------------------------------------------+
| Network Access     | Ethernet, Wi-Fi, fiber optic drivers       |
+--------------------+-------------------------------------------+
```

### How Encapsulation Works

When you send an HTTP request, each layer **wraps** the data in its own header:

```
Application Layer data:
  [HTTP Request: GET /index.html HTTP/1.1...]

Transport Layer wraps it:
  [TCP Header: src_port=52341, dst_port=80, seq=100, ...]
  [HTTP Request]

Network Layer wraps it:
  [IP Header: src=192.168.1.5, dst=93.184.216.34, ...]
  [TCP Header][HTTP Request]

Data Link Layer wraps it:
  [Ethernet Frame: src_mac=AA:BB:CC:DD:EE:FF, dst_mac=...]
  [IP Header][TCP Header][HTTP Request]

Physical Layer:
  01100101 01001000 00110001... (actual bits on wire)
```

At the receiver, each layer **unwraps** its header and passes the payload up. This is the encapsulation/decapsulation process.

### How to Think About It

> Each layer of the network stack is a team with one job. The HTTP layer says "give this document request to whoever is on port 80 at this IP." The TCP layer says "make sure all the pieces arrive in order and intact." The IP layer says "route this packet toward its destination, one hop at a time." The Ethernet layer says "get this frame to the next device on this physical network segment." They do not know or care about each other's jobs. This separation of concerns is why you can run HTTP over Wi-Fi or fiber or satellite without changing the application.

---

## 3. IP Addresses

### Definition

An IP (Internet Protocol) address is a numerical label assigned to each device on a network that uses IP for communication. It serves two functions: **network identification** (which network?) and **host identification** (which device on that network?).

### IPv4

IPv4 addresses are 32-bit integers, written as four decimal octets separated by dots:

```
192.168.1.100
│   │   │ │
│   │   │ └── Host portion (depends on subnet mask)
│   │   └──── Network portion (depends on subnet mask)
└───┴──────── Network portion (depends on subnet mask)

Total IPv4 space: 2^32 = ~4.3 billion addresses
```

**IPv4 Address Classes and CIDR**:

```
192.168.1.0/24  (CIDR notation)
                 ^^ subnet mask bits
                 
/24 means first 24 bits are the NETWORK, last 8 are HOSTS
  Network:  192.168.1.0
  Hosts:    192.168.1.1  through  192.168.1.254
  Broadcast: 192.168.1.255
  Total: 256 - 2 = 254 usable host addresses

/16 gives 65,534 hosts
/8 gives 16,777,214 hosts
```

**Private IP Ranges** (RFC 1918 — not routable on the public Internet):

```
10.0.0.0/8          (10.x.x.x)          — large private networks
172.16.0.0/12       (172.16.x.x to      — medium private networks
                     172.31.x.x)
192.168.0.0/16      (192.168.x.x)       — home/small office networks
127.0.0.0/8         (127.x.x.x)         — loopback (your machine itself)
```

Your home router gets one public IP from your ISP. Every device in your home gets a private IP. The router uses **NAT (Network Address Translation)** to map outgoing connections from private IPs to the single public IP, maintaining a table of which private device made which connection.

### IPv6

IPv4 exhaustion (we ran out of allocatable IPv4 addresses around 2011–2019) drove adoption of IPv6: 128-bit addresses, providing 2^128 = ~340 undecillion addresses.

```
IPv6 format: eight groups of four hex digits
  2001:0db8:85a3:0000:0000:8a2e:0370:7334
  (can compress consecutive zeros):
  2001:db8:85a3::8a2e:370:7334

Loopback: ::1  (equivalent of 127.0.0.1)
```

### Subnetting (Interview Depth)

Subnetting divides a large network into smaller segments. This is a common interview question for senior engineers:

```
Given: 192.168.10.0/24
Requirement: Divide into 4 equal subnets

Solution:
  Need 4 subnets → need 2 bits for subnet identifier (2^2 = 4)
  Borrow 2 bits from host portion: /24 + 2 = /26

  Subnet 1: 192.168.10.0/26   (hosts: .1 - .62)
  Subnet 2: 192.168.10.64/26  (hosts: .65 - .126)
  Subnet 3: 192.168.10.128/26 (hosts: .129 - .190)
  Subnet 4: 192.168.10.192/26 (hosts: .193 - .254)
  
  Each subnet has 2^(32-26) - 2 = 62 usable hosts
```

---

## 4. MAC Addresses

### Definition

A MAC (Media Access Control) address is a 48-bit hardware identifier burned into a network interface card (NIC) by the manufacturer. It is used for communication within a single network segment (Layer 2). Unlike IP addresses, MAC addresses are not routable — routers strip and replace them at each hop.

```
MAC Address format: 6 bytes in hex, separated by colons
  AA:BB:CC:DD:EE:FF
  │││││
  First 3 bytes: OUI (Organizationally Unique Identifier)
    — identifies the manufacturer
    00:1A:2B = Apple
    00:50:56 = VMware (virtual NIC)
  
  Last 3 bytes: NIC-specific identifier assigned by manufacturer
```

### IP vs. MAC — When Each Is Used

```
Scenario: Your laptop (192.168.1.5) requests google.com (142.250.80.46)

Step 1 — Same network segment (your LAN):
  Your laptop needs to send a packet to your router (192.168.1.1)
  It knows the router's IP (default gateway) but needs its MAC
  → ARP (Address Resolution Protocol): broadcast "who has 192.168.1.1?"
  → Router responds: "I do — my MAC is AA:BB:CC:11:22:33"
  → Packet sent with:
      IP:  src=192.168.1.5,      dst=142.250.80.46  (end-to-end, unchanged)
      MAC: src=your-laptop-MAC,  dst=router-MAC      (hop-specific, changes)

Step 2 — At the router:
  Router strips your MAC header
  Looks up routing table: "142.250.80.46 → send to ISP gateway"
  ARP for ISP gateway's MAC
  Sends packet with:
      IP:  src=192.168.1.5,      dst=142.250.80.46  (unchanged)
      MAC: src=router-MAC,       dst=ISP-gateway-MAC (new hop-specific)

Each hop: IP stays the same, MAC changes
```

**Why this matters for interviews**: When debugging network issues, understanding the IP vs MAC distinction explains why `ping 192.168.1.1` works but `ping 8.8.8.8` doesn't (your router is up but your ISP connection is down). It also explains ARP cache poisoning attacks (a security interview topic).

---

## 5. DNS

### Definition

DNS (Domain Name System) is a distributed, hierarchical database that maps human-readable domain names (e.g., `api.github.com`) to IP addresses (e.g., `140.82.114.5`). It is the Internet's phonebook.

### Why It Exists

IP addresses change. Servers scale horizontally, migrate between data centers, update infrastructure. The domain name provides a stable human-readable identifier that DNS translates to the current IP. Without DNS, every browser bookmark would break when a server's IP changed.

### DNS Hierarchy

```
.  (Root — 13 root server clusters worldwide)
│
├── .com  (TLD — Top-Level Domain, managed by Verisign)
│     ├── github.com  (Authoritative NS — managed by GitHub/their DNS provider)
│     │     └── api.github.com  → 140.82.114.5
│     └── google.com
│
├── .org
├── .io
└── .uk  (country code TLD)
```

### DNS Resolution — Step by Step

When your browser resolves `api.github.com`:

```
1. Browser cache check:
   → Did I already resolve this recently? (TTL not expired?)
   → If yes: return cached IP. DONE.

2. OS resolver cache check (/etc/hosts or Windows host file):
   → Is there a local override?
   → systemd-resolved or nscd cache on Linux?
   → If yes: return. DONE.

3. Recursive resolver query (your ISP's or 8.8.8.8):
   → Your OS sends UDP packet to configured DNS resolver
   (e.g., 8.8.8.8 for Google's resolver)

4. Recursive resolver works the hierarchy:

   a. Query root servers: "Who handles .com?"
      → Root server: "Ask 192.5.6.30 (com. nameserver)"

   b. Query .com TLD servers: "Who handles github.com?"
      → TLD server: "Ask 205.251.196.1 (github.com nameserver)"

   c. Query github.com authoritative NS: "What is api.github.com?"
      → Auth NS: "api.github.com → 140.82.114.5, TTL=60"

5. Recursive resolver caches the result for TTL seconds
   Returns 140.82.114.5 to your OS

6. OS returns to browser, browser caches result
   Browser connects to 140.82.114.5:443
```

```
Your Machine        Recursive Resolver     Root NS     .com NS   Github NS
     │                      │                │            │           │
     │──"api.github.com?"──→│                │            │           │
     │                      │──"who has.com"→│            │           │
     │                      │←──"ask X.X.X.X"│            │           │
     │                      │────────────────────"github.com?"──→│           │
     │                      │◄───────────────────"ask Y.Y.Y.Y"──│           │
     │                      │──────────────────────────────────────→│
     │                      │◄─────────────────────────────────────│
     │                      │           "140.82.114.5, TTL=60"      │
     │◄────"140.82.114.5"───│                │            │           │
```

### DNS Record Types

| Type | Purpose | Example |
|---|---|---|
| A | IPv4 address | `github.com → 140.82.114.5` |
| AAAA | IPv6 address | `github.com → 2606:50c0:8000::154` |
| CNAME | Alias to another hostname | `www.github.com → github.com` |
| MX | Mail exchange server | `github.com → aspmx.l.google.com` |
| TXT | Arbitrary text (SPF, DKIM, domain verification) | `v=spf1 include:...` |
| NS | Authoritative nameservers for the domain | `github.com → ns1.p16.dynect.net` |
| SOA | Start of Authority (zone metadata) | Serial, refresh, retry, expire |
| PTR | Reverse DNS (IP → hostname) | `5.114.82.140.in-addr.arpa → github.com` |
| SRV | Service discovery | `_http._tcp.example.com → priority weight port target` |

### DNS TTL and Caching Implications

TTL (Time To Live) is the duration in seconds that resolvers may cache a record. This has production consequences:

```
Low TTL (60 seconds):
  ✓ DNS changes propagate fast (migration, failover)
  ✗ More DNS queries, higher resolver load, more latency per request
  Use for: active migrations, blue-green deployments

High TTL (86400 = 24 hours):
  ✓ Fewer DNS queries, faster resolution from cache
  ✗ Changes take up to 24h to propagate globally
  Use for: stable, long-lived infrastructure

Operational Reality:
  Before a migration: lower TTL to 60s, wait 24h
  Perform migration
  Update DNS record to new IP
  Propagation is fast (60s TTL already in effect)
  After migration stabilizes: raise TTL back to 3600+
```

### DNS Security

**DNS Spoofing / Cache Poisoning**: An attacker injects false DNS records into a resolver's cache, redirecting traffic to a malicious IP. Mitigation: **DNSSEC** (cryptographically signs DNS records).

**DNS over HTTPS (DoH)**: Encrypts DNS queries inside HTTPS, preventing ISPs from seeing your DNS lookups. Used by Firefox and Chrome. Controversial because it centralizes DNS to providers like Cloudflare and Google.

**DNS Hijacking**: ISPs or malicious actors intercept DNS queries to redirect traffic (e.g., showing ads on NXDOMAIN responses, or nation-state surveillance).

### Implementation: DNS Lookup in Node.js

```javascript
// Basic DNS resolution
const dns = require('dns');
const { promisify } = require('util');

const resolve4 = promisify(dns.resolve4);
const resolveMx = promisify(dns.resolveMx);
const resolveTxt = promisify(dns.resolveTxt);

async function inspectDomain(domain) {
  try {
    const [aRecords, mxRecords, txtRecords] = await Promise.all([
      resolve4(domain),
      resolveMx(domain).catch(() => []),
      resolveTxt(domain).catch(() => []),
    ]);

    console.log(`=== DNS Records for ${domain} ===`);
    console.log('A records (IPv4):', aRecords);
    console.log('MX records (mail):', mxRecords);
    console.log('TXT records:', txtRecords.flat());
  } catch (err) {
    if (err.code === 'ENOTFOUND') {
      console.log(`${domain}: domain does not exist`);
    } else if (err.code === 'ETIMEOUT') {
      console.log(`${domain}: DNS resolver timed out`);
    } else {
      throw err;
    }
  }
}

inspectDomain('github.com');
```

```javascript
// Production DNS health check with fallback resolvers
const dns = require('dns');

class ResilientDNS {
  constructor(resolvers = ['8.8.8.8', '1.1.1.1', '9.9.9.9']) {
    this.resolvers = resolvers;
    this.cache = new Map();
  }

  async resolve(hostname) {
    // Check cache first
    const cached = this.cache.get(hostname);
    if (cached && cached.expires > Date.now()) {
      return cached.addresses;
    }

    // Try each resolver in order
    for (const resolver of this.resolvers) {
      try {
        const addresses = await this._queryResolver(hostname, resolver);
        // Cache with 60 second TTL (in production, respect actual DNS TTL)
        this.cache.set(hostname, {
          addresses,
          expires: Date.now() + 60_000
        });
        return addresses;
      } catch (err) {
        console.warn(`Resolver ${resolver} failed for ${hostname}: ${err.message}`);
        // Try next resolver
      }
    }

    throw new Error(`All DNS resolvers failed for ${hostname}`);
  }

  _queryResolver(hostname, resolverIP) {
    return new Promise((resolve, reject) => {
      const dnsInstance = new dns.Resolver();
      dnsInstance.setServers([resolverIP]);
      
      dnsInstance.resolve4(hostname, (err, addresses) => {
        if (err) reject(err);
        else resolve(addresses);
      });
    });
  }
}

const dnsClient = new ResilientDNS();
const ips = await dnsClient.resolve('api.example.com');
```

### How Interviewers Attack DNS

**Question**: "How does DNS resolution work?"

Follow-up chain:
- "What if the recursive resolver's cache has a stale entry?" → It serves the stale entry until TTL expires. No mechanism forces immediate cache invalidation across the Internet.
- "How does low TTL help during a database migration?" → Lower TTL means caches expire sooner, so the new IP propagates faster after you update the record.
- "Can DNS be a single point of failure?" → Yes. Dyn DNS attack (2016) took down Twitter, Spotify, Reddit for hours by DDoSing a major DNS provider. Mitigation: multiple DNS providers, anycast routing.
- "What's the difference between a CNAME and an A record? When can you NOT use a CNAME?" → CNAME is an alias; cannot use CNAME at the zone apex (root of a domain). `example.com` cannot be a CNAME — only subdomains can. (Solution: ALIAS/ANAME records, or DNS providers that flatten CNAME.)

---

## 6. Ports

### Definition

A port is a 16-bit unsigned integer (0–65535) that identifies a specific process or service on a host. IP addresses identify machines; port numbers identify which service on that machine should receive a packet.

### Port Ranges

```
0 – 1023:     Well-known ports (requires root/admin to bind)
              80:   HTTP
              443:  HTTPS
              22:   SSH
              25:   SMTP (email)
              53:   DNS
              3306: MySQL
              5432: PostgreSQL

1024 – 49151: Registered ports (IANA-registered applications)
              3000: Common Node.js dev server
              6379: Redis
              27017: MongoDB
              8080: Alternative HTTP

49152 – 65535: Ephemeral (dynamic) ports
              Assigned by OS for outgoing connections (client side)
              When your browser connects to a server, it picks a random
              port from this range as the source port
```

### The 4-Tuple That Defines a Connection

Every TCP connection is uniquely identified by four values:

```
(source IP, source port, destination IP, destination port)

Your browser connecting to GitHub:
  (192.168.1.5, 54312, 140.82.114.5, 443)

Same machine, another tab connecting to GitHub:
  (192.168.1.5, 54313, 140.82.114.5, 443)

These are DIFFERENT connections even though they go to the same server.
The OS demultiplexes incoming packets to the right socket using all 4 values.
```

This is why a single server can handle tens of thousands of simultaneous connections on one port (443): each connection is distinguished by the client's ephemeral source port. The server doesn't need 50,000 ports — it needs one.

---

## 7. TCP

### Definition

TCP (Transmission Control Protocol) is a connection-oriented, reliable, ordered, error-checked transport protocol. It is the protocol underlying HTTP, HTTPS, SSH, SMTP, and most data-transfer protocols.

"Reliable" means: every byte sent is guaranteed to arrive, in order, or the sender is notified of failure.

### Why TCP Exists

IP is inherently unreliable. IP routers drop packets under congestion. Packets can arrive out of order (different paths). Packets can be corrupted. IP does nothing to fix these problems — it just delivers best-effort.

TCP was designed to layer reliability on top of unreliable IP.

### TCP Three-Way Handshake

Before any data can flow, TCP establishes a connection:

```
Client                          Server
  │                               │
  │──── SYN (seq=1000) ──────────→│  "I want to connect; my seq starts at 1000"
  │                               │
  │←─── SYN-ACK (seq=5000,       │  "OK; my seq starts at 5000;
  │            ack=1001) ─────────│   I received your seq, expecting 1001 next"
  │                               │
  │──── ACK (ack=5001) ──────────→│  "Got it; expecting your seq 5001 next"
  │                               │
  │═══════ DATA TRANSFER ═════════│
  │                               │

Time cost:  1 RTT (Round Trip Time) to establish connection
            before any HTTP data can be sent
```

This 1 RTT cost of TCP handshake is why HTTP/2 and QUIC (HTTP/3) work hard to reduce connection establishment time.

### TCP Four-Way Teardown

```
Client                          Server
  │                               │
  │──── FIN ────────────────────→ │  "I'm done sending"
  │                               │
  │ ←── ACK ──────────────────── │  "Got it"
  │                               │
  │ ←── FIN ──────────────────── │  "I'm also done sending"
  │                               │
  │──── ACK ────────────────────→ │  "Got it"
  │                               │
  Client enters TIME_WAIT state for 2 × MSL (Maximum Segment Lifetime)
  (~2 minutes) before the port is reused
```

**TIME_WAIT** is why high-traffic servers can exhaust ephemeral port ranges: each closed connection holds a port in TIME_WAIT for ~60–120 seconds.

### TCP Reliability Mechanisms

#### Sequence Numbers and Acknowledgments

```
Sender sends:
  Segment 1: bytes 1-1000   (seq=1)
  Segment 2: bytes 1001-2000 (seq=1001)
  Segment 3: bytes 2001-3000 (seq=2001)

If Segment 2 is dropped:
  Receiver ACKs: ack=1001 (got up to byte 1000, expecting 1001)
  Receives Segment 3: still sends ack=1001 (missing bytes 1001-2000!)
  Sender receives 3 duplicate ACKs for 1001 → fast retransmit
  Sender retransmits Segment 2
```

#### Sliding Window / Flow Control

TCP prevents a fast sender from overwhelming a slow receiver:

```
Receiver advertises its receive buffer size: rwnd (receive window)
Sender may not have more than rwnd bytes unacknowledged in flight

If receiver is slow (buffer fills): rwnd shrinks → sender slows down
If receiver processes data: rwnd grows → sender speeds up

This is flow control: matching sender speed to receiver capacity
```

#### Congestion Control

TCP also adapts to network congestion (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery):

```
Slow Start:
  Begin with cwnd (congestion window) = 1 MSS (~1460 bytes)
  Double cwnd each RTT until a packet is dropped
  (Exponential growth: 1 → 2 → 4 → 8 → 16 → ...)

Congestion Avoidance:
  After hitting ssthresh (slow start threshold):
  Increase cwnd by 1 MSS per RTT (linear growth)
  Until packet loss detected

On packet loss:
  ssthresh = cwnd / 2
  Reset cwnd = 1 (Tahoe) or cwnd = ssthresh (Reno/CUBIC)
  Resume Slow Start or Congestion Avoidance

This is why bandwidth-delay product matters:
  BDP = bandwidth × RTT
  A 1 Gbps link with 100ms RTT can have 100 Mbps × 0.1s = 10 MB in flight
  TCP's window must be large enough to fill the "pipe"
```

### TCP vs. UDP Comparison

| Property | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (handshake) | Connectionless |
| Reliability | Guaranteed delivery + ordering | Best-effort, no guarantee |
| Order | In-order delivery guaranteed | May arrive out of order |
| Error checking | Checksum + retransmit | Checksum only (no retransmit) |
| Flow control | Yes (receiver window) | No |
| Congestion control | Yes (slow start, CUBIC) | No |
| Speed | Slower (overhead) | Faster (minimal overhead) |
| Latency | Higher (ACKs, retransmits) | Lower |
| Use cases | HTTP, SSH, database, email | DNS, video streaming, gaming, VoIP |
| Header size | 20–60 bytes | 8 bytes |

---

## 8. UDP

### Definition

UDP (User Datagram Protocol) is a connectionless, unreliable, unordered transport protocol. It provides minimal service: send a datagram to an IP:port and hope it arrives. No handshake, no acknowledgment, no retransmit.

### Why UDP Exists

For many applications, TCP's reliability mechanisms are a liability, not an asset:

**DNS**: A single question-answer pair. If no response arrives, the client simply retries. No need for a persistent TCP connection.

**Video streaming**: Old frames have no value. If frame 100 is dropped, retransmitting it at frame 110 would cause the video to stutter worse than just skipping it. UDP lets the application decide what to do with loss.

**Online gaming**: Position updates must be low-latency. A TCP retransmit of an old position update could cause more jank than ignoring the loss.

**QUIC (HTTP/3)**: Built on UDP, but implements its own reliability, multiplexing, and encryption. Gets the benefits of TCP while avoiding head-of-line blocking.

### UDP Implementation: DNS Client

```javascript
// A raw UDP DNS query — demonstrates exactly what DNS over UDP looks like
const dgram = require('dgram');

function buildDNSQuery(hostname) {
  // DNS wire format (RFC 1035)
  const buf = Buffer.alloc(512);
  let offset = 0;

  // Header (12 bytes)
  buf.writeUInt16BE(0x1234, offset); offset += 2; // Transaction ID
  buf.writeUInt16BE(0x0100, offset); offset += 2; // Flags: standard query, recursion desired
  buf.writeUInt16BE(1, offset);      offset += 2; // QDCOUNT: 1 question
  buf.writeUInt16BE(0, offset);      offset += 2; // ANCOUNT: 0 answers
  buf.writeUInt16BE(0, offset);      offset += 2; // NSCOUNT: 0 authority
  buf.writeUInt16BE(0, offset);      offset += 2; // ARCOUNT: 0 additional

  // Question section
  // Encode hostname: api.github.com → \x03api\x06github\x03com\x00
  const labels = hostname.split('.');
  for (const label of labels) {
    buf.writeUInt8(label.length, offset++);
    Buffer.from(label, 'ascii').copy(buf, offset);
    offset += label.length;
  }
  buf.writeUInt8(0, offset++); // Null terminator

  buf.writeUInt16BE(1, offset); offset += 2; // QTYPE: A (IPv4)
  buf.writeUInt16BE(1, offset); offset += 2; // QCLASS: IN (Internet)

  return buf.slice(0, offset);
}

function queryDNS(hostname, resolver = '8.8.8.8') {
  return new Promise((resolve, reject) => {
    const socket = dgram.createSocket('udp4');
    const query = buildDNSQuery(hostname);
    
    socket.on('message', (msg) => {
      socket.close();
      // Parse the DNS response (simplified)
      // In production: use a proper DNS parsing library
      const answerCount = msg.readUInt16BE(6);
      if (answerCount === 0) {
        reject(new Error(`No DNS answers for ${hostname}`));
        return;
      }
      // Skip header (12 bytes) + question section to find answer
      // Actual parsing is more complex due to DNS compression
      resolve(`DNS response received (${msg.length} bytes), ${answerCount} answers`);
    });

    socket.on('error', reject);
    
    // UDP: fire and forget — send the query datagram
    socket.send(query, 53, resolver, (err) => {
      if (err) { socket.close(); reject(err); }
    });

    // Timeout: UDP has no connection, so we must implement our own timeout
    setTimeout(() => {
      socket.close();
      reject(new Error(`DNS query for ${hostname} timed out`));
    }, 3000);
  });
}

queryDNS('github.com').then(console.log).catch(console.error);
```

---

## 9. HTTP

### Definition

HTTP (HyperText Transfer Protocol) is an application-layer request-response protocol that defines how clients and servers communicate. It is stateless, text-based (HTTP/1.1), and runs over TCP (HTTP/1.1, HTTP/2) or UDP (HTTP/3 / QUIC).

### HTTP Version History

```
HTTP/0.9 (1991):  Single method (GET), single document type (HTML)
HTTP/1.0 (1996):  Headers, status codes, multiple content types
                  One TCP connection per request → huge overhead
HTTP/1.1 (1997):  Persistent connections (Keep-Alive), Host header,
                  chunked transfer encoding, pipelining (flawed)
HTTP/2 (2015):    Multiplexing, header compression (HPACK),
                  server push, binary framing, single TCP connection
HTTP/3 (2022):    Built on QUIC (UDP), 0-RTT connection, no
                  head-of-line blocking at transport layer
```

### HTTP/1.1 Request and Response Anatomy

```
HTTP Request:
  ┌─────────────────────────────────────────────────────────────┐
  │ GET /api/users/42 HTTP/1.1                                  │ ← Request line
  │ Host: api.example.com                                       │
  │ Authorization: Bearer eyJhbGc...                            │ ← Headers
  │ Accept: application/json                                    │
  │ Accept-Encoding: gzip, deflate, br                         │
  │ Connection: keep-alive                                      │
  │                                                             │ ← Empty line (end of headers)
  │ (no body for GET)                                           │
  └─────────────────────────────────────────────────────────────┘

HTTP Response:
  ┌─────────────────────────────────────────────────────────────┐
  │ HTTP/1.1 200 OK                                             │ ← Status line
  │ Content-Type: application/json; charset=utf-8               │
  │ Content-Length: 127                                         │ ← Headers
  │ Cache-Control: max-age=60                                   │
  │ X-Request-Id: f3a2c8b1-...                                  │
  │                                                             │ ← Empty line
  │ {"id": 42, "name": "Harish", "email": "h@example.com"}     │ ← Body
  └─────────────────────────────────────────────────────────────┘
```

### HTTP Methods — Semantics and Safety Properties

| Method | Safe? | Idempotent? | Has Body? | Usage |
|---|---|---|---|---|
| GET | Yes | Yes | No | Retrieve resource |
| HEAD | Yes | Yes | No | GET without body (check existence, headers) |
| OPTIONS | Yes | Yes | No | Discover allowed methods (used in CORS preflight) |
| POST | No | No | Yes | Create resource, trigger action |
| PUT | No | Yes | Yes | Replace entire resource |
| PATCH | No | No* | Yes | Partial update |
| DELETE | No | Yes | Optional | Delete resource |

**Safe**: Does not modify server state. **Idempotent**: Multiple identical requests produce the same result as one.

Idempotency is critical for retry logic. A network timeout on a POST (create order) and retrying may create a duplicate order. A timeout on a PUT (set quantity to 5) and retrying is safe — the result is the same.

### HTTP Status Codes

```
1xx — Informational
  100 Continue:            Server received request headers; send body
  101 Switching Protocols: Upgrading to WebSocket

2xx — Success
  200 OK:                  Standard success
  201 Created:             Resource created (POST/PUT success)
  204 No Content:          Success but no body (DELETE success)
  206 Partial Content:     Range request response (video streaming)

3xx — Redirection
  301 Moved Permanently:   Permanent redirect (update bookmarks, caches)
  302 Found:               Temporary redirect (don't update caches)
  304 Not Modified:        Client cache is valid; use cached response
  307 Temporary Redirect:  Like 302 but preserves HTTP method
  308 Permanent Redirect:  Like 301 but preserves HTTP method

4xx — Client Errors
  400 Bad Request:         Malformed request syntax
  401 Unauthorized:        Authentication required (despite the name!)
  403 Forbidden:           Authenticated but not authorized
  404 Not Found:           Resource doesn't exist
  405 Method Not Allowed:  Method not supported for this endpoint
  409 Conflict:            State conflict (duplicate creation, edit conflict)
  410 Gone:                Resource existed but was permanently deleted
  422 Unprocessable:       Semantic validation failure
  429 Too Many Requests:   Rate limited

5xx — Server Errors
  500 Internal Server Error: Generic server failure
  502 Bad Gateway:           Upstream server returned invalid response
  503 Service Unavailable:   Server overloaded or in maintenance
  504 Gateway Timeout:       Upstream server didn't respond in time
```

**Interview trap**: "What's the difference between 401 and 403?"
- 401 means: "I don't know who you are. Authenticate first." (unauthenticated)
- 403 means: "I know who you are. You're not allowed." (unauthorized)

The HTTP spec named 401 "Unauthorized" but it functionally means "unauthenticated." This naming is a historical mistake that confuses everyone.

### HTTP/2 — What Changed and Why

HTTP/1.1's fundamental problem: each request-response pair must complete before the next starts on a TCP connection. Even with Keep-Alive (reusing the connection), requests are sequential. Loading a page with 30 assets requires 30 sequential round-trips — or multiple TCP connections (browsers open up to 6 per origin).

```
HTTP/1.1 (sequential on each connection):
  Connection 1: [req1────resp1][req2────resp2]
  Connection 2: [req3────resp3][req4────resp4]
  Connection 3: [req5────resp5][req6────resp6]
  (6 parallel connections max per browser)

HTTP/2 (multiplexed on one connection):
  Stream 1:  [req1──────────────────resp1]
  Stream 2:    [req2──────────────resp2]
  Stream 3:      [req3──────────resp3]
  Stream 4:        [req4──────resp4]
  All on ONE TCP connection, interleaved
```

HTTP/2 innovations:
- **Multiplexing**: Multiple streams on one connection. No head-of-line blocking at HTTP layer.
- **Binary framing**: Instead of text, frames are binary — smaller, faster to parse.
- **Header compression (HPACK)**: Headers are compressed using a shared dynamic table. Repetitive headers (like `Authorization: Bearer ...`) sent once, referenced by index thereafter.
- **Server push**: Server can proactively send resources the client will need (e.g., push CSS when HTML is requested). Largely deprecated in practice due to caching complexity.
- **Stream prioritization**: Clients can signal priority of streams (CSS before images).

**HTTP/2's remaining problem**: Still uses TCP. A single packet loss causes ALL streams to stall (TCP-level head-of-line blocking).

### HTTP/3 / QUIC

HTTP/3 moves from TCP to **QUIC** (Quick UDP Internet Connections), a protocol built on UDP:

```
HTTP/2 over TCP:
  Single TCP connection → packet loss stalls ALL streams
  
HTTP/3 over QUIC:
  QUIC stream is independent — loss in stream 1 doesn't stall stream 2
  0-RTT connection establishment for repeated connections
  Built-in TLS 1.3 (no separate TLS handshake round-trip)
  Connection migration: same QUIC connection survives IP change
    (your phone moving from Wi-Fi to cellular — connection persists!)
```

---

## 10. HTTPS and TLS

### Definition

HTTPS is HTTP over TLS (Transport Layer Security). TLS provides: **confidentiality** (encrypted data), **integrity** (tamper detection), and **authentication** (server identity verified via certificate).

### TLS 1.3 Handshake

TLS 1.3 reduced the handshake to 1 RTT (from TLS 1.2's 2 RTTs):

```
Client                                          Server
  │                                               │
  │──── ClientHello ────────────────────────────→ │
  │     supported_versions=[TLS1.3]               │
  │     cipher_suites=[AES_256_GCM_SHA384, ...]   │
  │     client_random=<32 bytes>                  │
  │     key_share=[x25519 public key]             │
  │                                               │
  │ ←── ServerHello + Certificate + Finished ──── │
  │     server_random=<32 bytes>                  │
  │     key_share=[server's x25519 public key]    │
  │     Certificate=[server cert chain]           │
  │     CertificateVerify=[signature over handshake]
  │     Finished=[HMAC of handshake]              │
  │                                               │
  │ Both sides derive the same session keys       │
  │ using ECDH: client_private × server_public    │
  │ = server_private × client_public              │
  │ (Diffie-Hellman key exchange magic)           │
  │                                               │
  │──── Finished ───────────────────────────────→ │
  │     [HMAC proving client derived same keys]   │
  │                                               │
  │═════════ Encrypted Application Data ══════════│
  │         (HTTP request/response)               │

Total cost: 1 RTT for TLS + 1 RTT for TCP = 2 RTTs before first byte
(Plus DNS resolution time)
```

### Certificate Chain and PKI

When your browser connects to `https://github.com`, how does it trust the server?

```
Trust Chain:

Root CA Certificate (trusted by OS/browser by default)
  └── Intermediate CA Certificate (issued by Root CA)
        └── github.com Certificate (issued by Intermediate CA)

Browser verifies:
  1. github.com cert is signed by Intermediate CA (valid signature?)
  2. Intermediate CA cert is signed by Root CA (valid signature?)
  3. Root CA is in browser's trusted root store (shipped with OS/browser)
  4. github.com cert's CN/SAN matches the hostname we connected to
  5. Cert is not expired
  6. Cert is not in CRL (Certificate Revocation List) or OCSP says valid

If ALL checks pass → connection is trusted
If ANY check fails → browser shows "Not Secure" / warning
```

### TLS Implementation Details

```javascript
// Express HTTPS server with TLS configuration
const https = require('https');
const express = require('express');
const fs = require('fs');
const tls = require('tls');

const app = express();
app.get('/', (req, res) => res.send('Secure!'));

// In production: obtain certificates via Let's Encrypt / certbot
// For local dev: generate with: openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
const options = {
  key: fs.readFileSync('./key.pem'),
  cert: fs.readFileSync('./cert.pem'),
  
  // TLS security hardening
  minVersion: 'TLSv1.2',   // Reject TLS 1.0 and 1.1 (deprecated, vulnerable)
  maxVersion: 'TLSv1.3',
  
  // Only strong cipher suites
  // TLS 1.3 ciphers are configured separately and are all strong
  ciphers: [
    'ECDHE-RSA-AES256-GCM-SHA384',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-CHACHA20-POLY1305',
  ].join(':'),
  
  // ECDHE key exchange (perfect forward secrecy)
  // Each connection uses ephemeral keys
  // If the server's private key is later compromised,
  // past sessions CANNOT be decrypted
  dhparam: fs.readFileSync('./dhparam.pem'), // For DHE suites
  
  // HSTS: tell browsers to always use HTTPS for this domain
  // (handled via HTTP headers, see below)
};

const server = https.createServer(options, app);

// Security headers
app.use((req, res, next) => {
  // Force HTTPS for 1 year, include subdomains, allow preloading
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');
  next();
});

server.listen(443, () => console.log('HTTPS server running on port 443'));

// Also redirect HTTP to HTTPS
const http = require('http');
http.createServer((req, res) => {
  res.writeHead(301, { Location: `https://${req.headers.host}${req.url}` });
  res.end();
}).listen(80);
```

### Perfect Forward Secrecy

A critical TLS concept interviewers probe:

Without PFS: If an attacker records encrypted traffic today and later obtains the server's private key, they can decrypt all historical traffic.

With PFS (ECDHE key exchange): Each connection uses ephemeral (temporary) key pairs. The session key is derived from these ephemeral keys, which are discarded after the session. Even with the server's long-term private key, past sessions cannot be decrypted.

PFS is achieved with **DHE** (Diffie-Hellman Ephemeral) or **ECDHE** (Elliptic Curve DHE) key exchange. All TLS 1.3 cipher suites require ECDHE — PFS is mandatory in TLS 1.3.

---

## 11. The Full Request Lifecycle

Let us trace the complete journey of `fetch('https://api.github.com/users/torvalds')` from a browser:

```
Browser calls fetch('https://api.github.com/users/torvalds')

PHASE 1 — DNS RESOLUTION (~1-100ms, often cached)
  1. Browser checks DNS cache → miss
  2. OS checks /etc/hosts → miss
  3. OS sends UDP query to 8.8.8.8 for api.github.com
  4. Recursive resolver traverses root → .com → github.com nameservers
  5. Returns: 140.82.113.5, TTL=60
  6. Browser caches for 60 seconds

PHASE 2 — TCP HANDSHAKE (~1 RTT = ~10-100ms depending on distance)
  7. OS allocates ephemeral port: 54231
  8. SYN → 140.82.113.5:443
  9. ← SYN-ACK
  10. ACK →
  TCP connection established

PHASE 3 — TLS HANDSHAKE (~1 RTT for TLS 1.3)
  11. ClientHello (with key share)
  12. ← ServerHello + Certificate + Finished
  13. Browser verifies certificate chain:
      github.com cert → DigiCert CA → root trusted by browser
  14. Finished → (confirms key derivation)
  Session keys established

PHASE 4 — HTTP/2 CONNECTION SETUP
  15. SETTINGS frame exchanged (max streams, header table size, etc.)
  16. New stream opened (stream ID = 1)

PHASE 5 — HTTP REQUEST
  17. HEADERS frame (compressed):
      :method: GET
      :path: /users/torvalds
      :authority: api.github.com
      :scheme: https
      authorization: token ghp_...
      accept: application/json

PHASE 6 — SERVER PROCESSING
  18. GitHub's load balancer receives request
  19. Routes to an application server based on headers/path
  20. App server queries internal DB/cache for user "torvalds"
  21. Serializes response to JSON

PHASE 7 — HTTP RESPONSE
  22. HEADERS frame:
      :status: 200
      content-type: application/json; charset=utf-8
      cache-control: public, max-age=60
      x-ratelimit-remaining: 59
  23. DATA frame(s): { "login": "torvalds", "id": 1024025, ... }

PHASE 8 — BROWSER PROCESSING
  24. Decompress body if Content-Encoding: gzip/br
  25. Parse JSON
  26. Resolve fetch() promise with Response object
  27. Your .then() callback runs with the data

PHASE 9 — CONNECTION HANDLING
  28. TCP connection kept alive (HTTP/2 persistent connection)
  29. Next fetch() to api.github.com reuses this connection
  30. Skips DNS + TCP + TLS handshake!
```

This is the answer to "what happens when you make an HTTP request?" at senior level.

---

## 12. Cookies

### Definition

Cookies are small key-value data stores maintained by the browser and sent with every HTTP request to the matching domain. They were invented to add statefulness to stateless HTTP — primarily for session management.

### Cookie Attributes and Their Security Implications

```
Set-Cookie: sessionId=abc123;
            Domain=example.com;
            Path=/;
            Expires=Thu, 01 Jan 2026 00:00:00 GMT;
            HttpOnly;
            Secure;
            SameSite=Strict
```

| Attribute | Effect | Security Relevance |
|---|---|---|
| `Domain` | Which domains receive this cookie | Too broad (`.example.com`) exposes to subdomains |
| `Path` | Which paths receive this cookie | Rarely used for security |
| `Expires`/`Max-Age` | Cookie lifetime | Session cookies (no Expires) deleted on browser close |
| `HttpOnly` | JS cannot access via `document.cookie` | **Prevents XSS cookie theft** |
| `Secure` | Only sent over HTTPS | **Prevents cookie interception on HTTP** |
| `SameSite=Strict` | Never sent in cross-site requests | **Prevents CSRF** |
| `SameSite=Lax` | Sent on top-level navigations, not sub-resources | Default in modern browsers |
| `SameSite=None` | Always sent (requires Secure) | Needed for cross-site OAuth flows |

### Cookies vs. LocalStorage vs. SessionStorage

| Property | Cookie | LocalStorage | SessionStorage |
|---|---|---|---|
| Capacity | ~4 KB | ~5–10 MB | ~5–10 MB |
| Sent with requests | Yes (automatically) | No | No |
| Server access | Yes | No | No |
| Expiration | Configurable | Never (manual clear) | Tab close |
| JS access | Yes (unless HttpOnly) | Yes | Yes |
| Security controls | HttpOnly, Secure, SameSite | None | None |
| Best for | Session tokens | User preferences, cache | Temp form state |

**Critical insight**: Never store JWT access tokens in localStorage. XSS can steal them. Store short-lived tokens in `HttpOnly; Secure; SameSite=Strict` cookies. (Covered in depth in Pillar 10.)

---

## 13. HTTP Headers

### Definition

HTTP headers are metadata key-value pairs in the HTTP request and response. They control caching, security, content negotiation, authentication, connection behavior, and more.

### Essential Headers (Grouped by Function)

#### Request Headers

```
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9...   ← authentication token
Accept: application/json, text/html;q=0.9       ← content type preference
Accept-Encoding: gzip, deflate, br              ← compression preference
Accept-Language: en-US,en;q=0.9                 ← language preference
Content-Type: application/json                  ← body format (for POST/PUT)
Content-Length: 127                             ← body size in bytes
Host: api.example.com                           ← required in HTTP/1.1
User-Agent: Mozilla/5.0...                      ← client identification
Referer: https://example.com/page              ← where request came from
Cookie: sessionId=abc123; theme=dark            ← cookies for this domain
Origin: https://app.example.com                 ← CORS origin
If-None-Match: "abc123etag"                     ← conditional GET (ETag)
If-Modified-Since: Thu, 01 Jan 2025 00:00:00   ← conditional GET (date)
X-Request-Id: f3a2c8b1-7e2d-4f3a-8c9b-...     ← tracing correlation ID
```

#### Response Headers

```
Content-Type: application/json; charset=utf-8   ← what the body is
Content-Length: 127                             ← body size
Content-Encoding: gzip                          ← body is compressed
Transfer-Encoding: chunked                      ← streaming body
Cache-Control: public, max-age=3600, s-maxage=86400
ETag: "abc123etag"                              ← resource version identifier
Last-Modified: Mon, 01 Jan 2024 00:00:00 GMT   ← last modification time
Location: /users/42                             ← redirect target (3xx)
Retry-After: 60                                 ← rate limit reset (429)
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1735689600
Access-Control-Allow-Origin: https://app.com   ← CORS permission
Set-Cookie: sessionId=abc123; HttpOnly; Secure  ← set cookie
Strict-Transport-Security: max-age=31536000     ← HSTS
X-Frame-Options: DENY                           ← clickjacking prevention
X-Content-Type-Options: nosniff                 ← MIME sniffing prevention
Content-Security-Policy: default-src 'self'    ← XSS mitigation
```

### Cache-Control Directives

This is heavily tested in senior interviews:

```
Cache-Control: public, max-age=3600, s-maxage=86400, stale-while-revalidate=60

public:                  CDNs and proxies may cache this response
private:                 Only the end-user's browser may cache (not CDNs)
no-cache:                MUST revalidate with server before using cache
                         (confusingly named — it doesn't mean "don't cache")
no-store:                Never cache — not even in browser (medical records, banking)
max-age=3600:            Browser cache valid for 3600 seconds (1 hour)
s-maxage=86400:          Shared cache (CDN) valid for 86400 seconds (1 day)
                         Overrides max-age for CDNs
must-revalidate:         After max-age expires, must check server before serving
stale-while-revalidate=60: Serve stale response for 60s while fetching fresh
immutable:               Resource will NEVER change; browsers skip revalidation
                         (used for content-hashed assets like bundle.abc123.js)
```

### ETags and Conditional Requests

```
First request:
  GET /api/users/42 HTTP/1.1

  HTTP/1.1 200 OK
  ETag: "v1-abc123"          ← fingerprint of the response body
  Cache-Control: max-age=60
  {"id": 42, "name": "Harish"}

60 seconds later, browser re-requests:
  GET /api/users/42 HTTP/1.1
  If-None-Match: "v1-abc123"  ← "Do you have a newer version?"

  If resource unchanged:
  HTTP/1.1 304 Not Modified   ← No body! Browser uses cached version
                               → Saves bandwidth, saves server processing

  If resource changed:
  HTTP/1.1 200 OK
  ETag: "v2-def456"           ← New fingerprint
  {"id": 42, "name": "Harish S."}  ← Full response
```

---

## 14. CORS

### Definition

CORS (Cross-Origin Resource Sharing) is a browser security mechanism that restricts JavaScript's ability to make HTTP requests to a different origin than the one that served the current page.

An **origin** is the combination of `scheme + host + port`:
- `https://app.example.com` is an origin
- `https://api.example.com` is a **different** origin (different subdomain)
- `http://app.example.com` is a **different** origin (different scheme)
- `https://app.example.com:8080` is a **different** origin (different port)

### The Same-Origin Policy

Without CORS, browsers enforce the Same-Origin Policy: JavaScript on `https://evil.com` cannot make authenticated requests to `https://your-bank.com` because:
1. The browser automatically sends your bank's cookies
2. The response would contain your private data
3. evil.com's JavaScript would read that data

CORS is the controlled relaxation of this restriction.

### CORS Request Types

**Simple Request** (no preflight): Automatically sent for GET/POST with basic headers:

```
Origin: https://app.example.com
GET /api/data HTTP/1.1
Host: api.differentdomain.com

←── Access-Control-Allow-Origin: https://app.example.com
    (or *)
←── Response body (browser allows JS to read it)
```

**Preflight Request** (OPTIONS first): Required for custom headers, non-simple methods (PUT, DELETE, PATCH):

```
Browser sends preflight:
OPTIONS /api/users/42 HTTP/1.1
Origin: https://app.example.com
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: Authorization, X-Custom-Header

Server responds to preflight:
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH
Access-Control-Allow-Headers: Authorization, X-Custom-Header
Access-Control-Max-Age: 86400      ← Cache preflight for 24 hours
                                     (avoid preflight on every request)

Only if preflight succeeds does browser send actual request:
DELETE /api/users/42 HTTP/1.1
Origin: https://app.example.com
Authorization: Bearer token...
```

### CORS Implementation in Express

```javascript
// Production CORS configuration — NOT the simple "cors()" default
const express = require('express');
const app = express();

// Define allowed origins — do NOT use wildcard (*) with credentials
const ALLOWED_ORIGINS = new Set([
  'https://app.example.com',
  'https://staging.example.com',
  process.env.NODE_ENV === 'development' ? 'http://localhost:3000' : null,
].filter(Boolean));

function corsMiddleware(req, res, next) {
  const origin = req.headers.origin;
  
  // Check if this origin is allowed
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);  // Not *!
    res.setHeader('Vary', 'Origin');  // CRITICAL: tell caches this varies by origin
    res.setHeader('Access-Control-Allow-Credentials', 'true');  // Allow cookies
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 
      'Authorization, Content-Type, X-Request-Id, X-CSRF-Token'
    );
    res.setHeader('Access-Control-Expose-Headers',
      'X-Request-Id, X-RateLimit-Remaining'  // Headers JS can read
    );
    res.setHeader('Access-Control-Max-Age', '86400');  // Cache preflight 24h
  }
  
  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }
  
  next();
}

app.use(corsMiddleware);

// Why NOT Access-Control-Allow-Origin: * with credentials?
// Using * prevents browsers from sending cookies/auth headers.
// You must specify the exact origin to use credentials.
// If you use * with credentials, browser refuses the response.
```

### CORS Common Misconceptions (Interview Traps)

1. **"CORS is a server-side security mechanism."** WRONG. CORS is a BROWSER mechanism. The server receives the request regardless. CORS only controls whether the browser lets JavaScript read the response. Server-side firewalls and auth are separate.

2. **"Disabling CORS fixes the security issue."** WRONG. Disabling CORS (allowing `*`) removes the browser's protection. The security issue was having unauthenticated endpoints.

3. **"curl has a CORS error."** IMPOSSIBLE. curl is not a browser. CORS only exists in browsers.

4. **"Adding `Access-Control-Allow-Origin: *` is always safe."** WRONG. When used with `Access-Control-Allow-Credentials: true`, browsers refuse the response. And `*` prevents reading response cookies.

---

## 15. Load Balancers

### Definition

A load balancer is a device (hardware or software) that distributes incoming network traffic across multiple backend servers. It prevents any single server from becoming a bottleneck and provides fault tolerance.

### Load Balancing Algorithms

```
Round Robin:
  Request 1 → Server A
  Request 2 → Server B
  Request 3 → Server C
  Request 4 → Server A  (back to start)
  Simple, ignores server load

Weighted Round Robin:
  Server A has weight 3, Server B has weight 1
  3 requests to A, 1 to B, 3 to A, 1 to B...
  For servers with different capacities

Least Connections:
  Send to server with fewest active connections
  Better for requests with variable processing time
  
Least Response Time:
  Send to server with lowest latency
  Requires health check probes

IP Hash / Sticky Sessions:
  Hash client IP → always route to same server
  Required for stateful applications (sessions not in shared store)
  Caveat: poor distribution if many users behind one NAT IP

Random:
  Random selection — surprisingly effective at scale
  (AWS Application Load Balancer uses this + least outstanding requests)
```

### Layer 4 vs. Layer 7 Load Balancing

```
Layer 4 (Transport — TCP/UDP):
  Routes based on IP + port only
  Cannot inspect HTTP headers or paths
  Fast (minimal packet inspection)
  Example: AWS NLB (Network Load Balancer)
  Use case: TCP streams, databases, when L7 overhead isn't acceptable

Layer 7 (Application — HTTP):
  Inspects HTTP headers, URLs, cookies
  Can route based on path (/api/ → API servers, /static/ → file servers)
  Can modify headers, compress responses, terminate TLS
  Slower (must parse full HTTP)
  Example: AWS ALB, Nginx, HAProxy, Cloudflare
  Use case: Web applications, microservices routing
```

### Health Checks

```
Load Balancer → Server A: GET /health HTTP/1.1
Server A: 200 OK {"status": "healthy", "db": "connected", "queue": "connected"}

Load Balancer → Server B: GET /health HTTP/1.1
Server B: 500 Internal Server Error (database connection failed)

Load Balancer:
  Server B marked as UNHEALTHY
  No traffic routed to Server B
  Alerts fired
  Continue health checking every 10s
  When Server B returns 200, gradually restore traffic
```

### Implementation: Health Check Endpoint

```javascript
// Production-grade health check endpoint
const express = require('express');
const { Pool } = require('pg');

const app = express();
const db = new Pool({ connectionString: process.env.DATABASE_URL });

// Shallow health check — just confirms process is alive
// Used for load balancer basic liveness checks
app.get('/health/live', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Deep health check — checks all dependencies
// Used for readiness (is the server ready to handle traffic?)
app.get('/health/ready', async (req, res) => {
  const checks = {};
  let healthy = true;
  
  // Database check
  try {
    const result = await db.query('SELECT 1');
    checks.database = { status: 'ok', latencyMs: 0 }; // add real timing
  } catch (err) {
    checks.database = { status: 'error', message: err.message };
    healthy = false;
  }
  
  // Redis check (if applicable)
  // try { await redis.ping(); checks.redis = { status: 'ok' }; }
  // catch (err) { checks.redis = { status: 'error' }; healthy = false; }
  
  // Memory check
  const memUsage = process.memoryUsage();
  const heapUsedMB = Math.round(memUsage.heapUsed / 1024 / 1024);
  const heapLimitMB = 512; // Our configured heap limit
  if (heapUsedMB > heapLimitMB * 0.9) {
    checks.memory = { status: 'warning', heapUsedMB, limit: heapLimitMB };
    // Don't mark unhealthy for memory warnings, but do alert
  } else {
    checks.memory = { status: 'ok', heapUsedMB };
  }
  
  const statusCode = healthy ? 200 : 503;
  res.status(statusCode).json({
    status: healthy ? 'healthy' : 'unhealthy',
    checks,
    version: process.env.APP_VERSION,
    uptime: process.uptime(),
  });
});

app.listen(3000);
```

---

## 16. Proxies and Reverse Proxies

### Forward Proxy

A **forward proxy** sits between clients and the Internet, forwarding requests on behalf of clients. The server sees the proxy's IP, not the client's.

```
Clients → [Forward Proxy] → Internet → Servers
          (clients are hidden)

Use cases:
  - Corporate networks (content filtering, monitoring)
  - VPN-like anonymization
  - Caching outbound requests
  - Access control (which sites can employees visit)
```

### Reverse Proxy

A **reverse proxy** sits between the Internet and servers, forwarding requests on behalf of servers. Clients see the proxy's address, not the servers'.

```
Internet → [Reverse Proxy] → Servers (multiple)
           (servers are hidden)

Use cases:
  - Load balancing
  - TLS termination (decrypt HTTPS at proxy, HTTP internally)
  - Caching (static files, API responses)
  - Request buffering (protect slow servers from slow clients)
  - Security (WAF, rate limiting, DDoS mitigation)
  - Unified entry point for microservices
```

### Nginx as Reverse Proxy

```nginx
# /etc/nginx/nginx.conf — Production reverse proxy configuration

worker_processes auto;  # One worker per CPU core
worker_rlimit_nofile 65535;  # Max open file descriptors per worker

events {
    worker_connections 10000;  # Max simultaneous connections per worker
    use epoll;                  # Linux's high-performance I/O event mechanism
    multi_accept on;            # Accept multiple connections per epoll event
}

http {
    # Upstream group of app servers (load balanced)
    upstream app_servers {
        least_conn;  # Least connections algorithm
        
        server 10.0.1.1:3000 weight=3 max_fails=3 fail_timeout=30s;
        server 10.0.1.2:3000 weight=3 max_fails=3 fail_timeout=30s;
        server 10.0.1.3:3000 weight=1 max_fails=3 fail_timeout=30s;
        
        keepalive 32;  # Keep 32 idle connections to upstream
    }

    server {
        listen 80;
        server_name api.example.com;
        return 301 https://$server_name$request_uri;  # Redirect HTTP → HTTPS
    }

    server {
        listen 443 ssl http2;
        server_name api.example.com;
        
        # TLS configuration
        ssl_certificate     /etc/ssl/certs/api.example.com.crt;
        ssl_certificate_key /etc/ssl/private/api.example.com.key;
        ssl_protocols       TLSv1.2 TLSv1.3;
        ssl_ciphers         ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256;
        ssl_session_cache   shared:SSL:10m;   # Share TLS sessions across workers
        ssl_session_timeout 10m;
        
        # Security headers
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
        add_header X-Frame-Options DENY always;
        add_header X-Content-Type-Options nosniff always;
        
        # Rate limiting (define zone above in http block)
        # limit_req zone=api burst=20 nodelay;
        
        location /api/ {
            proxy_pass http://app_servers;  # Forward to upstream
            
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';  # WebSocket support
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;  # Pass client IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # Timeouts
            proxy_connect_timeout 5s;
            proxy_read_timeout 60s;
            proxy_send_timeout 60s;
            
            # Buffer settings
            proxy_buffering on;          # Buffer responses (protect slow clients)
            proxy_buffer_size 4k;
            proxy_buffers 8 4k;
        }
        
        location /static/ {
            # Serve static files directly from nginx (bypass Node.js)
            alias /var/www/static/;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

---

## 17. CDNs

### Definition

A CDN (Content Delivery Network) is a globally distributed network of servers (Points of Presence, PoPs) that serve content from the edge location closest to the user. CDNs reduce latency by minimizing the physical distance between server and client.

### How CDNs Work

```
Without CDN:
  User in Mumbai → Request → Origin Server in Virginia
  Round trip: ~200ms × 14 hops = ~280ms RTT
  
With CDN:
  User in Mumbai → Request → Cloudflare PoP in Mumbai
  Cache HIT: response served locally → ~5ms RTT
  Cache MISS: Cloudflare fetches from origin, caches, serves
              Future requests served from Mumbai PoP
```

### CDN Caching Strategies

```
Cache-Control: public, max-age=31536000, immutable
  → CDN caches forever; browser caches forever; never re-checks
  → Use for content-hashed static assets (bundle.a3f8c1.js)
  → Content hash changes → URL changes → new cache entry

Cache-Control: public, s-maxage=86400, max-age=0, must-revalidate
  → CDN caches for 24 hours; browser always checks CDN
  → Use for frequently updated, globally consistent content
  → CDN serves cached; browser gets fast response even if CDN revalidates

Surrogate-Control: max-age=3600  (Varnish/Fastly CDN header)
  → CDN-specific cache duration, stripped before sending to browser
  → Browser can have different cache behavior from CDN
```

### CDN Cache Invalidation

CDN cache invalidation is the hard problem:

```
Strategy 1: URL-based cache busting (BEST for static assets)
  Old: /static/bundle.js          → cached everywhere
  New: /static/bundle.a3f8c1.js  → new URL, cold cache
  Never need to invalidate! Just change the URL.
  
Strategy 2: Manual purge API
  Cloudflare, Fastly, CloudFront all expose purge APIs
  POST /zones/{zone_id}/purge_cache { "files": ["https://..."] }
  Risk: eventual consistency — purge propagates to ~400 PoPs
  Not instant; during propagation, some users get stale content
  
Strategy 3: Short TTL
  Cache-Control: max-age=60
  Staleness window is bounded to 60 seconds
  High origin load (every 60s, CDN re-fetches)
  Trade-off: freshness vs. performance
```

---

## 18. WebSockets

### Definition

WebSocket is a protocol providing **full-duplex** (bidirectional) communication over a single TCP connection. After an HTTP-based handshake, the connection is "upgraded" to the WebSocket protocol, and both client and server can send messages at any time without request-response overhead.

### HTTP vs WebSocket

```
HTTP (request-response):
  Client: "Give me data" ────────→ Server
  Server: "Here it is"  ←────────
  Client: "Give me data" ────────→ Server
  Client must poll to receive updates

WebSocket (full-duplex):
  Client ←────────────────────────→ Server
         send anytime, receive anytime
         no polling needed
  Server can PUSH data without client asking
```

### WebSocket Handshake

```
HTTP Upgrade Request:
  GET /ws HTTP/1.1
  Host: api.example.com
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==   ← random base64
  Sec-WebSocket-Version: 13

HTTP 101 Switching Protocols:
  HTTP/1.1 101 Switching Protocols
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
  (Accept = SHA1(Key + magic string), base64 encoded)
  
  After this exchange: TCP connection switches to WebSocket frames.
  HTTP is gone. Both sides speak WebSocket protocol.
```

### WebSocket Implementation

```javascript
// Server: WebSocket with ws library (production-ready)
const WebSocket = require('ws');
const http = require('http');
const { v4: uuidv4 } = require('uuid');

const server = http.createServer();
const wss = new WebSocket.Server({ server });

// Track connected clients
const clients = new Map();

wss.on('connection', (ws, req) => {
  const clientId = uuidv4();
  const clientIp = req.socket.remoteAddress;
  
  clients.set(clientId, {
    ws,
    id: clientId,
    ip: clientIp,
    connectedAt: Date.now(),
    isAlive: true,
  });
  
  console.log(`Client connected: ${clientId} from ${clientIp}. Total: ${clients.size}`);

  // Heartbeat: WebSocket doesn't auto-detect dead connections
  // We use ping/pong to detect stale connections
  ws.on('pong', () => {
    const client = clients.get(clientId);
    if (client) client.isAlive = true;
  });

  ws.on('message', (data) => {
    let message;
    try {
      message = JSON.parse(data.toString());
    } catch {
      ws.send(JSON.stringify({ error: 'Invalid JSON' }));
      return;
    }
    
    // Echo back to sender
    ws.send(JSON.stringify({ type: 'echo', data: message }));
    
    // Broadcast to all other clients
    if (message.type === 'broadcast') {
      broadcast(message, clientId);
    }
  });

  ws.on('close', (code, reason) => {
    clients.delete(clientId);
    console.log(`Client ${clientId} disconnected: ${code} ${reason}`);
  });

  ws.on('error', (err) => {
    console.error(`WebSocket error for ${clientId}:`, err.message);
    clients.delete(clientId);
  });

  // Send welcome message
  ws.send(JSON.stringify({ type: 'connected', clientId }));
});

// Heartbeat interval — detect dead connections every 30s
const heartbeatInterval = setInterval(() => {
  clients.forEach((client, clientId) => {
    if (!client.isAlive) {
      // No pong received — connection is dead
      console.log(`Terminating dead connection: ${clientId}`);
      client.ws.terminate(); // Force close
      clients.delete(clientId);
      return;
    }
    client.isAlive = false;   // Reset; expect pong before next check
    client.ws.ping();          // Send ping; client responds with pong
  });
}, 30000);

wss.on('close', () => clearInterval(heartbeatInterval));

function broadcast(message, senderId) {
  const payload = JSON.stringify({ type: 'broadcast', from: senderId, ...message });
  clients.forEach((client, clientId) => {
    if (clientId !== senderId && client.ws.readyState === WebSocket.OPEN) {
      client.ws.send(payload);
    }
  });
}

server.listen(8080, () => console.log('WebSocket server on port 8080'));
```

```javascript
// Client: WebSocket with reconnection logic
class ResilientWebSocket {
  constructor(url, options = {}) {
    this.url = url;
    this.options = {
      maxReconnectAttempts: 10,
      reconnectIntervalMs: 1000,
      maxReconnectIntervalMs: 30000,
      reconnectDecay: 1.5,  // Exponential backoff multiplier
      ...options
    };
    this.reconnectAttempts = 0;
    this.handlers = { message: [], open: [], close: [], error: [] };
    this.connect();
  }

  connect() {
    this.ws = new WebSocket(this.url);
    
    this.ws.onopen = (event) => {
      console.log('WebSocket connected');
      this.reconnectAttempts = 0;  // Reset on successful connection
      this.handlers.open.forEach(h => h(event));
    };

    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.handlers.message.forEach(h => h(data));
    };

    this.ws.onclose = (event) => {
      this.handlers.close.forEach(h => h(event));
      
      if (!event.wasClean && this.reconnectAttempts < this.options.maxReconnectAttempts) {
        // Exponential backoff: 1s, 1.5s, 2.25s, 3.375s, ...
        const delay = Math.min(
          this.options.reconnectIntervalMs * Math.pow(this.options.reconnectDecay, this.reconnectAttempts),
          this.options.maxReconnectIntervalMs
        );
        console.log(`Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1})`);
        setTimeout(() => this.connect(), delay);
        this.reconnectAttempts++;
      }
    };

    this.ws.onerror = (event) => {
      this.handlers.error.forEach(h => h(event));
    };
  }

  on(event, handler) {
    this.handlers[event].push(handler);
    return this;
  }

  send(data) {
    if (this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    } else {
      console.warn('WebSocket not open. Message dropped:', data);
    }
  }

  close() {
    this.options.maxReconnectAttempts = 0;  // Prevent reconnect
    this.ws.close(1000, 'Client closed');
  }
}

// Usage
const ws = new ResilientWebSocket('wss://api.example.com/ws');
ws.on('open', () => ws.send({ type: 'subscribe', channel: 'prices' }));
ws.on('message', (data) => console.log('Price update:', data));
```

---

## 19. Server-Sent Events

### Definition

SSE (Server-Sent Events) is a one-directional server-push mechanism over HTTP where the server continuously streams events to a client. Unlike WebSockets (full-duplex), SSE is unidirectional: server → client only. The client communicates back via normal HTTP requests.

### SSE vs. WebSocket

| Property | SSE | WebSocket |
|---|---|---|
| Direction | Server → Client only | Bidirectional |
| Protocol | HTTP/1.1 or HTTP/2 | WebSocket (ws:// or wss://) |
| Reconnection | Automatic (browser handles) | Manual implementation needed |
| Firewall friendly | Yes (HTTP) | Sometimes blocked |
| Multiplexing | Yes (over HTTP/2) | No (one connection per stream) |
| Complexity | Low | Higher |
| Use cases | Live feeds, notifications, logs | Chat, gaming, real-time collaboration |

### SSE Implementation

```javascript
// Server: SSE endpoint with proper headers and event formatting
const express = require('express');
const app = express();

app.get('/events', (req, res) => {
  // SSE headers — these are MANDATORY
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('X-Accel-Buffering', 'no');  // Disable Nginx buffering for SSE
  
  // Send initial connection confirmation
  res.write('data: {"type":"connected"}\n\n');

  // SSE event format:
  // event: eventType\n    (optional — 'message' if omitted)
  // id: eventId\n         (optional — enables client reconnection from last ID)
  // data: payload\n       (required — can be multiple lines)
  // retry: milliseconds\n (optional — reconnection delay hint)
  // \n                    (blank line = end of event)

  let eventId = 0;
  
  // Simulate a real-time data stream
  const interval = setInterval(() => {
    const event = {
      type: 'price_update',
      symbol: 'BTC/USD',
      price: 45000 + Math.random() * 1000,
      timestamp: Date.now(),
    };
    
    res.write(`id: ${++eventId}\n`);
    res.write(`event: price_update\n`);
    res.write(`data: ${JSON.stringify(event)}\n`);
    res.write(`\n`);  // Blank line terminates the event
  }, 1000);

  // Heartbeat comment — keeps connection alive through proxies
  // Lines starting with : are comments, ignored by client
  const heartbeat = setInterval(() => {
    res.write(`: heartbeat\n\n`);
  }, 25000);

  // Clean up when client disconnects
  req.on('close', () => {
    clearInterval(interval);
    clearInterval(heartbeat);
    console.log(`SSE client disconnected: ${req.ip}`);
  });
});

app.listen(3000);
```

```javascript
// Client: Browser EventSource API
const eventSource = new EventSource('/events', {
  withCredentials: true,  // Send cookies with SSE request
});

// Default 'message' events
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Default message:', data);
};

// Named event type listener
eventSource.addEventListener('price_update', (event) => {
  const data = JSON.parse(event.data);
  console.log(`${data.symbol}: $${data.price.toFixed(2)}`);
  // Update UI...
});

eventSource.addEventListener('error', (event) => {
  if (eventSource.readyState === EventSource.CLOSED) {
    console.log('Connection closed permanently');
  } else {
    // Browser will automatically reconnect
    // The Last-Event-ID header will be sent, allowing server to resume
    console.log('Connection error — browser will retry');
  }
});

// To close the connection
// eventSource.close();
```

---

## Summary: Networking Stack Layered View

```
User types: https://api.github.com/users/torvalds

Application Layer:
  HTTPS (HTTP + TLS)
  DNS resolution → IP
  HTTP/2 or HTTP/1.1 request framing
  
Transport Layer:
  TCP: reliable, ordered, flow-controlled stream
  3-way handshake before data flows
  TLS handshake within TCP stream
  
Internet Layer:
  IP packets routed hop-by-hop through BGP network
  NAT at home router translates private → public IP
  
Data Link / Physical Layer:
  Wi-Fi frames → router
  Ethernet frames → ISP
  Fiber optic signals across backbone
  
Each layer: knows only its job, wraps previous layer's data.
All these layers run every time you click a link.
```

---

## Interview Questions — Pillar 2

### Junior Level

1. What is DNS and what problem does it solve?
2. What is the difference between TCP and UDP?
3. What is an HTTP status code? What does 404 mean? What does 401 mean?
4. What is HTTPS and how is it different from HTTP?
5. What is CORS and why does it exist?

### Mid Level

1. Walk me through what happens when a browser makes an HTTPS request.
2. What is the TCP three-way handshake? Why is it necessary?
3. What is the difference between 301 and 302? Between 401 and 403?
4. Explain how TLS provides confidentiality, integrity, and authentication.
5. What is a reverse proxy? What does it do that your Node.js app server shouldn't do?
6. What is perfect forward secrecy and why does it matter?
7. How does a CDN work? What determines cache hit vs. miss?

### Senior Level

1. Your API is experiencing "CORS errors" in production only. Users' browsers show `Access-Control-Allow-Origin` issues, but your development environment works fine. What would you investigate?
2. Explain cache-control: `no-cache` vs. `no-store` vs. `max-age=0, must-revalidate`. When would you use each?
3. How would you design a real-time notification system for 100,000 concurrent users? Compare SSE, WebSocket, and long-polling. What are the tradeoffs?
4. A user in Mumbai connecting to a US-based server has high latency. Walk me through every step in the connection lifecycle where you could reduce this latency.
5. What is BGP and why does a DNS attack like the Dyn incident in 2016 take down half the Internet?
6. Your load balancer is forwarding requests to 4 app servers. One server has CPU at 95%, others at 30%. What does this tell you about your load balancing algorithm? What would you change?
7. Explain how HTTP/2 multiplexing works and why HTTP/3 was still needed after HTTP/2 solved head-of-line blocking at the HTTP layer.
8. A client is getting intermittent 504 Gateway Timeout errors. Your Node.js server logs show no errors. Where is the timeout occurring and how would you diagnose it?

---

*Continue to `03-JavaScript-Fundamentals.md` →*
