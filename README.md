# CipherPurge
Modern data sanitization software in compliance with NIST SP 800-88 Guidelines


<div align="center">
<h1 align="center">
<img src="https://github.com/DannnyzZ/OSFortify/blob/main/OSFortify_logo_wide.jpg" >
<br>
</h1>
<p align="center">
</p>
 
<p align="center">
  <img src="https://img.shields.io/badge/PowerShell-5391FE.svg?style&logo=PowerShell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/Batch-Script-4EAA25.svg?style=flat&logo=Windows%20Terminal&logoColor=white" alt="Batch Script" />
  <img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/GitHub-007ACC.svg?style=flat&logo=GitHub&logoColor=white" alt="GitHub" />
  <img src="https://img.shields.io/badge/OS%20Hardening-FFA500.svg" alt="OS%20Hardening" />
  <img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
  <img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>


![GitHub license](https://img.shields.io/github/license/eli64s/readme-ai?style&color=5D6D7E)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-4429-25A9E0.svg?style=flat)
![Code Size](https://img.shields.io/badge/Code%20Size-185%20KB-25A9E0.svg?style=flat)
</div>

---


## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [💻 Installation](#-installation)
  - [🎮 Using OSFortify](#-using-OSFortify)
  - [⚠️ Warning](#-warning)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)


---


## 📍 Overview

OSFortify is a sophisticated terminal-based utility designed to enhance system security, streamline operating system hardening, and facilitate efficient system administration. With a focus on cybersecurity, system integrity, and user-friendly interactions, OSFortify empowers users to manage various aspects of their system's services, features, and ports through a secure and organized interface.

The primary **purpose** of OSFortify is to provide an advanced yet accessible tool for users to bolster their system's security posture, elevate operating system hardening, and seamlessly administer critical system functions. By enabling users to interact with their system through a curated selection of options, OSFortify bridges the gap between cybersecurity and user experience.

OSFortify brings robust control to your system's **services, features, and ports**. It allows real-time status checks, seamless activation or deactivation during boot, and dynamic adjustments on-the-fly. With OSFortify, you can finely manage your system's components, optimize resources, and bolster security.


---

## ⚙️ Features

| Feature                | Description                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚡️ Efficient Admininistration** | The program streamlines system administration by offering a user-friendly interface to manage services and features. This enhances operational efficiency by minimizing manual command-line interactions and simplifying routine tasks. |
| **🧩 Modularity** | The program's design demonstrates modularity by organizing functionalities into distinct modules and classes. Each module focuses on specific aspects of system security, administration, and hardening, enhancing maintainability and reusability. |
| **✔️ Secure Execution** | OSFortify emphasizes secure execution of commands and scripts, crucial for system integrity and cybersecurity. It ensures proper progress tracking during script execution and safeguards against unauthorized access. |
| **🔐 Enhanced Security** | OSFortify contributes to enhanced security by enabling users to selectively manage services, features, and ports. This granular control aids in system hardening, mitigating potential vulnerabilities, and bolstering overall cybersecurity measures. |
| **🔌 Flexibility** | The program's dynamic configuration switching and adaptable options provide flexibility to tailor system settings to specific needs. This accommodates various security profiles and allows users to optimize their systems for different scenarios. |
| **📶 Insightful Data** | OSFortify offers users valuable insights into their system's architecture through detailed system information retrieval. This aids decision-making, system understanding, and helps identify potential areas for further optimization. |
| **🔗 Comprehensive Functionality** | OSFortify encompasses a diverse array of essential services, features, and ports, collectively enhancing system security, hardening, and administration. These elements form a critical foundation for a robust and secure computing environment, fortifying against potential threats and vulnerabilities. |
- *Services and Features*
OSFortify encompasses a comprehensive range of essential services and features, including guest user account management, FTP control, oversight of Windows Media Player, and management of USB ports. These functionalities contribute significantly to system security by offering control over potential entry points, data transfers, and media-related threats.
- *Windows Features*
The program covers an array of critical Windows features, including Windows Defender, Windows Firewall, Windows Update, remote management functionalities, and more. By providing control over these features, OSFortify enhances cybersecurity by allowing administrators to fortify defenses, manage remote access, and stay updated against known vulnerabilities.
- *Ports*
OSFortify encompasses an extensive list of important ports, such as SSH (Port 22), HTTPS (Port 443), RDP (Port 3389), and many more. These ports serve as critical communication channels, and their proper management through OSFortify enhances cybersecurity by preventing unauthorized access, securing data transfers, and protecting against potential exploits. |

---

## 🧩 Modules

<details closed><summary>Services</summary>

| Service                                                                   | Details                                                                                                                                                                                                            |
| ---                                                                    | ---                                                                                                                                                                                                                |
| Windows Defender | Protocol: N/A. Function: Antivirus and antimalware tool. Use: System protection. Security: Reliable; ensure regular updates for best protection. |
| Windows Firewall | Protocol: N/A. Function: Filters incoming/outgoing network traffic. Use: Network security. Security: Essential for system protection; configure rules appropriately. |
| Windows Update | Protocol: N/A. Function: Provides system and software updates. Use: System maintenance. Security: Critical for patching vulnerabilities; keep automatic updates on. |
| Windows Remote Registry | Protocol: N/A. Function: Access to system registry remotely. Use: System administration. Security: Risky; disable unless specifically needed. |
| Windows Remote Management | Protocol: TCP. Function: Remote administration tool. Use: System administration. Security: Secure endpoints; restrict access. |
| Windows Management Instrumentation (WMI) | Protocol: N/A. Function: Management infrastructure for Windows. Use: System monitoring and management. Security: Potential target; ensure proper configuration. |
| Remote Desktop Protocol (RDP) | Protocol: TCP/UDP. Function: Remote desktop access. Use: Remote system management. Security: High-risk; enable Network Level Authentication and restrict access. |
| Windows Error Reporting | Protocol: N/A. Function: Sends error reports to Microsoft. Use: Debugging. Security: Minor risk; sensitive info might be sent. |
| Windows Remote Assistance | Protocol: N/A. Function: Remote system help and support. Use: Tech support. Security: Secure sessions; only use with trusted parties. |
| Windows Fax and Scan | Protocol: N/A. Function: Send/receive faxes; scan documents. Use: Office tasks. Security: Ensure secure configurations for fax transmissions. |
| Internet Printing Client | Protocol: N/A. Function: Allows printing over the internet. Use: Remote printing. Security: Ensure secure network and printer configurations. |
| Universal Plug and Play (UPnP) | Protocol: N/A. Function: Automatic device discovery and configuration. Use: Device connectivity. Security: Known vulnerabilities; disable unless needed. |
| Bluetooth | Protocol: N/A. Function: Short-range wireless communication. Use: Device pairing. Security: Vulnerable to "bluejacking"; turn off when not in use. |
| Windows Search | Protocol: N/A. Function: Search tool for files and apps. Use: File and application access. Security: Ensure indexing of sensitive data is restricted. |
| Print Spooler | Protocol: N/A. Function: Manages print tasks. Use: Printing tasks. Security: Known vulnerabilities; update regularly and restrict access. |
| Microsoft IIS | Protocol: TCP. Function: Web server software. Use: Hosting web applications. Security: Regularly update and harden configurations. |
| NetBIOS | Protocol: TCP/UDP. Function: Legacy network support. Use: Windows networking. Security: Known vulnerabilities; restrict or disable. |
| Link-Local Multicast Name Resolution (LLMNR) | Protocol: N/A. Function: Resolves single-label domains. Use: Network operations. Security: Vulnerable to spoofing; consider disabling. |
| Server Message Block Version 1 (SMB1) | Protocol: TCP/UDP. Function: File sharing protocol. Use: Network file sharing. Security: Deprecated due to vulnerabilities; disable. |
| Server Message Block Version 2 (SMB2) | Protocol: TCP/UDP. Function: Updated file sharing protocol. Use: Network file sharing. Security: More secure than SMB1; ensure up-to-date configurations. |
| Telnet | Protocol: TCP. Function: Remote command-line access. Use: Remote system administration. Security: Unencrypted; use SSH as a more secure alternative. |

</details>

<details closed><summary>Features</summary>

| Feature                                                                     | Details                                                                                                                                                                                                                                               |
| ---                                                                      | ---                                                                                                                                                                                                                                                   |
| Guest user account | Protocol: N/A. Function: Provides limited access to a system without a personalized login. Use: Temporary or restricted access. Security: Risky; can be exploited if not properly restricted. |
| File Transfer Protocol (FTP) | Protocol: TCP. Function: Protocol for transferring files over a network. Use: File sharing and download/upload. Security: Unencrypted; use FTPS or SFTP for secure transfers. |
| Windows Media Player | Protocol: N/A. Function: Media player for viewing/hearing media files. Use: Multimedia playback. Security: Vulnerabilities may arise from codecs/plugins; ensure updates. |
| USB ports | Protocol: N/A. Function: Interface for connecting external devices. Use: Data transfer, device charging, peripheral connections. Security: Potential for malicious device connections or data theft; use device controls. |

</details>

<details closed><summary>Ports</summary>

| Port                                                                               | Details                                                                                                                                                                                                                                                                                                           |
| ---                                                                                | ---                                                                                                                                                                                                                                                                                                                     |
| Port 7 - Echo | *Protocol*: TCP/UDP. *Function*: Returns received data (echoes back). *Use*: Network testing. *Security*: Risky; often disabled or blocked due to potential exploits. |
| Port 20 - File Transfer Protocol (FTP) | Protocol: TCP. Function: Transfers files (data channel). Use: File sharing. Security: Use with caution; encrypted alternatives recommended. |
| Port 21 - File Transfer Protocol Control | Protocol: TCP. Function: Command channel for FTP. Use: File sharing control. Security: Use with caution; encrypted alternatives recommended. |
| Port 22 - Secure Shell (SSH) | Protocol: TCP. Function: Secure remote login and command execution. Use: Secure system management. Security: Highly secure; ensure strong keys and passwords. |
| Port 23 - Telnet | Protocol: TCP. Function: Remote login (plaintext). Use: Remote system management. Security: Risky; use SSH instead due to lack of encryption. |
| Port 25 - Simple Mail Transfer Protocol (SMTP) | Protocol: TCP. Function: Email transmission. Use: Mail servers. Security: Vulnerable to spam and misuse; ensure proper configurations. |
| Port 37 - Time | Protocol: TCP/UDP. Function: Provides system time. Use: Synchronizing system clocks. Security: Generally low risk; ensure only trusted sources are used. |
| Port 53 - Domain Name System (DNS) | Protocol: TCP/UDP. Function: Translates domain names to IP addresses. Use: Web browsing, app connectivity. Security: Risk of DNS spoofing; use DNSSEC where possible. |
| Port 69 - Trivial File Transfer Protocol (TFTP) | Protocol: UDP. Function: File transfers (simpler than FTP). Use: Often for network devices, firmware updates. Security: No authentication; use in secure environments only. |
| Port 80 - Hyper Text Transfer Protocol (HTTP) | Protocol: TCP. Function: Transfers web pages. Use: Web browsing. Security: Unencrypted; HTTPS (Port 443) is more secure. |
| Port 110 - Post Office Protocol 3 (POP3) | Protocol: TCP. Function: Retrieves email from a mail server. Use: Email clients. Security: Unencrypted; secure alternatives available (e.g., POP3S). |
| Port 111 - Remote Procedure Calls (RPC) | Protocol: TCP/UDP. Function: Executes remote commands. Use: Distributed systems. Security: Vulnerable if not properly secured; risk of DDoS and unauthorized access. |
| Port 123 - Network Time Protocol (NTP) | Protocol: UDP. Function: Synchronizes system clocks. Use: Clock synchronization. Security: Exploitable if misconfigured; use authenticated mode. |
| Port 135 - Microsoft Remote Procedure Call (MSRPC) | Protocol: TCP. Function: Executes remote procedures. Use: Microsoft distributed applications. Security: Risky; should be firewalled in untrusted environments. |
| Port 137 - Server Message Block (SMB) | Protocol: TCP/UDP. Function: Provides shared access to files, printers, etc. Use: File and printer sharing in Windows networks. Security: Vulnerable to various attacks; secure configurations and recent versions are essential. |
| Port 139 - Server Message Block/NetBIOS Session Service (SMB/NetBIOS-SSN) | Protocol: TCP. Function: Facilitates file, printer, and other shared resource access. Use: Windows networking. Security: Risk of unauthorized access; should be firewalled in untrusted environments. |
| Port 143 - Internet Message Access Protocol (IMAP) | Protocol: TCP. Function: Accesses email messages on a remote server. Use: Email clients. Security: Unencrypted; secure version IMAPS (Port 993) recommended. |
| Port 161 - Simple Network Management Protocol (SNMP) | Protocol: UDP. Function: Monitors and manages network devices. Use: Network management. Security: Versions prior to SNMPv3 lack encryption and are insecure. |
| Port 162 - Simple Network Management Protocol Trap (SNMP Trap) | Protocol: UDP. Function: Notification from network devices about specific conditions. Use: Network management. Security: Ensure filtering and proper configurations to avoid misuse. |
| Port 389 - Lightweight Directory Access Protocol (LDAP) | Protocol: TCP. Function: Accesses and maintains directory services. Use: Directory operations. Security: Unencrypted; use LDAPS (Port 636) for secure connections. |
| Port 443 - HTTP Secure (HTTPS) | Protocol: TCP. Function: Transfers encrypted web pages. Use: Secure web browsing. Security: Encrypted; ensure valid certificates for authenticity. |
| Port 445 - Microsoft-DS (Directory Services) SMB/Active Directory | Protocol: TCP. Function: Access to shared resources like files and printers. Use: Windows networking and domain services. Security: Potential target for ransomware and other attacks; secure appropriately. |
| Port 636 - Secure Lightweight Directory Access Protocol (SLDAP) | Protocol: TCP. Function: Accesses and maintains encrypted directory services. Use: Directory operations. Security: Encrypted; offers secure alternative to LDAP. |
| Port 993 - Internet Message Access Protocol Secure (IMAPS) | Protocol: TCP. Function: Accesses email messages securely on a remote server. Use: Secure email clients. Security: Encrypted; preferred over IMAP. |
| Port 995 - Post Office Protocol 3 Secure (POP3S) | Protocol: TCP. Function: Secure retrieval of email from a server. Use: Secure email clients. Security: Encrypted; preferred over POP3. |
| Port 989 - FTP over TLS/SSL (FTPS data) | Protocol: TCP. Function: Encrypted data channel for FTP. Use: Secure file sharing. Security: Encrypted; safer than regular FTP. |
| Port 990 - FTP over TLS/SSL (FTPS control) | Protocol: TCP. Function: Command channel for encrypted FTP. Use: Secure file sharing control. Security: Encrypted; safer than regular FTP. |
| Port 1433 - Microsoft SQL Server | Protocol: TCP. Function: SQL Server database access. Use: Database operations. Security: Potential target for attacks; firewall and restrict access. |
| Port 1434 - Microsoft SQL Server Browser Service | Protocol: UDP. Function: Provides info about SQL Server instances. Use: Database operations. Security: Limit exposure; can reveal sensitive info. |
| Port 1723 - Point-to-Point Tunneling Protocol (PPTP) | Protocol: TCP. Function: VPN tunnel creation. Use: VPNs. Security: Vulnerabilities known; consider more secure VPN protocols. |
| Port 1812 - RADIUS Authentication | Protocol: UDP. Function: Remote user authentication. Use: VPNs, networking. Security: Ensure secure configurations and strong encryption. |
| Port 1813 - RADIUS Accounting | Protocol: UDP. Function: Tracks resources usage of remote users. Use: VPNs, networking. Security: Ensure data integrity and confidentiality. |
| Port 3268 - Global Catalog Service | Protocol: TCP. Function: Directory service for AD domains. Use: Microsoft AD. Security: Ensure proper configurations for AD environment. |
| Port 3269 - Secure Global Catalog Service | Protocol: TCP. Function: Directory service for AD domains over SSL. Use: Microsoft AD. Security: Encrypted; ensure valid certificates. |
| Port 3389 - RDP/MS-WBT-server | Protocol: TCP/UDP. Function: Remote desktop access. Use: Remote system management. Security: High-risk; enable Network Level Authentication and restrict access. |
| Port 5060 - SIP (Non-encrypted) | Protocol: TCP/UDP. Function: Initiates/modifies VoIP calls. Use: VoIP services. Security: Unencrypted; risks of eavesdropping. |
| Port 5061 - SIP over TLS (Encrypted) | Protocol: TCP/UDP. Function: Secure VoIP call initiation. Use: Secure VoIP services. Security: Encrypted; preferred over non-encrypted SIP. |
| Port 5190 - AOL | Protocol: TCP. Function: Online services and instant messaging. Use: Communication. Security: Ensure latest software versions; avoid untrusted content. |
| Port 5631 - Symantec pcAnywhere (data) | Protocol: TCP. Function: Remote desktop data transfer. Use: Remote system access. Security: Ensure secure configurations and updates. |
| Port 5632 - Symantec pcAnywhere (status) | Protocol: UDP. Function: Remote desktop status communication. Use: Remote system access. Security: Ensure secure configurations and updates. |
| Port 5800 - VNC over HTTP | Protocol: TCP. Function: Web-based remote desktop access. Use: Remote system management. Security: Use strong passwords and consider tunneling over SSL. |
| Port 5900 - VNC Standalone | Protocol: TCP. Function: Remote desktop access. Use: Remote system management. Security: Risky; use strong passwords and restrict access. |
| Port 8080 - HTTP Proxy | Protocol: TCP. Function: Alternative port for web services. Use: Web applications, proxies. Security: Regularly monitor and restrict to known users. |

</details>

---

## 🚀 Getting Started

<div align="center">
  <img src="https://github.com/DannnyzZ/OSFortify/assets/119814239/ae897cfc-2a04-4dc8-a691-1c109f861c46" alt="gui_screen">
</div>


### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

>  ` Windows 8/10/11`

>  ` Python`

>  ` Python Package Installer `

>  ` Python library: curses `

>  ` Python library: tkinter `

>  ` Internet connection `

### 💻 Installation

1. Install python
```sh
1.	Visit the official Python website: https://www.python.org/downloads/
2.	Go to the Downloads section and choose the version of Python you want to install (e.g., Python 3.9.6).
3.	Scroll down to the bottom of the page and select the installer that matches your system architecture (32-bit or 64-bit).
4.	Run the downloaded installer.
5.	In the installer, select the option to add Python to the system PATH, which will make it accessible from the command line.
6.	Make sure that in optional features you choose pip to be installed.
7.	Complete the installation by following the on-screen instructions.
```

2. Install dependencies
```sh
pip install pip & pip install tk windows-curses
```

3. Check version of python and pip:
```sh
python --version && pip --version
```

### 🎮 Using OSFortify

1. Run Powershell as administrator.
2. Download osfortify.py from this link:
```sh
https://github.com/DannnyzZ/OSFortify/blob/main/osfortify
```
4. Execute:
```sh
python osfortify.py
```
3. WARNING! Make sure You provide the correct location of OSFortify.
4. Example of use:
```sh
python C:\Users\Danny\Desktop\osfortify.py
```

---


### ⚠️ Warning


**Using OSFortify Safely:**

1. Knowledge is Key: Understand changes' impact on security and stability.

2. Caution and Expertise: Modify with care, avoid vulnerabilities or data loss.

3. Backup Always: Prioritize system backups to ensure recovery options.

4. Authorized Access: Limit OSFortify access to knowledgeable personnel.

5. Controlled Testing: Experiment in safe environments before implementing changes.

6. Secure Scripts: Verify PowerShell scripts before execution.

**Use OSFortify wisely to enhance security while minimizing risks.**

## 🗺 Roadmap

> - [X] ` Task 1: Multiple bug fixes`
> - [X] ` Task 2: New features: tidy and colored output`

> - [ ] ` Incoming feature 1: Exporting results to PDF file`
> - [ ] ` Incoming feature 2: New services: HDMI, Mini-Jack, DVI, CD-DVD, CTRL+ALT+DEL on login prompt, Trivial File Transfer Protocol`
> - [ ] ` Incoming feature 3: One button evaluation of security state (Risk analysis)`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `NEW_FIX`).
```sh
git checkout -b NEW_FIX
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Applied changes.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin NEW_FIX
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  MIT` License. 

---

## 👏 Acknowledgments

  `ℹ️  Stack Overflow`
   
  `ℹ️  ChatGPT 4.0`
   
  `ℹ️  Readme-ai https://github.com/eli64s/readme-ai`

  `ℹ️  Logo.com https://logo.com`
  

---
