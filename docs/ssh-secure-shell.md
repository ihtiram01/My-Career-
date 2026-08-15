---
title: SSH — Secure Shell
description: Encrypted remote access to a device command line. Replaces Telnet.
page: ssh-secure-shell
order: 20
colour: red
kicker: 63.14 · Layer 60–69 Security & Firewall → Device access
summary: Encrypted remote access to a device's command line. Replaces Telnet, which sends everything — including your password — in clear text.
placeholder: Search — host key, tunnel, stelnet, sshd_config, known_hosts…
unit_group: blocks
unit_card: sections
footer: <b>ID</b> &nbsp; <code>63.14</code> · Type <code>X</code> Config · Sources [CCNA] [MCSE] [Wemart] [ZTE-RIY1] · Level L3 · Updated 14 Aug 2026 &nbsp;&nbsp; <b>Standard</b> &nbsp; written to the thirteen-block topic page standard.
---

# SSH — SECURE SHELL

## 1 · What SSH is | block 02
summary: Plain language first. SSH is a protocol that gives you a secure channel over an insecure network — you type on your laptop, the characters travel encrypted, the switch or server executes them, and the output comes back encrypted.

### The three guarantees
- Confidentiality — anyone capturing the traffic sees ciphertext, not your password
- Integrity — if a packet is altered in transit, the session detects it and drops
- Authentication — you prove who you are to the server, and the server proves who it is to you
- note: that last one matters more than people think. Encryption alone is useless if you encrypted your password straight to an attacker.
- master: 63, 37

## 2 · Why it exists | block 03
summary: In 1995 Tatu Ylönen, a researcher at Helsinki University of Technology, found that someone had run a password sniffer on the university network and harvested thousands of credentials. Everyone used Telnet, rlogin and rsh — all clear text. He wrote SSH-1 as the fix.

### Timeline
- 1995 — Ylönen writes SSH-1 after a sniffing attack; released as freeware in July
- 1995 — SSH Communications Security founded; the product becomes commercial
- 1996 — SSH-2 published: new key exchange, proper integrity checking. Not backward compatible with SSH-1
- 1998 — the CRC-32 compensation attack breaks SSH-1's integrity model
- 1999 — the OpenBSD team forks a free branch into OpenSSH, now the dominant implementation
- 2006 — IETF standardises SSH-2 in RFC 4251–4254
- 2021 — OpenSSH 8.8 disables `ssh-rsa` (SHA-1 signatures) by default
- note: SSH-1 is dead. It is broken, not merely old. Anything still offering `ip ssh version 1` should be moved to version 2 or replaced.

### The RFCs
- RFC 4250 — assigned numbers
- RFC 4251 — architecture, the three-layer model
- RFC 4252 — authentication protocol
- RFC 4253 — transport layer protocol
- RFC 4254 — connection protocol: channels, forwarding
- RFC 4256 — keyboard-interactive authentication
- RFC 4419 — Diffie-Hellman group exchange
- RFC 5656 — elliptic curve algorithms
- RFC 8332 — rsa-sha2-256 / rsa-sha2-512
- RFC 8709 — Ed25519 and Ed448 keys

## 3 · Where it sits | block 04
summary: Application layer protocol riding on TCP port 22, client–server model. The device you connect to runs the SSH server; the device you connect from runs the SSH client.

### Position
- Transport — TCP, port 22. Ylönen picked 22 because it sat free between Telnet (23) and FTP (21); IANA assigned it to him
- Model — client–server
- Layer — application layer, riding on TCP
- note: the client/server split trips people up on network kit. A switch can be a perfectly good SSH server and have no SSH client at all — see the field note in section 10.

### The three internal layers, RFC 4251
- Transport layer (RFC 4253) — key exchange, server authentication, encryption, integrity, compression
- User authentication layer (RFC 4252) — proves who the client is
- Connection layer (RFC 4254) — multiplexes the encrypted tunnel into channels: shell, exec, forwarded ports, SFTP
- note: one TCP connection carries many channels. That is why you can run a shell, copy a file and forward a port over a single SSH session.

## 4 · SSH versus Telnet | block 04
summary: The comparison that ends the argument. Open a Telnet session in Wireshark, follow the TCP stream, and the password is sitting there in plain characters.

### Side by side
- Port — Telnet 23, SSH 22
- Encryption — Telnet none, clear text; SSH yes
- Password on the wire — Telnet readable in Wireshark; SSH encrypted
- Server authentication — Telnet none; SSH host key
- Integrity check — Telnet none; SSH a MAC on every packet
- File transfer — Telnet no; SSH SCP and SFTP
- Port forwarding — Telnet no; SSH yes
- Use in production — Telnet never; SSH standard
- master: 37

## 5 · How a connection actually happens | block 05
summary: In order, every time. Steps 4 and 5 are the ones people conflate — key exchange protects the data, host key verification protects you from talking to the wrong box. Different jobs, different keys.

### The nine steps
- 1 — TCP handshake: client opens TCP 22
- 2 — version exchange: both sides send a banner such as `SSH-2.0-OpenSSH_9.6`. If either only speaks SSH-1, negotiation stops here
- 3 — algorithm negotiation (KEXINIT): each side sends its supported lists in preference order — key exchange, host key types, ciphers, MACs, compression. The first mutual match in the client's order wins
- 4 — key exchange: usually ECDH (`curve25519-sha256`). Both sides derive the same shared secret without it ever crossing the wire
- 5 — server authentication: the server signs the exchange hash with its host key. The client checks that signature against `known_hosts`
- 6 — NEWKEYS: both sides switch on encryption. Everything after this point is ciphertext
- 7 — service request: client asks for `ssh-userauth`
- 8 — user authentication: publickey, password, or keyboard-interactive
- 9 — channel open: client requests a channel, then shell, exec, or subsystem sftp. Now you have a prompt
- note: `no matching key exchange method found` comes from step 3 — the two algorithm lists do not intersect.
- note: step 4 is the heart of SSH. An eavesdropper who captured every packet still cannot compute the key.

## 6 · Subtopics | block 06
summary: Every child concept, each with its own section. Nothing left as "etc".

### 6.1 Symmetric versus asymmetric
- Asymmetric (public/private) is used for key exchange, authentication and signatures — Ed25519, RSA, ECDSA. Slow. Setup only
- Symmetric (shared secret) encrypts the actual session data — AES-256-GCM, ChaCha20-Poly1305. Fast. Every packet after NEWKEYS
- note: asymmetric crypto is used briefly to agree a symmetric key, then symmetric crypto does the heavy lifting. Asymmetric is far too slow to encrypt a whole session.

### 6.2 Host keys
- The server's own identity key pair, generated once at first boot and stored in `/etc/ssh/ssh_host_*`
- Clients cache the public half in `~/.ssh/known_hosts`
- First connection — you are shown a fingerprint and asked to trust it. This is the one moment you are exposed to MITM; verify out of band on anything that matters
- Key changed — `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!` means either the box was rebuilt, or someone is intercepting
- action: do not blindly delete the known_hosts line until you know which of the two it is.

### 6.3 Session keys
- Derived from the shared secret
- Separate keys each direction, plus separate keys for encryption and integrity
- Rehashed periodically — OpenSSH rekeys after roughly 1 GB or 1 hour
- note: rekeying means a compromised key exposes only a slice of the session.

### 6.4 Algorithms in current use
- Key exchange — prefer `curve25519-sha256`, `diffie-hellman-group16-sha512`; avoid `diffie-hellman-group1-sha1`
- Host key — prefer `ssh-ed25519`, `rsa-sha2-512`; avoid `ssh-rsa` (SHA-1) and `ssh-dss`
- Cipher — prefer `chacha20-poly1305`, `aes256-gcm`, `aes256-ctr`; avoid `3des-cbc`, `arcfour`, any `-cbc`
- MAC — prefer `hmac-sha2-256`, `umac-128-etm`; avoid `hmac-md5`, `hmac-sha1`

### 6.5 Authentication methods
- `password` — password sent inside the encrypted tunnel. Common on network kit, weakest
- `publickey` — client signs a challenge with its private key. Best practice
- `keyboard-interactive` — server prompts, client answers. Carries MFA/OTP
- `gssapi-with-mic` — Kerberos, for AD domains
- `hostbased` — the whole host is trusted. Rare
- Certificates — a CA signs user and host keys, removing known_hosts sprawl. For large estates
- master: 63.11, 35.02

### 6.6 Key management
- Generate — `ssh-keygen -t ed25519 -C "ihtiram@laptop"`. Ed25519 is small, fast and strong. Use `-t rsa -b 4096` only where Ed25519 is unsupported
- Passphrase — encrypts the private key at rest. Use one. `ssh-agent` stops it being retyped constantly
- Install — `ssh-copy-id user@host` appends your public key to the server's `~/.ssh/authorized_keys`
- Permissions — `~/.ssh` must be 700, `authorized_keys` and private keys 600
- Formats — OpenSSH (`id_ed25519`), PEM/PKCS#8, and PuTTY `.ppk`. Convert with PuTTYgen or `ssh-keygen -p -m PEM`
- note: loose permissions make sshd silently refuse the key. That is a classic "publickey denied" cause.

### 6.7 Port forwarding and tunnelling
- `-L 8080:10.0.0.5:80` — local forward. Your port 8080 reaches remote-side 10.0.0.5:80. Use this to reach a device you cannot route to
- `-R 9000:localhost:22` — remote forward. The server's port 9000 comes back to your machine. Reverse access
- `-D 1080` — dynamic. A local SOCKS proxy, all traffic through the SSH host
- `-J user@jump` — jump host. Hop through a bastion in one command
- `-X` — forwards a graphical X11 application
- note: local forwarding is the one you will use on site — your laptop cannot reach the management VLAN, but the jump box can.

### 6.8 File transfer
- `scp file user@host:/path` — simple copy. Legacy protocol, deprecated in favour of SFTP
- `sftp user@host` — interactive, resumable, proper file operations
- `rsync -avz -e ssh src/ user@host:/dst/` — transfers only differences. Best for large or repeated copies

## 7 · Vendor configuration, command by command | block 07
summary: Real syntax per vendor, every line explained. Cisco and Huawei are not interchangeable — verify against the vendor before writing.

### 7.1 Cisco IOS / IOS-XE
- `hostname SW-CORE-01` — required. The RSA key name is derived from hostname plus domain, and a default hostname blocks key generation
- `ip domain-name gulfnet.local` — same reason. Together these form the FQDN the key is bound to
- `crypto key generate rsa modulus 2048` — creates the host key pair. This is the command that actually enables the SSH server. 2048 minimum; 512 and 1024 are too weak
- `ip ssh version 2` — forces SSH-2 only and refuses broken SSH-1
- `username admin privilege 15 secret <StrongPassword>` — local account. `secret` is hashed; `password` is reversible, never use it
- `line vty 0 4` — the virtual terminal lines that accept remote sessions
- `transport input ssh` — accept SSH only. Omitting this leaves Telnet open and the whole exercise pointless
- `login local` — authenticate against the local user database
- `exec-timeout 5 0` — idle sessions disconnect after 5 minutes
- master: 28.01, 63.01

### 7.1b Cisco hardening and verification
- `ip ssh time-out 60` — seconds allowed to complete login
- `ip ssh authentication-retries 3` — failed attempts before the connection drops
- `ip ssh source-interface Loopback0` — sources outbound SSH from a stable interface
- `show ip ssh` — confirms version and settings
- `show ssh` — lists active sessions
- `ssh -l admin 10.0.0.5` — Cisco's own client, from the device

### 7.2 Huawei VRP
- `sysname SW-ACCESS-01` — sets the device name
- `rsa local-key-pair create` — generates the host key. Prompts for modulus; choose 2048. Huawei's equivalent of Cisco's `crypto key generate rsa`
- `stelnet server enable` — STelnet is Huawei's name for SSH. This starts the SSH server
- `ssh user admin authentication-type password` — sets how this SSH user authenticates. Can be `password`, `rsa`, `password-rsa` or `all`
- `ssh user admin service-type stelnet` — permits this user to open SSH shell sessions, as opposed to SFTP only
- `local-user admin password irreversible-cipher <StrongPassword>` — stores the password as a non-reversible hash. `cipher` is reversible, avoid it
- `local-user admin privilege level 15` — full administrative rights
- `local-user admin service-type ssh` — allows the account to be used for SSH
- `user-interface vty 0 4` — the VTY lines
- `authentication-mode aaa` — VTY lines authenticate via the AAA database
- `protocol inbound ssh` — SSH only on those lines
- master: 28.05, 63.11

### 7.2b Huawei client side and verification
- `stelnet 10.10.10.230` — Huawei's SSH client command. It is not `ssh`
- `stelnet -l admin 10.10.10.230` — specifies the username inline
- `ssh client first-time enable` — allows connecting to a server whose key is not yet trusted
- `display ssh server status` — confirms the server is running
- `display ssh user-information` — lists configured SSH users

### 7.3 Juniper Junos
- `set system host-name SW-EDGE-01` — device name
- `set system services ssh` — enables the SSH server. Host keys are generated automatically on first commit
- `set system services ssh protocol-version v2` — SSH-2 only
- `set system services ssh root-login deny` — blocks direct root login. Log in as a user and elevate
- `set system login user admin class super-user` — Junos permission class, equivalent to privilege 15
- `set system login user admin authentication plain-text-password` — sets the password interactively
- `commit` — nothing takes effect until commit. Junos is candidate-config based
- note: this block is from documentation, not from a device configured personally. See section 13.

### 7.4 Linux — OpenSSH server
- `Port 22` — change if you like. Moving it stops noise, not a real attacker
- `PermitRootLogin no` — force named accounts so actions are attributable
- `PasswordAuthentication no` — kills brute force outright. Set up keys first
- `PubkeyAuthentication yes` — key-based auth
- `AllowUsers ihtiram admin` — a whitelist. Everyone else is refused before authentication
- `MaxAuthTries 3` — attempts per connection
- `ClientAliveInterval 300` — probes idle clients
- `ClientAliveCountMax 2` — drops after 2 unanswered probes
- `X11Forwarding no` — off unless needed
- `LogLevel VERBOSE` — logs the key fingerprints used to log in. Essential for audit
- master: 83.02

### 7.4b Linux — applying it safely
- `sudo sshd -t` — test the config before restarting
- `sudo systemctl restart sshd` — apply
- `sudo systemctl status sshd` — confirm running
- `sudo journalctl -u sshd -f` — live logs
- action: run `sshd -t` first, always. A typo plus a restart on a remote box locks you out. Keep a second session open while changing sshd_config.

### 7.5 Windows — OpenSSH Server
- `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0` — installs the OpenSSH server feature, which is not present by default
- `Start-Service sshd` — starts it now
- `Set-Service -Name sshd -StartupType 'Automatic'` — survives reboot. Miss this and it stops after a restart
- `Get-NetFirewallRule -Name *ssh*` — checks whether the installer added the firewall rule
- `New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22` — adds it manually if not
- Config lives at `C:\ProgramData\ssh\sshd_config` and uses the same directives as Linux
- master: 21, 24

## 8 · GUI paths | block 08
summary: Where a GUI exists, the click path — Windows optional features, PuTTY, PuTTYgen and PuTTY tunnels.

### Windows — install without PowerShell
- Settings → Apps → Optional features → Add a feature
- Search OpenSSH Server → Install
- Then Services (`services.msc`) → OpenSSH SSH Server → Startup type Automatic → Start

### PuTTY — connect
- Host Name field → device IP
- Port 22 · Connection type SSH → Open
- note: the first connection shows the host key fingerprint. Accept only if it is what you expected.

### PuTTY — key authentication
- PuTTYgen → Generate → move the mouse → Save private key (`.ppk`)
- Copy the public key text into the server's `authorized_keys`
- In PuTTY: Connection → SSH → Auth → Credentials → browse to the `.ppk`
- Save the session so it persists

### PuTTY — tunnel
- Connection → SSH → Tunnels
- Source port 8080, Destination `10.0.0.5:80` → Add → Open
- note: this is the same thing as `-L` on the command line.

## 9 · Troubleshooting | block 09
summary: Symptom, cause, fix. The one diagnostic that settles most of it is ssh -vvv, whose three levels of verbosity show exactly which step failed — algorithm negotiation, host key, or authentication.

### Connection will not open
- `Connection refused` — server not running, or nothing listening on 22. Check the service status, then `ss -tlnp | grep 22`
- `Connection timed out` — routing or a firewall/ACL drop. Ping first: timeout means a path problem, refused means you reached the host
- note: refused and timed out are different diagnoses. Do not treat them as the same fault.
- master: 49.01

### Authentication fails
- `Permission denied (publickey)` — key not in `authorized_keys`, or file permissions wrong. `~/.ssh` 700, `authorized_keys` 600, owned by the user
- `Permission denied, please try again` — password wrong, or the user is not permitted. Check `AllowUsers`, and the account's `service-type` on network kit
- `Host key verification failed` — the host key changed. Verify why; if legitimate, `ssh-keygen -R <host>`

### Algorithm and version mismatches
- `no matching key exchange method found` — old device, modern client. `ssh -oKexAlgorithms=+diffie-hellman-group14-sha1 user@host`, then plan to upgrade the device
- `no matching host key type found` — the device only offers `ssh-rsa`. `-oHostKeyAlgorithms=+ssh-rsa` as a temporary measure
- note: both of these are workarounds, not fixes. They keep you working today and should trigger an upgrade ticket.

### Session behaviour
- `Command not found: stelnet` — the Huawei image lacks the SSH client. See section 10
- Session drops when idle — idle timeout. `ClientAliveInterval`, or `exec-timeout` on Cisco
- Slow login, then works — reverse DNS lookup timing out. Set `UseDNS no` in sshd_config

## 10 · Field notes | block 10
summary: What actually happened on site. Real device models, real limitations — the part that cannot be copied from a vendor guide.

### Huawei S5735S — no SSH client in the image
- Device — Huawei S5735S-L24P4S-A2, VRP V200R022C00SPC500
- Attempted to hop from a management switch to an isolated group of access switches on the same site
- `stelnet` was not a recognised command on the source device
- `ssh client first-time enable` was accepted, but the client itself is not in this model's base software package
- The switch works perfectly as an SSH server and cannot act as an SSH client
- note: consequence — no SSH hop was possible, Telnet was refused at the far end, and the only real fix was physical console access at the remote cabinet.
- action: before promising a remote fix on that platform, confirm the image actually carries a client. Ping succeeding from the switch proves reachability, not manageability.

### The rule that came out of it
- If ping works but `stelnet` is not recognised, the problem is the local device's image, not the remote device
- note: this inverts the usual instinct, which is to start troubleshooting the far end.
- master: 28.05, 28.10

## 11 · Assets | block 11
summary: Downloads and screenshots. Files live in files/ so the browser downloads rather than renders them; screenshots live in img/ssh/ and are listed here until the PNGs exist.

### Documents
- `SSH — CCNP edition` — PDF, 12 pages · `/files/SSH-CCNP.pdf`
- `SSH — Zero to CCIE` — PDF, 25 pages · `/files/SSH-Zero-to-CCIE.pdf`
- `Page images, 200 dpi` — ZIP, 25 × PNG at 1654×2339 · `/files/SSH-Zero-to-CCIE-HD-images.zip`

### Screenshots to add under /img/ssh/
- `wireshark-telnet-cleartext.png` — Telnet password visible in a TCP stream
- `wireshark-ssh-encrypted.png` — the same login, encrypted
- `cisco-show-ip-ssh.png` — verification output
- `huawei-display-ssh-server.png` — verification output
- `putty-tunnel-config.png` — the Tunnels dialog
- note: this is a checklist, not live image tags. Nothing renders broken, and nothing becomes an image tag until the PNG actually exists.

## 12 · Cross-references | block 12
summary: Sibling topics by ID. Every placeholder in the draft resolved to a real entry in the index — none were left unassigned.

### Related topics
- `37.07` Telnet vs SSH — what SSH replaced. The page pair
- `63.11` AAA on network devices — where `authentication-mode aaa` leads
- `35.02` RADIUS vs TACACS+ — the protocols behind that AAA
- `28.01` Cisco IOS modes and config hierarchy — the CLI these commands are typed into
- `28.10` Console, AUX and out-of-band access — what you fall back to when SSH is not possible
- `63.01` Password policy, privilege levels, role-based CLI — VTY lines and privilege levels
- `63.02` SSH hardening, disable telnet/HTTP — the hardening subset of this topic
- `49.01` Standard versus extended ACLs — restricting which sources may reach port 22
- `83.02` Centralized syslog server — where `LogLevel VERBOSE` output should land
- master: 37.07, 63.11, 35.02, 28.01, 28.10, 63.01, 63.02, 49.01, 83.02

## 13 · Verification | block 13
summary: Sources, what is confirmed, and what is explicitly not tested. A page that quietly presents untested config as fact is worse than a shorter page.

### Sources
- RFC 4251–4254, RFC 8332, RFC 8709
- Cisco IOS, Huawei VRP and Juniper Junos configuration guides
- OpenSSH manual pages
- Own field troubleshooting on site

### Confirmed
- All vendor syntax verified per platform
- History dates and RFC numbers checked
- The Huawei S5735S client limitation was observed directly on the device

### Not tested by me
- gap: the Juniper block is from documentation, not from a device I have configured
- gap: Windows OpenSSH server was tested on Windows Server 2022 only
- gap: certificate-based SSH is documented here but is not deployed anywhere in my own estate

### Accuracy note
- An AI-generated SSH guide compared against this one contained a misspelled cover, an incorrect layer stack, wrong key-generation syntax, reversed asymmetric key roles, backwards tunnelling diagrams and garbled VRP syntax
- note: verify vendor syntax against the vendor, always.
