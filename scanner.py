import socket
import threading
from queue import Queue
from datetime import datetime

# 1. استقبال مدخلات المستخدم
target_input = input("Enter Target IP or Domain: ")
target = target_input.strip()

try:
    start_port = int(input("Enter Start Port (e.g., 1): "))
    end_port = int(input("Enter End Port (e.g., 100): "))
except ValueError:
    print("[!] Invalid port number. Defaulting to 1-100.")
    start_port, end_port = 1, 100

print(f"\n{'='*50}")
print(f"[*] Starting Scan on Target: {target}")
print(f"[*] Time Started: {str(datetime.now())}")
print(f"{'='*50}\n")

print_lock = threading.Lock()
port_queue = Queue()
open_ports = []

def scan_port():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            result = s.connect_ex((target, port))

            if result == 0:
                banner_info = "No Banner"
                try:
                    s.send(b"Hello\r\n")
                    banner = s.recv(1024).decode().strip()
                    if banner:
                        banner_info = banner.splitlines()[0]
                except:
                    pass

                res_str = f"[+] Port {port}: OPEN | Service/Banner: {banner_info}"

                with print_lock:
                    print(res_str)
                    open_ports.append(res_str)
            s.close()
        except:
            pass
        finally:
            port_queue.task_done()

# إضافة البورتات لطابور العمل
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# تشغيل الـ Threads للسرعة
for _ in range(50):
    thread = threading.Thread(target=scan_port)
    thread.daemon = True
    thread.start()

port_queue.join()

# 2. حفظ النتائج في ملف نصي Report
filename = "scan_report.txt"
with open(filename, "w") as f:
    f.write(f"Scan Report for: {target}\n")
    f.write(f"Date: {datetime.now()}\n")
    f.write("="*40 + "\n")
    if open_ports:
        for item in open_ports:
            f.write(item + "\n")
    else:
        f.write("No open ports found.\n")

print(f"\n{'='*50}")
print(f"[✔] Scan Completed successfully!")
print(f"[✔] Results saved to '{filename}'")
print(f"{'='*50}")