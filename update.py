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

# Başlık (meta bilgi)
header = [
    "# Title: Hakan/Hosts",
    "#",
    "# Custom Hosts File – Generated on: " + datetime.utcnow().strftime("%Y-%m-%d"),
    "#",
    "# Sources:"
] + [f"#  - {url}" for url in urls] + [
    "#",
    "# Info: Bu dosya, Hakan tarafından reklam, takipçi ve zararlı alan adlarını engellemek amacıyla hazırlanmıştır.",
    "#",
    "# ==================================================",
    "# 🧱 Sistemsel DNS & Yerel Ağ Tanımları (IPv4/IPv6)",
    "# =================================================="
]

# Sistemsel başlangıç girişleri (sabit)
static_entries = [
    "127.0.0.1 localhost",
    "127.0.0.1 localhost.localdomain",
    "127.0.0.1 local",
    "255.255.255.255 broadcasthost",
    "::1 localhost",
    "::1 ip6-localhost",
    "::1 ip6-loopback",
    "fe80::1%lo0 localhost",
    "ff00::0 ip6-localnet",
    "ff00::0 ip6-mcastprefix",
    "ff02::1 ip6-allnodes",
    "ff02::2 ip6-allrouters",
    "ff02::3 ip6-allhosts",
    "0.0.0.0 0.0.0.0"
]

blocklist_intro = [
    "",
    "# =================================================================",
    "# ⛔ Reklam, takipçi ve zararlı alan adları aşağıda listelenmiştir",
    "# ================================================================="
]

with open("hosts", "w") as f:
    f.write("\n".join(header + [""] + static_entries + blocklist_intro + sorted(domain_map.values())))
