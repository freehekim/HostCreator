import requests
from datetime import datetime

with open("urls.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

domain_map = {}

for url in urls:
    try:
        res = requests.get(url, timeout=10)
        lines = res.text.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                ip = parts[0].replace("127.0.0.1", "0.0.0.0")
                domain = parts[1]
                domain_map[domain] = "0.0.0.0 " + domain  # Daima 0.0.0.0 ile güncelle
    except Exception as e:
        print(f"Error fetching {url}: {e}")

header = [
    "# Custom Hosts File – Generated on: " + datetime.utcnow().strftime("%Y-%m-%d"),
    "# Sources:"
] + [f"#  - {url}" for url in urls] + [
    "# info: Hakan tarafından kök Android reklam engelleme için hazırlanmıştır."
]

with open("hosts", "w") as f:
    f.write("\n".join(header + sorted(domain_map.values())))
