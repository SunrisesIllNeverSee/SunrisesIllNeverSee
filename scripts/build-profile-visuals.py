#!/usr/bin/env python3
"""Build the GitHub-profile architecture and full contribution-calendar SVGs.

Palette is the existing banner.svg brand black (#0a0a0a) / dirty gold (#c4923a).
Pixel marks preserve the 3x3 silhouettes used by SigRank PixelBadge, recolored
as interface accents, NOT represented as achievements the user has earned.
The contribution graphic is a date-stamped snapshot of the GitHub API calendar.
"""
from __future__ import annotations
import datetime as dt
from html import escape
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BG="#0a0a0a"; INSET="#14110e"; PANEL="#19150e"; GOLD="#c4923a"
GOLD_LIGHT="#e9c277"; GOLD_DARK="#57452b"; TEXT="#e8e0d4"; MUTED="#a7977c"
DULL="#776a58"; SHADOW="#272016"
FONT="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

def txt(x,y,s,size=15,color=TEXT,weight=400,anchor="start",spacing=0):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{escape(s)}</text>')

def rect(x,y,w,h,fill,stroke="none",r=0,sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1,y1,x2,y2,color=GOLD_DARK,width=2,dash=""):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{width}"'+ (f' stroke-dasharray="{dash}"' if dash else "") +'/>')

def root_svg(width,height,title,desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="ttl dsc">',
            '<title id="ttl">'+escape(title)+'</title><desc id="dsc">'+escape(desc)+'</desc>',
            rect(0,0,width,height,BG),
            '<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#c4923a" opacity=".12"/></pattern></defs>',
            rect(0,0,width,height,'url(#dots)')]

# Actual 3x3 SigRank PixelBadge patterns. These are visual tokens, not awards.
PATTERNS=["LL./LGK/GGL",".PR/BPK/.YM","C.W/CWK/CWC","YYO/RRK/RGM"]
PXC={"L":GOLD,"G":GOLD_DARK,"K":BG,"P":GOLD_LIGHT,"R":"#b58242","B":"#8a6837","Y":"#cfa457","M":"#6b522e","C":GOLD,"W":TEXT,"O":"#836b40"}

def pix_hex(x,y,pattern,scale=5):
    out=[f'<polygon points="{x+22},{y} {x+44},{y+12} {x+44},{y+35} {x+22},{y+47} {x},{y+35} {x},{y+12}" '
         f'fill="#241d13" stroke="{GOLD_DARK}" stroke-width="1.4"/>']
    rows=pattern.split("/")
    for r,row in enumerate(rows):
        for c,k in enumerate(row):
            if k==".":continue
            color=PXC.get(k,GOLD)
            out.append(rect(x+14+c*6,y+15+r*6,5,5,color,r=0))
    return ''.join(out)

def arrow_down(x,y):
    return f'<polygon points="{x-5},{y-7} {x+5},{y-7} {x},{y}" fill="{GOLD}"/>'

def architecture():
    o=root_svg(960,648,"Portfolio system architecture","Commitment Theory provides the conservation law; MO§ES is the shared governing execution substrate; SignalAF, AQUA and Signomy are product surfaces, with TTEOP and Upsilon supporting operator measurement.")
    o += [rect(18,18,924,612,"none",GOLD_DARK,2,1),
          txt(42,49,"THE SYSTEM  /  ARCHITECTURE MAP",18,GOLD_LIGHT,700,spacing=1.3),
          txt(918,48,"01 / PORTFOLIO",11,MUTED,500,"end"),
          line(42,64,918,64,GOLD_DARK,1)]
    # Law layer
    o += [rect(255,91,450,96,INSET,GOLD_DARK,8,2),
          pix_hex(273,113,PATTERNS[1]),
          txt(333,115,"FOUNDATION / CONSERVATION LAW",11,GOLD,650,spacing=1.2),
          txt(333,146,"COMMITMENT THEORY",26,TEXT,750),
          txt(333,169,"Preserve binding meaning through transformation",12,MUTED)]
    # The central substrate
    o += [line(480,188,480,213,GOLD,2),arrow_down(480,217),
          rect(144,221,672,121,PANEL,GOLD,9,2.7),
          rect(156,232,648,98,"none",GOLD_DARK,5,0.8),
          pix_hex(175,250,PATTERNS[0]),
          txt(241,250,"SHARED EXECUTION SUBSTRATE",12,GOLD_LIGHT,680,spacing=1.1),
          txt(241,290,"MO§ES",38,TEXT,800),
          txt(242,314,"Commitments  ·  temporal gates  ·  lineage  ·  provenance",13,MUTED)]
    # Branch buses
    o += [line(480,342,480,371,GOLD,2),
          line(170,371,790,371,GOLD_DARK,2),
          line(170,371,170,392,GOLD_DARK,2),
          line(480,371,480,392,GOLD_DARK,2),
          line(790,371,790,392,GOLD_DARK,2),
          arrow_down(170,399),arrow_down(480,399),arrow_down(790,399)]
    cards=[
        (35,"01 / OPERATOR INTELLIGENCE","SIGRANK / SIGNALAF",
         "TTEOP telemetry  ·  Upsilon B2B pilot",
         "Measurement → ranking → public proof",PATTERNS[0]),
        (346,"02 / ANSWER MEMORY","AQUA",
         "Universal knowledge  ·  local-first",
         "Approved answers → application flows",PATTERNS[2]),
        (657,"03 / AGENT ECONOMY","SIGNOMY",
         "CIVITAE runtime  ·  mission controls",
         "Agent roles → accountable execution",PATTERNS[3])
    ]
    for x,kicker,title,sub1,sub2,pattern in cards:
        o += [rect(x,406,268,157,INSET,GOLD_DARK,7,1.7),
              rect(x+1,406,266,5,GOLD_DARK,r=1),
              txt(x+17,437,kicker,10,GOLD_LIGHT,700,spacing=.3),
              pix_hex(x+207,414,pattern),
              txt(x+17,480,title,20,TEXT,800),
              txt(x+17,516,sub1,11,MUTED),
              txt(x+17,537,sub2,10,DULL)]
    o += [line(42,586,918,586,GOLD_DARK,1),
          txt(480,610,"ONE SHARED GOVERNANCE / VERIFICATION LAYER   •   DISTINCT PRODUCT INTERFACES",12,GOLD_LIGHT,600,"middle",.15),
          txt(480,626,"Pixel motifs adapted from the SigRank 3×3 visual language; not earned badges.",10,DULL,400,"middle"),'</svg>']
    (ROOT/"portfolio-architecture.svg").write_text('\n'.join(o)+"\n",encoding="utf-8")

def load_calendar():
    query='query { user(login: "SunrisesIllNeverSee") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'
    run=subprocess.run(["gh","api","graphql","-f","query="+query],check=True,capture_output=True,text=True)
    body=json.loads(run.stdout)
    return body["data"]["user"]["contributionsCollection"]["contributionCalendar"]

def heatmap():
    d=load_calendar()
    weeks=d["weeks"]
    flat=[day for wk in weeks for day in wk["contributionDays"]]
    nonzero=sorted(day["contributionCount"] for day in flat if day["contributionCount"])
    def quantile(p):
        return nonzero[min(len(nonzero)-1,int((len(nonzero)-1)*p))] if nonzero else 0
    cuts=[quantile(p) for p in (.25,.5,.75)]
    shades=["#211c15","#58472b","#846531","#ac8137","#d6aa58"]
    def shade(v):
        if v==0:return shades[0]
        if v<=cuts[0]:return shades[1]
        if v<=cuts[1]:return shades[2]
        if v<=cuts[2]:return shades[3]
        return shades[4]
    o=root_svg(960,284,"Complete GitHub contribution heat map","All 53 weeks of the GitHub contribution calendar, from "+flat[0]["date"]+" to "+flat[-1]["date"]+", in the black and dirty-gold palette.")
    o += [rect(18,18,924,247,"none",GOLD_DARK,3,1),
          txt(40,48,"CONTRIBUTION FIELD  /  53 WEEKS",17,GOLD_LIGHT,700,spacing=.9),
          txt(919,48,f'{d["totalContributions"]:,} CONTRIBUTIONS',13,GOLD,700,"end"),
          line(40,62,920,62,GOLD_DARK,1)]
    first=dt.date.fromisoformat(flat[0]["date"]);last=dt.date.fromisoformat(flat[-1]["date"])
    o += [txt(40,82,first.strftime("%d %b %Y")+" — "+last.strftime("%d %b %Y"),11,MUTED),
          txt(41,120,"SUN",10,DULL),txt(41,163,"WED",10,DULL),txt(41,206,"SAT",10,DULL)]
    left=116; top=104; step=14.65; square=11.5
    # Labels use the first available day for each new month.
    used=set()
    for wi,wk in enumerate(weeks):
        for day in wk["contributionDays"]:
            date=dt.date.fromisoformat(day["date"])
            mon=(date.year,date.month)
            if mon not in used and date.day<=7:
                used.add(mon)
                o.append(txt(round(left+wi*step,2),93,date.strftime("%b").upper(),10,MUTED,600))
            x=left+wi*step
            row=(date.weekday()+1)%7
            y=top+row*step
            count=day["contributionCount"]
            o.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{square}" height="{square}" rx="1.4" fill="{shade(count)}" stroke="#3d3325" stroke-width=".35"><title>{escape(day["date"])}: {count} contributions</title></rect>')
    o += [line(40,226,920,226,GOLD_DARK,1),
          txt(40,248,"SOURCE  GitHub contribution calendar  /  full-year snapshot",10,MUTED,500),
          txt(728,248,"LESS",10,DULL,550)]
    for k,color in enumerate(shades):
        o.append(rect(765+k*22,237,14,14,color,r=2))
    o += [txt(919,248,"MORE",10,MUTED,550,"end"),'</svg>']
    (ROOT/"contributions.svg").write_text('\n'.join(o)+"\n",encoding="utf-8")
    return {"weeks":len(weeks),"days":len(flat),"totalContributions":d["totalContributions"],"sumDaily":sum(x["contributionCount"] for x in flat),"first":flat[0]["date"],"last":flat[-1]["date"],"quantiles":cuts}

if __name__=="__main__":
    architecture()
    stats=heatmap()
    readme=ROOT/"README.md"
    orig=readme.read_text()
    anchor="## The architecture\n"
    replacement="""## The architecture

<div align="center">
  <img src="portfolio-architecture.svg" width="960" alt="Portfolio system architecture: Commitment Theory above the MO§ES shared execution substrate; its branches reach SigRank and SignalAF with TTEOP and Upsilon, AQUA, and Signomy." />
</div>

"""
    if 'src="portfolio-architecture.svg"' not in orig:
        if anchor not in orig:raise RuntimeError("Architecture section not found")
        orig=orig.replace(anchor,replacement,1)
    anchor2='<details>\n<summary>GitHub activity</summary>'
    addition="""## Full contribution heat map

<div align="center">
  <img src="contributions.svg" width="960" alt="Full 53-week GitHub contribution calendar with every day rendered in black and dirty gold." />
</div>

<sub>Complete 53-week GitHub contribution calendar, captured October 27, 2026. This is a dated snapshot; the existing GitHub activity graphic continues to update separately.</sub>

---

"""
    if 'src="contributions.svg"' not in orig:
        if anchor2 not in orig:raise RuntimeError("GitHub activity section not found")
        orig=orig.replace(anchor2,addition+anchor2,1)
    # Keep the snapshot label accurate on subsequent manual refreshes.
    latest = dt.date.fromisoformat(stats["last"])
    stamp = f"{latest.strftime('%B')} {latest.day}, {latest.year}"
    import re
    orig = re.sub(r"captured [A-Za-z]+ \d{1,2}, \d{4}\.", f"captured {stamp}.", orig)
    readme.write_text(orig)
    print("CREATED",json.dumps(stats))
    print("FILES",[(p.name,p.stat().st_size) for p in (ROOT/"portfolio-architecture.svg",ROOT/"contributions.svg",readme)])

