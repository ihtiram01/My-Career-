---
title: Career & Projects
page: experience
order: 1
colour: violet
kicker: Section 01 · career
summary: Roles and projects across data centres, telecom IP core, building systems, enterprise IT and CCTV — newest first, with the technologies actually touched.
placeholder: Search — huawei, zte, bms, center3, zabbix, cctv…
unit_group: roles
unit_card: projects
footer: Newest first. Each card opens the full project record; use the arrows at the bottom of a project to step through the sequence.
title_ar: المسيرة المهنية والمشاريع
title_ur: کیریئر اور پروجیکٹس
summary_ar: أدوار ومشاريع في مراكز البيانات، والشبكات الأساسية للاتصالات، وأنظمة المباني، وتقنية المعلومات للمؤسسات، وأنظمة المراقبة — الأحدث أولاً، مع التقنيات التي تم العمل عليها فعلياً.
summary_ur: ڈیٹا سینٹرز، ٹیلی کام آئی پی کور، بلڈنگ سسٹمز، انٹرپرائز آئی ٹی اور سی سی ٹی وی میں کردار اور پروجیکٹس — تازہ ترین پہلے، ان ٹیکنالوجیز کے ساتھ جن پر عملی طور پر کام کیا گیا۔
---

# FIELD EXPERIENCE & PROJECTS

<!--
HOW THIS FILE WORKS

  Order on the page = order in this file. Newest first. Move a `##` block to
  re-sequence; the numbers 01, 02, 03 … are added by the build.

  ## Name | location | period        one role or engagement, gets its own page
  role:     job title
  type:     Employment · Contract · Freelance · Independent   (sets the colour)
  slug:     the page address — set once, never change it
  summary:  one public sentence, shown on the card and the page
  cover:    img/experience/<slug>/cover.jpg   (optional dashboard photo)
  private:  a note for you only — kept here, never shown on the site

  ### Project title                   a project inside that role
  - any line                          becomes a bullet
  - photo: img/experience/<slug>/01.jpg | caption
  - master: 41, 42                    links into Knowledge by Layer
  - private: note for you only

  Photos: put them in img/experience/<slug>/. JPEG, about 1600 px wide,
  under 1.5 MB. Blur badges, rack labels, serials, IPs and faces first.
  A photo path that does not exist fails the build on purpose.
-->

## ANMAT Operations — Ministry of Tourism Project | Riyadh | Aug 2026 – present
role: BMS Controls & Low Current Engineer
type: Contract
slug: anmat-ministry-of-tourism
summary: VAV controller retrofit inside an occupied government building — replacing Trend IQeco controllers with Schneider SpaceLogic RP-V and preparing each device for the central BMS.

### VAV controller retrofit
- Trend IQeco VAV controllers replaced with Schneider SpaceLogic RP-V
- Carried out on night shifts inside a live, occupied facility
- Field device preparation for integration into the central BMS
- master: 89

### Cabling and field bus
- Cat 6A termination for controller connectivity
- RS-485 field bus loops, around five controllers per segment
- master: 10

### Site coordination and records
- Work permits and coordination with facility management
- As-installed records for each replaced controller
- Crew timesheet and shift reporting
- master: 86, 89

## center3 Riyadh — AI Infrastructure Rack Deployment | Riyadh | Oct 2026
role: Networking Level 2 Field Engineer
type: Freelance
slug: center3-ai-rack-deployment
summary: Physical installation of a five-rack AI compute deployment in a colocation data hall, dispatched through RADX Global Services for ITARMI.
private: Worked days 1 and 2 of a 3-day booking. Day 3 scope (optics to the accelerator racks, Lantronix config, labelling, handover) was not mine — do not claim it.

### Rack receiving and placement
- Received, inspected and uncrated five 42U racks — one Core Services Rack and four SambaNova SN40L-16 accelerator racks, around 520 kg each
- Moved and positioned the racks in the data hall
- Rack grounding and A/B PDU power feeds
- master: 13, 14

### Core Services Rack build
- Installed two Fortinet FortiGate 200G firewalls in the CSR, with internal cabling
- CSR platform: Juniper EX4400 management and QFX5130 400GbE data switching, Lantronix SLC8000 console server
- master: 13, 61

### Structured cabling and power-on
- Landed homerun console, management and data cabling to the CSR
- Patch panel terminations and NAP uplinks
- Console support during firewall bring-up
- PDU power-on after the overnight acclimatisation window
- master: 10, 11, 14

## Leon Technology — GO-ZTE IPCORE Project | Riyadh & Hail | Jun – Aug 2026
role: Data Center Deployment Engineer
type: Contract
slug: leon-go-zte-ipcore
summary: Physical deployment of GO Telecom's IP core across a 63-site rollout — ZTE carrier routing and switching, server staging, fibre and DC power.
private: Physical and staging work, not routing configuration. Be precise about that in interviews.

### Rollout scope
- 63-site rollout across Riyadh and Hail
- ZTE M6000-4SE and M6000-3S Plus routers, ZXR10 5950 / 5960 switches, R5300 G5 servers
- master: 89

### E-row cloud pod
- ZTE 5960M / 5960X leaf-spine fabric
- R5300 G5 servers as Ceph storage nodes
- Rack build, mounting and cable management
- master: 12, 13, 40, 73

### J-row M6000 IP core
- Brownfield T8000 swap-out
- Method of Procedure authoring and handover checklist
- master: 13, 86, 89

### Fibre, optics and power
- MPO/MTP trunks, LC OM4 patching and ODF cross-connects
- SFP+, SFP28 and QSFP28 optics
- DC power: -48V plant, rectifiers, breakers and PDUs
- master: 10, 11, 14

### Staging and asset control
- Bench testing of ZXR10 switches and R5300 G5 servers before install
- iEPMS asset scanning
- master: 12, 89

## MAMCO — Private Estate ICT Maintenance | Diriyah | May – Aug 2026
role: ICT Maintenance Engineer
type: Contract
slug: mamco-diriyah-estate
summary: Maintenance of an eleven-system ICT and low-current estate — networks, IPTV, AV and cinema, telephony, access control and intercom — on a private residential development.
private: The estate is confidential. Keep the client and the original installer unnamed on the site.

### IPTV and multicast
- Vitec AvediaStream encoders, AvediaServer and m9500 set-top boxes
- IGMP snooping and querier on Cisco CBS350 switches for multicast reliability
- Diagnosed missing free-to-air channels as a channel-lineup configuration gap, not a hardware fault
- master: 41

### Asset and lifecycle register
- 78-device End-of-Life register across every platform on the estate
- Identified Cisco CBS350 as end-of-sale, with a Catalyst 1300 migration path
- Master device inventory and a per-system document library
- master: 86

### Snag management
- Filtered a 6,500-item master snag list to around 500 open low-current items, classified by system and activity
- Flagged out-of-scope BMS and fire-system items instead of absorbing them
- master: 85, 89

### Control, AV and cinema
- Crestron and KNX control, Trinnov and Crown cinema audio, LG commercial displays
- Configuration backup practice across the estate
- private: Crestron/KNX reprogramming was blocked — the original installer holds the source code and ETS files.

## UCT — Two-Office SMB Deployment | Riyadh | May 2026
role: IT Infrastructure Engineer
type: Freelance
slug: uct
summary: End-to-end delivery of a two-office Windows environment — scoped, built and handed over solo.
private: Collected SAR 2,000.

### Windows Server 2022 build
- AD DS with the uct.local domain, built from scratch
- DNS, DHCP and NTFS permissions
- Group Policy: shared folders, drive mapping, USB block
- master: 21, 22, 23, 24

### Site-to-site link
- Point-to-point wireless bridge between the two offices
- master: 50, 54

### Delivery
- Client scoping and quoting
- Two-site rollout and handover
- master: 89

## Wemart Arabia Trading Co. (WenChao Group) | Riyadh | Oct 2025 – Apr 2026
role: IT Engineer
type: Employment
slug: wemart
summary: Full Huawei enterprise stack across a retail and warehouse estate, with a 237-camera CCTV system and Zabbix monitoring.
private: Your deepest production environment and the strongest source of interview material.

### Huawei core switching
- CloudEngine S6730 core switch — VLAN design, inter-VLAN routing, uplinks
- eKitEngine access switching and Eth-Trunk link aggregation
- VRP CLI daily operation and config backup discipline
- master: 28, 41, 42

### Huawei firewall and VPN
- USG6000E — zones, security policies, NAT
- IPsec site-to-site VPN to the Dubai head office over Zain
- master: 61, 62, 36

### Huawei wireless
- AirEngine WAC with 50+ access points
- AP provisioning at scale, SSID and security policy
- master: 52, 53

### Hikvision CCTV estate
- 237 cameras across 4 NVRs
- PoE budget planning and VLAN segmentation for cameras
- Storage retention calculation and a disk-full recovery incident
- Fibre plus media converter for a long basement run, after a converter failure
- Camera placement corrections after a coverage review
- master: 90, 91, 92, 93, 94

### Zabbix monitoring
- Huawei VRP SNMP template, host and item configuration
- Trigger and severity tuning — around 40% less alert noise
- Email alerting, printer and toner monitoring
- Network topology map through the JSON-RPC API
- master: 81, 82

### Windows and endpoints
- Active Directory, Group Policy and file shares
- POS terminal support, backup and endpoint management
- master: 15, 22, 23, 24, 25

## AlmavivA Information Technology | Riyadh | Mar 2024 – Oct 2025
role: Network Engineer
type: Employment
slug: almaviva
summary: Enterprise network operations — Cisco Catalyst core, VMware virtualisation, wireless bridge links and site-to-site VPNs under SLA monitoring.
private: Still the thinnest record on the page. Was Riyadh Metro Line 3 part of this role? If yes, merge the two.

### Core network
- Cisco Catalyst 4510 core switching
- IPsec site-to-site VPNs
- master: 40, 42, 62

### Wireless bridge links
- MOXA wireless bridges, with RF and VSWR testing
- master: 50, 54

### Virtualisation
- VMware vCenter and ESXi hosts
- master: 71

### Operations
- NMS and SLA monitoring
- ITIL-aligned incident and change handling
- master: 80, 85

## Riyadh Metro Line 3 — OCC-CTN | Riyadh
role: Network engineering support
type: Project
slug: riyadh-metro-line-3
summary: Extreme Networks EXOS environment on a metro transit network — Layer 2 ring resilience and live fault diagnosis.

### Extreme EXOS operations
- EXOS CLI, show commands and config management
- master: 28

### Layer 2 resilience
- EAPS ring protection — master and transit nodes, control VLAN
- MLAG configuration and behaviour
- Stack reconvergence diagnosis
- master: 42

### Fault diagnosis
- CRC and input-error investigation — cable, SFP and duplex causes
- Reference PDFs and troubleshooting cheat sheets for the team
- master: 40, 86, 88

## Express Publications (Pvt.) Ltd. | Peshawar | Jan 2023 – Feb 2024
role: System Support Engineer
type: Employment
slug: express-publications
summary: Systems and network support for a media house — 100+ endpoints on Windows Server, with Cisco routing and switching, pfSense and ESXi.

### Infrastructure
- Cisco routing and switching
- pfSense firewall
- VMware ESXi host
- master: 40, 61, 71

### Support operations
- Windows Server for 100+ endpoints
- Windows client deployment and troubleshooting
- Printer and peripheral support, user and permission administration
- master: 15, 20, 22, 88

### Backup and endpoint security
- Veeam backup
- Kaspersky endpoint protection
- master: 25, 64

## Veevo Tech (Pvt.) Ltd. | Peshawar | Apr 2021 – Dec 2022
role: NOC Engineer — promoted from Trainee
type: Employment
slug: veevo-tech
summary: A 24/7 NOC role — monitoring, Linux and SMS platform operations. Where the Zabbix and Linux skills started.

### NOC operations
- 24/7 monitoring with SSH and console diagnostics
- Ticketing and severity escalation
- ISP and field-team coordination
- Performance reports
- master: 80, 85, 88

### SMS platform
- SMS platform network and services
- Asterisk telephony
- Node.js services under PM2
- master: 30, 37, 84

### Monitoring and load balancing
- Zabbix server, agents and templates
- HAProxy with a Roxy-WI front end
- Dell OpenManage for hardware health
- master: 81, 84

### Linux and connectivity
- Ubuntu Server administration
- Site-to-site VPN between the Islamabad and Peshawar branches
- master: 27, 62

## Freelance and Side Work | Riyadh
role: Independent
type: Independent
slug: freelance-and-side-work
summary: Small paid jobs, self-directed builds and networking education content.

### Shared-internet router build
- Digitech S1 5G router for a shared, paid-access scenario
- Reached the limits of locked ISP firmware
- Identified a MikroTik captive portal as the right long-term design
- master: 53, 36

### Cisco 2960 PoE switch configuration
- Paid configuration work for a client in Saudi Arabia
- master: 41, 42

### @gulf_networking
- Networking education content on TikTok and LinkedIn (formerly @networkingwithmickey)
- Fibre, Ethernet vs fibre, OSI model and CCTV incident reels
- Python/PIL and FFmpeg rendering pipeline, CapCut workflow
- master: 87
