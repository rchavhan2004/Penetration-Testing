# Penetration-Testing-Toolkit

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : ROHIT CHAVHAN

**INTERN ID** : CT08JJO

**DOMAIN** : Cyber-Security & Ethical Hacking

**BATCH DURATION** : JANUARY 5th,2025 to FEBRUARY 5th,2025

**MENTOR NAME** : NEELA SANTHOSH KUMAR


## DESCRIPTION :
This project is a Python-based toolkit designed to perform basic penetration testing tasks. The toolkit consists of four main modules, each serving a specific purpose to test and gather information about network security.

## Features
- User-friendly CLI-based interaction.
- Error handling for invalid inputs and network-related issues.
- Modular design for easy maintenance and extension.

## Modules

### 1. Port Scanner
- **Task**: Scans a target IP address for open ports within a specified range.
- **Description**: The tool attempts to connect to each port in the given range using the `socket` library. If the connection is successful, the port is identified as open and displayed in the output. This module helps in identifying services running on the target system.

### 2. FTP Brute Forcer
- **Task**: Attempts to brute-force login credentials for an FTP server.
- **Description**: Using the `ftplib` library, this module tries multiple passwords for a specified username on a target FTP server. It reports successful login attempts or indicates failure after exhausting all possibilities. This helps test the strength of FTP credentials.

### 3. HTTP Header Scanner
- **Task**: Retrieves and displays HTTP headers from a specified URL.
- **Description**: This module sends a GET request to a target URL using the `requests` library and prints the HTTP headers in the response. It helps in gathering information about the target server, such as server type, content type, security headers, etc.

### 4. Ping Module
- **Task**: Sends ICMP echo requests (ping) to a target to test connectivity.
- **Description**: This module executes the `ping` command via the `subprocess` library to determine if a target system is reachable. It reports the results of the ping operation, including packet loss and response time.

