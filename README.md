# Port Scanner

A basic TCP port scanner written in Python.  
This tool attempts to connect to a range of ports on a target host and reports which ports are open.

**Internship ID:** `CITS6344`

---

## Features
- Scans TCP ports using a full TCP connect scan
- Hostname to IP resolution
- Customisable port ranges
- Lightweight and easy to use
- Clean command-line output with timestamps

---

## Usage

```bash
python3 port_scanner.py <target> [start_port] [end_port]
