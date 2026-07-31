---
title: Course Syllabus Index
owner: Ihtiram Ullah
version: 1.0
generated: 2026-07-30
courses: 13
modules: 69
topics: 445
subtopics: 951
scheme: COURSE > MODULE > TOPIC > SUBTOPIC
companion: master-knowledge-index.md
---

# COURSE SYLLABUS INDEX

What each syllabus actually covered. The companion **Master Knowledge Index** holds the
technology content; this file holds the *structure* of each course and links back to it.
A `→ 44` marker means the topic maps to master category 44.

## Courses at a glance

| Course | Code | Vendor | Status | Modules | Topics | Subtopics |
|---|---|---|---|---:|---:|---:|
| Cisco Certified Support Technician | `CCST` | Cisco | REFERENCE | 6 | 25 | 81 |
| CCNA | `200-301 v1.1` | Cisco | CERTIFIED | 6 | 53 | 116 |
| CCNP ENCOR | `350-401 v1.1` | Cisco | COURSEWORK ONLY | 6 | 33 | 109 |
| CCNP ENARSI | `300-410 v1.1` | Cisco | COURSEWORK ONLY | 4 | 32 | 90 |
| CCNP SCOR | `350-701 v1.1` | Cisco | PLANNED | 9 | 45 | 0 |
| CCNP SNCF | `300-710` | Cisco | PLANNED | 7 | 28 | 0 |
| CompTIA A+ | `220-1201 / 220-1202 (V15)` | CompTIA | CERTIFIED — OLDER VERSION | 2 | 43 | 148 |
| CompTIA Network+ | `N10-009 (V9)` | CompTIA | NOT TAKEN | 5 | 25 | 87 |
| CompTIA Linux+ | `XK0-006 (V8)` | CompTIA | NOT TAKEN | 5 | 29 | 44 |
| CompTIA ITF+ | `FC0-U61 (V5)` | CompTIA | BELOW LEVEL | 6 | 33 | 86 |
| Microsoft Azure Administrator | `AZ-104` | Microsoft | COURSEWORK ONLY | 5 | 17 | 92 |
| MCSE: Server Infrastructure | `70-410 → 70-414` | Microsoft | ⚠ RECORD CONFLICT | 5 | 61 | 24 |
| LPIC-1 / Linux Administration | `101 + 102` | LPI | SELF-STUDY | 3 | 21 | 74 |
| | | | | **69** | **445** | **951** |

## Status legend

- **CERTIFIED** — Passed and certified.
- **CERTIFIED — OLDER VERSION** — Certified, but on a superseded exam version.
- **COURSEWORK ONLY** — Training complete. Exam not sat.
- **PLANNED** — On the roadmap. Not started.
- **NOT TAKEN** — Not studied.
- **SELF-STUDY** — Own notes, no formal enrolment.
- **REFERENCE** — Included for mapping only.
- **BELOW LEVEL** — Retained for completeness.
- **⚠ RECORD CONFLICT** — Source syllabus contradicts your stated credential.

---

# Cisco Certified Support Technician — Networking

`CCST` · Cisco · **REFERENCE**

> Entry-level Cisco track. Not taken — included because it maps the foundation you already hold.

<sub>Sources merged: Cisco official objectives (PDF)</sub>

### 1 · Standards and Concepts

- **`1.1`** Fundamental conceptual building blocks of networks  →  `30`, `38`
  - TCP/IP model
  - OSI model
  - Frames and packets
  - Addressing
- **`1.2`** Differentiate bandwidth and throughput
  - Latency
  - Delay
  - Speed test vs. iPerf
- **`1.3`** Differentiate LAN, WAN, MAN, CAN, PAN, WLAN  →  `48`, `52`
  - Physical and logical network topologies
- **`1.4`** Cloud vs on-premises applications and services  →  `74`
  - Public, private, hybrid
  - SaaS, PaaS, IaaS
  - Remote/hybrid work
- **`1.5`** Common network applications and protocols  →  `32`, `33`, `34`
  - TCP vs UDP
  - FTP, SFTP, TFTP
  - HTTP, HTTPS
  - DHCP, DNS
  - ICMP, NTP

### 2 · Addressing and Subnet Formats

- **`2.1`** Private vs public addresses  →  `36`
  - Address classes
  - NAT concepts
- **`2.2`** IPv4 addresses and subnet formats  →  `30`
  - Subnet concepts
  - Subnet calculator
  - Slash notation and subnet mask
  - Broadcast domain
- **`2.3`** IPv6 addresses and prefix formats  →  `30`, `31`
  - Types of addresses
  - Prefix concepts

### 3 · Endpoints and Media Types

- **`3.1`** Cables and connectors in local area networks  →  `10`, `11`, `63`
  - Fiber, copper, twisted pair
  - Coax, RJ-45, RJ-11
  - Fiber connector types
- **`3.2`** Wi-Fi, cellular, and wired network technologies  →  `10`, `11`, `51`
  - Copper and sources of interference
  - Fiber
  - 802.11 unlicensed 2.4/5/6 GHz
  - Cellular licensed
- **`3.3`** Endpoint devices  →  `15`, `64`
  - IoT devices
  - Computers, mobile devices
  - IP phone, printer, server
- **`3.4`** Set up and check network connectivity across OSes  →  `27`, `28`, `35`
  - Windows, Linux, macOS
  - Android, Apple iOS
  - Wireless client settings: SSID, authentication, WPA mode

### 4 · Infrastructure

- **`4.1`** Status lights on a Cisco device
  - Link light colour and status
- **`4.2`** Use a network diagram to attach the appropriate cables  →  `10`, `13`, `14`
  - Patch cables
  - Switches and routers
  - Power, rack layout
- **`4.3`** Identify ports on network devices  →  `10`, `11`, `37`
  - Console port, serial port
  - Fiber port, Ethernet ports
  - SFPs, USB port, PoE
- **`4.4`** Basic routing concepts
  - Default gateway
  - Layer 2 vs Layer 3 switches
  - Local vs remote network
- **`4.5`** Basic switching concepts  →  `40`, `41`, `47`
  - MAC address tables
  - MAC address filtering
  - VLAN

### 5 · Diagnosing Problems

- **`5.1`** Troubleshooting methodologies and help desk best practices  →  `85`, `86`, `88`
  - Ticketing
  - Documentation
  - Information gathering
  - Prioritization
- **`5.2`** Perform a packet capture with Wireshark  →  `38`, `88`
  - Purpose of a packet analyzer
  - Saving and opening a .pcap file
- **`5.3`** Run basic diagnostic commands and interpret results  →  `61`, `88`
  - ping
  - ipconfig / ifconfig / ip
  - tracert / traceroute
  - nslookup
  - How firewalls influence results
- **`5.4`** Ways to access and collect data about network devices  →  `62`, `74`
  - RDP, SSH, telnet
  - VPN, terminal emulators, console
  - Network management systems
  - Cloud-managed (Meraki), scripts
- **`5.5`** Run basic show commands on a Cisco device  →  `28`, `40`
  - show run, show version
  - show cdp neighbors
  - show ip interface brief, show ip route
  - show mac address-table
  - show interface / status
  - Privilege levels, command help

### 6 · Security

- **`6.1`** How firewalls filter traffic  →  `37`, `61`
  - Blocked ports and protocols
  - Rules deny or permit access
- **`6.2`** Foundational security concepts  →  `22`, `35`, `60`
  - CIA triad
  - AAA
  - Multifactor authentication
  - Encryption, certificates, password complexity
  - Identity stores (Active Directory)
  - Spam, phishing, malware, denial of service
- **`6.3`** Configure basic wireless security on a home router  →  `52`, `53`
  - WPA, WPA2, WPA3
  - Personal vs Enterprise

---

# CCNA — Implementing and Administering Cisco Solutions

`200-301 v1.1` · Cisco · **CERTIFIED**

> Certified via Corvit, Jan–Apr 2021. Your certificate predates v1.1 — see the version diff.

<sub>Sources merged: Cisco blueprint v1.1 (2024) · Cisco blueprint v1.0 (2021)</sub>

### 1 · Network Fundamentals (20%)

- **`1.1`** Role and function of network components  →  `10`, `52`, `61`
  - Routers
  - Layer 2 and Layer 3 switches
  - Next-generation firewalls and IPS
  - Access points
  - Controllers
  - Endpoints
  - Servers
  - PoE
- **`1.2`** Network topology architectures  →  `40`, `48`, `74`
  - Two-tier
  - Three-tier
  - Spine-leaf
  - WAN
  - Small office/home office (SOHO)
  - On-premises and cloud
- **`1.3`** Physical interface and cabling types  →  `10`, `11`, `38`
  - Single-mode fiber, multimode fiber, copper
  - Ethernet shared media and point-to-point
- **`1.4`** Identify interface and cable issues  →  `10`, `40`
  - Collisions
  - Errors
  - Duplex mismatch
  - Speed mismatch
- **`1.5`** Compare TCP to UDP  →  `38`
- **`1.6`** Configure and verify IPv4 addressing and subnetting  →  `30`
- **`1.7`** Describe private IPv4 addressing  →  `30`
- **`1.8`** Configure and verify IPv6 addressing and prefix  →  `30`, `31`
- **`1.9`** IPv6 address types  →  `31`
  - Unicast: global, unique local, link local
  - Anycast
  - Multicast
  - Modified EUI-64
- **`1.10`** Verify IP parameters for client OS  →  `27`, `28`
  - Windows
  - macOS
  - Linux
- **`1.11`** Wireless principles  →  `50`, `51`, `52`
  - Nonoverlapping Wi-Fi channels
  - SSID
  - RF
  - Encryption
- **`1.12`** Virtualization fundamentals  →  `43`, `70`
  - Server virtualization
  - Containers
  - VRFs
- **`1.13`** Switching concepts  →  `38`, `40`
  - MAC learning and aging
  - Frame switching
  - Frame flooding
  - MAC address table

### 2 · Network Access (20%)

- **`2.1`** Configure and verify VLANs spanning multiple switches  →  `37`, `41`
  - Access ports (data and voice)
  - Default VLAN
  - InterVLAN connectivity
- **`2.2`** Configure and verify interswitch connectivity  →  `36`, `37`, `41`
  - Trunk ports
  - 802.1Q
  - Native VLAN
- **`2.3`** Layer 2 discovery protocols  →  `37`
  - Cisco Discovery Protocol
  - LLDP
- **`2.4`** Configure and verify EtherChannel (LACP)  →  `42`
  - Layer 2 EtherChannel
  - Layer 3 EtherChannel
- **`2.5`** Rapid PVST+ Spanning Tree Protocol  →  `37`, `42`
  - Root port, root bridge primary/secondary, port names
  - Port states and roles
  - PortFast
  - Root guard, loop guard, BPDU filter, BPDU guard
- **`2.6`** Cisco Wireless Architectures and AP modes  →  `52`
- **`2.7`** Physical infrastructure connections of WLAN components  →  `37`, `41`, `52`
  - AP
  - WLC
  - Access/trunk ports
  - LAG
- **`2.8`** Network device management access  →  `35`, `74`
  - Telnet, SSH
  - HTTP, HTTPS
  - Console
  - TACACS+/RADIUS
  - Cloud managed
- **`2.9`** Interpret wireless LAN GUI configuration  →  `49`, `52`
  - WLAN creation
  - Security settings
  - QoS profiles
  - Advanced settings

### 3 · IP Connectivity (25%)

- **`3.1`** Interpret the components of the routing table  →  `30`, `37`, `43`
  - Routing protocol code
  - Prefix
  - Network mask
  - Next hop
  - Administrative distance
  - Metric
  - Gateway of last resort
- **`3.2`** How a router makes a forwarding decision by default  →  `30`, `37`, `43`
  - Longest prefix match
  - Administrative distance
  - Routing protocol metric
- **`3.3`** Configure and verify IPv4 and IPv6 static routing  →  `31`, `43`
  - Default route
  - Network route
  - Host route
  - Floating static
- **`3.4`** Configure and verify single area OSPFv2  →  `44`
  - Neighbor adjacencies
  - Point-to-point
  - Broadcast (DR/BDR selection)
  - Router ID
- **`3.5`** First hop redundancy protocols — purpose, functions, concepts  →  `37`, `42`

### 4 · IP Services (10%)

- **`4.1`** Configure and verify inside source NAT using static and pools  →  `36`
- **`4.2`** Configure and verify NTP in client and server mode  →  `28`, `34`
- **`4.3`** Role of DHCP and DNS within the network  →  `32`, `33`
- **`4.4`** Function of SNMP in network operations  →  `37`, `82`
- **`4.5`** Syslog features including facilities and severity levels  →  `37`, `83`
- **`4.6`** Configure and verify DHCP client and relay  →  `28`, `32`
- **`4.7`** Forwarding per-hop behavior (PHB) for QoS  →  `49`
  - Classification
  - Marking
  - Queuing
  - Congestion
  - Policing
  - Shaping
- **`4.8`** Configure network devices for remote access using SSH
- **`4.9`** Capabilities and functions of TFTP/FTP

### 5 · Security Fundamentals (15%)

- **`5.1`** Key security concepts  →  `60`
  - Threats
  - Vulnerabilities
  - Exploits
  - Mitigation techniques
- **`5.2`** Security program elements  →  `95`
  - User awareness
  - Training
  - Physical access control
- **`5.3`** Configure and verify device access control using local passwords  →  `95`
- **`5.4`** Security password policy elements  →  `35`
  - Management
  - Complexity
  - Multifactor authentication
  - Certificates
  - Biometrics
- **`5.5`** IPsec remote access and site-to-site VPNs  →  `61`, `62`
- **`5.6`** Configure and verify access control lists  →  `49`, `95`
- **`5.7`** Configure and verify Layer 2 security features  →  `32`, `37`, `63`
  - DHCP snooping
  - Dynamic ARP inspection
  - Port security
- **`5.8`** Compare authentication, authorization, and accounting concepts  →  `35`
- **`5.9`** Wireless security protocols  →  `37`, `52`, `53`
  - WPA
  - WPA2
  - WPA3
- **`5.10`** Configure and verify WLAN within the GUI using WPA2 PSK  →  `52`, `53`

### 6 · Automation and Programmability (10%)

- **`6.1`** How automation impacts network management  →  `87`
- **`6.2`** Compare traditional networks with controller-based networking
- **`6.3`** Controller-based, software defined architecture  →  `48`, `63`, `87`
  - Overlay, underlay, fabric
  - Separation of control plane and data plane
  - Northbound and Southbound APIs
- **`6.4`** Explain AI (generative and predictive) and machine learning in network operations
- **`6.5`** Characteristics of REST-based APIs  →  `35`, `87`
  - Authentication types
  - CRUD
  - HTTP verbs
  - Data encoding
- **`6.6`** Configuration management mechanisms  →  `87`
  - Ansible
  - Terraform
- **`6.7`** Recognize components of JSON-encoded data  →  `87`

---

# CCNP ENCOR — Implementing Cisco Enterprise Network Core Technologies

`350-401 v1.1` · Cisco · **COURSEWORK ONLY**

> Coursework complete. Exam NOT sat. Highest-priority gap on your roadmap.

<sub>Sources merged: Cisco blueprint v1.1 · Cisco blueprint v1.0 · NetAcad-aligned breakdown · CBT Nuggets 24-week plan · Global Knowledge ENCOR 1.3 + 31 labs · NetCom ENCOR v1.3 outline</sub>

### 1 · Architecture (15%)

- **`1.1`** Explain enterprise design principles  →  `40`, `42`, `48`
  - High-level designs: 2-tier, 3-tier, fabric, cloud
  - High availability: redundancy, FHRP, SSO
  - Enterprise network design models (two-tier, three-tier, spine-leaf)
  - Physical infrastructure comparison: on-prem vs cloud vs hybrid
  - Enterprise campus and WAN design principles
- **`1.2`** Describe wireless design principles  →  `28`, `52`, `74`
  - Deployment models: centralized, distributed, controller-less, controller-based, cloud, remote branch
  - Location services in WLAN design
  - Client density
- **`1.3`** Explain Cisco SD-WAN working principles  →  `48`, `49`
  - Control/data-plane elements
  - Benefits & limitations
  - SD-WAN components: control, data, management planes
  - QoS architecture: classification, marking, queuing, scheduling
- **`1.4`** Explain Cisco SD-Access working principles  →  `40`, `63`
  - Control/data-plane elements
  - Interoperation with traditional campus
  - Cisco SD-Access architecture: fabric, edge nodes, control plane
- **`1.5`** Interpret wired/wireless QoS configurations  →  `49`, `52`, `74`
  - QoS components
  - QoS policy
  - WLAN deployment models (autonomous, centralized, cloud)
- **`1.6`** Describe hardware/software switching mechanisms  →  `12`, `40`, `52`
  - CEF, CAM, TCAM, FIB, RIB, adjacency tables
  - 📚 Sources used (Module 1): Cisco ENCOR v1.1 exam topics (official); Cisco ENCOR exam page; Cisco Press Official Cert Guide 2e.
  - Discrepancy: Older v1.0 PDFs don’t list wireless 'groups/profiles/tags'.
  - Switching hardware architecture: ASIC, TCAM, CEF

### 2 · Virtualization (10%)

- **`2.1`** Describe device virtualization technologies  →  `40`, `43`, `48`
  - Type-1/Type-2 hypervisors
  - Virtual machines (VMs)
  - Virtual switching
  - Hypervisors (Type 1 vs Type 2), Virtual machines
  - Device virtualization: VRF, GRE/IPsec tunnels
  - Overlay technologies: LISP, VXLAN
- **`2.2`** Configure & verify data-path virtualization  →  `36`, `43`, `48`
  - VRF
  - GRE and IPsec tunneling
- **`2.3`** Describe network virtualization concepts  →  `40`, `48`, `70`
  - LISP
  - VXLAN
  - 📚 Sources used (Module 2): Cisco ENCOR v1.1 exam topics; Cisco Press OCG 2e; Cisco ENCOR course page.
  - Virtual switching and routing (vSwitch, vRouter)

### 3 · Infrastructure (30%)

- **`3.1`** Layer 2  →  `37`, `41`, `42`
  - Troubleshoot static/dynamic 802.1Q trunking
  - Troubleshoot static/dynamic EtherChannel
  - Configure/verify RSTP, MST and enhancements (root guard, BPDU guard)
  - Layer 2 protocols: STP, RSTP, MST, EtherChannel
  - Layer 2 troubleshooting: loops, BPDU guard, portfast
- **`3.2`** Layer 3  →  `36`, `37`, `43`
  - Compare EIGRP vs OSPF (adv-dist-vector vs link-state, load balancing, path selection/ops, metrics, area types)
  - Configure simple OSPFv2/v3 (multi-area, summarization, filtering; adjacencies on p2p/broadcast; passive-interface)
  - Configure/verify eBGP between directly connected neighbors (best-path and relationships)
  - Describe policy-based routing
  - Layer 3 routing protocols: EIGRP, OSPFv2, OSPFv3, eBGP
- **`3.3`** Wireless  →  `14`, `28`, `50`
  - L1 concepts: RF power, RSSI, SNR, interference, noise, bands, channels, client capabilities
  - AP modes & antenna types
  - AP discovery & join (discovery algorithms, WLC selection)
  - L2/L3 roaming principles & use cases
  - Troubleshoot WLAN config & client connectivity (GUI only)
  - Wireless segmentation with groups, profiles, tags
  - Wireless LAN: RF fundamentals, AP modes, roaming, channel planning
  - Wireless security: PSK, EAP, WebAuth, rogue detection
- **`3.4`** IP Services  →  `32`, `34`, `36`
  - Interpret NTP/PTP configurations
  - Configure NAT/PAT
  - Configure HSRP/VRRP
  - Describe multicast (RPF check, PIM, IGMPv2/v3)
  - 📚 Sources used (Module 3): Cisco ENCOR v1.1 exam topics; Cisco ENCOR course page; Cisco Press OCG 2e.
  - Discrepancy: v1.0 blueprint lacks the wireless segmentation bullet present in v1.1.
  - First-hop redundancy: HSRP, VRRP
  - IP Services: NTP, NAT/PAT, Syslog, DHCP, SNMP, NetFlow

### 4 · Network Assurance (10%)

- **`4.1`** Diagnose with tools  →  `37`, `82`, `83`
  - debug/conditional debug
  - traceroute
  - ping
  - SNMP
  - syslog
- **`4.2`** Configure & verify Flexible NetFlow  →  `37`, `80`, `82`
  - Device monitoring using SNMP, syslog, NetFlow
- **`4.3`** Configure SPAN/RSPAN/ERSPAN
  - SPAN, RSPAN, ERSPAN configuration and use
  - IP SLA configuration and tracking
- **`4.4`** Configure & verify IP SLA
- **`4.5`** Describe Cisco DNA Center workflows (config, monitoring, management)  →  `36`, `80`, `87`
  - Network troubleshooting using ping, traceroute, debugs
  - Automation tools: Cisco DNA Center path trace, health monitoring
- **`4.6`** Configure & verify NETCONF/RESTCONF  →  `87`
  - 📚 Sources used (Module 4): Cisco ENCOR v1.1 exam topics; Cisco ENCOR course page; Cisco Press OCG 2e.
  - Configuration validation using NETCONF and RESTCONF

### 5 · Security (20%)

- **`5.1`** Configure & verify device access control  →  `35`, `49`, `95`
  - Lines & local user authentication
  - AAA (authentication/authorization)
  - Access control: AAA with RADIUS and TACACS+
  - Access Control Lists (standard, extended, time-based)
- **`5.2`** Configure & verify infrastructure security  →  `49`, `63`
  - ACLs
  - Control Plane Policing (CoPP)
  - Infrastructure security: control plane policing (CoPP)
- **`5.3`** Describe REST API security  →  `87`
  - REST API security models: OAuth, token-based auth
- **`5.4`** Configure & verify wireless security  →  `35`, `52`, `53`
  - 802.1X
  - WebAuth
  - PSK
  - EAPOL (4-way handshake)
  - Wireless security: WPA2/WPA3, RADIUS-based authentication
- **`5.5`** Describe components of network security design  →  `35`, `60`, `63`
  - Threat defense, endpoint security, NGFW, TrustSec, MACsec
  - Access control: 802.1X, MAB, WebAuth
  - 📚 Sources used (Module 5): Cisco ENCOR v1.1 exam topics; Cisco ENCOR course page; Cisco Press OCG 2e.
  - Device hardening: secure passwords, privilege levels

### 6 · Automation (15%)

- **`6.1`** Interpret basic Python components/scripts  →  `87`
  - Introduction to Python scripting and libraries
- **`6.2`** Construct valid JSON files  →  `87`
  - Data serialization: JSON, YAML
- **`6.3`** Describe YANG (principles/benefits)  →  `87`
  - Model-driven programmability: YANG, NETCONF, RESTCONF
- **`6.4`** Describe APIs for Cisco DNA Center and vManage  →  `87`
  - Cisco DNA Center APIs, sandbox environment usage
  - EEM applets and event-driven automation
  - Interacting with APIs using Postman and curl
- **`6.5`** Interpret REST response codes & payloads (DNA Center, RESTCONF)  →  `87`
- **`6.6`** Construct an EEM applet (config/troubleshooting/data collection)  →  `87`, `88`
- **`6.7`** Compare agent vs agentless orchestration tools (Chef, Puppet, Ansible, SaltStack)  →  `29`, `38`, `48`
  - 📚 Sources used (Module 6): Cisco ENCOR v1.1 exam topics; Cisco ENCOR course page; Cisco Press OCG 2e.
  - Quality & Coverage Checks
  - Mirrors the official v1.1 blueprint end-to-end, including all topics/subtopics and exact weights.
  - Duration/languages are taken from the official ENCOR exam page; ignore unofficial claims about question counts or pass scores.
  - Source Pack (≥5 total; official first)
  - Official exam page (350-401 ENCOR) — duration, languages, overview, v1.1 label.
  - Official exam topics PDF (v1.1, 2023) — complete blueprint with weights.
  - Official exam topics PDF (v1.0, 2019) — version-history comparison.
  - Cisco Learning Network — first-date-to-test for v1.1 (Sep 20, 2023).
  - CBT Nuggets — 2023 ENCOR update timing corroboration.
  - Cisco ENCOR course page — official training page.
  - Cisco Press — Official Cert Guide, 2nd Ed. (2023) — mapped to v1.1.
  - Upcoming v1.2 (2026) notice — CLN banner (v1.1 last test Mar 18, 2026).
  - Automation frameworks: Ansible, Puppet, Chef overview
- **`6.8`** High availability concepts (FHRP, SSO, redundancy) <sub>*(merged)*</sub>  →  `42`, `73`
- **`6.9`** Multicast: IGMP, PIM sparse/dense modes <sub>*(merged)*</sub>

---

# CCNP ENARSI — Implementing Cisco Enterprise Advanced Routing and Services

`300-410 v1.1` · Cisco · **COURSEWORK ONLY**

> Coursework complete. Exam NOT sat. Sit after ENCOR.

<sub>Sources merged: Cisco blueprint v1.1 · Module breakdown · CBT Nuggets 14-week plan · Global Knowledge ENARSI 1.1 + 29 labs</sub>

### 1 · Layer 3 Technologies (35%)

- **`1.1`** Administrative distance  →  `37`, `43`, `88`
  - Troubleshoot AD across routing protocols
  - Administrative distance and recursive route issues
- **`1.2`** Route-maps (any protocol)  →  `37`, `47`
  - Attributes, tagging, filtering
- **`1.3`** Loop-prevention mechanisms  →  `47`
  - Filtering, tagging, split horizon, route poisoning
- **`1.4`** Redistribution (any sources/protocols)  →  `35`, `37`, `44`
  - Route redistribution between OSPF, EIGRP, BGP
  - EIGRP authentication and wide metrics
  - Stub routing and route filtering
  - DR/BDR elections and passive interfaces
- **`1.5`** Summarization  →  `37`, `47`
  - Manual and auto-summary (any protocol)
- **`1.6`** Policy-Based Routing (PBR)  →  `43`
  - Configure & verify
  - VRF-Lite and routing instances
- **`1.7`** VRF-Lite  →  `43`
  - Configure & verify
- **`1.8`** BFD
  - Describe Bidirectional Forwarding Detection
- **`1.9`** EIGRP (classic & named; VRF & global)  →  `31`, `35`, `36`
  - Address families (IPv4/IPv6)
  - Neighbors & authentication
  - Loop-free path selection (RD, FD, FC, successor/FS, SIA)
  - Stubs
  - Load-balancing (equal/unequal)
  - Metrics
  - EIGRP named mode and classic mode
- **`1.10`** OSPFv2/v3  →  `31`, `35`, `36`
  - Address families (IPv4/IPv6)
  - Neighbors & authentication
  - Network types: p2p, multipoint, broadcast, NBMA
  - Areas: backbone/normal/transit/stub/NSSA/totally-stub
  - Roles: internal, backbone, ABR, ASBR; virtual links
  - Path preference
- **`1.11`** BGP (iBGP/eBGP; unicast; VRF-Lite)  →  `31`, `36`, `43`
  - Address families (IPv4/IPv6)
  - Neighbors & auth (next-hop, multihop, 4-byte AS, pvt AS, refresh, sync, peer-groups, states/timers)
  - Attributes & best-path
  - Route reflectors (excl. multiple RRs, confeds, dynamic peer)
  - Policies (in/out filtering, path manipulation)
  - 📚 Sources used (Module 1): Official exam topics v1.1 (PDF); Cisco ENARSI exam page; Cisco Learning blog (PBR).

### 2 · VPN Technologies (20%)

- **`2.1`** MPLS operations  →  `29`, `40`, `44`
  - LSR, LDP, label switching, LSP
  - OSPFv2 and OSPFv3 operations
  - MPLS L3VPN fundamentals and configuration
  - NHRP and IPsec integration in DMVPN
- **`2.2`** MPLS Layer 3 VPN  →  `48`, `62`
  - Describe components & flow
- **`2.3`** DMVPN (single hub) — configure & verify  →  `48`, `61`, `62`
  - GRE/mGRE
  - NHRP
  - IPsec
  - Dynamic neighbor
  - Spoke-to-spoke
  - 📚 Sources used (Module 2): Official exam topics v1.1 (PDF); Cisco ENARSI training course page; Cisco Press OCG 2e (2023).
  - DMVPN Phase 1, 2, 3 architecture

### 3 · Infrastructure Security (20%)

- **`3.1`** Device security with IOS AAA — troubleshoot  →  `28`, `35`, `88`
  - TACACS+, RADIUS, local DB
  - AAA with TACACS+ and RADIUS
- **`3.2`** Router security features — troubleshoot  →  `31`, `47`, `49`
  - IPv4 ACLs (standard/extended/time-based)
  - IPv6 traffic filter
  - uRPF
  - Route summarization techniques and route filtering
- **`3.3`** Control Plane Policing (CoPP)  →  `37`, `44`, `45`
  - Telnet, SSH, HTTP(S), SNMP, EIGRP, OSPF, BGP
- **`3.4`** IPv6 First-Hop Security — describe  →  `31`, `32`
  - RA guard, DHCP guard, binding table, ND inspection/snooping, source guard
  - 📚 Sources used (Module 3): Official exam topics v1.1 (PDF); Cisco ENARSI exam page (overview).
  - IPv6 First Hop Security (RA Guard, DHCPv6 Guard, Source Guard)

### 4 · Infrastructure Services (25%)

- **`4.1`** Device management — troubleshoot  →  `88`
  - Console/VTY
  - Telnet, HTTP/HTTPS, SSH, SCP
  - (T)FTP
- **`4.2`** SNMP — troubleshoot  →  `37`, `82`, `88`
  - v2c, v3
- **`4.3`** Logging — troubleshoot  →  `37`, `83`, `88`
  - Local, syslog, debugs, conditional debugs, timestamps
- **`4.4`** DHCPv4/v6 — troubleshoot  →  `28`, `31`, `32`
  - Client, IOS DHCP server, relay, options
  - OSPFv3 for IPv6 and troubleshooting
- **`4.5`** IP SLA — troubleshoot  →  `88`
  - Jitter, tracking objects, delay, connectivity
- **`4.6`** NetFlow — troubleshoot  →  `82`, `88`
  - v5, v9, Flexible NetFlow
  - NetFlow and Flexible NetFlow
  - Real-world troubleshooting scenarios
- **`4.7`** Cisco DNA Center Assurance — troubleshoot with  →  `31`, `45`, `54`
  - Connectivity, monitoring, device & network health
  - 📚 Sources used (Module 4): Official exam topics v1.1 (PDF); Cisco ENARSI exam page; Cisco Live references to ENARSI blueprint.
  - Quality & Coverage Checks
  - Mirrors the latest official v1.1 blueprint (2023), including every topic and subtopic and the exact weights.
  - Duration/languages come from the current Cisco exam page; where third-party sites differ, we flag the discrepancy.
  - Source Pack (≥5 total; official first)
  - Official exam page (300-410 ENARSI) — duration, languages, overview.
  - Official exam topics (PDF, v1.1, 2023) — full blueprint & weights.
  - CCNP Enterprise v1.1 Release Notes (PDF, Mar 9, 2023) — delta list for v1.1.
  - Cisco Learning Network — CCNP Enterprise page (v2.0 window; Feb 3, 2026 first-test).
  - Cisco Press — ENARSI Official Cert Guide, 2nd Ed. (Oct 2023).
  - CBT Nuggets update note (Mar 24, 2023) — corroborates Sep 20, 2023 first-test date for v1.1.
  - EIGRP IPv6 configuration and troubleshooting
- **`4.8`** Bidirectional Forwarding Detection (BFD) <sub>*(merged)*</sub>  →  `35`, `36`, `63`
  - Virtual links and authentication methods
  - Unicast Reverse Path Forwarding (uRPF)
- **`4.9`** External routes, variance, and load balancing <sub>*(merged)*</sub>  →  `28`, `31`, `32`
  - BGP route selection, path attributes, and filtering
  - DHCP client/server/relay for IPv4 and IPv6
- **`4.10`** LSA types and area types (stub, NSSA, totally stubby) <sub>*(merged)*</sub>  →  `48`, `62`
  - GRE and mGRE tunnels
- **`4.11`** eBGP and iBGP configuration and neighbor states <sub>*(merged)*</sub>  →  `29`, `30`, `31`
  - BGP communities, confederations, and peer-groups
  - BGP troubleshooting and neighbor issues
  - IPv4/IPv6 ACLs and prefix lists
  - SNMP v2/v3 configuration and monitoring
  - Syslog, logging levels, and conditional debugging
  - IP SLA configuration and use cases
  - Hands-on lab simulations using NetSim or GNS3/EVE-NG
- **`4.12`** Multiprotocol BGP (MP-BGP) with IPv6 <sub>*(merged)*</sub>  →  `31`, `46`
- **`4.13`** Mock exams and timed quizzes <sub>*(merged)*</sub>
- **`4.14`** Command recall and syntax drills <sub>*(merged)*</sub>

---

# CCNP SCOR — Implementing and Operating Cisco Security Core Technologies

`350-701 v1.1` · Cisco · **PLANNED**

> Roadmap item 5. Not started. Core exam for CCNP Security.

<sub>Sources merged: Cisco blueprint v1.1 · NetAcad-aligned syllabus</sub>

### 1 · Security Concepts (25%)

- **`1.1`** Common threats (malware, phishing, DDoS, spoofing)  →  `60`
- **`1.2`** Threat intelligence types and feeds  →  `60`
- **`1.3`** Confidentiality, Integrity, Availability (CIA triad)
- **`1.4`** Security terms: exploits, vulnerabilities, risk management  →  `60`
- **`1.5`** SOC processes: SIEM, SOAR, NIST IR framework  →  `38`

### 2 · Network Security (20%)

- **`2.1`** Layer 2 security: DHCP snooping, DAI, Port Security  →  `32`, `37`, `63`
- **`2.2`** Layer 3 security: uRPF, IP Source Guard, ACLs  →  `49`, `63`
- **`2.3`** Infrastructure device protection: control plane policing (CoPP)  →  `49`, `63`
- **`2.4`** Network segmentation and VLAN hopping prevention  →  `41`
- **`2.5`** Router/switch hardening: banners, SSH, SNMPv3  →  `37`, `63`, `82`

### 3 · Secure Network Access (20%)

- **`3.1`** Authentication, Authorization, Accounting (AAA)  →  `35`
- **`3.2`** RADIUS vs TACACS+  →  `35`
- **`3.3`** 802.1X, MAB, WebAuth, posture assessment  →  `35`
- **`3.4`** Cisco ISE architecture and policy enforcement
- **`3.5`** Guest access, profiling, and posture in Cisco ISE

### 4 · Endpoint Protection and Detection (15%)

- **`4.1`** Endpoint-based malware protection: AMP for Endpoints  →  `60`, `64`
- **`4.2`** EDR concepts: detection and response workflows
- **`4.3`** Host-based firewalls and antivirus  →  `61`, `64`
- **`4.4`** Behavioral detection and sandboxing
- **`4.5`** Endpoint vulnerability assessment  →  `60`, `64`

### 5 · Secure Cloud and Email (10%)

- **`5.1`** Cloud security responsibilities (shared model)  →  `74`
- **`5.2`** Cisco Umbrella and CASB concepts
- **`5.3`** DNS-layer security and filtering  →  `33`, `47`
- **`5.4`** Secure Email Gateway (ESA) features and deployment  →  `89`
- **`5.5`** SPF, DKIM, DMARC email authentication  →  `35`

### 6 · Content Security (10%)

- **`6.1`** Web proxy operations and filtering categories  →  `47`
- **`6.2`** Cisco WSA and cloud-based SWG overview  →  `74`
- **`6.3`** URL filtering and web reputation engines  →  `47`
- **`6.4`** Application visibility and control (AVC)
- **`6.5`** Decryption policies and SSL inspection

### 7 · Secure Firewall and IPS (15%)

- **`7.1`** Cisco ASA and FTD firewall features  →  `61`
- **`7.2`** Access Control Policies (ACP), NAT, App visibility  →  `36`, `95`
- **`7.3`** NGIPS (Snort rules, policy tuning, blacklisting)
- **`7.4`** Firepower management via FMC and FDM  →  `61`
- **`7.5`** IPS evasion techniques and countermeasures  →  `61`

### 8 · VPN and Encrypted Traffic (15%)

- **`8.1`** Site-to-Site VPN: IPsec, ISAKMP, IKEv1/v2  →  `61`, `62`
- **`8.2`** Remote access VPNs: SSL VPN, AnyConnect  →  `62`
- **`8.3`** IKE phases, proposals, policies  →  `62`
- **`8.4`** Public Key Infrastructure (PKI)
- **`8.5`** Encrypted traffic visibility using TLS fingerprinting

### 9 · Automation and Programmability (10%)

- **`9.1`** REST APIs and data formats (JSON, XML)  →  `87`
- **`9.2`** YANG and model-driven telemetry  →  `82`, `87`
- **`9.3`** Cisco pxGrid and ISE API integration  →  `87`
- **`9.4`** Python for automation (basic scripts and workflows)  →  `87`
- **`9.5`** Security automation platforms: Ansible, SecureX, Postman  →  `87`

---

# CCNP SNCF — Securing Networks with Cisco Firepower

`300-710` · Cisco · **PLANNED**

> Security concentration option. Not started.

<sub>Sources merged: NetAcad-aligned syllabus</sub>

### 1 · Firepower System Overview

- **`1.1`** Cisco Firepower Threat Defense (FTD) components and deployment  →  `60`, `61`, `89`
- **`1.2`** Firepower Management Center (FMC) vs Firepower Device Manager (FDM)  →  `61`
- **`1.3`** Device registration and communication flow
- **`1.4`** Basic FTD setup and licensing model  →  `61`

### 2 · Device Management

- **`2.1`** Adding FTD to FMC using registration keys and NAT IDs  →  `36`, `61`
- **`2.2`** FTD upgrade and backup procedures  →  `25`, `61`
- **`2.3`** Health monitoring and device status dashboards  →  `80`
- **`2.4`** High Availability (HA) configuration and failover testing  →  `73`

### 3 · Configuration and Policies

- **`3.1`** Access Control Policy (ACP) structure: rules, default actions  →  `95`
- **`3.2`** Intrusion policies (Snort), file/malware policies  →  `60`, `61`
- **`3.3`** Security Intelligence (SI) feeds and URL filtering  →  `47`
- **`3.4`** Application control using AVC and QoS  →  `49`

### 4 · NAT and VPN

- **`4.1`** Static, dynamic, and policy NAT on FTD  →  `36`, `61`
- **`4.2`** Split tunneling and NAT exemption  →  `36`, `62`
- **`4.3`** Remote access VPN with AnyConnect (SSL/IPSec)  →  `61`, `62`
- **`4.4`** Site-to-site VPNs: IKEv2, crypto maps, IPsec tunnels  →  `61`, `62`

### 5 · Threat Defense and Detection

- **`5.1`** Firepower NGIPS vs NGFW feature sets  →  `61`
- **`5.2`** Snort rule tuning and intrusion event actions  →  `61`
- **`5.3`** File and malware inspection integration  →  `60`
- **`5.4`** SSL decryption policies and certificate handling

### 6 · Logging, Monitoring, and Reporting

- **`6.1`** Syslog configuration and event logging in FMC  →  `37`, `83`
- **`6.2`** Connection, intrusion, file, and malware event logs  →  `60`, `61`
- **`6.3`** Correlation policies and rule creation
- **`6.4`** Dashboards, custom reports, and scheduled exports

### 7 · Troubleshooting and System Maintenance

- **`7.1`** Packet tracer and capture on FTD  →  `29`, `38`, `61`
- **`7.2`** Event analysis and troubleshooting denied traffic  →  `88`
- **`7.3`** License verification and feature enablement
- **`7.4`** CLI troubleshooting (expert mode, system support commands)  →  `28`, `88`

---

# CompTIA A+

`220-1201 / 220-1202 (V15)` · CompTIA · **CERTIFIED — OLDER VERSION**

> Certified via Corvit, Mar–May 2021 — that was an earlier version. V15 launched Mar 2025. Content below is current, not what you sat.

<sub>Sources merged: CompTIA V15 syllabus</sub>

### 1 · Core 1 (220-1201) — Mobile, Networking, Hardware, Virtualization, Troubleshooting (13% / 23% / 25% / 11% / 28%)

- **`1.1`** Monitor mobile device hardware & perform replacements  →  `10`, `12`, `15`
  - Battery; keyboard/keys; RAM; HDD/SSD; wireless cards
  - Privacy/security components (incl. biometrics); near-field scanner features
  - Wi‑Fi antenna connector/placement; camera/webcam; microphone
- **`1.2`** Accessories & connectivity options  →  `37`
  - USB/USB‑C/microUSB/miniUSB, Lightning, NFC, Bluetooth, tethering/hotspot
  - Accessories: stylus, headsets, speakers, webcam; docking station; port replicator
  - Trackpad/drawing pad/track points
- **`1.3`** Configure mobile network connectivity & application support  →  `52`, `74`
  - Wireless/cellular (3G/4G/5G, hotspot, Wi‑Fi, SIM/eSIM); pairing/tests
  - Location services (GPS/cellular)
  - MDM (corporate/BYOD, policy enforcement, corporate apps)
  - Sync (data caps, calendar, contacts); business apps (mail, cloud storage)
- **`2.1`** TCP/UDP ports, protocols & purposes  →  `32`, `33`, `37`
  - FTP 20–21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, NetBIOS 137–139, LDAP 389, HTTPS 443, SMB/CIFS 445, RDP 3389
  - TCP vs UDP characteristics
- **`2.2`** Wireless networking technologies  →  `50`, `51`, `52`
  - Frequencies 2.4/5/6 GHz; channels & widths; Bluetooth; 802.11 standards; NFC; RFID
- **`2.3`** Services provided by networked hosts  →  `32`, `33`, `34`
  - DNS, DHCP, file/print, mail, syslog, web, AAA, database, NTP
  - Internet appliances (spam gateway, UTM, load balancer, proxy)
  - Legacy/embedded (SCADA); IoT devices
- **`2.4`** Common network configuration concepts  →  `32`, `33`, `35`
  - DNS records (A, AAAA, CNAME, MX, TXT incl. DKIM/SPF/DMARC)
  - DHCP (leases, reservations, scope, exclusions)
  - VLAN; VPN
- **`2.5`** Common networking hardware devices  →  `10`, `12`, `36`
  - Routers; switches (managed/unmanaged); access points
  - Patch panels; firewalls; PoE/injectors; NIC/MAC
  - Cable/DSL modem; ONT
- **`2.6`** Configure basic wired/wireless SOHO networks  →  `30`, `31`, `52`
  - IP addressing: IPv4/IPv6, private/public, APIPA, static/dynamic, subnet mask, gateway
- **`2.7`** Internet connection types, network types & characteristics  →  `10`, `11`, `48`
  - Satellite, fiber, cable, DSL, cellular, WISP
  - LAN/WAN/PAN/MAN/SAN/WLAN
- **`2.8`** Networking tools & purposes  →  `10`
  - Crimper, cable stripper, Wi‑Fi analyzer, toner probe, punchdown tool
  - Cable tester, loopback plug, TAP
- **`3.1`** Display components & attributes  →  `61`
  - LCD (IPS/TN/VA), OLED, Mini‑LED; touch/digitizer; inverter
  - Pixel density, refresh rate, resolution, color gamut
- **`3.2`** Cables, connectors, features & purposes  →  `10`, `11`, `15`
  - Network: copper (categories, T568A/B, coax, STP/UTP incl. direct‑burial; plenum), fiber (single/multimode)
  - Peripheral: USB 2.0/3.x, serial, Thunderbolt
  - Video: HDMI, DisplayPort, DVI, VGA, USB‑C
  - Drive: SATA, eSATA; adapters
  - Connector types: RJ11, RJ45, F‑type, ST, SC, LC, punchdown block, micro/mini‑USB, USB‑C, Molex, Lightning, DB9
- **`3.3`** RAM characteristics  →  `12`, `50`
  - Form factors (SODIMM/DIMM); DDR generations; ECC vs non‑ECC; channel configs
- **`3.4`** Storage devices  →  `11`, `12`
  - HDD (spindle speeds, 2.5″/3.5″)
  - SSD (NVMe, SATA, PCIe, SAS; M.2/mSATA)
  - RAID 0/1/5/6/10; removable media; optical
- **`3.5`** Motherboards, CPUs & add‑on cards  →  `10`, `12`, `14`
  - Form factors (ATX/microATX/ITX); connectors (PCI/PCIe, power, SATA/eSATA, headers, M.2)
  - Compatibility (Intel/AMD sockets, multisocket)
  - BIOS/UEFI (boot, USB perms, TPM, fans, Secure Boot, passwords, temp monitoring)
  - Virtualization support; encryption (TPM/HSM)
  - CPU arch (x86/x64/ARM; cores)
  - Expansion (sound/video/capture/NIC)
  - Cooling (fans/heatsinks/thermal paste/liquid)
- **`3.6`** Power supplies  →  `14`, `42`
  - Input 110–120 VAC vs 220–240 VAC; output 3.3/5/12 V
  - 20+4‑pin; redundant/modular; wattage; efficiency
- **`3.7`** Deploy & configure MFDs/printers & settings  →  `15`, `38`, `40`
  - Unbox/setup; OS drivers (PCL vs PostScript); firmware
  - Connectivity (USB/Ethernet/Wi‑Fi); shared devices (share/print server)
  - Settings (duplex/orientation/tray/quality)
  - Security (user auth/badging/audit logs/secure prints)
  - Network scan (email/SMB/cloud); ADF/flatbed
- **`3.8`** Printer maintenance  →  `15`
  - Laser: toner, maintenance kit, calibrate, clean
  - Inkjet: cartridge/printhead/roller/feeder; clean/calibrate/clear jams
  - Thermal: feed assembly, special paper; clean element/remove debris
  - Impact: multipart paper; replace ribbon/printhead/paper
- **`4.1`** Virtualization concepts  →  `20`, `70`
  - VM purposes (sandbox, test/dev, app virtualization)
  - Requirements (security/network/storage)
  - Desktop virtualization (VDI); containers; hypervisors (Type 1/2)
- **`4.2`** Cloud computing concepts  →  `10`, `12`, `14`
  - Models (private/public/hybrid/community; IaaS/PaaS/SaaS)
  - Characteristics (shared vs dedicated, metered ingress/egress, elasticity, availability, sync, multitenancy)
  - 5.1–5.6 Hardware/Network troubleshooting
  - 5.1 Motherboards/RAM/CPU/power — POST beeps, blank screen/no power, sluggish/overheat/burning smell, random shutdown, app crashes, bad date/time, capacitor swelling
  - 5.2 Drive/RAID — data loss/corruption, grinding/clicking, no boot, RAID failure, S.M.A.R.T., slow IOPS, missing drives/arrays, audible alarms
  - 5.3 Video/projector/display — input source, cabling/bulb, fuzzy/burn‑in/dead pixels/flashing/incorrect color/audio/dim/shutdown/sizing/distortion
  - 5.4 Mobile — battery health/swollen/broken screen/charging/connectivity/liquid/overheat/digitizer/ports/malware/calibration/apps/performance
  - 5.5 Network — intermittent Wi‑Fi/Internet, slow speeds, limited connectivity, jitter/latency, poor VoIP, port flapping, interference, auth failures
  - 5.6 Printer — lines/garble/jams/fade/no‑feed/misfeed/queue backlog/speckling/double images/grinding/finishing/ orientation/tray/connection/queue frozen

### 2 · Core 2 (220-1202) — Operating Systems, Security, Software Troubleshooting, Operational Procedures (28% / 28% / 23% / 21%)

- **`1.1`** OS types & purposes  →  `27`, `28`
  - Windows, Linux, macOS, ChromeOS; mobile (iPadOS/iOS/Android)
  - Filesystems: NTFS, ReFS, FAT32, ext4, XFS, APFS, exFAT
  - Vendor life‑cycle & update limitations; cross‑OS compatibility concerns
- **`1.2`** OS installs & upgrades (diverse environments)  →  `25`
  - Boot methods (USB, network, flash, Internet, external, internal partition, multiboot)
  - Clean/upgrade; image/zero‑touch/remote; repair; drivers
  - Partitioning (GPT/MBR); upgrade considerations (backups, compatibility)
- **`1.3`** Windows editions & features  →  `12`, `36`, `64`
  - Windows 10/11 Home/Pro/Enterprise; N versions; domain vs workgroup; RDP availability; RAM limits
  - BitLocker; gpedit.msc; upgrade paths (in‑place/clean)
  - Hardware requirements (TPM/UEFI)
- **`1.4`** Windows features & tools  →  `12`, `23`, `80`
  - Task Manager/services/startup/performance/processes/users
  - MMC snap‑ins (Event Viewer, Disk Management, Task Scheduler)
  - Device Manager, Certificate Manager, Local Users & Groups, Performance Monitor, Group Policy Editor
  - System Info, Resource Monitor, MSConfig, Disk Cleanup/Defrag, Registry Editor
- **`1.5`** Windows command‑line tools  →  `12`, `36`, `88`
  - cd/dir; ipconfig/ping/nslookup/net use/tracert/pathping
  - chkdsk/format/diskpart; md/rd/robocopy; hostname/net user; winver/whoami/help; gpupdate/gpresult/sfc
- **`1.6`** Windows settings  →  `14`, `15`, `61`
  - Internet Options, Devices & Printers, Programs & Features, Network & Sharing Center, System
  - Defender Firewall, Mail, Sound, Device Manager, Indexing, Administrative Tools
  - File Explorer options; Power options (hibernate/sleep/standby/lid, fast startup, USB selective suspend)
  - Ease of Access, Update & Security, Personalization, Apps, Privacy, Devices, Network & Internet, Gaming, Accounts
- **`1.7`** Windows networking (client/desktop)  →  `15`, `20`, `24`
  - Domain vs workgroup; shares/printers/file servers/mapped drives
  - Local firewall rules; client IP/DNS/subnet/gateway (static/dynamic)
  - VPN; Wi‑Fi/WWAN/wired; proxy; public vs private; metered connections; network paths
- **`1.8`** macOS  →  `12`, `20`, `25`
  - Install/uninstall apps (.dmg/.pkg/App Store); system folders; Apple ID/corporate restrictions
  - Best practices (backups/AV/updates/RSR); System Settings; multiple desktops, Mission Control, Keychain, Spotlight, iCloud, gestures, Finder, Dock, Continuity
  - Disk Utility; Terminal; Force Quit
- **`1.9`** Linux (client/desktop)  →  `20`, `27`, `28`
  - File mgmt (ls/pwd/mv/cp/rm/chmod/chown/grep/find); fsck/mount; su/sudo
  - Packages (apt/dnf); network (ip/ping/curl/dig/traceroute)
  - Info (man/cat/top/ps/du/df); editors (nano)
  - Config files (/etc/passwd, /etc/shadow, /etc/hosts, /etc/fstab, /etc/resolv.conf); components (systemd/kernel/bootloader); root account
- **`1.10`** Install applications by requirements  →  `12`
  - System/CPU/VRAM/RAM/driver & compatibility; distribution (media vs downloadable vs image)
  - Impacts (device/network/operations/business)
- **`1.11`** Cloud-based productivity tools  →  `35`, `74`
  - Email systems; storage & sync; collaboration (spreadsheets/video/presentations/word processing/IM)
  - Identity sync; licensing assignment
- **`2.1`** Security measures & purposes  →  `12`, `49`, `95`
  - Physical: bollards/vestibules/video/alarm/motion/locks/equipment locks/guards/fences
  - Access: fobs/smart cards/keys/MDM keys; biometrics (retina/fingerprint/palm/face/voice); lighting; magnetometers
  - Logical: least privilege/Zero Trust/ACLs/MFA (apps/SMS/voice/TOTP/OTP/hardware token); SAML/SSO/JIT/PAM/MDM/DLP/IAM/directory services
- **`2.2`** Windows OS security settings  →  `14`, `23`, `37`
  - Antivirus enable/update; firewall (enable/ports/app rules)
  - Accounts (local vs Microsoft/standard/admin/guest/power); log‑in options (password/PIN/fingerprint/face/SSO/Windows Hello)
  - NTFS vs share permissions; attributes/inheritance; Run as admin vs standard; UAC
  - BitLocker/To‑Go; EFS; AD join/logon scripts/home folders/GPOs/groups/folder redirection
- **`2.3`** Wireless security protocols & authentication  →  `35`, `37`, `52`
  - WPA2/WPA3/TKIP/AES; RADIUS/TACACS+/Kerberos/MFA
- **`2.4`** Malware types & detection/removal/prevention  →  `25`, `60`, `61`
  - Malware: trojan/rootkit/virus/spyware/ransomware/keylogger/boot sector/cryptominer/stalkerware/fileless; adware/PUP
  - Tools/methods: Recovery Console modes, EDR/MDR/XDR, AV/anti‑malware, email gateways, software firewalls, user education, OS reinstall
- **`2.5`** Social engineering, threats & vulnerabilities  →  `36`, `60`
  - Social engineering: phishing/vishing/smishing/QR/spear/whaling/shoulder/tailgating/impersonation/dumpster
  - Threats: DoS/DDoS/evil twin/spoofing/on‑path/brute/dictionary/insider/SQLi/zero‑day
  - Vulnerabilities: non‑compliant/unpatched/unprotected/EOL/BYOD; XSS/BEC/supply‑chain
- **`2.6`** SOHO malware removal (procedure)  →  `25`, `60`
  - Verify → quarantine → disable System Restore (Windows Home) → remediate/update/scan (safe mode/preinstall env) → reimage if needed → schedule scans/updates → re‑enable restore & create point → educate user
- **`2.7`** Workstation security & hardening  →  `12`, `63`, `64`
  - Data‑at‑rest encryption; strong password policy (length/complexity/expiration/uniqueness)
  - BIOS/UEFI passwords; end‑user best practices (locks/logoff/protect hardware/PII/password managers)
  - Account mgmt (restrict perms, change default admin pwd, restrict logon times, disable guest/autorun/unneeded services; timeouts/locks)
- **`2.8`** Mobile device security  →  `10`, `15`, `25`
  - Hardening (device encryption, screen locks incl. face/fingerprint/PIN/pattern/swipe; config profiles)
  - Patch mgmt (OS/app); endpoint (AV/anti‑malware/content filtering)
  - Locator apps; remote wipes/backups; failed‑login limits; MDM/BYOD vs corporate; profile requirements
- **`2.9`** Data destruction & disposal
  - Physical (drill/shred/degauss/incinerate); erase/wipe (low‑level/standard format)
  - Recycle/repurpose; outsourcing (third‑party, certificates of destruction); regulatory/environmental requirements
- **`2.10`** SOHO network security settings  →  `30`, `37`, `47`
  - Router: change defaults, IP filtering, firmware/content filtering, placement/secure locations, UPnP, screened subnet, secure mgmt access
  - Wireless: SSID change; Firewall: disable unused ports, port forwarding/mapping; encryption; guest access
- **`2.11`** Browser security settings  →  `10`, `12`, `14`
  - Trusted sources & hashing; patching; extensions/plugins; password managers; TLS & valid certs
  - Settings (pop‑up block, clear cache/data, private mode, sync); ad blockers, proxy, secure DNS; feature management
  - 3.1–3.4 Software troubleshooting
  - 3.1 Windows OS issues — BSOD, degraded performance, boot/frequent shutdowns, services not starting, crashes, low memory, USB resource warnings, instability, 'No OS found', slow profile, time drift
  - 3.2 Mobile OS/app issues — install/close/update failures; slow response; OS won’t update; battery; random reboots; Bluetooth/Wi‑Fi/NFC; auto‑rotate
  - 3.3 Mobile OS/app security — unofficial app stores/developer mode/root/jailbreak/unauthorized apps; symptoms: high traffic, slow response, data‑limit notices, many ads, fake security warnings, unexpected behavior, leaked data
  - 3.4 PC security issues — network access blocked, desktop alerts/false AV alerts, altered/renamed/missing files, unwanted OS notifications/updates; browser pop‑ups, cert warnings, redirection, degraded performance
  - 4.1–4.6 Operational procedures
  - 4.1 Documentation & support systems — ticketing, asset mgmt (CMDB, tags, warranty, users), SOPs, onboarding/off‑boarding, SLAs, KBs; clear comms
  - 4.2 Change mgmt — request/purpose, scope, type (standard/normal/emergency), schedule (freeze/maintenance), risk, approvals, implementation, peer review, UAT
  - 4.3 Backup & recovery — full/incremental/differential/synthetic; in‑place vs alternate; testing & frequency; rotation (onsite/offsite, GFS, 3‑2‑1)
  - 4.4 Safety — ESD straps/mats, electrical safety/grounding, handling/storage, cable mgmt, antistatic bags; compliance; personal safety (disconnect power, lifting, fire safety, goggles, masks)
  - 4.5 Environmental — MSDS, battery/toner/device disposal, temperature/humidity/ventilation, placement, dust cleanup, compressed air; surges/brownouts/UPS/suppressors
  - 4.6 Content/privacy/licensing/policy — incident response (chain of custody, documentation, order of volatility); licensing/DRM/EULA; NDA/MNDA; regulated data (PCI/PII/PHI), retention; AUP; compliance; splash screens
  - Quality & Coverage Checks
  - Mirrors the latest official V15 objective maps for Core 1 and Core 2, including all numbered objectives and example subtopics.
  - Any older content (V14 and before) is superseded by V15 as of Mar 25, 2025.
  - Source Pack (official & reputable)
  - CompTIA A+ (V15) overview — exam codes, launch date, exam facts.
  - 220-1201 (Core 1) Objectives — weights & full outline.
  - 220-1202 (Core 2) Objectives — weights & full outline.
  - A+ V14 (1101/1102) retirement schedule for context.
  - Partner/press comparisons (V14→V15) and reputable training overviews.

---

# CompTIA Network+

`N10-009 (V9)` · CompTIA · **NOT TAKEN**

> Not taken. Overlaps heavily with CCNA — low marginal value unless an employer asks for it.

<sub>Sources merged: CompTIA V9 syllabus</sub>

### 1 · Networking Concepts (23%)

- **`1.1`** OSI model concepts  →  `38`, `88`
  - Layers 1–7: Physical, Data Link, Network, Transport, Session, Presentation, Application
  - Apply OSI to analysis and troubleshooting
- **`1.2`** Networking appliances, applications, functions  →  `52`, `61`, `62`
  - Appliances: routers, switches, firewalls, IDS/IPS, load balancers, proxies, NAS, SAN, wireless (AP, controller)
  - Applications: CDN
  - Functions: VPN; cloud service models (IaaS, PaaS); scalability, elasticity, multitenancy
- **`1.3`** Cloud & virtualization fundamentals  →  `70`, `74`, `89`
  - NFV/VPC; network security groups; gateways
  - Deployment & service models
- **`1.4`** Ports, protocols, services, traffic types  →  `32`, `33`, `34`
  - Common ports/protocols: FTP 20/21, SFTP/SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, LDAP 389, SMB 445, HTTPS 443, RDP 3389, SIP 5060/5061
  - Traffic types: unicast, multicast, anycast, broadcast; services: SNMP, NTP
- **`1.5`** Transmission media & transceivers  →  `10`, `11`, `38`
  - Wireless: 802.11, cellular, satellite; Wired: 802.3; SMF vs MMF; DAC/twinax; coax; plenum vs non-plenum; speeds
  - Transceivers: Ethernet/FC; SFP/QSFP
  - Connectors: SC, LC, ST, MPO, RJ11, RJ45, F-type, BNC
- **`1.6`** Topologies, architectures, types  →  `40`
  - Mesh, hybrid, star/hub-and-spoke, spine-leaf, point-to-point
  - Three-tier (core/distribution/access), collapsed core; traffic flows (north-south, east-west)
- **`1.7`** IPv4 addressing (given a scenario)  →  `30`, `50`, `87`
  - Public vs private, APIPA, RFC1918, loopback
  - Subnetting (VLSM, CIDR); address classes A–E
- **`1.8`** Evolving use cases  →  `31`, `36`, `43`
  - SDN/SD-WAN (app-aware, ZTP, transport-agnostic, central policy)
  - VXLAN/DCI (L2 encapsulation)
  - Zero-Trust Architecture (policy-based authN/Z, least-privilege)
  - SASE/SSE; Infrastructure as Code (automation, drift/compliance, upgrades, dynamic inventory; source control/branching)
  - IPv6 modernization (tunneling, dual-stack, NAT64)
  - 📚 Sources used (Module 1): Official N10-009 Objectives; Official exam page.

### 2 · Network Implementation (20%)

- **`2.1`** Routing technologies (characteristics)  →  `30`, `36`, `43`
  - Static vs dynamic (BGP, EIGRP, OSPF)
  - Route selection (administrative distance, prefix length, metric)
  - NAT/PAT; FHRP; VIP; subinterfaces
- **`2.2`** Switching technologies & features (scenario-based)  →  `36`, `38`, `40`
  - VLAN (database, SVI); interface config (native/voice VLAN, 802.1Q tagging, LAG, speed/duplex)
  - Spanning tree; MTU/jumbo frames
- **`2.3`** Wireless devices & technologies (select/configure)  →  `37`, `50`, `51`
  - Channels (width, non-overlap, 802.11h)
  - Bands 2.4/5/6 GHz, band steering
  - SSID/BSSID/ESSID; types (mesh, ad hoc, P2P, infrastructure)
  - Encryption WPA2/WPA3; guest/captive portal; auth PSK vs Enterprise
  - Antennas (omni vs directional); autonomous vs lightweight AP
- **`2.4`** Physical installation factors  →  `10`, `11`, `13`
  - Locations (IDF/MDF), rack size, port-side airflow
  - Cabling (patch panel, fiber distribution panel), lockable enclosures
  - Power (UPS, PDU, load, voltage); environment (humidity, fire suppression, temperature)
  - 📚 Sources used (Module 2): Official N10-009 Objectives; Official exam page.

### 3 · Network Operations (19%)

- **`3.1`** Organizational processes & procedures (purpose)  →  `10`, `13`, `25`
  - Documentation (physical/logical, rack, cable, L1/L2/L3 diagrams)
  - Asset inventory (HW/SW/licensing/warranty), IPAM, SLA, wireless survey/heat map
  - Lifecycle mgmt (EOL/EOS, SW mgmt—patches/bug-fixes/OS/firmware, decommissioning)
  - Change mgmt (request tracking); configuration mgmt (production/backup/baseline-golden)
- **`3.2`** Network monitoring technologies (scenario-based)  →  `37`, `38`, `80`
  - Methods: SNMP (traps, MIB, v2c/v3), flow data, packet capture, baseline metrics, anomaly alerts, log aggregation (syslog, SIEM), API integration, port mirroring
  - Solutions: discovery (ad hoc/scheduled), traffic/performance/availability/config monitoring
- **`3.3`** Disaster recovery concepts  →  `25`
  - Metrics: RPO, RTO, MTTR, MTBF
  - Sites: cold/warm/hot
  - HA: active-active, active-passive
  - Testing: tabletop, validation
- **`3.4`** IPv4/IPv6 network services (implement)  →  `28`, `30`, `31`
  - Addressing (static/dynamic); DHCP/SLAAC
  - DNS (A/AAAA/CNAME/MX/TXT; primary/secondary; recursive; hosts file)
  - Time protocols: NTP, PTP, NTS
  - VPN: site-to-site; client-to-site (clientless, split vs full tunnel)
- **`3.5`** Access & management methods (compare/contrast)  →  `87`
  - SSH/GUI/API/console; jump box/host; in-band vs out-of-band management
  - 📚 Sources used (Module 3): Official N10-009 Objectives.

### 4 · Network Security (14%)

- **`4.1`** Basic network security concepts (importance)  →  `35`, `40`, `60`
  - Logical security: encryption (in-transit/at-rest), certificates (PKI, self-signed)
  - IAM (auth, MFA, SSO, RADIUS/LDAP/SAML/OAuth/OIDC/TACACS+), authorization/least privilege/roles
  - Physical controls (cams/locks); deception (honeypot/honeynet)
  - Risk, vuln, exploit, threat, CIA; audits/compliance (data locality, PCI DSS, GDPR)
  - Segmentation (IoT/IIoT/SCADA/ICS/OT/guest/BYOD)
- **`4.2`** Common attack types & threats (explain)  →  `32`, `33`, `36`
  - DoS/DDoS, VLAN hopping, MAC flooding, ARP poisoning/spoofing
  - DNS poisoning/spoofing, rogue DHCP/AP, evil twin, on-path
  - Social engineering (phishing, dumpster diving, shoulder surfing, tailgating)
  - Malware categories
- **`4.3`** Features, defenses, solutions (apply)  →  `30`, `35`, `37`
  - Device hardening (disable unused ports/services; change defaults)
  - NAC (port security, 802.1X, MAC filtering)
  - Key management; security rules (ACL, URL/content filtering)
  - Zones (trusted/untrusted; screened subnet)
  - 📚 Sources used (Module 4): Official N10-009 Objectives.

### 5 · Network Troubleshooting (24%)

- **`5.1`** Troubleshooting methodology (explain)  →  `86`, `88`
  - Identify → establish theory (top-down/bottom-up, divide-and-conquer) → test → plan → implement/escalate → verify/prevent → document
- **`5.2`** Cabling & physical interface issues (troubleshoot)  →  `10`, `11`, `12`
  - Cable: wrong type (SMF/MMF; Cat5/6/7/8; STP vs UTP), crosstalk/interference/attenuation, improper termination, TX/RX reversed
  - Interface: rising counters (CRC, runts, giants, drops); port status (err-disabled/admin-down/suspended)
  - Hardware: PoE (budget/standard), transceiver mismatch/signal strength
- **`5.3`** Network services issues (troubleshoot)  →  `30`, `40`, `41`
  - Switching: STP loops/root/roles/states; VLAN assignment; ACLs
  - Routing: table/default routes; address pool exhaustion; wrong default gateway/IP/subnet; duplicate IP
- **`5.4`** Performance issues (troubleshoot)  →  `28`, `38`, `50`
  - Congestion/contention; bottlenecks; bandwidth/throughput; latency; packet loss; jitter
  - Wireless: interference (channel overlap), signal loss, coverage gaps, client disassociation, roaming misconfiguration
- **`5.5`** Tools & protocols (use appropriately)  →  `10`, `12`, `14`
  - Software: protocol analyzer; CLI—ping, traceroute/tracert, nslookup, tcpdump, dig, netstat, ip/ifconfig/ipconfig, arp, nmap
  - Discovery: LLDP/CDP; speed tester
  - Hardware: toner, cable tester, taps, Wi-Fi analyzer, visual fault locator
  - Device commands: show mac-address-table/route/interface/config/arp/vlan/power
  - 📚 Sources used (Module 5): Official N10-009 Objectives; Network+ blog Q&A (weights clarification).
  - Quality & Coverage Checks
  - Mirrors the official N10-009 V9 objectives end-to-end (domains 1.0–5.0).
  - Duration/languages/weights verified from CompTIA’s exam page and blog Q&A.
  - Source Pack (official & reputable)
  - Official: Network+ (V9) page — exam facts, domain weights, languages, launch date.
  - Official: N10-009 Objectives — complete blueprint.
  - Official: Partner/blog updates — launch/retirement timing for 008/009.
  - Reputable training overviews corroborating domain coverage and timing.

---

# CompTIA Linux+

`XK0-006 (V8)` · CompTIA · **NOT TAKEN**

> Not taken. Closes a real gap — your Linux is self-taught from Veevo.

<sub>Sources merged: CompTIA V8 syllabus</sub>

### 1 · System Management (23%)

- **`1.1`** Linux basics, boot & kernel  →  `12`, `27`
  - Identify boot sequence, kernel role, filesystems, CPU/arch variants
- **`1.2`** Device management  →  `12`
  - Kernel modules; key device utilities; hardware component management
- **`1.3`** Storage management  →  `12`
  - Partitions, LVM, RAID; mount/automount; verify/repair filesystems
- **`1.4`** Network configuration  →  `32`, `33`
  - Hosts/DNS; interfaces (static/DHCP); essential network tools
- **`1.5`** Shell operations  →  `27`
  - Navigation, editors, redirection/pipes, environment variables/profiles
- **`1.6`** Backups & restores  →  `25`
  - Archiving, compression, basic recovery workflows
- **`1.7`** Virtualization  →  `70`, `93`
  - Hypervisor basics; create VMs; manage images
  - 📚 Sources used (Module 1): Official V8 page; Press release; V7 objectives for continuity.

### 2 · Services & User Management (20%)

- **`2.1`** Files, directories & permissions
  - rwx/UGO, special bits; links; special files
- **`2.2`** Local accounts & groups
  - Add/modify/remove; default settings; group membership
- **`2.3`** Process control & scheduling  →  `27`
  - States, priorities, foreground/background; timers/cron/systemd
- **`2.4`** Software/package management  →  `27`
  - Install/update/remove packages & repos
- **`2.5`** System services & logs
  - Start/stop/enable; inspect logs; journalctl; service health
- **`2.6`** Containers (ops focus)  →  `70`
  - Run/inspect containers; manage images; basic networks
  - 📚 Sources used (Module 2): Official V8 page; Press release; V7 page.

### 3 · Security (18%)

- **`3.1`** AuthN & accounting
  - PAM, LDAP, Kerberos; enable auditing
- **`3.2`** Firewalls  →  `61`
  - iptables, nftables, UFW; zones/firewalld use cases
- **`3.3`** OS hardening & remote access  →  `63`
  - Ownership/permissions; sudo; secure SSH
- **`3.4`** Account security  →  `27`
  - Password policies; shell restrictions; MFA basics
- **`3.5`** Cryptography  →  `64`
  - File encryption, hashing, certs
- **`3.6`** Compliance & integrity
  - Integrity checks; scanning; standards alignment
  - 📚 Sources used (Module 3): Official V8 page; Press release; V7 objectives for mapping.

### 4 · Automation, Orchestration & Scripting (17%)

- **`4.1`** Configuration management & CI/CD  →  `87`
  - Ansible/Puppet usage; CI/CD pipeline touchpoints
- **`4.2`** Shell scripting  →  `27`
  - Variables, functions, control flow; debugging
- **`4.3`** Python basics  →  `87`
  - Environments, packaging, core data types
- **`4.4`** Version control
  - Git workflows, tagging, branching hygiene
- **`4.5`** AI best practices
  - Responsible code generation & prompt engineering
  - 📚 Sources used (Module 4): Official V8 page; Press release.

### 5 · Troubleshooting (22%)

- **`5.1`** System monitoring  →  `80`
  - Health checks; logs; alerting signals
- **`5.2`** Hardware & storage  →  `12`
  - Boot/mount failures; filesystem repair; disk performance
- **`5.3`** Networking  →  `33`, `61`
  - DNS/connectivity/firewall rules; routing mishaps
- **`5.4`** Security  →  `60`
  - SELinux/AppArmor, permissions, vulnerability remediation
- **`5.5`** Performance tuning  →  `12`, `27`, `54`
  - CPU/memory/I/O analysis; remediation & optimization
  - 📚 Sources used (Module 5): Official V8 page; Press release.
  - Quality & Coverage Checks
  - Mirrors the latest official V8 (XK0-006) outline and weights; older content (V7/V6) is flagged above.
  - If a full V8 objectives PDF is not publicly posted, the V8 page + press release are the authoritative sources; V7 PDF is used only for continuity.
  - Source Pack (≥5 total; official first)
  - Official: Linux+ V8 page (XK0-006) — domains, weights, exam facts, launch date.
  - Official: Press release (V8 announcement) — Jul 24, 2025.
  - Official: Linux+ main page (V8 “New Version”, V7 retire dates).
  - Official: Linux+ V7 page (XK0-005) — exam details.
  - Official: XK0-005 objectives PDF — domain weights & objective wording for comparison.
  - Official: CertMaster migration notice — confirms V8 (XK0-006) timing (mid‑July 2025).

---

# CompTIA ITF+ — IT Fundamentals

`FC0-U61 (V5)` · CompTIA · **BELOW LEVEL**

> Entry-level. Below where you are — kept for completeness only.

<sub>Sources merged: CompTIA V5 syllabus</sub>

### 1 · IT Concepts and Terminology (17%)

- **`1.1`** Compare and contrast notational systems
  - Binary
  - Hexadecimal
  - Decimal
  - Data representation: ASCII, Unicode
- **`1.2`** Compare and contrast fundamental data types & characteristics
  - Char
  - Strings
  - Numbers (integers, floats)
  - Boolean
- **`1.3`** Illustrate basics of computing & processing
  - Input
  - Processing
  - Output
  - Storage
- **`1.4`** Explain the value of data & information  →  `36`
  - Data/info as assets; invest in security
  - Data→information; IP: trademarks, copyright, patents
  - Digital products; data-driven decisions (capture/collection, correlation, meaningful reporting)
- **`1.5`** Compare & contrast common units of measure
  - Storage: bit, byte, KB, MB, GB, TB, PB
  - Throughput: bps, Kbps, Mbps, Gbps, Tbps
  - Processing speed: MHz, GHz
- **`1.6`** Explain the troubleshooting methodology  →  `86`, `88`
  - Identify → Research → Establish theory → Test → Plan → Implement/escalate → Verify & prevent → Document
  - 📚 Sources used (Module 1): Official objectives (FC0-U61 v3.0); Official ITF+ page.

### 2 · Infrastructure (22%)

- **`2.1`** Classify common input/output device interfaces  →  `15`, `50`, `52`
  - Networking: wired (RJ-11, RJ-45), wireless (Bluetooth, NFC)
  - Peripheral: USB, FireWire, Thunderbolt, Bluetooth, RF
  - Graphics: VGA, HDMI, DVI, DisplayPort, MiniDP
- **`2.2`** Install common peripherals to a laptop/PC (scenario)  →  `15`, `40`, `90`
  - Printer, scanner, keyboard, mouse, camera, external HDD, speakers, display
  - Plug-and-play vs driver install; IP-based peripherals; web-based config
- **`2.3`** Explain internal computing components  →  `12`, `52`
  - Motherboard/system board; Firmware/BIOS; RAM; CPU (ARM, 32/64-bit)
  - Storage (HDD, SSD); GPU; Cooling; NIC (wired/wireless; on-board vs add-on)
- **`2.4`** Compare Internet service types  →  `10`, `11`, `50`
  - Fiber optic; Cable; DSL; Wireless (RF, satellite, cellular)
- **`2.5`** Compare storage types  →  `11`, `12`, `24`
  - Volatile vs non-volatile
  - Local: RAM; HDD (spinning/solid-state); optical; flash
  - Local network: NAS; file server; Cloud storage services
- **`2.6`** Compare common computing devices & purposes  →  `15`, `40`, `87`
  - Phones, tablets, laptops, workstations, servers, game consoles
  - IoT: appliances; home automation; cars; IP cams; streaming; medical devices
- **`2.7`** Explain basic networking concepts  →  `33`, `37`, `38`
  - Packet basics; DNS (URL→IP); LAN vs WAN; IP and MAC addresses
  - Protocols: HTTP/S, POP3, IMAP, SMTP; Devices: modem, router, switch, AP, firewall
- **`2.8`** Install/configure/secure a basic wireless network (scenario)  →  `37`, `51`, `52`
  - 802.11 a/b/g/n/ac (age/speed/interference/attenuation)
  - Best practices: change SSID & defaults; encryption: open, captive portal, WEP, WPA, WPA2
  - 📚 Sources used (Module 2): Official objectives; Official ITF+ page.

### 3 · Applications & Software (18%)

- **`3.1`** Purpose of operating systems  →  `12`, `70`, `95`
  - Interface app↔hardware; disk mgmt; process/scheduling; app & memory mgmt; device mgmt; access control
  - OS types: mobile, workstation, server, embedded (firmware), hypervisor (Type 1)
- **`3.2`** OS components (compare/contrast)  →  `28`, `64`
  - File systems: NTFS, FAT32, HFS, ext4
  - Features: compression, encryption, permissions, journaling, limits, naming rules
  - File mgmt: folders, extensions, permissions; Services; Processes; Drivers; Utilities; CLI vs GUI
- **`3.3`** Purpose & proper use of software  →  `86`, `89`
  - Productivity: word proc, spreadsheet, presentation, browser, diagramming
  - Collaboration: email, conferencing, IM, online workspace, document sharing
  - Business: database, project mgmt, accounting
- **`3.4`** App architecture & delivery  →  `74`
  - Delivery: local install; local-network hosted; cloud hosted
  - Architecture: 1-tier, 2-tier, 3-tier, n-tier
- **`3.5`** Configure/use web browsers (scenario)  →  `28`
  - Cache/clear cache; disable client-side scripting; manage extensions
  - Private browsing; proxy settings; certs (valid/invalid); pop-up/script blockers; compatibility
- **`3.6`** General application concepts & uses  →  `75`
  - Single-platform vs cross-platform
  - Licensing: single use, site, concurrent, open-source vs proprietary, subscription vs one-time, product keys/serials
  - Install best practices
  - 📚 Sources used (Module 3): Official objectives.

### 4 · Software Development Concepts (12%)

- **`4.1`** Programming language categories (compare/contrast)
  - Interpreted (scripting, scripted, markup); Compiled; Query; Assembly
- **`4.2`** Use organizational techniques & interpret logic (scenario)
  - Pseudocode; Flow-charts (sequence); Logic: branching, looping
- **`4.3`** Purpose & use of programming concepts  →  `70`
  - Identifiers: variables, constants; Containers: arrays, vectors; Functions; Objects: properties, attributes, methods
  - 📚 Sources used (Module 4): Official objectives.

### 5 · Database Fundamentals (11%)

- **`5.1`** Database concepts & purpose
  - Usage: create, import/input, query, reports
  - Flat file vs database (concurrency, scalability, speed, data variety)
  - Records; Storage (persistence); Structured vs semi-structured vs unstructured
- **`5.2`** Database structures (compare/contrast)  →  `86`
  - Relational: schema; tables (rows, fields); primary/foreign keys; constraints
  - Non-relational: key/value, document
  - Relational methods: DML (select/insert/delete/update); DDL (create/alter/drop); permissions
- **`5.3`** Interface methods  →  `25`
  - Access: direct/manual; programmatic; UI/utility; query/report builders
  - Export/import: dump, backup
  - 📚 Sources used (Module 5): Official objectives.

### 6 · Security (20%)

- **`6.1`** CIA concerns (summarize)  →  `12`, `14`, `47`
  - Confidentiality: snooping, eavesdropping, wiretapping, social engineering, dumpster diving
  - Integrity: MITM, replay, impersonation, unauthorized alteration
  - Availability: DoS, power outage, hardware failure, destruction, service outage
- **`6.2`** Secure devices & best practices (explain)  →  `10`, `36`, `60`
  - AV/anti-malware; Host firewall; Change defaults/enable passwords; Safe browsing; Patching/updates
- **`6.3`** Behavioral security (summarize)  →  `47`
  - Policies/procedures; Handling confidential info (passwords; personal/customer/company data)
- **`6.4`** AAA & non-repudiation (compare/contrast)  →  `35`
  - Authentication (single-factor, multifactor); Authorization; Accounting; Non-repudiation concepts
- **`6.5`** Password best practices (explain)
  - Length/complexity/rotation/uniqueness; password managers
- **`6.6`** Common uses of encryption (explain)  →  `64`
  - In-transit and at-rest; certificates
- **`6.7`** Business continuity concepts (explain)  →  `25`, `54`, `74`
  - Cloud storage (on-site vs off-site); Contingency planning; Disaster recovery (restore data, prioritization, restore access)
  - 📚 Sources used (Module 6): Official objectives.
  - Quality & Coverage Checks
  - Mirrors the official FC0-U61 objectives v3.0 and domain weights. ITF+ is retired; retirement dates/version history included.
  - Where partner pages conflicted with the main site (launch date/languages), the conflict is noted in Version history.
  - Source Pack (official & reputable)
  - CompTIA ITF+ certification page — exam facts, languages, retirement dates.
  - ITF+ Objectives (FC0-U61 v3.0 PDF) — full blueprint by domain.
  - CompTIA Partners — IT Fundamentals — launch & details (partner view).
  - CompTIA Tech+ certification page — successor (FC0-U71).
  - CompTIA blog — ITF+ retirement in 2025 (context).

---

# Microsoft Azure Administrator

`AZ-104` · Microsoft · **COURSEWORK ONLY**

> Coursework via Technical Guftgu, Aug–Oct 2023. Exam pass status still unconfirmed.

<sub>Sources merged: Technical Guftgu course content</sub>

### 1 · Manage Azure identities and governance

- **`1.1`** Manage Entra ID (Azure AD) objects  →  `75`
  - Create users and groups
  - Manage user and group properties
  - Manage device settings
  - Perform bulk user updates
  - Manage guest accounts
  - Configure Azure AD join
  - Configure self-service password reset
- **`1.2`** Manage role-based access control (RBAC)  →  `35`, `75`, `95`
  - Create a custom role
  - Assign roles at different scopes
  - Interpret access assignments
- **`1.3`** Manage subscriptions and governance  →  `75`
  - Configure Azure policies
  - Configure resource locks
  - Apply and manage tags
  - Manage resource groups
  - Manage subscriptions
  - Manage costs
  - Configure management groups

### 2 · Implement and manage storage

- **`2.1`** Secure storage  →  `35`, `75`, `76`
  - Configure network access to storage accounts
  - Create and configure storage accounts
  - Generate SAS tokens
  - Manage access keys
  - Configure Entra authentication for storage
  - Configure access to Azure Files
- **`2.2`** Manage storage  →  `76`
  - Export from Azure job
  - Import into Azure job
  - Azure Storage Explorer
  - Copy data with AzCopy
  - Storage replication
  - Blob object replication
- **`2.3`** Configure Azure Files and Blob Storage  →  `76`
  - Create an Azure file share
  - Azure File Sync service
  - Configure Blob Storage
  - Storage tiers for Blob Storage
  - Blob lifecycle management

### 3 · Deploy and manage Azure compute resources

- **`3.1`** Automate VM deployment with ARM templates  →  `77`, `89`
  - Modify an ARM template
  - Configure a VHD template
  - Deploy from a template
  - Save a deployment as a template
  - Deploy VM extensions
- **`3.2`** Configure VMs  →  `12`, `64`, `73`
  - Azure Disk Encryption
  - Move VMs between resource groups
  - Manage VM sizes
  - Add data disks
  - Configure networking
  - Redeploy VMs
  - Configure high availability
  - Deploy and configure scale sets
- **`3.3`** Create and configure containers  →  `70`, `73`, `77`
  - Sizing and scaling for Container Instances
  - Container groups
  - Storage for AKS
  - Scaling for AKS
  - Network connections for AKS
  - Upgrade an AKS cluster
- **`3.4`** Create and configure Azure App Service  →  `25`, `77`, `89`
  - Create an App Service plan
  - Configure scaling settings
  - Create an App Service
  - Secure an App Service
  - Custom domain names
  - Backup for an App Service
  - Networking settings
  - Deployment settings

### 4 · Configure and manage virtual networking

- **`4.1`** Implement and manage virtual networking  →  `30`, `33`, `64`
  - Create and configure VNets including peering
  - Private and public IP addresses
  - User-defined network routes
  - Implement subnets
  - Endpoints on subnets
  - Private endpoints
  - Azure DNS, custom DNS, private/public zones
- **`4.2`** Secure access to virtual networks  →  `30`, `61`, `78`
  - Create security rules
  - Associate an NSG to subnet or NIC
  - Evaluate effective security rules
  - Implement Azure Firewall
  - Implement Azure Bastion
- **`4.3`** Configure load balancing  →  `78`, `88`
  - Azure Application Gateway
  - Internal or public load balancer
  - Troubleshoot load balancing
- **`4.4`** Monitor and troubleshoot virtual networking  →  `78`, `80`, `88`
  - Monitor on-premises connectivity
  - Network Performance Monitor
  - Troubleshoot external networking
  - Troubleshoot VNet connectivity
- **`4.5`** Integrate on-premises with an Azure virtual network  →  `48`, `62`, `78`
  - Azure VPN Gateway
  - Azure ExpressRoute
  - Azure Virtual WAN

### 5 · Monitor and back up Azure resources

- **`5.1`** Monitor resources with Azure Monitor  →  `79`, `80`
  - Configure and interpret metrics
  - Configure Azure Monitor logs
  - Query and analyze logs
  - Set up alerts and actions
- **`5.2`** Implement backup and recovery  →  `25`, `79`
  - Create a Recovery Services vault
  - Create and configure backup policy
  - Backup and restore with Azure Backup
  - Site-to-site recovery with Azure Site Recovery
  - Configure and review backup reports

---

# MCSE: Server Infrastructure

`70-410 → 70-414` · Microsoft · **⚠ RECORD CONFLICT**

> CONFLICT: this syllabus is Windows Server 2012 and these exams retired January 2021. Your records say "MCSE Server 2022", which is not a Microsoft credential. See the merge report.

<sub>Sources merged: Sansbound MCSE Server Infrastructure syllabus</sub>

### 1 · 70-410 Installing and Configuring Windows Server 2012

- **`1.1`** Installing Windows Server 2012  →  `21`
- **`1.2`** Disk management  →  `12`
  - MBR, GPT
  - Basic disk, dynamic disk
  - Storage pool, disk pool
  - VHD
- **`1.3`** NTFS file system and features
  - File permissions
  - Quota
  - VSS
  - Offline files
- **`1.4`** Hyper-V  →  `72`, `77`, `78`
  - Creating and configuring virtual machines
  - Virtual machine storage
  - Virtual networks
- **`1.5`** IPv4 and IPv6  →  `31`
- **`1.6`** DHCP deployment and configuration  →  `32`, `89`
- **`1.7`** DNS  →  `33`
  - Forward and reverse lookup
  - Primary, secondary, stub zone
  - Forwarders, root hints
  - Caching-only DNS
  - Dynamic DNS
- **`1.8`** Installing Active Directory domain controllers  →  `22`
- **`1.9`** Active Directory user, group, OU management  →  `22`
- **`1.10`** Group Policy objects  →  `23`
  - Create and manage GPOs
  - Configure security policies
  - Application restriction policies
- **`1.11`** Configure Windows Firewall  →  `61`

### 2 · 70-411 Administering Windows Server 2012

- **`2.1`** Windows Deployment Services (WDS)  →  `89`
- **`2.2`** Windows Server Update Services (WSUS)  →  `21`, `24`
- **`2.3`** Data Collector Sets monitoring  →  `80`, `93`
  - Servers, VMs
  - Networking
  - Real-time performance
- **`2.4`** Distributed File System (DFS)  →  `24`
- **`2.5`** File Server Resource Manager (FSRM)  →  `24`
- **`2.6`** File and disk encryption  →  `12`, `64`
- **`2.7`** Configure routing and NAT  →  `36`
- **`2.8`** Configure VPN  →  `62`
- **`2.9`** Configure RADIUS servers  →  `35`
- **`2.10`** Network Access Protection
- **`2.11`** FSMO roles  →  `22`
- **`2.12`** Active Directory backup and restoration  →  `22`, `25`, `70`
  - Object and container level recovery
  - Task delegation
- **`2.13`** Advanced Group Policy configuration and management  →  `23`

### 3 · 70-412 Configuring Advanced Windows Server 2012 Services

- **`3.1`** Network Load Balancing (NLB)  →  `73`, `78`
- **`3.2`** Failover clustering  →  `73`
- **`3.3`** Virtual machine migration  →  `77`, `89`
- **`3.4`** Advanced file services
- **`3.5`** Dynamic Access Control (DAC)  →  `95`
- **`3.6`** Configure and optimize storage
- **`3.7`** Windows Server Backup and bare metal recovery  →  `21`, `25`
- **`3.8`** Windows booting and troubleshooting boot issues  →  `88`
- **`3.9`** Hyper-V site level fault tolerance  →  `72`
- **`3.10`** Advanced DHCP and advanced DNS  →  `32`, `33`
- **`3.11`** Active Directory forest trust relationships  →  `22`
- **`3.12`** Active Directory Sites and Services  →  `22`
- **`3.13`** Active Directory Certificate Services  →  `22`, `24`
- **`3.14`** Active Directory Rights Management Services (ADRMS)  →  `22`

### 4 · 70-413 Designing and Implementing a Server Infrastructure

- **`4.1`** Design an automated server installation strategy  →  `89`
- **`4.2`** Plan and implement a server deployment infrastructure  →  `89`
- **`4.3`** Plan and implement server upgrade and migration  →  `89`
- **`4.4`** Plan and deploy Virtual Machine Manager services  →  `77`
- **`4.5`** Plan and implement file and storage services
- **`4.6`** Design and maintain a DHCP solution  →  `32`
- **`4.7`** Design a name resolution solution strategy  →  `33`
- **`4.8`** Design and manage an IP address management solution
- **`4.9`** Design a VPN solution  →  `62`
- **`4.10`** Design a forest and domain infrastructure  →  `22`
- **`4.11`** Design a Group Policy strategy  →  `23`
- **`4.12`** Design an Active Directory permission model  →  `22`
- **`4.13`** Design an Active Directory sites topology  →  `22`
- **`4.14`** Design a domain controller strategy  →  `22`

### 5 · 70-414 Implementing an Advanced Server Infrastructure

- **`5.1`** Plan and implement failover clustering  →  `73`
- **`5.2`** Plan and implement highly available network services
- **`5.3`** Plan and implement highly available storage solutions
- **`5.4`** Plan and implement highly available server roles  →  `21`
- **`5.5`** Plan and implement business continuity and disaster recovery  →  `25`
- **`5.6`** Plan and implement virtualization hosts  →  `70`
- **`5.7`** Plan and implement virtualization guests  →  `70`
- **`5.8`** Plan and implement virtualization networking  →  `70`
- **`5.9`** Plan and implement virtualization storage  →  `70`

---

# LPIC-1 / Linux Administration

`101 + 102` · LPI · **SELF-STUDY**

> Self-study notes, not a course enrolment. Modules 101–102 detailed; 103+ outstanding.

<sub>Sources merged: LPIC-1 101.1 notes · LPIC-1 101/102 notes (duplicated in source) · Linux+ & LPIC-1 merged roadmap</sub>

### 101 · System Architecture

- **`101.1`** Determine and configure hardware settings  →  `12`, `14`, `27`
  - BIOS vs UEFI, Secure Boot
  - MBR vs GPT
  - Boot process: POST, GRUB, kernel, init, login
  - Kernel basics: /boot/vmlinuz, modules, uname -r
  - Init systems: SysVinit, Upstart, systemd
  - /proc: cpuinfo, meminfo, uptime, version, cmdline, modules
  - /sys: class/net, class/block, class/backlight
  - Hardware discovery: lspci, lsusb, lshw, lsblk, lscpu, dmidecode
- **`101.2`** Boot the system  →  `12`, `25`
  - GRUB2 for BIOS and UEFI
  - grub.cfg and /etc/default/grub
  - Kernel and initramfs loading
  - Editing the kernel command line
  - Rescue and recovery, chroot from live media
- **`101.3`** Change runlevels/boot targets, shutdown, reboot  →  `14`, `27`
  - SysVinit runlevels 0-6
  - systemd targets: multi-user, graphical, rescue, emergency
  - systemctl isolate / set-default / get-default
  - shutdown, reboot, halt, poweroff
  - Scheduling and cancelling a shutdown

### 102 · Linux Installation and Package Management

- **`102.1`** Design hard disk layout  →  `12`
  - Mount points: /, /home, /boot, /var, /srv, /tmp
  - Filesystems: ext4, xfs, btrfs, FAT32, NTFS
  - Swap partition vs swap file
  - mkfs, lsblk, parted, fdisk, df -h, mount
- **`102.2`** Install a boot manager  →  `12`
  - grub-install, update-grub
  - UEFI vs BIOS booting
  - Dual booting
  - /etc/default/grub, /etc/grub.d/
- **`102.3`** Manage shared libraries  →  `36`
  - Shared object (.so) files
  - Library paths /lib, /usr/lib, /lib64
  - ldd, ldconfig, LD_LIBRARY_PATH
  - /etc/ld.so.conf and conf.d
- **`102.4`** Use Debian package management  →  `27`
  - dpkg -i, -r, -l, -s, -L, -S
  - apt update, upgrade, install, remove
  - apt search, show, autoremove, install -f
- **`102.5`** Use RPM, YUM, DNF, Zypper  →  `27`
  - rpm -i, -U, -e, -qa, -qi, -ql, -qf
  - yum install, remove, search, info, update
  - dnf as the modern yum
  - zypper install, remove, info, update, search
- **`102.6`** Shared object dependencies and package verification  →  `27`
  - ldd to list required libraries
  - ldconfig to refresh the linker cache
  - dpkg -s, -V, -S
  - rpm -V, -qf

### 103 · Practical Roadmap (self-study track)

- **`103.1`** Filesystem structure and shell basics  →  `27`
  - ls, cd, find, cat
  - Linux directory layout
- **`103.2`** User and group management
  - useradd, passwd
  - groupadd, usermod -aG
- **`103.3`** File permissions and ownership
  - chmod, chown
  - umask
  - rwx and special bits
- **`103.4`** Process and job management
  - ps aux, top
  - kill, nice
  - Signals and job control
- **`103.5`** Package management practice  →  `27`
  - apt update/install
  - yum remove, rpm -qi
- **`103.6`** Bash scripting and automation  →  `27`, `87`
  - Writing and chmod +x a script
  - crontab -e
  - at
- **`103.7`** Networking fundamentals  →  `88`
  - ip a, ping
  - ss -tuln
  - nmap
- **`103.8`** Log files and system monitoring  →  `37`, `80`, `83`
  - tail -f /var/log/syslog
  - journalctl -xe
  - free -h, df -h
- **`103.9`** Security and hardening  →  `63`
  - ufw enable/allow
  - sshd_config
  - chage
- **`103.10`** Boot and system initialization
  - systemctl status/enable
  - journalctl -b
  - update-grub
- **`103.11`** Disk and storage management  →  `12`
  - lsblk, mount
  - mkfs.ext4
  - df -Th
- **`103.12`** Archives and environment  →  `36`
  - tar -czvf
  - alias
  - export PATH

---

# Merge report

Thirteen courses were built from twenty-one source documents. What happened:

| Course | Sources folded in |
|---|---|
| Cisco Certified Support Technician | 1 — Cisco official objectives (PDF) |
| CCNA | 2 — Cisco blueprint v1.1 (2024) · Cisco blueprint v1.0 (2021) |
| CCNP ENCOR | 6 — Cisco blueprint v1.1 · Cisco blueprint v1.0 · NetAcad-aligned breakdown · CBT Nuggets 24-week plan · Global Knowledge ENCOR 1.3 + 31 labs · NetCom ENCOR v1.3 outline |
| CCNP ENARSI | 4 — Cisco blueprint v1.1 · Module breakdown · CBT Nuggets 14-week plan · Global Knowledge ENARSI 1.1 + 29 labs |
| CCNP SCOR | 2 — Cisco blueprint v1.1 · NetAcad-aligned syllabus |
| CCNP SNCF | 1 — NetAcad-aligned syllabus |
| CompTIA A+ | 1 — CompTIA V15 syllabus |
| CompTIA Network+ | 1 — CompTIA V9 syllabus |
| CompTIA Linux+ | 1 — CompTIA V8 syllabus |
| CompTIA ITF+ | 1 — CompTIA V5 syllabus |
| Microsoft Azure Administrator | 1 — Technical Guftgu course content |
| MCSE: Server Infrastructure | 1 — Sansbound MCSE Server Infrastructure syllabus |
| LPIC-1 / Linux Administration | 3 — LPIC-1 101.1 notes · LPIC-1 101/102 notes (duplicated in source) · Linux+ & LPIC-1 merged roadmap |

## Conflicts and version notes

1. **MCSE.** The uploaded syllabus is *Windows Server 2012* (70-410 → 70-414). Microsoft retired
   those exams in January 2021, and there is no Microsoft credential called "MCSE Server 2022".
   The training was real; the certification name on your CV is not. Describe it as
   *Windows Server administration training (Corvit, 2022)* instead.
2. **CCNA.** Two blueprints were supplied — v1.0 (2021) and v1.1 (2024). v1.1 is used here.
   Your certificate is from 2021, so it maps to v1.0. Differences that matter:
   v1.1 adds root guard / loop guard / BPDU filter / BPDU guard to STP; replaces the DNA Center
   management objective with **AI and machine learning in network operations**; and swaps
   Puppet/Chef for **Ansible and Terraform**.
3. **ENCOR.** Two blueprints supplied — v1.0 (2019) and v1.1 (2023). v1.1 used. It adds client
   density, STP enhancements, policy-based routing, wireless segmentation (groups/profiles/tags),
   PTP alongside NTP, and the EAPOL 4-way handshake.
4. **A+.** The uploaded syllabus is V15 (220-1201/1202, released March 2025). You certified in
   2021 on an earlier version. The content here is current, not what you sat.
5. **LPIC-1.** The 101/102 notes appear twice in the merged PDF. Deduplicated.
6. **ENARSI and ENCOR** each had an official blueprint plus an alternate breakdown. The alternates
   were not duplicates — they were the sub-content of the official objectives, so they were folded
   in one level down rather than appended as extra topics.

## Courses with no syllabus supplied

- **AZ-900** — passed, no syllabus in the upload
- **VMware ESXi / vCenter (Udemy)** — no syllabus in the upload
- **CCTV Operator (Corvit)** — no syllabus in the upload
