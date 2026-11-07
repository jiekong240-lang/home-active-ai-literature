import subprocess, re, xml.etree.ElementTree as ET

# (S-id, arxiv_id, expected_title_keyword)
entries = [
 ("S-01","2110.14168","Training Verifiers"),
 ("S-02","2305.20050","Verify Step by Step"),
 ("S-03","2312.08935","Math-Shepherd"),
 ("S-04","2308.04592","Shepherd"),
 ("S-05","2410.10934","Agent-as-a-Judge"),
 ("S-06","2305.11738","CRITIC"),
 ("S-07","2309.11495","Chain-of-Verification"),
 ("S-08","2310.12397","GPT-4 Doesn"),
 ("S-09","2303.17651","Self-Refine"),
 ("S-10","2408.08435","Automated Design of Agentic"),
 ("S-11","2305.14992","Reasoning with Language Model"),
 ("S-12","2305.15334","Gorilla"),
 ("S-13","2307.16789","ToolLLM"),
 ("S-14","2411.15100","XGrammar"),
 ("S-15","2310.06770","SWE-bench"),
 ("S-16","2405.15793","SWE-agent"),
 ("S-17","2411.02305","CRMArena"),
 ("S-18","2406.11896","DigiRL"),
 ("S-19","2203.14465","STaR"),
 ("S-20","2401.10020","Self-Rewarding"),
 ("S-21","2401.01335","Self-Play Fine-Tuning"),
 ("S-22","2409.12917","Self-Correct via Reinforcement"),
 ("S-23","2308.08998","ReST"),
 ("S-24","2505.22954","Darwin"),
 ("S-25","2305.16291","Voyager"),
 ("S-26","2412.09605","AgentTrek"),
 ("S-27","2412.19723","OS-Genesis"),
 ("S-28","2504.10458","GUI-R1"),
]

ids = [e[1] for e in entries]
idlist = ",".join(ids)
url = f"https://export.arxiv.org/api/query?id_list={idlist}&max_results={len(ids)}"

def curl(url):
    try:
        out = subprocess.run(["curl","-sS","--max-time","40",url], capture_output=True, text=True)
        return out.stdout
    except Exception as ex:
        return ""

xml_text = curl(url)
root = ET.fromstring(xml_text)
ns = "{http://www.w3.org/2005/Atom}"
api_titles = {}
for entry in root.findall(ns+"entry"):
    eid = entry.find(ns+"id").text  # http://arxiv.org/abs/XXXXvN
    m = re.search(r"abs/([0-9.]+)", eid)
    aid = m.group(1) if m else eid
    title = " ".join(entry.find(ns+"title").text.split())
    api_titles[aid] = title

print(f"API returned {len(api_titles)} entries\n")
print(f"{'S-id':6} {'arXiv':12} {'API_TITLE_MATCH':8} {'HTTP':5}  EXPECTED")
print("-"*100)
allok = True
for sid, aid, kw in entries:
    t = api_titles.get(aid, "")
    match = (kw.lower() in t.lower())
    # HTTP status of abs page
    code = subprocess.run(["curl","-sS","--max-time","25","-o","/dev/null","-w","%{http_code}",f"https://arxiv.org/abs/{aid}"], capture_output=True, text=True).stdout.strip()
    flag = "OK" if (match and code=="200") else "FAIL"
    if flag=="FAIL": allok=False
    print(f"{sid:6} {aid:12} {str(match):8} {code:5}  [{kw}] -> {t[:60]}")
print("-"*100)
print("ALL SOURCES VERIFIED (technical paper + reachable + title matches):", allok)
