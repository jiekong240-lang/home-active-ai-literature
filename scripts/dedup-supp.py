import re

with open("existing-277-urls.txt", encoding="utf-8") as f:
    base = [l.strip() for l in f if l.strip()]

def arx_ids(urls):
    out = {}
    for u in urls:
        m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", u)
        if m:
            out[m.group(1)] = u
    return out

base_ids = arx_ids(base)

cand = [
 "https://arxiv.org/abs/2110.14168",
 "https://arxiv.org/abs/2305.20050",
 "https://arxiv.org/abs/2312.08935",
 "https://arxiv.org/abs/2308.04592",
 "https://arxiv.org/abs/2410.10934",
 "https://arxiv.org/abs/2305.11738",
 "https://arxiv.org/abs/2309.11495",
 "https://arxiv.org/abs/2310.12397",
 "https://arxiv.org/abs/2303.11366",
 "https://arxiv.org/abs/2303.17651",
 "https://arxiv.org/abs/2408.08435",
 "https://arxiv.org/abs/2210.03629",
 "https://arxiv.org/abs/2305.10601",
 "https://arxiv.org/abs/2305.14992",
 "https://arxiv.org/abs/2302.04761",
 "https://arxiv.org/abs/2305.15334",
 "https://arxiv.org/abs/2307.16789",
 "https://arxiv.org/abs/2411.15100",
 "https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html",
 "https://arxiv.org/abs/2307.13854",
 "https://arxiv.org/abs/2310.06770",
 "https://arxiv.org/abs/2405.15793",
 "https://arxiv.org/abs/2406.12045",
 "https://arxiv.org/abs/2308.03688",
 "https://arxiv.org/abs/2411.02305",
 "https://arxiv.org/abs/2311.12983",
 "https://arxiv.org/abs/2406.11896",
 "https://arxiv.org/abs/2203.14465",
 "https://arxiv.org/abs/2401.10020",
 "https://arxiv.org/abs/2401.01335",
 "https://arxiv.org/abs/2409.12917",
 "https://arxiv.org/abs/2308.08998",
 "https://arxiv.org/abs/2505.22954",
 "https://arxiv.org/abs/2305.16291",
 "https://arxiv.org/abs/2304.03442",
 "https://arxiv.org/abs/2412.09605",
 "https://arxiv.org/abs/2412.19723",
 "https://arxiv.org/abs/2307.10088",
 "https://arxiv.org/abs/2503.21620",
 "https://arxiv.org/abs/2504.10458",
]

cand_ids = arx_ids(cand)
print("Baseline URL count:", len(base))
print("Baseline arxiv ID count:", len(base_ids))
print("Candidate count:", len(cand))
print("Candidate arxiv ID count:", len(cand_ids))

url_overlap = [c for c in cand if c in base]
id_overlap = [cid for cid in cand_ids if cid in base_ids]
loose = [(cid, [u for u in base if cid in u]) for cid in cand_ids if any(cid in u for u in base)]
print("\nExact URL overlap (should be 0):", url_overlap)
print("arXiv ID overlap (should be 0):", id_overlap)
print("Loose ID-in-URL overlap (should be 0):", [(c,h) for c,h in loose if h])

print("\n=== RESULT ===")
print("Total supplement candidates:", len(cand))
ok = (not url_overlap) and (not id_overlap) and (not [h for c,h in loose if h])
print("Confirmed zero-overlap with 277-set:", ok)
print("Net new articles after diff:", len(cand))
