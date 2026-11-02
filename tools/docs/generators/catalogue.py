"""Driver catalogue regions, from ``.gitmodules`` (what is in the umbrella) and ``tools/docs/drivers.yml`` (facts).

- ``catalogue``: a chip card per submodule, grouped, linking the driver's site (when it has one) and GitHub.
- ``driver-table``: one row per submodule: path, chip, vendor, bus, links.

A submodule without facts, or facts for a repository that is not a submodule, stops the generator, so the catalogue
always matches the umbrella.
"""

from __future__ import annotations

import configparser

import yaml

from hardfoc_mkdocs_theme.paths import repo_root


def _load():
    root = repo_root()
    gm = configparser.ConfigParser()
    gm.read(root / ".gitmodules")
    subs = []
    for sec in gm.sections():
        path = gm[sec]["path"]
        repo = gm[sec]["url"].rstrip("/").removesuffix(".git").rsplit("/", 1)[-1]
        subs.append((path, repo, gm[sec]["url"].removesuffix(".git")))
    facts = yaml.safe_load((root / "tools/docs/drivers.yml").read_text())
    drivers = facts["drivers"]
    missing = sorted({r for _, r, _ in subs} - set(drivers))
    extra = sorted(set(drivers) - {r for _, r, _ in subs})
    if missing or extra:
        raise SystemExit(f"[gen] drivers.yml out of date: missing {missing}, not submodules {extra}")
    return subs, facts["groups"], drivers


def _links(repo: str, url: str, f: dict) -> str:
    site = f"[Documentation](https://hardfoc.github.io/{repo}/)" if f["site"] else "No site yet"
    return f"{site} · [GitHub]({url})"


def catalogue() -> str:
    subs, groups, drivers = _load()
    out = []
    for key, title in groups.items():
        members = sorted((p, r, u) for p, r, u in subs if drivers[r]["group"] == key)
        if not members:
            continue
        out += [f"## {title}", "", '<div class="grid" markdown>', ""]
        for path, repo, url in sorted(members, key=lambda m: drivers[m[1]]["chip"].lower()):
            f = drivers[repo]
            out += [
                '<div class="hf-chip" markdown>',
                '<div class="hf-chip__head">',
                f'<span class="hf-chip__kicker">{f["function"]}</span>',
                f'<span class="hf-chip__name">{f["chip"]}</span>',
                f'<span class="hf-chip__vendor">{f["vendor"]}</span>',
                "</div>",
                "",
                "Bus",
                f':   {f["bus"]}',
                "",
                "Language",
                f':   {f["cpp"]}',
                "",
                _links(repo, url, f),
                "</div>",
                "",
            ]
        out += ["</div>", ""]
    return "\n".join(out)


def driver_table() -> str:
    subs, groups, drivers = _load()
    rows = ["| Chip | Vendor | Bus | Path | Links |", "| --- | --- | --- | --- | --- |"]
    order = list(groups)
    for path, repo, url in sorted(subs, key=lambda s: (order.index(drivers[s[1]]["group"]), drivers[s[1]]["chip"].lower())):
        f = drivers[repo]
        rows.append(f'| {f["chip"]} | {f["vendor"]} | {f["bus"]} | `{path}` | {_links(repo, url, f)} |')
    return f"{len(subs)} submodules.\n\n" + "\n".join(rows) + "\n"


REGIONS = {"catalogue": catalogue, "driver-table": driver_table}
