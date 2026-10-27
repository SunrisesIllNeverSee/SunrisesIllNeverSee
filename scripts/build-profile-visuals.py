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
GOLD_LIGHT="#e9c277"; GOLD_DARK="#57452b"; TEXT="#e8e0d4"; MUTED="#c0ae90"
DULL="#9f8968"; SHADOW="#272016"
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
    """Large-type, GitHub-width architecture. Keep the distinct product surfaces."""
    o=root_svg(960,684,"MO§ES portfolio architecture",
        "Commitment Theory provides the conservation law. MO§ES is the shared "
        "execution substrate. SignalAF/SigRank, AQUA and Signomy are distinct "
        "products; TTEOP and the Upsilon pilot support operator intelligence.")
    o += [
        rect(18,18,924,640,"none",GOLD_DARK,4,1.3),
        txt(44,54,"SYSTEM ARCHITECTURE",24,GOLD_LIGHT,790,spacing=.9),
        txt(917,52,"01 / PORTFOLIO",14,MUTED,650,"end"),
        line(44,70,916,70,GOLD_DARK,1.2),
        # Foundation
        rect(231,94,498,116,INSET,GOLD_DARK,7,2),
        pix_hex(249,111,PATTERNS[1]),
        txt(480,120,"FOUNDATION  /  CONSERVATION",15,GOLD,750,"middle",.7),
        txt(480,164,"COMMITMENT THEORY",31,TEXT,800,"middle"),
        txt(480,191,"Binding meaning through transformation",16,MUTED,440,"middle"),
        line(480,210,480,230,GOLD,2.6),arrow_down(480,239),
        # Shared substrate
        rect(131,243,698,141,PANEL,GOLD,8,2.7),
        rect(141,253,678,121,"none",GOLD_DARK,5,.8),
        pix_hex(158,270,PATTERNS[0]),
        txt(480,273,"SHARED EXECUTION SUBSTRATE",16,GOLD_LIGHT,750,"middle",.8),
        txt(480,326,"MO§ES",48,TEXT,820,"middle"),
        txt(480,358,"Temporal gates  ·  commitments  ·  lineage  ·  provenance",16,MUTED,470,"middle"),
        # Bus
        line(480,384,480,410,GOLD,2.5),
        line(172,410,788,410,GOLD_DARK,2),
    ]
    for x in (172,480,788):
        o.extend((line(x,410,x,434,GOLD_DARK,2),arrow_down(x,442)))
    cards=[
       (35,"01  /  INTELLIGENCE","SIGRANK / SIGNALAF",
        "Compare AI operators","TTEOP  ·  Upsilon B2B",PATTERNS[0],22),
       (346,"02  /  ANSWER MEMORY","AQUA",
        "Reuse approved answers","Local-first  ·  applications",PATTERNS[2],29),
       (657,"03  /  AGENT ECONOMY","SIGNOMY",
        "Governed agent teamwork","CIVITAE  ·  missions  ·  roles",PATTERNS[3],29),
    ]
    for x,kicker,title,sub1,sub2,pattern,heading in cards:
        mid=x+134
        o += [
            rect(x,448,268,171,INSET,GOLD_DARK,8,1.9),
            rect(x+1,448,266,5,GOLD_DARK,r=1),
            pix_hex(x+8,455,pattern),
            txt(mid,478,kicker,14,GOLD_LIGHT,740,"middle",.3),
            txt(mid,527,title,heading,TEXT,800,"middle"),
            line(x+31,543,x+237,543,GOLD_DARK,1),
            txt(mid,569,sub1,16,MUTED,460,"middle"),
            txt(mid,596,sub2,14,DULL,460,"middle"),
        ]
    o += [
        line(44,636,916,636,GOLD_DARK,1),
        txt(480,660,"ONE GOVERNED SYSTEM   /   THREE PRODUCT SURFACES",16,GOLD_LIGHT,730,"middle",.35),
        '</svg>'
    ]
    (ROOT/"portfolio-architecture.svg").write_text('\n'.join(o)+"\n",encoding="utf-8")

def clickable_architecture():
    """README-compatible clickable modules, avoiding SVG image-map hotspot stripping."""
    # Each image is wrapped by its own anchor in README. Thus links work even
    # though GitHub displays SVG assets as embedded <img> elements.
    common_desc = "Clickable module from the black/dirty-gold portfolio architecture."
    tiles = [
        ("arch-commitment.svg", 560, 112, "COMMITMENT THEORY",
         "FOUNDATION / CONSERVATION LAW", "Preserve binding meaning through transformation",
         PATTERNS[1], 24, GOLD_DARK),
        ("arch-moses.svg", 780, 136, "MO§ES", "SHARED EXECUTION SUBSTRATE",
         "Commitments  ·  temporal gates  ·  lineage  ·  provenance",
         PATTERNS[0], 33, GOLD),
        ("arch-signalaf.svg", 305, 172, "SIGRANK / SIGNALAF",
         "01 / OPERATOR INTELLIGENCE", "TTEOP telemetry · Upsilon B2B pilot",
         PATTERNS[0], 19, GOLD_DARK),
        ("arch-aqua.svg", 305, 172, "AQUA",
         "02 / ANSWER MEMORY", "Local-first application knowledge",
         PATTERNS[2], 23, GOLD_DARK),
        ("arch-signomy.svg", 305, 172, "SIGNOMY",
         "03 / AGENT ECONOMY", "CIVITAE runtime · mission controls",
         PATTERNS[3], 23, GOLD_DARK),
    ]
    for name,w,h,title,kicker,desc,pattern,tsize,border in tiles:
        o = root_svg(w,h,title,common_desc)
        o += [rect(4,4,w-8,h-8,PANEL,border,7,2),
              rect(13,13,w-26,h-26,"none",GOLD_DARK,5,.7)]
        if w < 400:
            o += [rect(8,8,w-16,5,GOLD_DARK,r=1),
                  pix_hex(w-59,13,pattern),
                  txt(w/2,37,kicker,10,GOLD_LIGHT,700,"middle",.2),
                  txt(w/2,97,title,tsize,TEXT,800,"middle"),
                  txt(w/2,139,desc,10,MUTED,400,"middle"),
                  txt(w/2,154,"CLICK TO OPEN  ↗",9,GOLD,600,"middle")]
        else:
            o += [pix_hex(29,25,pattern),
                  txt(w/2,34,kicker,11,GOLD_LIGHT,700,"middle",1),
                  txt(w/2,79,title,tsize,TEXT,800,"middle"),
                  txt(w/2,h-16,desc,11,MUTED,400,"middle")]
        o.append("</svg>")
        (ROOT/name).write_text("\n".join(o)+"\n",encoding="utf-8")
    # Separate, simple connector files for responsive Markdown/HTML layout.
    # SVG elements themselves are not interactive; only the linked panels are.
    a=root_svg(960,38,"Vertical architecture connection","A gold arrow from law to execution.")
    a += [line(480,0,480,27,GOLD,2),arrow_down(480,35),"</svg>"]
    (ROOT/"arch-arrow.svg").write_text("\n".join(a)+"\n",encoding="utf-8")
    a=root_svg(960,68,"Execution to product branches",
         "Shared substrate connects to all three product surfaces.")
    a += [line(480,0,480,22,GOLD,2),line(157,22,803,22,GOLD_DARK,2)]
    for x in (157,480,803):
        a += [line(x,22,x,55,GOLD_DARK,2),arrow_down(x,63)]
    a.append("</svg>")
    (ROOT/"arch-branches.svg").write_text("\n".join(a)+"\n",encoding="utf-8")


def compose_unified_profile():
    """One self-contained SVG replaces eight independently rendered README blocks."""
    def inner(path, prefix):
        src = (ROOT / path).read_text(encoding="utf-8")
        body = src.split(">", 1)[1].rsplit("</svg>", 1)[0]
        for original, replacement in (
            ('id="ttl"', f'id="{prefix}-ttl"'),
            ('id="dsc"', f'id="{prefix}-dsc"'),
            ('id="dots"', f'id="{prefix}-dots"'),
            ('url(#dots)', f'url(#{prefix}-dots)'),
        ):
            body = body.replace(original, replacement)
        return body
    arch = inner("portfolio-architecture.svg", "arch")
    heat = inner("contributions.svg", "heat")
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="999" '
        'viewBox="0 0 960 999" role="img" aria-labelledby="profile-title profile-desc">',
        '<title id="profile-title">Architecture and full contribution calendar</title>',
        '<desc id="profile-desc">Black and dirty-gold portfolio architecture: Commitment Theory '
        'through MO§ES to SignalAF, AQUA and Signomy, followed by the full 53-week '
        'GitHub contribution calendar. Use the directly linked project badges below '
        'the diagram to open each destination.</desc>',
        rect(0,0,960,999,BG),
        '<g id="architecture-panel">', arch, '</g>',
        '<g id="contribution-panel" transform="translate(0 684)">', heat, '</g>',
        '</svg>'
    ]
    (ROOT / "profile-unified.svg").write_text("\n".join(out)+"\n", encoding="utf-8")

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
    o=root_svg(960,315,"Full GitHub contribution heat map",
      "Complete GitHub contribution calendar from "+flat[0]["date"]+" to "+flat[-1]["date"]+".")
    o += [
      rect(18,5,924,294,"none",GOLD_DARK,4,1.3),
      txt(44,47,"CONTRIBUTION FIELD",23,GOLD_LIGHT,770,spacing=.5),
      txt(918,47,f'{d["totalContributions"]:,}  CONTRIBUTIONS',19,GOLD,750,"end"),
      line(44,64,916,64,GOLD_DARK,1.2),
    ]
    first=dt.date.fromisoformat(flat[0]["date"]);last=dt.date.fromisoformat(flat[-1]["date"])
    o += [
      txt(44,92,first.strftime("%d %b %Y")+"  —  "+last.strftime("%d %b %Y"),14,MUTED,490),
      txt(48,133,"SUN",12,MUTED,640),
      txt(48,178,"WED",12,MUTED,640),
      txt(48,220,"SAT",12,MUTED,640),
    ]
    left=118; top=121; step=14.8; square=12.1
    used=set()
    for wi,wk in enumerate(weeks):
        for day in wk["contributionDays"]:
            date=dt.date.fromisoformat(day["date"])
            mon=(date.year,date.month)
            if mon not in used and date.day<=7:
                used.add(mon)
                o.append(txt(round(left+wi*step,2),109,date.strftime("%b").upper(),12,MUTED,600))
            x=left+wi*step
            row=(date.weekday()+1)%7
            y=top+row*step
            count=day["contributionCount"]
            o.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{square}" height="{square}" rx="1.7" fill="{shade(count)}" stroke="#3d3325" stroke-width=".35"><title>{escape(day["date"])}: {count} contributions</title></rect>')
    o += [
        line(44,244,916,244,GOLD_DARK,1),
        txt(44,271,"SOURCE / GitHub contribution calendar",13,MUTED,480),
        txt(740,271,"LESS",12,DULL,550)
    ]
    for i,color in enumerate(shades):
        o.append(rect(776+i*23,259,16,16,color,r=2))
    o += [txt(916,271,"MORE",12,MUTED,570,"end"),'</svg>']
    (ROOT/"contributions.svg").write_text('\n'.join(o)+"\n",encoding="utf-8")
    return {"weeks":len(weeks),"days":len(flat),"totalContributions":d["totalContributions"],"sumDaily":sum(x["contributionCount"] for x in flat),"first":flat[0]["date"],"last":flat[-1]["date"],"quantiles":cuts}

if __name__=="__main__":
    architecture()
    clickable_architecture()
    import sys
    if "--architecture-only" not in sys.argv:
        stats=heatmap()
        print("GENERATED",json.dumps(stats))
    else:
        print("GENERATED architecture and linked panels; heatmap unchanged")
    compose_unified_profile()
    print("GENERATED unified visual")
