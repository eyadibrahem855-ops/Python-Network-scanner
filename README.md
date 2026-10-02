# Multithreaded Python Network Scanner 🛡️

A high-performance, multithreaded CLI network security scanner built with Python. Designed for rapid open-port detection, service banner grabbing, and dynamic reporting.

## 🚀 Features

- **Concurrent Multi-Threading:** Employs Python's `threading` and `queue` modules to scan dozens of ports simultaneously.
- **Service Banner Grabbing:** Identifies service versions and network banners on exposed open ports.
- **Custom Port Ranges:** Accepts dynamic target IPs/domains and custom user-defined port ranges.
- **Automated Report Generation:** Automatically exports clean, timestamped scan findings to `scan_report.txt`.
- **Robust Exception Handling:** Implements socket timeouts and error handling for invalid input and connection drops (`gaierror`).

## 🛠️ Tech Stack

- **Language:** Python 3
- **Core Modules:** `socket`, `threading`, `queue`, `datetime`

## 💻 Usage Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-Network-Scanner.git
   cd Python-Network-Scanner