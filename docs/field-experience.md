---
title: Career & Projects
page: experience
order: 1
colour: violet
kicker: Section 01 · career
summary: Two parts, newest first — Company Experience for the employers on staff, Project Experience for contracts, freelance dispatches and site projects.
placeholder: Search — huawei, zte, bms, center3, zabbix, cctv…
unit_group: companies
unit_card: projects
footer: Each card opens the full record. The arrows at the bottom of a record step through its own section.
title_ar: المسيرة المهنية والمشاريع
title_ur: کیریئر اور پروجیکٹس
summary_ar: قسمان، الأحدث أولاً — الخبرة في الشركات للوظائف الثابتة، وخبرة المشاريع للعقود والمهام المستقلة ومشاريع المواقع.
summary_ur: دو حصے، تازہ ترین پہلے — کمپنی کا تجربہ مستقل ملازمتوں کے لیے، اور پروجیکٹ کا تجربہ کنٹریکٹس، فری لانس اسائنمنٹس اور سائٹ پروجیکٹس کے لیے۔
---

# FIELD EXPERIENCE & PROJECTS

<!--
HOW THIS FILE WORKS

  Order on the page = order in this file. Newest first. Move a `##` block to
  re-sequence; the numbers 01, 02, 03 … are added by the build and restart
  in each section (Company 01–04, Project 01–07).

  ## Name | location | period        one role or engagement, gets its own page
  role:     job title
  type:     Employment · Contract · Freelance · Independent   (sets the colour)
            Employment goes under Company Experience; every other type
            goes under Project Experience.
  section:  company | projects      (optional — overrides the rule above)
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

## center3 Riyadh — Viasat IGW Cabinet Build | Riyadh | Oct 2026
role: Network Engineer
type: Freelance
slug: center3-viasat-igw
summary: Two-engineer build of a Viasat internet-gateway cabinet in a center3 data hall, dispatched through RADX Global Services for ITARMI, client INS Group.
private: Worked 21–22 Oct 2026, resumed 29 Oct, with Rafi Ullah. HRS form approved. Do not publish ticket or permit numbers or the day rate.

### Documentation before install
- Started with no project documents on site
- Requested and assembled the device list, cable schedule, label sheet and labelling guide, front elevation, serial / MAC sheet, site point of contact and delivery location before installing anything
- master: 86, 89

### Cabinet build
- Equipment racked to the front elevation and labelled to the client guide
- Absorbed a late client change: one device moved to rear U45, with new labels and an updated elevation
- master: 13, 86

### Cabling and console
- Caught a connector mismatch on the terminal-server console cables — RJ12, not RJ45, at the PDU end
- Left those runs unterminated pending the correct part instead of forcing a fit
- master: 10, 28, 88

### Site access
- Data-centre access, work permits and approvals handled with center3
- master: 65, 89

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

### Site access
- Part of a four-engineer team
- A missing site-access permit blocked the start on day one; cleared it by contacting center3 and stc directly, so the team could begin work
- master: 65, 89

## ANMAT Operations — Ministry of Tourism Project | Riyadh | Aug – Oct 2026
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

## Leon Technology — GO-ZTE IPCORE Project | Riyadh & Hail | Jun – Aug 2026
role: Data Center Deployment Engineer
type: Contract
slug: leon-go-zte-ipcore
summary: Physical deployment of GO Telecom's IP core across a 63-site rollout — ZTE carrier routing and switching, server staging, fibre and DC power.
private: Physical and staging work, not routing configuration. Be precise about that in interviews.

### Rollout scope
- National 63-site rollout for GO Telecom across Riyadh and Hail
- Hands-on at RIY1 and other Riyadh data-centre sites
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
- MPO/MTP trunks, LC OM4 jumpers, inter-rack runs and ODF termination, to carrier installation standards
- SFP+, SFP28 and QSFP28 optics
- DC power: -48V plant, rectifiers, breakers and PDUs
- master: 10, 11, 14

### Staging and asset control
- Bench testing of ZXR10 switches and R5300 G5 servers before install
- Equipment receipt and iEPMS material scanning
- Installs left ready for the ZTE commissioning teams
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
- Master device inventory and a per-system document library — datasheets, manuals and as-builts
- Reviewed contractor handover documents and closed the gaps
- master: 86

### Snag management
- Filtered a 6,500-item master snag list to around 500 open low-current items, classified by system and activity
- Flagged out-of-scope BMS and fire-system items instead of absorbing them
- master: 85, 89

### Control, AV and cinema
- Crestron and KNX control, Trinnov and Crown cinema audio, LG commercial displays
- Identified the devices that needed configuration backups and set up backup and version-control practice for critical systems
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
- Point-to-point wireless bridge (TP-Link / Huawei) joining both offices into one routed network
- master: 50, 54

### Delivery
- Client scoping and quoting
- Two-site rollout, design through handover
- Full configuration documentation and on-site staff training for day-two operations
- master: 89

## Wemart Arabia Trading Co. (WenChao Group) | Riyadh | Oct 2025 – Apr 2026
role: IT Engineer
type: Employment
slug: wemart
summary: Took ownership of a live, undocumented Huawei enterprise network across a multi-site retail and warehouse estate, and turned it into a documented, monitored environment — 237-camera CCTV, 50+ APs and Zabbix monitoring.
private: Your deepest production environment and the strongest source of interview material.

### Huawei core switching
- CloudEngine S6730 core switch — VLAN design, inter-VLAN routing, uplinks
- eKitEngine access switching and Eth-Trunk link aggregation
- VRP CLI daily operation and config backup discipline
- Built end-to-end visibility of an undocumented network from scratch
- master: 28, 41, 42

### Huawei firewall and VPN
- USG6000E — zones, security policies, NAT
- IPsec site-to-site VPN to the Dubai head office over Zain fibre
- NAT / PAT and firewall policy management
- master: 61, 62, 36

### Huawei wireless
- AirEngine WAC with 50+ access points
- AP provisioning at scale, SSID and security policy
- Stabilised the WLAN by resolving CAPWAP, DHCP Option 43 and controller-uplink issues
- master: 52, 53

### Hikvision CCTV estate
- 237 cameras across 4 NVRs
- PoE budget planning and VLAN segmentation for cameras
- Storage retention calculation and a disk-full recovery incident
- Fibre plus media converter for a long basement run, after a converter failure
- Camera placement corrections after a coverage review
- master: 90, 91, 92, 93, 94

### Production incidents
- Asymmetric routing on the CCTV network, traced and corrected
- DHCP pool exhaustion on a user VLAN
- ARP conflicts on the LAN
- All three resolved with zero service downtime
- master: 32, 43, 88

### Zabbix monitoring
- Huawei VRP SNMP template, host and item configuration
- PoE discovery, configuration-change tracking and device alerts
- Trigger and severity tuning — around 40% less alert noise
- Email alerting, printer and toner monitoring
- Network topology map through the JSON-RPC API
- master: 81, 82

### Windows and endpoints
- Active Directory, Group Policy and file shares
- POS and retail systems — Posiflex terminals, Zebra printers, mada payment terminals
- Backup and endpoint management
- master: 15, 22, 23, 24, 25

### Documentation
- Topology diagrams, IP schema, VLAN maps and runbooks, maintained throughout
- master: 86

## AlmavivA Information Technology | Riyadh | Mar 2024 – Oct 2025
role: Network Engineer
type: Employment
slug: almaviva
summary: Network operations for the Riyadh Metro transport project across stations and depots — Cisco Catalyst core, Extreme EXOS rings, VMware virtualisation, MOXA wireless links and site-to-site VPNs under SLA monitoring.
private: The Riyadh Metro Line 3 (OCC-CTN) Extreme EXOS work was a separate entry until Nov 2026 and is now merged here, because AlmavivA's role was the Riyadh Metro project. If the EXOS work was not under AlmavivA, split it back out.

### Stations and depots
- Network operations across multiple stations and depots of the Riyadh Metro, consistently meeting SLA targets
- master: 80, 89

### Cisco core network
- Cisco Catalyst 4510 core switching
- VLAN segmentation, STP optimisation, EtherChannel and inter-VLAN routing
- master: 40, 41, 42

### Line 3 OCC-CTN — Extreme EXOS
- EXOS CLI, show commands and config management
- EAPS ring protection — master and transit nodes, control VLAN
- MLAG configuration and behaviour
- Stack reconvergence diagnosis
- CRC and input-error investigation — cable, SFP and duplex causes
- Reference PDFs and troubleshooting cheat sheets for the team
- master: 28, 42, 86, 88

### VPN
- Site-to-site and remote-access IPsec VPNs across distributed locations
- master: 62

### Wireless bridge links
- MOXA wireless bridges on field communication links
- RF surveys and VSWR testing
- master: 50, 54

### Virtualisation
- VMware vCenter and ESXi — lifecycle management, live migrations, patching and capacity planning
- Backup and snapshot management
- master: 71

### Site systems
- Deployment and support of IP telephony, wireless networks, CCTV and physical access control
- master: 37, 52, 92, 95

### Operations
- Performance monitoring through the NMS, with KPI and SLA analysis driving root-cause remediation
- ITIL change, incident and problem processes
- Runbooks and configuration backups
- master: 80, 85, 86

## Express Publications (Pvt.) Ltd. | Peshawar | Jan 2023 – Feb 2024
role: System Support Engineer
type: Employment
slug: express-publications
summary: Systems and network support for a media house — 100+ endpoints on Windows Server, with Cisco routing and switching, pfSense and ESXi.

### Infrastructure
- Cisco routing and switching — VLANs, trunking and inter-VLAN routing across a multi-floor office
- pfSense firewall — NAT, VPN tunnels, access-control policy and traffic monitoring
- VMware ESXi — VM provisioning, patching and snapshot-based backups
- master: 40, 61, 71

### Support operations
- Windows Server for 100+ endpoints — Active Directory, DNS, DHCP and Group Policy
- L1 / L2 technical support and system deployments with minimal downtime
- Windows client deployment and troubleshooting
- Printer and peripheral support, user and permission administration
- master: 15, 20, 22, 88

### Backup and endpoint security
- Veeam backup
- Kaspersky Security Center endpoint protection
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
- Link turn-ups, site cutovers and last-mile faults with ISPs and field engineers
- Capacity and performance reports
- Runbooks, configuration backups and change logs
- master: 80, 85, 88

### SMS platform
- SMS platform network and services
- Asterisk telephony
- Node.js services under PM2
- master: 30, 37, 84

### Monitoring and load balancing
- Zabbix server, agents and templates
- Proactive monitoring of interface errors, discards, uptime and device health, with severity-based escalation
- HAProxy with a Roxy-WI front end
- Dell OpenManage for hardware health
- master: 81, 84

### Switching and DHCP
- VLANs, trunking, inter-VLAN routing and DHCP configuration and support
- master: 32, 41

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
- Networking education content on TikTok, Instagram and LinkedIn (formerly @networkingwithmickey)
- 24.5K followers on TikTok and 11.4K on Instagram (Nov 2026)
- Real fibre, SFP and data-centre work, RJ45 pinouts, OSI and CCNA / CCNP prep, made with own field photos
- Playlists: Fiber & SFP, Data Center, Real field work
- Fibre, Ethernet vs fibre, OSI model and CCTV incident reels
- Python/PIL and FFmpeg rendering pipeline, CapCut workflow
- master: 87
