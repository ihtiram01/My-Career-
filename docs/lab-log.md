---
title: Labs & Practice
page: labs
order: 7
colour: aqua
kicker: Section 07 · practice
summary: EVE-NG topologies built and what each one proved. Lab time is the gap between coursework and a pass.
placeholder: Search — ospf, bgp, mpls, vlan…
unit_group: tracks
unit_card: labs
footer: <b>Rule</b> &nbsp; a lab you cannot rebuild from blank is a lab you have not learned.
title_ar: المختبرات والتطبيق العملي
title_ur: لیبز اور پریکٹس
summary_ar: مخططات EVE-NG التي تم بناؤها وما أثبتته كل واحدة. وقت المختبر هو الفجوة بين الدراسة والنجاح.
summary_ur: EVE-NG ٹوپولوجیز جو بنائی گئیں اور ہر ایک نے کیا ثابت کیا۔ لیب کا وقت کورس ورک اور کامیابی کے درمیان کا فرق ہے۔
---

# LAB & PRACTICE LOG

## Routing | EVE-NG
summary: Core protocol practice. This is where ENCOR and ENARSI get passed.

### OSPF multi-area
- status: Built
- note: areas 0, 1, 2 with a stub and a totally stubby
- Verified LSA types 1 through 5 in the LSDB
- Practised summarisation at the ABR
- master: 44

### BGP eBGP and iBGP
- status: Not built
- priority: high — weakest ENCOR area
- master: 46

### MPLS L3VPN
- status: Not built
- note: final year project was MPLS VPN — rebuild it properly
- master: 48

## Switching | EVE-NG
summary: Layer 2 behaviour under fault conditions.

### STP root election and guards
- status: Built
- Forced root changes with priority, watched reconvergence
- master: 42

### EtherChannel LACP
- status: Not built
- master: 42

## Services | EVE-NG
summary: The supporting protocols that break everything when misconfigured.

### DHCP relay across subnets
- status: Built
- master: 32

### NAT and PAT
- status: Built
- master: 36
