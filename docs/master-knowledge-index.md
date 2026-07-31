---
title: Master Knowledge Index
owner: Ihtiram Ullah — Network & IT Infrastructure Engineer
version: 2.0
generated: 2026-07-30
areas: 10
categories: 77
topics: 741
subtopics: 562
cross_references: 132
scheme: Johnny.Decimal — AREA.CATEGORY.TOPIC.SUBTOPIC
---

# MASTER KNOWLEDGE INDEX

Four levels. One home per concept. Courses are tags, not folders.

```
AREA        40–49   Switching & Routing        folder, colour, fiber strand
CATEGORY    44      OSPF                       the subject
TOPIC       44.04   Area types                 the note you open
SUBTOPIC    44.04.3 Stub — no LSA5             the thing you actually revise
```

## Legend

| Axis | Values |
|---|---|
| **Type** | `C` concept · `X` config · `T` troubleshoot · `R` reference |
| **Level** | `0` heard of it · `1` can explain · `2` studied/labbed · `3` production · `4` own it |
| **Source** | course tags `[CCNA]` etc. · **field tags** `[Wemart]` `[MetroL3]` `[ZTE-RIY1]` `[AlmavivA]` `[Veevo]` `[UCT]` |
| **Refs** | `→ 44.05` means the topic connects there. Links are bidirectional. |

**Claim rule.** Only L3+ belongs on a CV. L1–2 is *familiar with, not in production*.
**Rating rule.** Add a date: `L3 t:07/26`. An unrated skill and a stale rating are different problems.

## Areas at a glance

| Area | Strand | Categories | Topics | Subtopics |
|---|---|---:|---:|---:|
| `00–09` Index, Meta & Exam Tracking | Slate | 4 | 18 | 0 |
| `10–19` Physical Infrastructure | Orange | 6 | 64 | 74 |
| `20–29` Operating Systems | Green | 10 | 104 | 35 |
| `30–39` IP Core & Services | Aqua | 9 | 79 | 54 |
| `40–49` Switching & Routing | Blue | 10 | 125 | 125 |
| `50–59` Wireless | Violet | 5 | 45 | 50 |
| `60–69` Security & Firewall | Red | 6 | 53 | 35 |
| `70–79` Virtualization & Cloud | Rose | 10 | 104 | 84 |
| `80–89` Monitoring, Ops & Automation | Yellow | 10 | 92 | 65 |
| `90–99` CCTV & Physical Security | Bronze | 7 | 57 | 40 |
| | | **77** | **741** | **562** |

## Exam scope map

Which categories carry each tag — use this to bound revision instead of reading everything.

| Tag | Categories |
|---|---|
| `Wemart` <sub>**field**</sub> | `10` `11` `13` `14` `15` `20` `22` `23` `25` `28` `32` `33` `34` `36` `41` `42` `49` `50` `52` `53` `54` `61` `62` `64` `65` `80` `81` `82` `84` `86` `90` `91` `92` `93` `94` `96` |
| `ENCOR` <sub>course</sub> | `28` `30` `31` `35` `36` `40` `41` `42` `43` `44` `45` `46` `47` `48` `49` `50` `51` `52` `53` `54` `60` `61` `62` `63` `82` `83` `87` |
| `CCNA` <sub>course</sub> | `10` `11` `28` `29` `30` `31` `32` `33` `34` `35` `36` `37` `38` `40` `41` `42` `43` `44` `45` `49` `50` `51` `53` `60` `63` `88` |
| `MCSE` <sub>course</sub> | `20` `21` `22` `23` `24` `25` `26` `32` `33` `34` `35` `62` `64` `70` `72` `73` |
| `A+` <sub>course</sub> | `10` `11` `12` `13` `15` `20` `30` `36` `37` `60` `64` `88` |
| `ZTE-RIY1` <sub>**field**</sub> | `10` `11` `12` `13` `14` `28` `46` `48` `73` `84` `86` `89` |
| `AZ104` <sub>course</sub> | `32` `33` `35` `74` `75` `76` `77` `78` `79` |
| `ENARSI` <sub>course</sub> | `43` `44` `45` `46` `47` `48` `49` `62` `63` |
| `CCTV-OP` <sub>course</sub> | `65` `90` `91` `92` `93` `94` `95` `96` |
| `Self` <sub>course</sub> | `27` `29` `37` `53` `61` `72` `87` |
| `Veevo` <sub>**field**</sub> | `27` `61` `80` `81` `82` `83` `84` |
| `MetroL3` <sub>**field**</sub> | `28` `40` `42` `44` `86` `89` |
| `AZ900` <sub>course</sub> | `70` `74` |
| `AlmavivA` <sub>**field**</sub> | `22` `52` |
| `UCT` <sub>**field**</sub> | `23` `89` |
| `VMware` <sub>course</sub> | `70` `71` |
| `CV` <sub>course</sub> | `84` |
| `CV — unverified` <sub>course</sub> | `85` |
| `Field` <sub>**field**</sub> | `88` |
| `YT` <sub>course</sub> | `27` |

---

# 00–09 · INDEX, META & EXAM TRACKING

<sub>Slate strand · 4 categories · 18 topics</sub>

### 00 · System

- **`00.01`** Legend, rules, how to use this index  `R`  `L:_`
- **`00.02`** Change log — structure revisions  `R`  `L:_`

### 01 · Exam & Certification Tracker

- **`01.01`** ENCOR 350-401 — coursework done, exam NOT sat  `R`  `L:_`
- **`01.02`** ENARSI 300-410 — coursework done, exam NOT sat  `R`  `L:_`
- **`01.03`** AZ-800 — RETIRES SEP 2026, urgent  `R`  `L:_`
- **`01.04`** AZ-104 — confirm pass status  `R`  `L:_`
- **`01.05`** AZ-900 — passed  `R`  `L:_`
- **`01.06`** CCNA / A+ / CCTV-OP / MCSE — status per certificate  `R`  `L:_`
- **`01.07`** SCE registration (Saudi Council of Engineers)  `R`  `L:_`
- **`01.08`** Degree attestation chain: HEC → MoFA → Saudi Embassy  `R`  `L:_`

### 02 · Career

- **`02.01`** Roadmap — priority order of remaining certs  `R`  `L:_`
- **`02.02`** Skill gap list (auto-derived: L0–L1 inside target exams)  `R`  `L:_`
- **`02.03`** Interview story bank (source: all L3–L4 entries)  `R`  `L:_`
- **`02.04`** CV claim register — what is defensible, what is not  `R`  `L:_`

### 03 · Labs & Resources

- **`03.01`** EVE-NG topology inventory  `R`  `L:_`
- **`03.02`** Study material index (books, Udemy, YouTube channels)  `R`  `L:_`
- **`03.03`** Vendor doc bookmarks  `R`  `L:_`
- **`03.04`** Glossary & project abbreviations  `R`  `L:_`

---

# 10–19 · PHYSICAL INFRASTRUCTURE

<sub>Orange strand · 6 categories · 64 topics</sub>

### 10 · Copper Cabling  `[A+]` `[CCNA]` `[Wemart]` `[ZTE-RIY1]`

- **`10.01`** Categories Cat5e/6/6a/7/8 — bandwidth & distance  `C`  `L:_`
  - `10.01.1` Cat5e — 1 Gb, 100 MHz
  - `10.01.2` Cat6 — 1 Gb @100m / 10 Gb @55m, 250 MHz
  - `10.01.3` Cat6a — 10 Gb @100m, 500 MHz
  - `10.01.4` Cat7 / Cat8 — shielded, DC-only in practice
  - `10.01.5` Choosing a category: distance × speed × budget
- **`10.02`** T568A vs T568B pinout  `R`  `L:_`
- **`10.03`** Straight-through, crossover, rollover — when each  `C`  `L:_`
- **`10.04`** Making patch cords: crimping, RJ45, boots, pass-through  `X`  `L:_`
  - `10.04.1` Strip length and jacket damage
  - `10.04.2` Untwist limit — 13 mm maximum
  - `10.04.3` Pair order for T568B
  - `10.04.4` Load bar vs pass-through connectors
  - `10.04.5` Crimp force and strain relief
  - `10.04.6` Verify before you leave the ladder
- **`10.05`** Punch-down: keystone, patch panel, 110 block, krone tool  `X`  `L:_`
  - `10.05.1` Keystone jack termination
  - `10.05.2` Patch panel loading and port numbering
  - `10.05.3` 110 block vs krone block
  - `10.05.4` Punch tool blade orientation
  - `10.05.5` Labelling both ends at termination time
- **`10.06`** Cable testing: continuity, wiremap, TDR  `X`  `L:_`
  - `10.06.1` Continuity — is a wire connected
  - `10.06.2` Wiremap — is it connected correctly
  - `10.06.3` Length via TDR
  - `10.06.4` Certification: NEXT, return loss, delay skew
  - `10.06.5` Reading a failed cert report
- **`10.07`** Certification vs verification testing  `C`  `L:_`
- **`10.08`** 100m rule, attenuation, NEXT/FEXT, EMI  `C`  `L:_`
- **`10.09`** Shielding: UTP, STP, FTP, S/FTP — when needed  `C`  `L:_`
- **`10.10`** Cable management, bend radius, labelling standards  `R`  `L:_`
- **`10.11`** PoE 802.3af / at / bt — power classes & budget  `C`  `L:_`  →  `52.07`, `92.02`
  - `10.11.1` 802.3af — 15.4 W at source, 12.95 W at device
  - `10.11.2` 802.3at — 30 W, PoE+
  - `10.11.3` 802.3bt Type 3 / Type 4 — 60 W / 100 W
  - `10.11.4` Power class negotiation (LLDP)
  - `10.11.5` Switch power budget vs sum of ports
  - `10.11.6` Voltage drop over distance
- **`10.12`** PoE injectors, midspan, endspan  `X`  `L:_`
- **`10.13`** Structured cabling standards TIA/EIA-568  `R`  `L:_`
- **`10.14`** Common faults: bad crimp, split pair, short, open  `T`  `L:_`
  - `10.14.1` Bad crimp — intermittent, worst under movement
  - `10.14.2` Split pair — passes continuity, fails NEXT
  - `10.14.3` Short and open — wiremap catches it
  - `10.14.4` Exceeding 100 m — works then doesn't
  - `10.14.5` EMI from parallel power runs

### 11 · Fiber Optics  `[A+]` `[CCNA]` `[Wemart]` `[ZTE-RIY1]`

- **`11.01`** Single-mode vs multi-mode — OS1/OS2, OM1–OM5  `C`  `L:_`
  - `11.01.1` Single-mode 9/125 — OS1 indoor, OS2 outdoor
  - `11.01.2` Multi-mode 50/125 — OM2/3/4/5
  - `11.01.3` Multi-mode 62.5/125 — OM1, legacy orange
  - `11.01.4` Distance vs cost trade-off
  - `11.01.5` Never mix SMF and MMF on one link
- **`11.02`** Core/cladding diameters, refractive index  `C`  `L:_`
- **`11.03`** Connectors: LC, SC, ST, FC, MPO/MTP  `R`  `L:_`
  - `11.03.1` LC — small form factor, duplex clip
  - `11.03.2` SC — push-pull square
  - `11.03.3` ST — bayonet twist, legacy
  - `11.03.4` FC — threaded, vibration-resistant
  - `11.03.5` MPO/MTP — 12/24 fibre ribbon, polarity types A/B/C
- **`11.04`** Polish types: PC, UPC, APC  `C`  `L:_`
- **`11.05`** Transceivers: SFP, SFP+, SFP28, QSFP+, QSFP28  `R`  `L:_`
  - `11.05.1` SFP — 1 Gb
  - `11.05.2` SFP+ — 10 Gb
  - `11.05.3` SFP28 — 25 Gb
  - `11.05.4` QSFP+ / QSFP28 — 40 Gb / 100 Gb
  - `11.05.5` Coding and vendor lock
  - `11.05.6` Reading DDM/DOM optical levels
- **`11.06`** DAC and AOC cables  `C`  `L:_`
- **`11.07`** Wavelengths 850 / 1310 / 1550 nm  `R`  `L:_`
- **`11.08`** Patch cords, pigtails, ODF/FDF, splice trays  `X`  `L:_`
- **`11.09`** Fusion splicing vs mechanical splicing  `X`  `L:_`
- **`11.10`** Power meter & light source testing  `X`  `L:_`  →  `11.11`
  - `11.10.1` Reference method — set your zero
  - `11.10.2` Measuring in both directions
  - `11.10.3` dBm vs dB — absolute vs relative
  - `11.10.4` Recording results against the budget
- **`11.11`** dB loss budget calculation  `R`  `L:_`  →  `11.10`
  - `11.11.1` Connector loss ≈ 0.75 dB each
  - `11.11.2` Splice loss ≈ 0.3 dB each
  - `11.11.3` Fibre attenuation per km by wavelength
  - `11.11.4` Adding margin for future repairs
  - `11.11.5` Worked example: campus SMF run
- **`11.12`** OTDR — reading traces, events, reflections  `T`  `L:_`
  - `11.12.1` Launch cable — why the first event is hidden
  - `11.12.2` Reflective vs non-reflective events
  - `11.12.3` Reading a break location
  - `11.12.4` Ghost reflections
  - `11.12.5` Bi-directional averaging
- **`11.13`** Cleaning & inspection, contamination faults  `T`  `L:_`
- **`11.14`** Media converters — copper↔fiber  `X`  `L:_`  →  `92.05`
- **`11.15`** BiDi optics, CWDM / DWDM basics  `C`  `L:_`
- **`11.16`** Cross-connect planning, MDF/ODF documentation  `X`  `L:_`

### 12 · Compute Hardware  `[A+]` `[ZTE-RIY1]`

- **`12.01`** CPU: sockets, cores/threads, cache, clock, architecture  `C`  `L:_`
- **`12.02`** RAM: DDR3/4/5, ECC vs non-ECC, registered/buffered  `C`  `L:_`
- **`12.03`** Memory channels, DIMM population rules  `R`  `L:_`
- **`12.04`** Storage media: HDD, SSD, NVMe — SAS vs SATA  `C`  `L:_`
- **`12.05`** RAID 0 / 1 / 5 / 6 / 10 — capacity & fault tolerance  `C`  `L:_`  →  `24.14`, `73.08`
  - `12.05.1` RAID 0 — stripe, no redundancy
  - `12.05.2` RAID 1 — mirror, 50% usable
  - `12.05.3` RAID 5 — single parity, one disk fault
  - `12.05.4` RAID 6 — dual parity, two disk faults
  - `12.05.5` RAID 10 — mirror + stripe, best rebuild
  - `12.05.6` Usable capacity formulas
  - `12.05.7` Rebuild window is when arrays die
- **`12.06`** Hardware vs software RAID, hot spare, rebuild  `C`  `L:_`
- **`12.07`** Motherboards, chipsets, PCIe lanes & generations  `C`  `L:_`
- **`12.08`** PSU sizing, redundant supplies, efficiency ratings  `C`  `L:_`
- **`12.09`** BIOS / UEFI, boot order, secure boot, POST codes  `X`  `L:_`
  - `12.09.1` POST sequence and error codes
  - `12.09.2` Boot order and boot mode UEFI vs Legacy
  - `12.09.3` Secure Boot implications
  - `12.09.4` RAID controller configuration at boot
  - `12.09.5` Firmware/BIOS update discipline
- **`12.10`** Server form factors: rack U, blade, tower; rail kits  `C`  `L:_`
- **`12.11`** Out-of-band mgmt: iDRAC / iLO / BMC  `X`  `L:_`
- **`12.12`** Thermal & airflow, hot/cold aisle  `C`  `L:_`
- **`12.13`** Hardware fault diagnosis — POST, beep, LED, logs  `T`  `L:_`

### 13 · Racks & Data Centre  `[ZTE-RIY1]` `[Wemart]` `[A+]`

- **`13.01`** Rack units, depth, cabinet types, cage nuts  `R`  `L:_`
- **`13.02`** Rack elevation drawing & layout planning  `X`  `L:_`
- **`13.03`** Cable routing, vertical/horizontal managers  `X`  `L:_`
- **`13.04`** Grounding & bonding  `C`  `L:_`
- **`13.05`** Environmental monitoring: temp, humidity  `C`  `L:_`
- **`13.06`** Physical rack build & equipment mounting  `X`  `L:_`

### 14 · Power & UPS  `[ZTE-RIY1]` `[Wemart]`

- **`14.01`** Single-phase vs three-phase, PDU types  `C`  `L:_`
- **`14.02`** UPS topologies: offline, line-interactive, online  `C`  `L:_`
- **`14.03`** Battery sizing & runtime calculation  `R`  `L:_`
- **`14.04`** DC power plants (-48V), rectifiers, breakers  `X`  `L:_`
- **`14.05`** Dual-feed / A+B power design  `C`  `L:_`
- **`14.06`** Generator & ATS basics  `C`  `L:_`
- **`14.07`** Earthing requirements  `C`  `L:_`

### 15 · Peripherals & Endpoints  `[A+]` `[Wemart]`

- **`15.01`** Printers: laser, inkjet, thermal — mechanics  `C`  `L:_`
- **`15.02`** Network printing, drivers, print server  `X`  `L:_`
- **`15.03`** Consumables: toner, drum, fuser — lifecycle  `R`  `L:_`
- **`15.04`** Printer troubleshooting  `T`  `L:_`
- **`15.05`** POS terminals (Posiflex XT-8315, RT-6016, EK-1610)  `X`  `L:_`
- **`15.06`** Monitors, KVM switches  `C`  `L:_`
- **`15.07`** Laptop components & servicing  `X`  `L:_`
- **`15.08`** Mobile device basics  `C`  `L:_`

---

# 20–29 · OPERATING SYSTEMS

<sub>Green strand · 10 categories · 104 topics</sub>

### 20 · Windows Client  `[A+]` `[MCSE]` `[Wemart]`

- **`20.01`** Installation, imaging, deployment  `X`  `L:_`
- **`20.02`** Activation & licensing  `C`  `L:_`
- **`20.03`** User profiles: local, roaming, mandatory  `C`  `L:_`
- **`20.04`** Registry structure & editing  `X`  `L:_`
- **`20.05`** Boot process, safe mode, recovery environment  `T`  `L:_`
- **`20.06`** Event logs & basic diagnostics  `T`  `L:_`
- **`20.07`** Common desktop faults  `T`  `L:_`

### 21 · Windows Server — Core  `[MCSE]`

- **`21.01`** Editions Standard vs Datacenter, licensing, CALs  `C`  `L:_`
- **`21.02`** Server Core vs Desktop Experience  `C`  `L:_`
- **`21.03`** Installation & post-install configuration  `X`  `L:_`
- **`21.04`** Roles & features, Server Manager  `X`  `L:_`
- **`21.05`** Windows Admin Center  `X`  `L:_`
- **`21.06`** Server hardening baseline  `X`  `L:_`
- **`21.07`** Upgrade & migration paths  `C`  `L:_`
- **`21.08`** Windows Server 2025 — what's new  `C`  `L:_`

### 22 · Active Directory Domain Services  `[MCSE]` `[Wemart]` `[AlmavivA]`

- **`22.01`** Forest / tree / domain / OU — design logic  `C`  `L:_`
  - `22.01.1` Forest — security boundary
  - `22.01.2` Domain — replication and policy boundary
  - `22.01.3` Tree — contiguous namespace
  - `22.01.4` OU — delegation and GPO boundary
  - `22.01.5` When to add a domain vs an OU (usually an OU)
- **`22.02`** Schema & Global Catalog  `C`  `L:_`
- **`22.03`** FSMO roles ×5 — placement, transfer, seize  `C`  `L:_`  →  `22.14`, `34.04`
  - `22.03.1` Schema Master — forest-wide
  - `22.03.2` Domain Naming Master — forest-wide
  - `22.03.3` RID Master — domain
  - `22.03.4` PDC Emulator — domain, time source, lockout
  - `22.03.5` Infrastructure Master — domain
  - `22.03.6` Transfer (graceful) vs seize (DC is gone)
- **`22.04`** Sites & Services, replication topology  `C`  `L:_`
- **`22.05`** Trusts: types, direction, transitivity  `C`  `L:_`
- **`22.06`** Read-Only Domain Controller  `C`  `L:_`
- **`22.07`** DC promotion / demotion, adprep  `X`  `L:_`
- **`22.08`** Users, computers, contacts  `X`  `L:_`
- **`22.09`** Group scope (DL/G/U) and type (security/distribution)  `C`  `L:_`
  - `22.09.1` Domain Local — grant permission here
  - `22.09.2` Global — collect users from this domain
  - `22.09.3` Universal — span domains, lives in GC
  - `22.09.4` Security vs Distribution type
  - `22.09.5` AGDLP: Account → Global → Domain Local → Permission
- **`22.10`** AGDLP nesting strategy  `C`  `L:_`
- **`22.11`** Service accounts, gMSA  `X`  `L:_`
- **`22.12`** Delegation of control  `X`  `L:_`
- **`22.13`** AD backup, authoritative restore, tombstone  `X`  `L:_`
- **`22.14`** Replication troubleshooting (repadmin, dcdiag)  `T`  `L:_`  →  `22.03`
  - `22.14.1` repadmin /replsummary — first command
  - `22.14.2` dcdiag /v — health sweep
  - `22.14.3` USN rollback symptoms
  - `22.14.4` Lingering objects
  - `22.14.5` DNS is usually the actual cause
- **`22.15`** Domain build from scratch (uct.local reference)  `X`  `L:_`

### 23 · Group Policy  `[MCSE]` `[Wemart]` `[UCT]`

- **`23.01`** GPO structure: computer vs user configuration  `C`  `L:_`
- **`23.02`** LSDOU processing order  `C`  `L:_`  →  `23.03`
  - `23.02.1` Local policy first
  - `23.02.2` Site
  - `23.02.3` Domain
  - `23.02.4` OU — parent then child
  - `23.02.5` Last writer wins on conflict
- **`23.03`** Inheritance, block inheritance, enforced  `C`  `L:_`  →  `23.02`
  - `23.03.1` Inheritance is the default
  - `23.03.2` Block Inheritance on the OU
  - `23.03.3` Enforced on the GPO link beats Block
  - `23.03.4` Enforced + Block interaction table
- **`23.04`** Security filtering  `X`  `L:_`
- **`23.05`** WMI filtering  `X`  `L:_`
- **`23.06`** Loopback processing  `C`  `L:_`
- **`23.07`** Group Policy Preferences  `X`  `L:_`
- **`23.08`** ADMX/ADML central store  `X`  `L:_`
- **`23.09`** Drive mapping & folder redirection  `X`  `L:_`
- **`23.10`** USB / removable storage block  `X`  `L:_`
- **`23.11`** Software restriction & AppLocker  `X`  `L:_`
- **`23.12`** Password & account lockout policy  `X`  `L:_`
- **`23.13`** gpupdate, gpresult, RSoP troubleshooting  `T`  `L:_`
  - `23.13.1` gpupdate /force
  - `23.13.2` gpresult /r and /h report
  - `23.13.3` RSoP planning vs logging mode
  - `23.13.4` Event log: Group Policy operational
  - `23.13.5` Slow link detection and why a policy silently skipped

### 24 · Windows Roles & Services  `[MCSE]`

- **`24.01`** File shares, SMB  `X`  `L:_`
- **`24.02`** NTFS vs share permissions — effective permissions  `C`  `L:_`
- **`24.03`** Access-Based Enumeration  `X`  `L:_`
- **`24.04`** DFS Namespaces  `X`  `L:_`
- **`24.05`** DFS Replication  `X`  `L:_`
- **`24.06`** Shadow Copies / Previous Versions  `X`  `L:_`
- **`24.07`** FSRM: quotas, file screening, reports  `X`  `L:_`
- **`24.08`** Print Services role  `X`  `L:_`
- **`24.09`** AD CS: CA hierarchy, templates, enrollment, CRL  `X`  `L:_`
- **`24.10`** WSUS — patch management  `X`  `L:_`
- **`24.11`** NPS / RADIUS  `X`  `L:_`  →  `35.03`
- **`24.12`** RRAS & VPN: L2TP, SSTP, IKEv2  `X`  `L:_`
- **`24.13`** IIS basics  `X`  `L:_`
- **`24.14`** Storage Spaces / Storage Spaces Direct  `X`  `L:_`  →  `12.05`
- **`24.15`** iSCSI target & initiator  `X`  `L:_`
- **`24.16`** Data deduplication  `X`  `L:_`
- **`24.17`** NIC teaming  `X`  `L:_`
- **`24.18`** IPAM  `X`  `L:_`

### 25 · Windows Backup & Monitoring  `[MCSE]` `[Wemart]`

- **`25.01`** Windows Server Backup, system state, BMR  `X`  `L:_`
- **`25.02`** Acronis backup  `X`  `L:_`
- **`25.03`** 3-2-1 backup strategy  `C`  `L:_`  →  `76.05`
- **`25.04`** Restore testing & RTO/RPO  `C`  `L:_`
- **`25.05`** Event Viewer, custom views, log forwarding  `T`  `L:_`
- **`25.06`** Performance Monitor & counters  `T`  `L:_`
- **`25.07`** Resource Monitor, Reliability Monitor  `T`  `L:_`
- **`25.08`** Task Scheduler  `X`  `L:_`

### 26 · PowerShell  `[MCSE]`

- **`26.01`** Cmdlets, verb-noun, pipeline, objects  `C`  `L:_`
- **`26.02`** Execution policy  `C`  `L:_`
- **`26.03`** Variables, loops, conditionals, functions  `X`  `L:_`
- **`26.04`** Remoting (WinRM), PSSession, Invoke-Command  `X`  `L:_`
- **`26.05`** AD module cmdlets — bulk user operations  `X`  `L:_`
- **`26.06`** Modules & script signing  `C`  `L:_`

### 27 · Linux  `[Veevo]` `[Self]` `[YT]`

- **`27.01`** Distributions & filesystem hierarchy  `C`  `L:_`
- **`27.02`** Package management: apt, yum, dnf  `X`  `L:_`
- **`27.03`** Users, groups, permissions, sudo, chmod/chown  `X`  `L:_`
- **`27.04`** systemd, systemctl, service management  `X`  `L:_`
- **`27.05`** journalctl and /var/log  `T`  `L:_`
- **`27.06`** Networking: ip, netplan, routes, resolv.conf  `X`  `L:_`
- **`27.07`** Firewall: iptables, firewalld, ufw  `X`  `L:_`
- **`27.08`** SSH, key-based authentication, hardening  `X`  `L:_`
- **`27.09`** cron & scheduled tasks  `X`  `L:_`
- **`27.10`** Disk management, LVM, mount, fstab  `X`  `L:_`
- **`27.11`** Process management: ps, top, htop, kill  `T`  `L:_`
- **`27.12`** Text editors: vi, nano  `X`  `L:_`
- **`27.13`** Ubuntu Server install & baseline (Roxy-WI build)  `X`  `L:_`

### 28 · Network Device CLI  `[CCNA]` `[ENCOR]` `[Wemart]` `[MetroL3]` `[ZTE-RIY1]`

- **`28.01`** Cisco IOS: modes, config hierarchy, context help  `X`  `L:_`
- **`28.02`** IOS show & debug commands  `T`  `L:_`
- **`28.03`** IOS file system, image upgrade  `X`  `L:_`
- **`28.04`** Config register, password recovery  `T`  `L:_`
- **`28.05`** Huawei VRP: system-view, display, save, quit  `X`  `L:_`  →  `81.07`
- **`28.06`** VRP ↔ IOS command translation table  `R`  `L:_`
- **`28.07`** Extreme EXOS CLI structure & show commands  `X`  `L:_`
- **`28.08`** ZTE ZXROS basics  `X`  `L:_`
- **`28.09`** MikroTik RouterOS basics  `X`  `L:_`
- **`28.10`** Console, AUX, out-of-band access, terminal settings  `X`  `L:_`
- **`28.11`** Config backup/restore — TFTP, FTP, SCP  `X`  `L:_`
- **`28.12`** Device licensing & activation  `C`  `L:_`

### 29 · Lab Environments  `[Self]` `[CCNA]`

- **`29.01`** EVE-NG: install, image import, topology build  `X`  `L:_`
- **`29.02`** GNS3  `X`  `L:_`
- **`29.03`** Packet Tracer  `X`  `L:_`
- **`29.04`** Lab design for exam practice  `C`  `L:_`

---

# 30–39 · IP CORE & SERVICES

<sub>Aqua strand · 9 categories · 79 topics</sub>

### 30 · IP Addressing & Subnetting  `[CCNA]` `[A+]` `[ENCOR]`

- **`30.01`** Binary ↔ decimal conversion  `C`  `L:_`
- **`30.02`** IPv4 classes A–E  `C`  `L:_`
- **`30.03`** RFC1918 private ranges, APIPA, loopback, multicast  `R`  `L:_`
- **`30.04`** Subnet mask & prefix length, CIDR notation  `C`  `L:_`
- **`30.05`** Subnetting — host/network calculation  `C`  `L:_`  →  `30.06`, `32.02`
  - `30.05.1` Powers of two — memorise to 2^10
  - `30.05.2` Hosts = 2^n − 2 and why minus two
  - `30.05.3` Block size / magic number method
  - `30.05.4` Finding the network and broadcast address
  - `30.05.5` Speed drill: /26 /27 /28 /29 /30
- **`30.06`** VLSM  `C`  `L:_`  →  `30.05`
  - `30.06.1` Summarise contiguous blocks only
  - `30.06.2` Finding the common prefix in binary
  - `30.06.3` Over-summarisation risk
  - `30.06.4` Summarising at the right boundary
- **`30.07`** Route summarization / supernetting  `C`  `L:_`
- **`30.08`** Subnet cheat table  `R`  `L:_`
- **`30.09`** IP scheme design for a site  `X`  `L:_`

### 31 · IPv6  `[CCNA]` `[ENCOR]`

- **`31.01`** Address format & abbreviation rules  `C`  `L:_`
- **`31.02`** Address types: GUA, LLA, ULA, multicast, anycast  `C`  `L:_`
- **`31.03`** EUI-64 formation  `C`  `L:_`
- **`31.04`** SLAAC & Router Advertisement  `C`  `L:_`
- **`31.05`** DHCPv6 stateful vs stateless  `C`  `L:_`
- **`31.06`** NDP & ICMPv6  `C`  `L:_`
- **`31.07`** Dual-stack, tunneling, NAT64  `C`  `L:_`
- **`31.08`** IPv6 static & dynamic routing  `X`  `L:_`
- **`31.09`** IPv6 first-hop security (RA Guard, DHCPv6 Guard)  `X`  `L:_`

### 32 · DHCP  `[CCNA]` `[MCSE]` `[Wemart]` `[AZ104]`

- **`32.01`** DORA process  `C`  `L:_`
  - `32.01.1` Discover — broadcast from client
  - `32.01.2` Offer — server proposes
  - `32.01.3` Request — client accepts publicly
  - `32.01.4` Acknowledge — lease committed
  - `32.01.5` Renew at T1 (50%), rebind at T2 (87.5%)
- **`32.02`** Scopes, ranges, exclusions, reservations  `X`  `L:_`  →  `30.05`
- **`32.03`** Options 3, 6, 43, 66/67, 150  `R`  `L:_`
  - `32.03.1` Option 3 — default gateway
  - `32.03.2` Option 6 — DNS servers
  - `32.03.3` Option 43 — vendor specific (AP/WLC discovery)
  - `32.03.4` Option 66/67 — TFTP server and boot file
  - `32.03.5` Option 150 — TFTP for Cisco phones
- **`32.04`** Lease duration strategy  `C`  `L:_`
- **`32.05`** DHCP relay / ip helper-address  `X`  `L:_`  →  `43.04`
- **`32.06`** Windows DHCP failover & split scope  `X`  `L:_`
- **`32.07`** Huawei interface-based & pool-based DHCP  `X`  `L:_`
- **`32.08`** DHCP snooping  `X`  `L:_`
- **`32.09`** Troubleshooting: rogue DHCP, exhaustion, no offer  `T`  `L:_`  →  `63.06`
  - `32.09.1` No address at all — relay or VLAN fault
  - `32.09.2` Wrong subnet — rogue server
  - `32.09.3` APIPA 169.254 — nothing answered
  - `32.09.4` Scope exhaustion — lease time too long
  - `32.09.5` Duplicate address — reservation vs static overlap

### 33 · DNS  `[CCNA]` `[MCSE]` `[Wemart]` `[AZ104]`

- **`33.01`** Namespace hierarchy, FQDN, root & TLD  `C`  `L:_`
- **`33.02`** Record types: A, AAAA, CNAME, MX, PTR, NS, SOA, SRV, TXT  `R`  `L:_`
  - `33.02.1` A / AAAA — name to address
  - `33.02.2` CNAME — alias, never at zone apex
  - `33.02.3` PTR — reverse, lives in in-addr.arpa
  - `33.02.4` MX — mail, with priority
  - `33.02.5` NS / SOA — delegation and zone authority
  - `33.02.6` SRV — service location, used heavily by AD
  - `33.02.7` TXT — SPF, DKIM, verification
- **`33.03`** Forward & reverse lookup zones  `X`  `L:_`
- **`33.04`** Zone types: primary, secondary, stub, AD-integrated  `C`  `L:_`
  - `33.04.1` Primary — read/write master copy
  - `33.04.2` Secondary — read-only zone transfer
  - `33.04.3` Stub — NS records only
  - `33.04.4` AD-integrated — multi-master, replicates with AD
  - `33.04.5` Choosing zone type per role
- **`33.05`** Forwarders, conditional forwarders, root hints  `X`  `L:_`
- **`33.06`** Recursion vs iteration, caching, TTL  `C`  `L:_`
- **`33.07`** Dynamic DNS, aging & scavenging  `X`  `L:_`
- **`33.08`** DNSSEC basics  `C`  `L:_`
- **`33.09`** Split-brain / split-horizon DNS  `C`  `L:_`
- **`33.10`** Azure DNS & Private DNS zones  `X`  `L:_`  →  `78.13`
- **`33.11`** Troubleshooting: nslookup, dig, flushdns  `T`  `L:_`
  - `33.11.1` nslookup basics and setting the server
  - `33.11.2` dig +trace to follow delegation
  - `33.11.3` ipconfig /flushdns and /displaydns
  - `33.11.4` Testing authoritative vs cached answer
  - `33.11.5` Symptom: works by IP, fails by name

### 34 · NTP & Time  `[CCNA]` `[MCSE]` `[Wemart]`

- **`34.01`** Stratum hierarchy  `C`  `L:_`
- **`34.02`** Client, server, peer, broadcast modes  `X`  `L:_`
- **`34.03`** NTP authentication  `X`  `L:_`
- **`34.04`** Why time matters: Kerberos, certs, logs, CCTV evidence  `C`  `L:_`  →  `22.03`, `83.02`, `92.08`, `96.01`
- **`34.05`** Time drift troubleshooting  `T`  `L:_`

### 35 · AAA & Identity  `[CCNA]` `[ENCOR]` `[MCSE]` `[AZ104]`

- **`35.01`** Authentication vs authorization vs accounting  `C`  `L:_`
- **`35.02`** RADIUS vs TACACS+ — differences & use cases  `C`  `L:_`
- **`35.03`** 802.1X: supplicant, authenticator, auth server  `C`  `L:_`  →  `24.11`, `53.02`, `63.11`
- **`35.04`** EAP methods: PEAP, EAP-TLS, EAP-FAST  `C`  `L:_`
- **`35.05`** Local user database & privilege levels  `X`  `L:_`
- **`35.06`** Kerberos fundamentals  `C`  `L:_`
- **`35.07`** LDAP & LDAPS  `C`  `L:_`
- **`35.08`** MFA concepts  `C`  `L:_`

### 36 · NAT  `[CCNA]` `[ENCOR]` `[Wemart]` `[A+]`

- **`36.01`** Static NAT  `X`  `L:_`  →  `61.04`
- **`36.02`** Dynamic NAT with pools  `X`  `L:_`
- **`36.03`** PAT / overload  `X`  `L:_`  →  `61.04`
- **`36.04`** Inside/outside local & global terminology  `C`  `L:_`
- **`36.05`** Port forwarding  `X`  `L:_`  →  `53.05`
- **`36.06`** NAT on Huawei USG / pfSense / MikroTik  `X`  `L:_`  →  `61.04`, `78.02`
- **`36.07`** Hairpinning / NAT loopback  `T`  `L:_`
- **`36.08`** CGNAT concept  `C`  `L:_`
- **`36.09`** NAT troubleshooting  `T`  `L:_`

### 37 · Application Protocols & Ports  `[CCNA]` `[A+]` `[Self]`

- **`37.01`** Well-known port number table  `R`  `L:_`
- **`37.02`** HTTP / HTTPS, TLS handshake basics  `C`  `L:_`
- **`37.03`** FTP, SFTP, TFTP  `C`  `L:_`
- **`37.04`** SMTP, POP3, IMAP  `C`  `L:_`
- **`37.05`** SNMP v1 / v2c / v3  `C`  `L:_`  →  `82.01`
- **`37.06`** Syslog facilities & severities  `R`  `L:_`
- **`37.07`** Telnet vs SSH  `C`  `L:_`
- **`37.08`** SMB/CIFS, NFS  `C`  `L:_`
- **`37.09`** RDP, VNC  `C`  `L:_`
- **`37.10`** VoIP: SIP, RTP — Asterisk exposure  `C`  `L:_`

### 38 · OSI, TCP/IP & Transport  `[CCNA]`

- **`38.01`** OSI 7 layers & PDUs  `C`  `L:_`  →  `88.02`
  - `38.01.1` L1 Physical — bits, cable, optics
  - `38.01.2` L2 Data Link — frames, MAC, switching
  - `38.01.3` L3 Network — packets, IP, routing
  - `38.01.4` L4 Transport — segments, TCP/UDP, ports
  - `38.01.5` L5 Session
  - `38.01.6` L6 Presentation — encoding, encryption
  - `38.01.7` L7 Application
  - `38.01.8` Using layers as a fault-isolation ladder
- **`38.02`** Encapsulation / de-encapsulation  `C`  `L:_`
- **`38.03`** TCP/IP model mapping  `C`  `L:_`
- **`38.04`** TCP: 3-way handshake, seq/ack, flags, windowing  `C`  `L:_`
  - `38.04.1` SYN → SYN-ACK → ACK
  - `38.04.2` Sequence and acknowledgement numbers
  - `38.04.3` Window size and flow control
  - `38.04.4` FIN and RST teardown
  - `38.04.5` Reading a handshake in Wireshark
- **`38.05`** UDP characteristics & use cases  `C`  `L:_`
- **`38.06`** MTU, fragmentation, MSS, PMTUD  `C`  `L:_`
- **`38.07`** ARP, gratuitous ARP, proxy ARP  `C`  `L:_`
- **`38.08`** ICMP types & codes  `R`  `L:_`
- **`38.09`** Ethernet frame format  `R`  `L:_`

---

# 40–49 · SWITCHING & ROUTING

<sub>Blue strand · 10 categories · 125 topics</sub>

### 40 · Switching Fundamentals & Design  `[CCNA]` `[ENCOR]` `[MetroL3]`

- **`40.01`** MAC table: learning, flooding, forwarding, aging  `C`  `L:_`
- **`40.02`** Collision vs broadcast domains  `C`  `L:_`
- **`40.03`** Speed & duplex, auto-negotiation  `C`  `L:_`
- **`40.04`** Duplex mismatch symptoms  `T`  `L:_`
- **`40.05`** Store-and-forward vs cut-through  `C`  `L:_`
- **`40.06`** CAM table overflow, MAC flapping  `T`  `L:_`
- **`40.07`** CRC & input errors — cable, SFP, duplex causes  `T`  `L:_`
- **`40.08`** Hierarchical design: access / distribution / core  `C`  `L:_`
- **`40.09`** Collapsed core vs 3-tier  `C`  `L:_`
- **`40.10`** Spine-leaf architecture  `C`  `L:_`
- **`40.11`** Oversubscription & uplink sizing  `C`  `L:_`

### 41 · VLANs & Trunking  `[CCNA]` `[ENCOR]` `[Wemart]`

- **`41.01`** VLAN concept & benefits  `C`  `L:_`
- **`41.02`** Access, trunk, hybrid ports  `C`  `L:_`
- **`41.03`** 802.1Q tagging & frame format  `C`  `L:_`  →  `42.01`, `72.03`
  - `41.03.1` 4-byte tag inserted after source MAC
  - `41.03.2` TPID 0x8100 and the 12-bit VLAN ID
  - `41.03.3` Priority bits (PCP) carry CoS
  - `41.03.4` Untagged frames on the native VLAN
  - `41.03.5` Why the frame FCS is recalculated
- **`41.04`** Native VLAN & mismatch risk  `C`  `L:_`
- **`41.05`** VLAN ranges: normal vs extended  `R`  `L:_`
- **`41.06`** Voice VLAN  `X`  `L:_`
- **`41.07`** VTP modes & pruning  `C`  `L:_`
- **`41.08`** Inter-VLAN routing: router-on-a-stick  `X`  `L:_`
  - `41.08.1` Sub-interfaces with encapsulation dot1Q
  - `41.08.2` One physical link, many logical
  - `41.08.3` Bandwidth is shared — the bottleneck
  - `41.08.4` When SVI is the better answer
- **`41.09`** Inter-VLAN routing: SVI & routed ports  `X`  `L:_`
- **`41.10`** Huawei port link-type & PVID  `X`  `L:_`
- **`41.11`** Private VLANs  `C`  `L:_`
- **`41.12`** VLAN troubleshooting  `T`  `L:_`
  - `41.12.1` VLAN missing from the trunk allowed list
  - `41.12.2` Native VLAN mismatch
  - `41.12.3` Port in the wrong access VLAN
  - `41.12.4` VLAN not created on the transit switch
  - `41.12.5` show interface trunk is the first command

### 42 · STP, Aggregation & L2 Redundancy  `[CCNA]` `[ENCOR]` `[MetroL3]` `[Wemart]`

- **`42.01`** STP 802.1D: BPDU, root election, port states  `C`  `L:_`  →  `41.03`
  - `42.01.1` Lowest bridge ID wins root
  - `42.01.2` Root path cost decides root port
  - `42.01.3` Designated port per segment
  - `42.01.4` Blocking / Listening / Learning / Forwarding
  - `42.01.5` Bridge ID = priority + extended sys-id + MAC
- **`42.02`** STP timers & convergence  `C`  `L:_`
- **`42.03`** RSTP 802.1w  `C`  `L:_`  →  `42.15`
- **`42.04`** MSTP 802.1s  `C`  `L:_`
- **`42.05`** PVST+ / Rapid PVST+  `C`  `L:_`
- **`42.06`** PortFast, BPDU Guard, BPDU Filter  `X`  `L:_`
  - `42.06.1` PortFast — skip listening/learning on access ports
  - `42.06.2` BPDU Guard — err-disable if a BPDU arrives
  - `42.06.3` BPDU Filter — stop sending, use with care
  - `42.06.4` Why PortFast on a trunk causes loops
- **`42.07`** Root Guard, Loop Guard, UDLD  `X`  `L:_`
- **`42.08`** Broadcast storms & L2 loop diagnosis  `T`  `L:_`
- **`42.09`** EtherChannel: LACP, PAgP, static  `X`  `L:_`  →  `42.11`, `42.14`
  - `42.09.1` LACP — 802.3ad, active/passive, standard
  - `42.09.2` PAgP — Cisco, desirable/auto
  - `42.09.3` Static on — no negotiation, mismatch risk
  - `42.09.4` Matching speed, duplex, VLAN, mode both ends
  - `42.09.5` Load balance is per-flow, not per-packet
- **`42.10`** EtherChannel load-balancing methods  `C`  `L:_`
- **`42.11`** Huawei Eth-Trunk  `X`  `L:_`  →  `42.09`
- **`42.12`** Stacking: StackWise / iStack / CSS  `C`  `L:_`
- **`42.13`** Stack reconvergence behaviour & faults  `T`  `L:_`  →  `42.15`
- **`42.14`** MLAG — Extreme & ZTE implementations  `X`  `L:_`  →  `42.09`
- **`42.15`** EAPS ring protection (Extreme)  `X`  `L:_`  →  `42.03`, `42.13`
  - `42.15.1` Master and transit nodes
  - `42.15.2` Primary and secondary ports
  - `42.15.3` Control VLAN vs protected VLAN
  - `42.15.4` Ring fault detection and reconvergence
  - `42.15.5` Shared ports for multi-ring — where it gets hard
- **`42.16`** FHRP: HSRP  `X`  `L:_`
- **`42.17`** FHRP: VRRP (incl. Huawei)  `X`  `L:_`
- **`42.18`** FHRP: GLBP  `X`  `L:_`

### 43 · Routing Fundamentals  `[CCNA]` `[ENCOR]` `[ENARSI]`

- **`43.01`** Routing table anatomy, longest prefix match  `C`  `L:_`
  - `43.01.1` Prefix, next-hop, exit interface
  - `43.01.2` Longest prefix match wins first
  - `43.01.3` Then administrative distance
  - `43.01.4` Then metric within the protocol
  - `43.01.5` Reading show ip route codes
- **`43.02`** Administrative distance table  `R`  `L:_`  →  `47.01`, `47.07`
  - `43.02.1` Connected 0 / Static 1
  - `43.02.2` eBGP 20
  - `43.02.3` EIGRP 90 / internal
  - `43.02.4` OSPF 110
  - `43.02.5` IS-IS 115 / RIP 120
  - `43.02.6` External EIGRP 170 / iBGP 200
  - `43.02.7` AD is local to the router, not advertised
- **`43.03`** Metrics by protocol  `R`  `L:_`
- **`43.04`** Static routes & default route  `X`  `L:_`  →  `32.05`
- **`43.05`** Floating static routes  `X`  `L:_`
- **`43.06`** Recursive vs directly-attached next-hop  `C`  `L:_`
- **`43.07`** Null0 & blackhole routes  `X`  `L:_`
- **`43.08`** Equal & unequal cost load balancing  `C`  `L:_`  →  `45.01`
- **`43.09`** CEF & switching paths  `C`  `L:_`
- **`43.10`** Policy-based routing (PBR)  `X`  `L:_`
- **`43.11`** VRF-lite  `X`  `L:_`  →  `48.03`
- **`43.12`** Routing troubleshooting methodology  `T`  `L:_`

### 44 · OSPF  `[CCNA]` `[ENCOR]` `[ENARSI]` `[MetroL3]`

- **`44.01`** Link-state fundamentals, LSDB, SPF  `C`  `L:_`
- **`44.02`** Neighbor states & adjacency formation  `C`  `L:_`  →  `44.13`
  - `44.02.1` Down → Init → 2-Way
  - `44.02.2` ExStart — master/slave and DBD
  - `44.02.3` Exchange → Loading → Full
  - `44.02.4` 2-Way is normal on a broadcast segment (non-DR)
  - `44.02.5` Which state it sticks in tells you the cause
- **`44.03`** Network types & DR/BDR election  `C`  `L:_`
  - `44.03.1` Broadcast — DR/BDR elected, hello 10
  - `44.03.2` Point-to-point — no DR, hello 10
  - `44.03.3` NBMA — DR needed, hello 30, manual neighbours
  - `44.03.4` Point-to-multipoint
  - `44.03.5` Highest priority wins, then highest router-ID
  - `44.03.6` DR is not preemptive
- **`44.04`** Area types: backbone, standard, stub, totally stubby, NSSA  `C`  `L:_`  →  `44.05`, `47.01`
  - `44.04.1` Backbone area 0 — all areas must touch it
  - `44.04.2` Standard area
  - `44.04.3` Stub — no external LSA5, default injected
  - `44.04.4` Totally stubby — no LSA3 either, Cisco only
  - `44.04.5` NSSA — external routes allowed in as LSA7
  - `44.04.6` Choosing the right type per site
- **`44.05`** LSA types 1–7  `R`  `L:_`  →  `44.04`
  - `44.05.1` Type 1 Router LSA — within area
  - `44.05.2` Type 2 Network LSA — from the DR
  - `44.05.3` Type 3 Summary — inter-area, from ABR
  - `44.05.4` Type 4 ASBR Summary
  - `44.05.5` Type 5 External — from ASBR
  - `44.05.6` Type 7 NSSA External — converted to 5 at ABR
- **`44.06`** Cost calculation & reference bandwidth  `C`  `L:_`
- **`44.07`** Authentication  `X`  `L:_`
- **`44.08`** Summarization: inter-area & external  `X`  `L:_`
- **`44.09`** Virtual links  `X`  `L:_`
- **`44.10`** Default route origination  `X`  `L:_`
- **`44.11`** OSPFv3 for IPv6  `X`  `L:_`
- **`44.12`** Multi-area configuration  `X`  `L:_`
- **`44.13`** Troubleshoot: hello/dead, area, MTU, mask mismatch  `T`  `L:_`  →  `44.02`, `88.02`
  - `44.13.1` Hello / dead interval mismatch
  - `44.13.2` Area ID mismatch
  - `44.13.3` Subnet mask mismatch on the segment
  - `44.13.4` MTU mismatch — sticks in ExStart/Exchange
  - `44.13.5` Authentication mismatch
  - `44.13.6` Network type mismatch
- **`44.14`** Troubleshoot: stuck in EXSTART / 2-WAY / INIT  `T`  `L:_`
  - `44.14.1` Stuck in INIT — hellos one-way, check ACL/filter
  - `44.14.2` Stuck in 2-WAY — normal if neither is DR/BDR
  - `44.14.3` Stuck in EXSTART — classic MTU mismatch
  - `44.14.4` Stuck in LOADING — LSA request unanswered
  - `44.14.5` debug ip ospf adj is the fast path

### 45 · EIGRP  `[CCNA]` `[ENCOR]` `[ENARSI]`

- **`45.01`** DUAL algorithm, successor, feasible successor  `C`  `L:_`  →  `43.08`
  - `45.01.1` Successor — best path, installed
  - `45.01.2` Feasible successor — instant backup
  - `45.01.3` Feasibility condition: AD of backup < FD of successor
  - `45.01.4` Query and reply when no FS exists
  - `45.01.5` Stuck-In-Active is a query scope problem
- **`45.02`** Feasibility condition  `C`  `L:_`
- **`45.03`** K-values & composite metric  `C`  `L:_`
- **`45.04`** Neighbor discovery, hello/hold timers  `C`  `L:_`
- **`45.05`** Summarization  `X`  `L:_`
- **`45.06`** Stub routing  `X`  `L:_`
- **`45.07`** Named mode configuration  `X`  `L:_`
- **`45.08`** Variance & unequal-cost load balancing  `X`  `L:_`
- **`45.09`** Authentication  `X`  `L:_`
- **`45.10`** Troubleshooting: SIA, neighbor flap, K mismatch  `T`  `L:_`

### 46 · BGP  `[ENCOR]` `[ENARSI]` `[ZTE-RIY1]`

- **`46.01`** eBGP vs iBGP, AS numbers, private ASN range  `C`  `L:_`
- **`46.02`** Neighbor states (Idle→Established)  `C`  `L:_`
- **`46.03`** Next-hop behaviour & next-hop-self  `C`  `L:_`
- **`46.04`** Path attributes: weight, local pref, AS-path, MED, origin  `C`  `L:_`  →  `46.06`
  - `46.04.1` Weight — Cisco only, local, higher wins
  - `46.04.2` Local Preference — within AS, higher wins
  - `46.04.3` AS-Path — shorter wins
  - `46.04.4` Origin — IGP < EGP < Incomplete
  - `46.04.5` MED — hint to neighbour AS, lower wins
  - `46.04.6` Communities — tagging for policy
- **`46.05`** Communities  `C`  `L:_`
- **`46.06`** Best path selection order  `R`  `L:_`  →  `46.04`, `47.03`
  - `46.06.1` Weight → Local Pref → Locally originated
  - `46.06.2` AS-Path length → Origin → MED
  - `46.06.3` eBGP over iBGP
  - `46.06.4` Lowest IGP metric to next-hop
  - `46.06.5` Oldest path → lowest router-ID → lowest neighbour IP
  - `46.06.6` Mnemonic: We Love Oranges AS Oranges Mean Pure Refreshment
- **`46.07`** Route reflectors  `C`  `L:_`
- **`46.08`** Confederations  `C`  `L:_`
- **`46.09`** Filtering: prefix-list, route-map, AS-path ACL  `X`  `L:_`
- **`46.10`** Aggregation & summarization  `X`  `L:_`
- **`46.11`** MP-BGP & address families  `C`  `L:_`  →  `48.03`
- **`46.12`** Multihoming & internet edge design  `C`  `L:_`
- **`46.13`** Troubleshooting: neighbor down, route not installed  `T`  `L:_`
  - `46.13.1` Stuck in Idle — no route to peer / ACL
  - `46.13.2` Active — TCP 179 not completing
  - `46.13.3` Established but no routes — filter or next-hop
  - `46.13.4` Route received but not best — check attributes
  - `46.13.5` iBGP route not advertised on — full mesh or RR missing

### 47 · Redistribution & Route Manipulation  `[ENCOR]` `[ENARSI]`

- **`47.01`** Redistribution between protocols  `X`  `L:_`  →  `43.02`, `44.04`
  - `47.01.1` Set a seed metric or routes are dropped
  - `47.01.2` One-way vs mutual redistribution
  - `47.01.3` Filtering with route-maps at the boundary
  - `47.01.4` Tagging on the way in, filtering on the way out
  - `47.01.5` Two redistribution points = loop risk
- **`47.02`** Seed metric & default-metric  `C`  `L:_`
- **`47.03`** Route-maps  `X`  `L:_`  →  `46.06`
- **`47.04`** Prefix-lists & distribute-lists  `X`  `L:_`
- **`47.05`** Route tagging  `X`  `L:_`
- **`47.06`** Redistribution loops & suboptimal routing  `T`  `L:_`
  - `47.06.1` Symptom: routes flapping between protocols
  - `47.06.2` Cause: mutual redistribution without tags
  - `47.06.3` Suboptimal path from AD mismatch
  - `47.06.4` Fix: tag and deny on the return path
- **`47.07`** AD manipulation to control path selection  `X`  `L:_`  →  `43.02`

### 48 · MPLS, WAN & Overlay  `[ENARSI]` `[ENCOR]` `[ZTE-RIY1]`

- **`48.01`** MPLS labels, LSR/LER, label stack  `C`  `L:_`
- **`48.02`** LDP  `C`  `L:_`
- **`48.03`** MPLS L3VPN: VRF, RD, RT  `C`  `L:_`  →  `43.11`, `46.11`
  - `48.03.1` VRF — separate routing table per customer
  - `48.03.2` Route Distinguisher — makes the prefix unique
  - `48.03.3` Route Target — controls import/export
  - `48.03.4` PE holds VRFs, P only switches labels
  - `48.03.5` CE is customer-managed and unaware
- **`48.04`** PE / CE / P router roles  `C`  `L:_`
- **`48.05`** MPLS TE basics  `C`  `L:_`
- **`48.06`** WAN types: leased line, metro-E, MPLS, broadband, 5G  `C`  `L:_`
- **`48.07`** PPP, PPPoE, HDLC  `C`  `L:_`
- **`48.08`** GRE tunnels  `X`  `L:_`  →  `62.05`
- **`48.09`** DMVPN phases, mGRE, NHRP  `C`  `L:_`
- **`48.10`** VXLAN & overlay fundamentals  `C`  `L:_`
- **`48.11`** LISP concept  `C`  `L:_`
- **`48.12`** SD-WAN concepts  `C`  `L:_`
- **`48.13`** SD-Access concept  `C`  `L:_`
- **`48.14`** QinQ  `C`  `L:_`
- **`48.15`** MPLS VPN (final year project)  `C`  `L:_`

### 49 · ACLs & QoS  `[CCNA]` `[ENCOR]` `[ENARSI]` `[Wemart]`

- **`49.01`** Standard vs extended ACLs  `X`  `L:_`  →  `61.03`, `63.03`, `78.02`
  - `49.01.1` Standard — source only, place near destination
  - `49.01.2` Extended — source, destination, protocol, port; place near source
  - `49.01.3` Implicit deny any at the end
  - `49.01.4` Order matters — first match wins
  - `49.01.5` Wildcard mask is the inverse of a subnet mask
- **`49.02`** Named ACLs & editing  `X`  `L:_`
- **`49.03`** Wildcard masks  `C`  `L:_`
- **`49.04`** ACL placement rules & implicit deny  `C`  `L:_`
- **`49.05`** Time-based ACLs  `X`  `L:_`
- **`49.06`** IPv6 ACLs  `X`  `L:_`
- **`49.07`** Huawei traffic-filter / traffic-policy  `X`  `L:_`
- **`49.08`** QoS models: best effort, IntServ, DiffServ  `C`  `L:_`
- **`49.09`** Classification & marking: DSCP, CoS, trust boundary  `C`  `L:_`
  - `49.09.1` Confirm direction: in vs out
  - `49.09.2` Confirm it is applied to the interface
  - `49.09.3` show access-list hit counters
  - `49.09.4` An implicit deny you forgot
  - `49.09.5` Return traffic blocked — the classic one-way ACL
- **`49.10`** Queuing: FIFO, WFQ, CBWFQ, LLQ  `C`  `L:_`
- **`49.11`** Shaping vs policing  `C`  `L:_`
- **`49.12`** Congestion avoidance & WRED  `C`  `L:_`
- **`49.13`** QoS for voice & video  `X`  `L:_`

---

# 50–59 · WIRELESS

<sub>Violet strand · 5 categories · 45 topics</sub>

### 50 · RF Fundamentals  `[CCNA]` `[ENCOR]` `[Wemart]`

- **`50.01`** Frequency, wavelength, amplitude, phase  `C`  `L:_`
- **`50.02`** Bands: 2.4 / 5 / 6 GHz — characteristics  `C`  `L:_`
- **`50.03`** Channels & non-overlapping channel plan  `R`  `L:_`  →  `54.05`
  - `50.03.1` 2.4 GHz — only 1, 6, 11 non-overlapping
  - `50.03.2` 5 GHz — UNII bands, DFS channels
  - `50.03.3` 6 GHz — Wi-Fi 6E, clean but short range
  - `50.03.4` Channel width halves the channel count
  - `50.03.5` Regulatory domain limits (KSA)
- **`50.04`** Channel width 20/40/80/160 MHz — trade-offs  `C`  `L:_`
- **`50.05`** dBm, mW, dBi, EIRP  `R`  `L:_`
  - `50.05.1` dBm — absolute power
  - `50.05.2` dB — a ratio, not a level
  - `50.05.3` dBi — antenna gain
  - `50.05.4` EIRP = Tx power − cable loss + antenna gain
  - `50.05.5` Rule of 3s and 10s for fast mental maths
- **`50.06`** Link budget & free space path loss  `C`  `L:_`
- **`50.07`** Attenuation, reflection, refraction, multipath  `C`  `L:_`
- **`50.08`** Antenna types & polarization  `C`  `L:_`
- **`50.09`** Co-channel & adjacent channel interference  `T`  `L:_`
- **`50.10`** RSSI, SNR, noise floor  `C`  `L:_`

### 51 · 802.11 Standards & Operation  `[CCNA]` `[ENCOR]`

- **`51.01`** 802.11 a/b/g/n/ac/ax — Wi-Fi 4/5/6/6E  `R`  `L:_`
  - `51.01.1` 802.11n — Wi-Fi 4, 2.4/5, MIMO
  - `51.01.2` 802.11ac — Wi-Fi 5, 5 GHz only, MU-MIMO DL
  - `51.01.3` 802.11ax — Wi-Fi 6, OFDMA, BSS colouring
  - `51.01.4` 6E — same as ax plus 6 GHz
  - `51.01.5` Backwards compatibility slows the whole cell
- **`51.02`** MIMO, MU-MIMO, beamforming  `C`  `L:_`
- **`51.03`** OFDMA & spatial streams  `C`  `L:_`
- **`51.04`** Frame types: management, control, data  `C`  `L:_`
- **`51.05`** Association: probe → auth → association  `C`  `L:_`
  - `51.05.1` Probe request / response
  - `51.05.2` Open authentication
  - `51.05.3` Association request / response
  - `51.05.4` 4-way handshake if WPA2
  - `51.05.5` Where it fails tells you what to fix
- **`51.06`** SSID, BSSID, BSS, ESS  `C`  `L:_`
- **`51.07`** Beacon interval & DTIM  `C`  `L:_`
- **`51.08`** Band steering & airtime fairness  `C`  `L:_`

### 52 · WLAN Architecture  `[ENCOR]` `[Wemart]` `[AlmavivA]`

- **`52.01`** Autonomous vs lightweight AP  `C`  `L:_`
- **`52.02`** WLC / WAC role — Huawei AirEngine 9700S-S  `X`  `L:_`  →  `53.02`, `54.02`
- **`52.03`** CAPWAP tunnel & split-MAC  `C`  `L:_`
  - `52.03.1` Control channel UDP 5246
  - `52.03.2` Data channel UDP 5247
  - `52.03.3` Split MAC — what stays on the AP
  - `52.03.4` DTLS encryption of control
  - `52.03.5` MTU and fragmentation issues over WAN
- **`52.04`** Central vs local switching / direct forwarding  `C`  `L:_`
- **`52.05`** AP modes: local, monitor, sniffer, mesh, bridge  `C`  `L:_`
- **`52.06`** AP discovery & join process  `T`  `L:_`
- **`52.07`** AP provisioning at scale (54+ AP deployment)  `X`  `L:_`  →  `10.11`
- **`52.08`** Mobility groups  `C`  `L:_`
- **`52.09`** Roaming: intra/inter-controller  `C`  `L:_`
  - `52.09.1` Intra-controller roam — fast
  - `52.09.2` Inter-controller, same mobility group
  - `52.09.3` Layer 2 vs Layer 3 roam
  - `52.09.4` Client decides when to roam, not the AP
  - `52.09.5` Sticky client is a client-side problem
- **`52.10`** Fast roaming 802.11r / k / v  `C`  `L:_`
- **`52.11`** Cloud-managed WLAN concepts  `C`  `L:_`

### 53 · Wireless Security  `[CCNA]` `[ENCOR]` `[Wemart]` `[Self]`

- **`53.01`** WEP, WPA, WPA2, WPA3 evolution  `C`  `L:_`
  - `53.01.1` WEP — broken, RC4
  - `53.01.2` WPA — TKIP, interim
  - `53.01.3` WPA2 — AES-CCMP, the long-time standard
  - `53.01.4` WPA3 — SAE, forward secrecy, mandatory PMF
  - `53.01.5` Transition modes and client support
- **`53.02`** PSK vs Enterprise (802.1X)  `C`  `L:_`  →  `35.03`, `52.02`
- **`53.03`** EAP types in WLAN  `C`  `L:_`
- **`53.04`** Guest network design  `X`  `L:_`
- **`53.05`** Captive portal / hotspot — MikroTik  `X`  `L:_`  →  `36.05`, `61.04`
  - `53.05.1` Hotspot on the bridge or IP interface
  - `53.05.2` Walled garden for pre-auth access
  - `53.05.3` User profiles: rate limit, session timeout, shared users
  - `53.05.4` Login page customisation
  - `53.05.5` MikroTik as the long-term answer to locked ISP firmware
- **`53.06`** MAC filtering & its limits  `C`  `L:_`
- **`53.07`** Rogue AP detection, WIPS  `C`  `L:_`
- **`53.08`** Client isolation  `X`  `L:_`

### 54 · WLAN Design & Troubleshooting  `[ENCOR]` `[Wemart]`

- **`54.01`** Coverage vs capacity design  `C`  `L:_`
- **`54.02`** AP placement & mounting  `X`  `L:_`  →  `52.02`
- **`54.03`** Site survey: predictive, passive, active  `X`  `L:_`
  - `54.03.1` Predictive — from a floor plan
  - `54.03.2` Passive — listening only, coverage
  - `54.03.3` Active — associated, throughput and roaming
  - `54.03.4` AP-on-a-stick validation
  - `54.03.5` Documenting before and after
- **`54.04`** Heat maps & survey tools  `C`  `L:_`
- **`54.05`** Channel & power planning  `X`  `L:_`  →  `50.03`
- **`54.06`** Sticky client problem  `T`  `L:_`
  - `54.06.1` Client holds a distant AP too long
  - `54.06.2` Raise minimum data rate
  - `54.06.3` Reduce AP power rather than adding APs
  - `54.06.4` 802.11k/v to nudge the client
  - `54.06.5` Some clients ignore everything — accept it
- **`54.07`** Low SNR / interference diagnosis  `T`  `L:_`
- **`54.08`** Client connectivity troubleshooting  `T`  `L:_`

---

# 60–69 · SECURITY & FIREWALL

<sub>Red strand · 6 categories · 53 topics</sub>

### 60 · Security Fundamentals  `[CCNA]` `[ENCOR]` `[A+]`

- **`60.01`** CIA triad  `C`  `L:_`
- **`60.02`** Threat vs vulnerability vs risk  `C`  `L:_`
- **`60.03`** Malware types  `C`  `L:_`
- **`60.04`** Social engineering & phishing  `C`  `L:_`
- **`60.05`** DoS / DDoS  `C`  `L:_`
- **`60.06`** MITM & spoofing  `C`  `L:_`
- **`60.07`** L2 attacks: ARP poisoning, VLAN hopping, MAC flood  `C`  `L:_`
- **`60.08`** DHCP starvation & rogue DHCP  `C`  `L:_`
- **`60.09`** Defense in depth  `C`  `L:_`
- **`60.10`** Zero trust concepts  `C`  `L:_`
- **`60.11`** Security policies & AUP  `C`  `L:_`

### 61 · Firewalls  `[Wemart]` `[ENCOR]` `[Self]` `[Veevo]`

- **`61.01`** Packet filter vs stateful vs proxy vs NGFW  `C`  `L:_`
- **`61.02`** Security zones & levels  `C`  `L:_`
- **`61.03`** Policy structure, rule order, implicit deny  `C`  `L:_`  →  `49.01`
  - `61.03.1` Top-down, first match wins
  - `61.03.2` Explicit deny at the end, and log it
  - `61.03.3` Zone pair direction matters
  - `61.03.4` Object groups keep it readable
  - `61.03.5` Review order after every insertion
- **`61.04`** NAT on firewall  `X`  `L:_`  →  `36.01`, `36.03`, `36.06`, `53.05`
- **`61.05`** UTM: IPS, AV, URL filtering, app control  `C`  `L:_`
- **`61.06`** Huawei USG6000E — configuration & policy  `X`  `L:_`
- **`61.07`** pfSense  `X`  `L:_`
- **`61.08`** FortiGate — GAP, target NSE4  `C`  `L:_`
- **`61.09`** Firewall HA: active/standby, active/active  `C`  `L:_`
- **`61.10`** Session table & logging  `T`  `L:_`
- **`61.11`** Policy troubleshooting — traffic denied/allowed wrongly  `T`  `L:_`
  - `61.11.1` Is it hitting the policy you think — check counters
  - `61.11.2` Session table: is a session created at all
  - `61.11.3` NAT applied before or after policy
  - `61.11.4` Route exists back out
  - `61.11.5` Asymmetric routing breaks stateful inspection

### 62 · VPN Technologies  `[Wemart]` `[ENARSI]` `[ENCOR]` `[MCSE]`

- **`62.01`** IPsec architecture: ESP vs AH  `C`  `L:_`
- **`62.02`** IKEv1 vs IKEv2, phase 1 & phase 2  `C`  `L:_`
  - `62.02.1` Phase 1 — protect the negotiation itself
  - `62.02.2` Main mode (6 msg) vs aggressive (3 msg)
  - `62.02.3` Phase 2 — protect the actual data (IPsec SA)
  - `62.02.4` IKEv2 — fewer messages, built-in NAT-T and DPD
  - `62.02.5` Lifetime mismatch causes periodic drops
- **`62.03`** Transform sets, DH groups, PFS  `C`  `L:_`
- **`62.04`** Tunnel vs transport mode  `C`  `L:_`
- **`62.05`** Site-to-site VPN configuration  `X`  `L:_`  →  `48.08`, `78.05`
  - `62.05.1` Matching transform set / proposal both ends
  - `62.05.2` Interesting traffic ACL must mirror exactly
  - `62.05.3` Pre-shared key or certificate
  - `62.05.4` NAT exemption for VPN traffic
  - `62.05.5` Peer reachability before anything else
- **`62.06`** Remote access VPN & SSL VPN  `X`  `L:_`
- **`62.07`** GRE over IPsec  `X`  `L:_`
- **`62.08`** Split tunneling  `C`  `L:_`
- **`62.09`** VPN troubleshooting: phase 1/2 mismatch, NAT-T  `T`  `L:_`
  - `62.09.1` Phase 1 down — PSK, DH group, encryption mismatch
  - `62.09.2` Phase 1 up, phase 2 down — proxy ID / ACL mismatch
  - `62.09.3` Tunnel up but no traffic — routing or NAT exemption
  - `62.09.4` Intermittent drop — lifetime or DPD
  - `62.09.5` UDP 500 / 4500 blocked upstream

### 63 · Network Hardening  `[CCNA]` `[ENCOR]` `[ENARSI]`

- **`63.01`** Password policy, privilege levels, role-based CLI  `X`  `L:_`
- **`63.02`** SSH hardening, disable telnet/HTTP  `X`  `L:_`
- **`63.03`** ACL on VTY lines  `X`  `L:_`  →  `49.01`
- **`63.04`** Control Plane Policing (CoPP)  `X`  `L:_`
- **`63.05`** Port security: sticky MAC, violation modes  `X`  `L:_`
  - `63.05.1` Maximum MAC addresses per port
  - `63.05.2` Sticky learning
  - `63.05.3` Violation: protect / restrict / shutdown
  - `63.05.4` Err-disable recovery
  - `63.05.5` Where it helps and where it just creates tickets
- **`63.06`** DHCP snooping  `X`  `L:_`  →  `32.09`, `63.07`, `63.08`
  - `63.06.1` Trusted vs untrusted ports
  - `63.06.2` The binding table it builds
  - `63.06.3` Uplinks and the DHCP server port must be trusted
  - `63.06.4` Rate limiting DHCP on access ports
  - `63.06.5` Feeds DAI and IP Source Guard
- **`63.07`** Dynamic ARP Inspection  `X`  `L:_`  →  `63.06`
- **`63.08`** IP Source Guard  `X`  `L:_`  →  `63.06`
- **`63.09`** Storm control  `X`  `L:_`
- **`63.10`** Disable unused ports & services  `X`  `L:_`
- **`63.11`** AAA on network devices  `X`  `L:_`  →  `35.03`
- **`63.12`** MACsec  `C`  `L:_`
- **`63.13`** Banners, logging & NTP for forensics  `X`  `L:_`

### 64 · Endpoint & Data Security  `[A+]` `[MCSE]` `[Wemart]`

- **`64.01`** Antivirus / EDR — Kaspersky deployment  `X`  `L:_`
- **`64.02`** Patch management strategy  `C`  `L:_`
- **`64.03`** BitLocker & disk encryption  `X`  `L:_`
- **`64.04`** Email security & spam filtering  `C`  `L:_`
- **`64.05`** Data classification basics  `C`  `L:_`
- **`64.06`** Incident response basics  `C`  `L:_`

### 65 · Physical & Operational Security  `[CCTV-OP]` `[Wemart]`

- **`65.01`** Access control: badge, biometric  `C`  `L:_`
- **`65.02`** Server room security & visitor policy  `C`  `L:_`
- **`65.03`** Asset disposal & data destruction  `C`  `L:_`

---

# 70–79 · VIRTUALIZATION & CLOUD

<sub>Rose strand · 10 categories · 104 topics</sub>

### 70 · Virtualization Fundamentals  `[VMware]` `[MCSE]` `[AZ900]`

- **`70.01`** Type 1 vs Type 2 hypervisor  `C`  `L:_`  →  `71.01`, `72.01`, `74.01`
- **`70.02`** vCPU scheduling, memory overcommit, ballooning  `C`  `L:_`
- **`70.03`** Thin vs thick provisioning  `C`  `L:_`
- **`70.04`** Snapshots vs backups — critical distinction  `C`  `L:_`
- **`70.05`** Containers vs VMs  `C`  `L:_`
- **`70.06`** Consolidation ratio & sizing  `C`  `L:_`

### 71 · VMware vSphere  `[VMware]`

- **`71.01`** ESXi installation & DCUI  `X`  `L:_`  →  `70.01`
- **`71.02`** vCenter (VCSA) deployment  `X`  `L:_`
- **`71.03`** Inventory: datacenter, cluster, folders, resource pools  `X`  `L:_`
- **`71.04`** Standard vSwitch  `X`  `L:_`
  - `71.04.1` Port groups and VLAN ID
  - `71.04.2` Uplinks and NIC teaming policy
  - `71.04.3` Load balancing: port ID, MAC hash, IP hash
  - `71.04.4` Failover order and failback
  - `71.04.5` Per-host configuration is the weakness
- **`71.05`** Distributed vSwitch  `X`  `L:_`
- **`71.06`** Port groups, VLAN tagging, NIC teaming  `X`  `L:_`
- **`71.07`** VMkernel adapters & traffic types  `X`  `L:_`
- **`71.08`** Datastores: VMFS & NFS  `X`  `L:_`
  - `71.08.1` VMFS — block storage, clustered filesystem
  - `71.08.2` NFS — file storage, simpler
  - `71.08.3` Datastore sizing and VMFS versions
  - `71.08.4` Multipathing policy: MRU, Fixed, Round Robin
  - `71.08.5` Free space and snapshot growth
- **`71.09`** iSCSI / FC storage, multipathing  `X`  `L:_`
- **`71.10`** RDM  `C`  `L:_`
- **`71.11`** vSAN basics  `C`  `L:_`
- **`71.12`** VM creation, hardware version, VMware Tools  `X`  `L:_`
- **`71.13`** Templates, clones, OVF/OVA  `X`  `L:_`
- **`71.14`** vMotion & Storage vMotion  `X`  `L:_`
  - `71.14.1` vMotion prerequisites: shared storage, vMotion VMkernel
  - `71.14.2` CPU compatibility and EVC
  - `71.14.3` Storage vMotion moves the disk, not the host
  - `71.14.4` Long-running vMotion causes
- **`71.15`** DRS  `X`  `L:_`
- **`71.16`** HA & admission control  `X`  `L:_`  →  `73.01`
  - `71.16.1` HA restarts VMs after host failure — brief outage
  - `71.16.2` Admission control reserves capacity
  - `71.16.3` Isolation response settings
  - `71.16.4` HA is not FT — know the difference in interview
- **`71.17`** Fault Tolerance  `C`  `L:_`
- **`71.18`** Lifecycle Manager / patching  `X`  `L:_`
- **`71.19`** Licensing model  `C`  `L:_`
- **`71.20`** Troubleshoot: host disconnect, datastore full, PSOD  `T`  `L:_`
  - `71.20.1` Host disconnected — management agents / network
  - `71.20.2` Datastore full — often snapshots
  - `71.20.3` PSOD — read the backtrace, usually hardware/driver
  - `71.20.4` VM won't power on — resource or lock file
  - `71.20.5` Where the logs actually live

### 72 · Microsoft Hyper-V  `[MCSE]` `[Self]`

- **`72.01`** Role installation & requirements  `X`  `L:_`  →  `70.01`
- **`72.02`** Generation 1 vs 2 VMs  `C`  `L:_`
- **`72.03`** Virtual switches: external, internal, private  `X`  `L:_`  →  `41.03`
  - `72.03.1` External — bound to a physical NIC
  - `72.03.2` Internal — host and VMs only
  - `72.03.3` Private — VMs only, no host
  - `72.03.4` VLAN tagging per adapter
  - `72.03.5` Common mistake: losing host connectivity on creation
- **`72.04`** VHD vs VHDX, differencing disks  `C`  `L:_`
- **`72.05`** Dynamic memory  `X`  `L:_`
- **`72.06`** Checkpoints: standard vs production  `X`  `L:_`
  - `72.06.1` Standard checkpoint — includes memory state
  - `72.06.2` Production checkpoint — uses VSS, application-consistent
  - `72.06.3` Checkpoints are not backups
  - `72.06.4` AVHDX chain growth and merge
  - `72.06.5` Deleting a checkpoint triggers a merge
- **`72.07`** Live migration & storage migration  `X`  `L:_`
- **`72.08`** Hyper-V Replica  `X`  `L:_`
- **`72.09`** Nested virtualization  `X`  `L:_`
- **`72.10`** Integration services  `C`  `L:_`

### 73 · Clustering & HA  `[MCSE]` `[ZTE-RIY1]`

- **`73.01`** Windows Failover Clustering overview  `C`  `L:_`  →  `71.16`
- **`73.02`** Quorum models & witness types  `C`  `L:_`
- **`73.03`** Cluster Shared Volumes  `X`  `L:_`
- **`73.04`** Cluster-Aware Updating  `X`  `L:_`
- **`73.05`** Network Load Balancing  `C`  `L:_`
- **`73.06`** Shared storage requirements  `C`  `L:_`
- **`73.07`** Split-brain scenarios  `T`  `L:_`
- **`73.08`** Ceph / software-defined storage (R5300 G5 nodes)  `C`  `L:_`  →  `12.05`

### 74 · Cloud Fundamentals  `[AZ900]` `[AZ104]`

- **`74.01`** IaaS / PaaS / SaaS  `C`  `L:_`  →  `70.01`
- **`74.02`** Public, private, hybrid, community models  `C`  `L:_`
- **`74.03`** CapEx vs OpEx  `C`  `L:_`
- **`74.04`** Shared responsibility model  `C`  `L:_`
- **`74.05`** Elasticity, scalability, agility, HA, DR  `C`  `L:_`
- **`74.06`** Cloud SLAs & service credits  `C`  `L:_`
- **`74.07`** Regions, availability zones, geographies  `C`  `L:_`

### 75 · Azure Identity & Governance  `[AZ104]`

- **`75.01`** Entra ID: tenants, users, groups  `X`  `L:_`
- **`75.02`** RBAC: roles, scope, assignments  `X`  `L:_`
  - `75.02.1` Scope: management group → subscription → RG → resource
  - `75.02.2` Built-in roles: Owner, Contributor, Reader, User Access Administrator
  - `75.02.3` Assignments inherit downward
  - `75.02.4` Deny assignments override allow
  - `75.02.5` Least privilege in practice
- **`75.03`** Custom roles  `X`  `L:_`
- **`75.04`** Administrative units  `C`  `L:_`
- **`75.05`** MFA & conditional access  `X`  `L:_`
  - `75.05.1` Conditional Access requires Entra ID P1
  - `75.05.2` Signals: user, device, location, risk
  - `75.05.3` Grant vs session controls
  - `75.05.4` Report-only mode before enforcing
  - `75.05.5` Break-glass account exclusion
- **`75.06`** Self-service password reset  `X`  `L:_`
- **`75.07`** Entra Connect / hybrid identity  `C`  `L:_`
- **`75.08`** Management groups, subscriptions, resource groups  `C`  `L:_`
- **`75.09`** Azure Policy & initiatives  `X`  `L:_`
- **`75.10`** Resource locks & tags  `X`  `L:_`
- **`75.11`** Cost Management & budgets  `X`  `L:_`

### 76 · Azure Storage  `[AZ104]`

- **`76.01`** Storage account types & performance tiers  `C`  `L:_`
- **`76.02`** Blob containers & access tiers (hot/cool/archive)  `X`  `L:_`
- **`76.03`** Lifecycle management policies  `X`  `L:_`
- **`76.04`** Azure Files & File Sync  `X`  `L:_`
- **`76.05`** Redundancy: LRS, ZRS, GRS, GZRS, RA-GRS  `R`  `L:_`  →  `25.03`
  - `76.05.1` LRS — 3 copies, one datacentre
  - `76.05.2` ZRS — 3 zones, one region
  - `76.05.3` GRS — secondary region, async
  - `76.05.4` GZRS — zones plus secondary region
  - `76.05.5` RA- variants allow read from secondary
  - `76.05.6` Cost rises with resilience
- **`76.06`** Access keys, SAS tokens, Entra auth  `X`  `L:_`
  - `76.06.1` Access keys — full control, rotate them
  - `76.06.2` SAS — scoped and time-limited
  - `76.06.3` Stored access policy for revocation
  - `76.06.4` Entra ID auth — the preferred route
  - `76.06.5` Anonymous public access risk
- **`76.07`** Encryption at rest  `C`  `L:_`
- **`76.08`** Storage Explorer & AzCopy  `X`  `L:_`

### 77 · Azure Compute  `[AZ104]`

- **`77.01`** VM sizes & series  `R`  `L:_`
- **`77.02`** Managed disks: OS & data, disk types  `X`  `L:_`
- **`77.03`** Availability sets: fault & update domains  `C`  `L:_`
  - `77.03.1` Fault domain — separate rack/power
  - `77.03.2` Update domain — separate patch window
  - `77.03.3` Availability set is within one datacentre
  - `77.03.4` Zones span datacentres — stronger SLA
  - `77.03.5` Cannot add an existing VM to a set later
- **`77.04`** Availability zones  `C`  `L:_`
- **`77.05`** VM Scale Sets & autoscale  `X`  `L:_`
  - `77.05.1` Uniform vs flexible orchestration
  - `77.05.2` Scale-in and scale-out rules
  - `77.05.3` Metric-based vs schedule-based autoscale
  - `77.05.4` Cooldown period
  - `77.05.5` Custom image vs extension for provisioning
- **`77.06`** VM extensions & custom script  `X`  `L:_`
- **`77.07`** Images & generalization  `X`  `L:_`
- **`77.08`** ARM templates & Bicep  `X`  `L:_`
- **`77.09`** App Service & App Service Plans  `X`  `L:_`
- **`77.10`** Azure Container Instances, AKS basics  `C`  `L:_`
- **`77.11`** Azure Functions concept  `C`  `L:_`

### 78 · Azure Networking  `[AZ104]`

- **`78.01`** Virtual Network & subnets, address planning  `X`  `L:_`
- **`78.02`** NSG & ASG, effective rules  `X`  `L:_`  →  `36.06`, `49.01`
  - `78.02.1` NSG on subnet vs on NIC — both apply
  - `78.02.2` Rules by priority, lowest number first
  - `78.02.3` Default rules you cannot delete
  - `78.02.4` ASG groups NICs by role instead of by IP
  - `78.02.5` Effective security rules is the debugging view
- **`78.03`** VNet peering: regional & global  `X`  `L:_`
- **`78.04`** User Defined Routes & route tables  `X`  `L:_`
  - `78.04.1` System routes exist by default
  - `78.04.2` UDR overrides system routes
  - `78.04.3` Next hop types: virtual appliance, gateway, internet, none
  - `78.04.4` Forced tunnelling to on-premises
  - `78.04.5` Route priority: UDR > BGP > system
- **`78.05`** VPN Gateway: site-to-site & point-to-site  `X`  `L:_`  →  `62.05`
  - `78.05.1` Gateway subnet requirement and sizing
  - `78.05.2` Route-based vs policy-based
  - `78.05.3` SKU decides throughput and tunnel count
  - `78.05.4` Local network gateway = on-prem side
  - `78.05.5` Point-to-site auth: certificate or Entra
- **`78.06`** ExpressRoute  `C`  `L:_`
- **`78.07`** Azure Firewall  `X`  `L:_`
- **`78.08`** Azure Bastion  `X`  `L:_`
- **`78.09`** Load Balancer: basic vs standard  `X`  `L:_`
- **`78.10`** Application Gateway & WAF  `X`  `L:_`
- **`78.11`** Front Door & Traffic Manager  `C`  `L:_`
- **`78.12`** Private Link & Private Endpoint  `C`  `L:_`
- **`78.13`** Service Endpoints  `C`  `L:_`  →  `33.10`
- **`78.14`** Network Watcher & NSG flow logs  `T`  `L:_`
- **`78.15`** Public IP & virtual public IP setup  `X`  `L:_`

### 79 · Azure Monitoring & Recovery  `[AZ104]`

- **`79.01`** Azure Monitor: metrics & logs  `X`  `L:_`
- **`79.02`** Log Analytics workspace & KQL basics  `X`  `L:_`  →  `81.01`, `83.02`
  - `79.02.1` Workspace as the collection point
  - `79.02.2` Tables: Heartbeat, AzureActivity, Perf
  - `79.02.3` KQL basics: where, project, summarize, render
  - `79.02.4` Time range is a filter, not a suggestion
  - `79.02.5` Retention and cost
- **`79.03`** Alerts & action groups  `X`  `L:_`
- **`79.04`** Application Insights concept  `C`  `L:_`
- **`79.05`** Azure Backup & Recovery Services vault  `X`  `L:_`
- **`79.06`** Backup policies & retention  `X`  `L:_`
- **`79.07`** Azure Site Recovery  `C`  `L:_`
- **`79.08`** Update Management  `X`  `L:_`

---

# 80–89 · MONITORING, OPS & AUTOMATION

<sub>Yellow strand · 10 categories · 92 topics</sub>

### 80 · Monitoring Fundamentals  `[Veevo]` `[Wemart]`

- **`80.01`** Metrics vs logs vs traces  `C`  `L:_`
- **`80.02`** Baselines & thresholds  `C`  `L:_`
- **`80.03`** Alert fatigue & tuning  `C`  `L:_`
- **`80.04`** Agent vs agentless monitoring  `C`  `L:_`
- **`80.05`** Polling vs trap-based  `C`  `L:_`
- **`80.06`** Availability vs performance monitoring  `C`  `L:_`

### 81 · Zabbix  `[Veevo]` `[Wemart]`

- **`81.01`** Architecture: server, agent, proxy, DB, frontend  `C`  `L:_`  →  `79.02`
  - `81.01.1` Server — the processing engine
  - `81.01.2` Agent — active vs passive checks
  - `81.01.3` Proxy — for remote sites and scale
  - `81.01.4` Database — the actual bottleneck
  - `81.01.5` Frontend — PHP, separate from server
- **`81.02`** Installation & initial setup  `X`  `L:_`
- **`81.03`** Hosts, host groups, interfaces  `X`  `L:_`
- **`81.04`** Items: keys, value types, update intervals  `X`  `L:_`
  - `81.04.1` Item key syntax and parameters
  - `81.04.2` Value type must match the data
  - `81.04.3` Update interval vs flexible interval
  - `81.04.4` Preprocessing steps
  - `81.04.5` Units and value mapping for readable output
- **`81.05`** Triggers & expressions, severity levels  `X`  `L:_`
  - `81.05.1` Expression syntax: last(), avg(), min/max
  - `81.05.2` Severity levels and what deserves each
  - `81.05.3` Recovery expression and hysteresis
  - `81.05.4` Dependencies to suppress alert storms
  - `81.05.5` Manual close for one-shot events
- **`81.06`** Templates: linkage & inheritance  `X`  `L:_`
- **`81.07`** Huawei VRP SNMP template  `X`  `L:_`  →  `28.05`, `82.01`
- **`81.08`** Low-Level Discovery (LLD)  `X`  `L:_`
  - `81.08.1` Discovery rule returns a JSON list
  - `81.08.2` Item, trigger and graph prototypes
  - `81.08.3` Filters with regex to exclude noise
  - `81.08.4` Keep lost resources period
  - `81.08.5` Where LLD makes 200 interfaces manageable
- **`81.09`** Actions, conditions, operations  `X`  `L:_`
- **`81.10`** Media types & email alerting (AliMail)  `X`  `L:_`
- **`81.11`** Dashboards & graphs  `X`  `L:_`
- **`81.12`** Network maps / topology via JSON-RPC API  `X`  `L:_`
- **`81.13`** Zabbix API  `X`  `L:_`
- **`81.14`** Printer / toner monitoring  `X`  `L:_`
- **`81.15`** Housekeeping & performance tuning  `T`  `L:_`
- **`81.16`** Troubleshoot: agent unreachable, no data, false alerts  `T`  `L:_`
  - `81.16.1` Agent unreachable — firewall, port 10050, agent config
  - `81.16.2` No data on an item — key wrong or permission
  - `81.16.3` Trigger not firing — expression or dependency
  - `81.16.4` Alert storm — no dependencies or hysteresis
  - `81.16.5` Queue growing — poller count or DB performance

### 82 · SNMP & Telemetry  `[Veevo]` `[Wemart]` `[ENCOR]`

- **`82.01`** OIDs, MIBs, SMI structure  `C`  `L:_`  →  `37.05`, `81.07`
  - `82.01.1` OID is a dotted numeric path
  - `82.01.2` MIB translates OID to a readable name
  - `82.01.3` Enterprise OIDs are vendor-specific
  - `82.01.4` Walk to discover, get to poll
  - `82.01.5` ifTable is where most interface data lives
- **`82.02`** v1 / v2c community strings  `C`  `L:_`
- **`82.03`** v3 users & security levels  `X`  `L:_`
  - `82.03.1` noAuthNoPriv — username only
  - `82.03.2` authNoPriv — MD5/SHA authentication
  - `82.03.3` authPriv — plus DES/AES encryption
  - `82.03.4` Engine ID and user context
  - `82.03.5` Why v3 matters on a carrier network
- **`82.04`** Get, GetNext, GetBulk, Walk  `X`  `L:_`
- **`82.05`** Traps vs informs  `C`  `L:_`
- **`82.06`** snmpwalk in practice  `X`  `L:_`
- **`82.07`** NetFlow / sFlow / IPFIX  `C`  `L:_`
- **`82.08`** Streaming telemetry concept  `C`  `L:_`

### 83 · Logging & Syslog  `[Veevo]` `[ENCOR]`

- **`83.01`** Facilities & severity levels 0–7  `R`  `L:_`
- **`83.02`** Centralized syslog server  `X`  `L:_`  →  `34.04`, `79.02`
- **`83.03`** Log rotation & retention  `X`  `L:_`
- **`83.04`** Log correlation & SIEM concept  `C`  `L:_`

### 84 · Other Tools & Platforms  `[Veevo]` `[Wemart]` `[ZTE-RIY1]` `[CV]`

- **`84.01`** PRTG  `X`  `L:_`
- **`84.02`** Dell OpenManage  `X`  `L:_`
- **`84.03`** HAProxy — load balancing concepts  `X`  `L:_`
- **`84.04`** Roxy-WI  `X`  `L:_`
- **`84.05`** Asterisk / VoIP server  `X`  `L:_`
- **`84.06`** Node.js & PM2 process manager  `X`  `L:_`
- **`84.07`** Nagios / LibreNMS concepts  `C`  `L:_`
- **`84.08`** iEPMS scanning (ZTE)  `X`  `L:_`
- **`84.09`** Huawei eSight / iMaster NCE  `C`  `L:_`
- **`84.10`** Cisco DNA Center concept  `C`  `L:_`

### 85 · Service Management & ITIL  `[CV — unverified]`

- **`85.01`** Incident management  `C`  `L:_`
- **`85.02`** Problem management & RCA  `C`  `L:_`
- **`85.03`** Change management & CAB  `C`  `L:_`
- **`85.04`** Request fulfilment  `C`  `L:_`
- **`85.05`** SLA, OLA, underpinning contracts  `C`  `L:_`
- **`85.06`** Priority matrix: impact × urgency  `R`  `L:_`
  - `85.06.1` Impact — how many are affected
  - `85.06.2` Urgency — how fast it must be fixed
  - `85.06.3` Priority = impact × urgency
  - `85.06.4` P1 to P4 and the response clock
  - `85.06.5` Agreeing priority before the incident, not during
- **`85.07`** CMDB & asset management  `C`  `L:_`
- **`85.08`** Ticketing workflow & escalation  `X`  `L:_`
- **`85.09`** Post-incident review  `C`  `L:_`

### 86 · Documentation  `[ZTE-RIY1]` `[MetroL3]` `[Wemart]`

- **`86.01`** Logical vs physical topology diagrams  `X`  `L:_`
- **`86.02`** IPAM & address registers  `X`  `L:_`
- **`86.03`** Port matrix / patch schedules  `X`  `L:_`
- **`86.04`** Rack elevations  `X`  `L:_`
- **`86.05`** Method of Procedure (MOP)  `X`  `L:_`
- **`86.06`** As-built & handover packs  `X`  `L:_`
- **`86.07`** Labelling standards  `R`  `L:_`
- **`86.08`** Config backup discipline  `X`  `L:_`
- **`86.09`** IT asset inventory  `X`  `L:_`

### 87 · Scripting & Automation  `[ENCOR]` `[Self]`

- **`87.01`** Python fundamentals: variables, loops, functions  `C`  `L:_`
- **`87.02`** Netmiko  `X`  `L:_`
  - `87.02.1` ConnectHandler and device_type
  - `87.02.2` send_command vs send_config_set
  - `87.02.3` Handling prompts and timeouts
  - `87.02.4` Looping a device inventory
  - `87.02.5` Saving output safely — never overwrite blind
- **`87.03`** Paramiko  `X`  `L:_`
- **`87.04`** NAPALM  `C`  `L:_`
- **`87.05`** REST APIs & requests library  `X`  `L:_`
- **`87.06`** JSON, XML, YAML formats  `C`  `L:_`
- **`87.07`** Ansible: inventory, playbooks, modules, idempotency  `X`  `L:_`
  - `87.07.1` Inventory file — hosts and groups
  - `87.07.2` Playbook structure: hosts, tasks, handlers
  - `87.07.3` Idempotency — run twice, same result
  - `87.07.4` Variables and templates with Jinja2
  - `87.07.5` Check mode before you commit
- **`87.08`** NETCONF & RESTCONF  `C`  `L:_`
- **`87.09`** YANG models  `C`  `L:_`
- **`87.10`** Cisco EEM  `C`  `L:_`
- **`87.11`** Git basics  `X`  `L:_`
- **`87.12`** Python PIL / FFmpeg rendering (content workflow)  `X`  `L:_`

### 88 · Troubleshooting Methodology  `[A+]` `[CCNA]` `[Field]`

- **`88.01`** Structured method: define → gather → analyse → test  `C`  `L:_`
  - `88.01.1` Define the problem in one sentence
  - `88.01.2` Gather facts before forming a theory
  - `88.01.3` One change at a time
  - `88.01.4` Test the theory, then verify the fix
  - `88.01.5` Document it — future you is the beneficiary
- **`88.02`** OSI approaches: bottom-up, top-down, divide & conquer  `C`  `L:_`  →  `38.01`, `44.13`
  - `88.02.1` Bottom-up — start at the cable, best for new installs
  - `88.02.2` Top-down — start at the application, best for a working system that broke
  - `88.02.3` Divide and conquer — start at L3, fastest with experience
  - `88.02.4` Follow the path — trace the traffic hop by hop
  - `88.02.5` Swap test — replace a suspect component
- **`88.03`** ping, traceroute, telnet-to-port  `X`  `L:_`
- **`88.04`** nslookup, arp, netstat, route print  `X`  `L:_`
- **`88.05`** Wireshark & packet capture basics  `T`  `L:_`
  - `88.05.1` Capture at the right point, not the convenient one
  - `88.05.2` Display filter vs capture filter
  - `88.05.3` Following a TCP stream
  - `88.05.4` Reading retransmits and resets
  - `88.05.5` Timing columns tell you where the delay is
- **`88.06`** SPAN / RSPAN / ERSPAN  `X`  `L:_`
- **`88.07`** Physical layer first — the discipline  `C`  `L:_`
- **`88.08`** Fault pattern log (personal)  `T`  `L:_`

### 89 · Project & Field Operations  `[ZTE-RIY1]` `[MetroL3]` `[UCT]`

- **`89.01`** Site survey & pre-deployment checks  `X`  `L:_`
- **`89.02`** BOQ / BOM preparation  `X`  `L:_`
- **`89.03`** Bench testing & staging  `X`  `L:_`
- **`89.04`** Cutover planning & rollback plan  `X`  `L:_`
- **`89.05`** Maintenance window discipline  `C`  `L:_`
- **`89.06`** Acceptance testing & handover  `X`  `L:_`
- **`89.07`** Vendor & ISP coordination  `X`  `L:_`
- **`89.08`** Health & safety on site  `C`  `L:_`
- **`89.09`** SMB deployment end-to-end (2-office reference build)  `X`  `L:_`
- **`89.10`** Client quoting & scope definition  `X`  `L:_`

---

# 90–99 · CCTV & PHYSICAL SECURITY

<sub>Bronze strand · 7 categories · 57 topics</sub>

### 90 · Camera Fundamentals  `[CCTV-OP]` `[Wemart]`

- **`90.01`** Types: bullet, dome, turret, PTZ, fisheye, panoramic  `C`  `L:_`
- **`90.02`** Sensor size & resolution 2/4/6/8 MP, 4K  `C`  `L:_`
- **`90.03`** Lens focal length & field of view calculation  `R`  `L:_`  →  `94.03`
  - `90.03.1` FoV narrows as focal length rises
  - `90.03.2` Sensor size changes the same lens's FoV
  - `90.03.3` Calculating coverage width at a distance
  - `90.03.4` Choosing between wide coverage and detail
  - `90.03.5` Varifocal buys you a second chance
- **`90.04`** Fixed vs varifocal vs motorized lens  `C`  `L:_`
- **`90.05`** IR / EXIR illumination & night distance  `C`  `L:_`
- **`90.06`** WDR, BLC, HLC  `C`  `L:_`
  - `90.06.1` WDR for scenes with bright and dark together
  - `90.06.2` BLC for a subject in front of a light source
  - `90.06.3` HLC to suppress headlights
  - `90.06.4` True WDR vs digital WDR
  - `90.06.5` Entrance doors are the classic WDR case
- **`90.07`** Low-light tech: DarkFighter, ColorVu  `C`  `L:_`
- **`90.08`** IP & IK ratings, vandal resistance  `R`  `L:_`
- **`90.09`** Analog HD-TVI / AHD / CVI vs IP  `C`  `L:_`
- **`90.10`** ONVIF & interoperability  `C`  `L:_`

### 91 · Recording & Storage  `[CCTV-OP]` `[Wemart]`

- **`91.01`** NVR vs DVR vs hybrid  `C`  `L:_`
- **`91.02`** Channel count & incoming bandwidth limits  `R`  `L:_`
- **`91.03`** Surveillance-grade HDD selection  `C`  `L:_`
- **`91.04`** RAID on NVR  `X`  `L:_`
- **`91.05`** Storage calculation: bitrate × channels × retention  `R`  `L:_`  →  `92.03`
  - `91.05.1` Bitrate × 3600 ÷ 8 = MB per camera-hour
  - `91.05.2` Multiply by cameras and retention days
  - `91.05.3` Add 10–15% overhead
  - `91.05.4` CBR vs VBR changes the maths
  - `91.05.5` Worked example: 237 cameras across 4 NVRs
- **`91.06`** Compression H.264 / H.265 / H.265+  `C`  `L:_`
- **`91.07`** Recording modes: continuous, motion, event, schedule  `X`  `L:_`
- **`91.08`** Retention policy & legal requirement  `C`  `L:_`
- **`91.09`** Disk-full & overwrite behaviour — recovery  `T`  `L:_`
  - `91.09.1` Overwrite enabled — oldest footage silently gone
  - `91.09.2` Overwrite disabled — recording simply stops
  - `91.09.3` Check disk health before assuming it is full
  - `91.09.4` Retention shrinks when bitrate is raised
  - `91.09.5` Alert on disk state before it bites
- **`91.10`** Multi-NVR architecture (4-NVR / 237-camera reference)  `X`  `L:_`

### 92 · CCTV Networking  `[CCTV-OP]` `[Wemart]`

- **`92.01`** IP scheme & VLAN segmentation for cameras  `X`  `L:_`
- **`92.02`** PoE budget planning & switch selection  `X`  `L:_`  →  `10.11`
  - `92.02.1` Sum camera draw, not port count
  - `92.02.2` Reserve headroom for PTZ and heaters
  - `92.02.3` Per-port limit vs total switch budget
  - `92.02.4` PoE class negotiation
  - `92.02.5` Cameras rebooting at night = budget or voltage drop
- **`92.03`** Per-camera bandwidth calculation  `R`  `L:_`  →  `91.05`
  - `92.03.1` Bitrate per camera at chosen resolution and fps
  - `92.03.2` Sum per switch uplink
  - `92.03.3` NVR incoming bandwidth ceiling
  - `92.03.4` Sub-stream for live view, main stream for recording
  - `92.03.5` Do not forget remote viewing traffic
- **`92.04`** Unicast vs multicast streaming  `C`  `L:_`
- **`92.05`** Long runs: fiber + media converter  `X`  `L:_`  →  `11.14`
- **`92.06`** Media converter failure diagnosis  `T`  `L:_`
- **`92.07`** Remote access: port forward vs P2P vs VPN  `C`  `L:_`
- **`92.08`** NTP for cameras — timestamp integrity  `X`  `L:_`  →  `34.04`

### 93 · VMS & Software  `[CCTV-OP]` `[Wemart]`

- **`93.01`** Hikvision iVMS-4200  `X`  `L:_`
- **`93.02`** HikCentral  `X`  `L:_`
- **`93.03`** SADP — discovery & activation  `X`  `L:_`
- **`93.04`** Live view, playback, export  `X`  `L:_`
- **`93.05`** User accounts & permissions  `X`  `L:_`
- **`93.06`** Firmware upgrade  `X`  `L:_`
- **`93.07`** Analytics: motion, line crossing, intrusion, tamper  `X`  `L:_`
- **`93.08`** Face detection / ANPR concepts  `C`  `L:_`

### 94 · Installation & Placement  `[CCTV-OP]` `[Wemart]`

- **`94.01`** Mounting height & angle guidelines  `R`  `L:_`
- **`94.02`** Coverage planning, overlap, blind spots  `X`  `L:_`
- **`94.03`** DORI: detection / observation / recognition / ID distance  `R`  `L:_`  →  `90.03`
  - `94.03.1` Detection — object present, ~25 px/m
  - `94.03.2` Observation — ~62 px/m
  - `94.03.3` Recognition — known person, ~125 px/m
  - `94.03.4` Identification — evidential, ~250 px/m
  - `94.03.5` Match the target to the purpose before choosing the lens
- **`94.04`** Avoiding backlight, glare, IR bounce  `T`  `L:_`
- **`94.05`** Priority zones: entry/exit, till points, perimeter  `C`  `L:_`
- **`94.06`** Cable routing, junction boxes, weatherproofing  `X`  `L:_`
- **`94.07`** Power: PoE vs local adapter  `C`  `L:_`
- **`94.08`** Commissioning checklist  `R`  `L:_`
- **`94.09`** Common placement mistakes  `T`  `L:_`
  - `94.09.1` Mounted too high — top of heads only
  - `94.09.2` Facing a window or the sun
  - `94.09.3` IR bounce from a nearby wall or ceiling
  - `94.09.4` Covering everything, identifying nothing
  - `94.09.5` No camera on the entry point itself

### 95 · Access Control & Alarms  `[CCTV-OP]`

- **`95.01`** Card readers & biometrics  `C`  `L:_`
- **`95.02`** Controllers & wiring  `C`  `L:_`
- **`95.03`** Locks: magnetic, electric strike  `C`  `L:_`
- **`95.04`** REX, door contacts, break-glass  `C`  `L:_`
- **`95.05`** Integration with CCTV  `C`  `L:_`
- **`95.06`** Intrusion alarm panels & sensors  `C`  `L:_`
- **`95.07`** Fire alarm interface basics  `C`  `L:_`

### 96 · Evidence & Operations  `[CCTV-OP]` `[Wemart]`

- **`96.01`** Incident retrieval workflow  `X`  `L:_`  →  `34.04`
- **`96.02`** Export formats & watermarking  `X`  `L:_`
- **`96.03`** Chain of custody basics  `C`  `L:_`
- **`96.04`** Privacy & data protection considerations  `C`  `L:_`
- **`96.05`** Maintenance schedule & camera health checks  `X`  `L:_`

---

# Where to extend

Categories where no topic has subtopics yet. These are the next places to break down —
start with whatever you are revising or interviewing on, not top to bottom.

| Category | Topics | |
|---|---:|---|
| `00` System | 2 | ☐ |
| `01` Exam & Certification Tracker | 8 | ☐ |
| `02` Career | 4 | ☐ |
| `03` Labs & Resources | 4 | ☐ |
| `13` Racks & Data Centre | 6 | ☐ |
| `14` Power & UPS | 7 | ☐ |
| `15` Peripherals & Endpoints | 8 | ☐ |
| `20` Windows Client | 7 | ☐ |
| `21` Windows Server — Core | 8 | ☐ |
| `24` Windows Roles & Services | 18 | ☐ |
| `25` Windows Backup & Monitoring | 8 | ☐ |
| `26` PowerShell | 6 | ☐ |
| `27` Linux | 13 | ☐ |
| `28` Network Device CLI | 12 | ☐ |
| `29` Lab Environments | 4 | ☐ |
| `31` IPv6 | 9 | ☐ |
| `34` NTP & Time | 5 | ☐ |
| `35` AAA & Identity | 8 | ☐ |
| `36` NAT | 9 | ☐ |
| `37` Application Protocols & Ports | 10 | ☐ |
| `40` Switching Fundamentals & Design | 11 | ☐ |
| `60` Security Fundamentals | 11 | ☐ |
| `64` Endpoint & Data Security | 6 | ☐ |
| `65` Physical & Operational Security | 3 | ☐ |
| `70` Virtualization Fundamentals | 6 | ☐ |
| `73` Clustering & HA | 8 | ☐ |
| `74` Cloud Fundamentals | 7 | ☐ |
| `80` Monitoring Fundamentals | 6 | ☐ |
| `83` Logging & Syslog | 4 | ☐ |
| `84` Other Tools & Platforms | 10 | ☐ |
| `86` Documentation | 9 | ☐ |
| `89` Project & Field Operations | 10 | ☐ |
| `93` VMS & Software | 8 | ☐ |
| `95` Access Control & Alarms | 7 | ☐ |
| `96` Evidence & Operations | 5 | ☐ |

<sub>35 of 77 categories awaiting breakdown.</sub>

---

# What I could not know

This index is built from published exam blueprints plus documented field work. Yours to fill:

1. **Notebook-only content** — what Corvit instructors taught beyond the blueprint.
2. **Udemy and YouTube specifics** — VMware and AZ-900 courses may cover more than listed.
3. **AlmavivA** — thin here. I know the role, not the stack.
4. **Mis-tagged topics** — if you learned it at Wemart, the field tag matters more than the course tag.
5. **Things you have only heard of** — add at L:0. SASE, Kubernetes, Terraform, Palo Alto, Juniper.
6. **Anything placed wrongly** — say so and it moves.
