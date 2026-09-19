---
type: guide
area: documentation
status: active
updated: 2026-09-19
---

# Knowledge Base Maintenance

[Home](Home.md) · [Repository instructions](../../AGENTS.md)

The repository root is the vault. The same files are visible in Obsidian and Git; no import, duplicate vault or additional synchronization layer is required. Git changes become visible locally after they reach this working tree. Obsidian does not fetch, commit or push them automatically.

## Source ownership

| Information | Authoritative location | Knowledge-base follow-through |
| --- | --- | --- |
| Scope, progress and workstreams | [README](../../README.md), [roadmap](../ROADMAP.md), stage records | Home, Project Overview, Current State, Roadmap, Build |
| Design and decisions | [Architecture](../final-build-architecture.md), [motion architecture](../../hardware/generation-3-linear-motion.md), [smart-spool architecture](../../hardware/generation-3-smart-spool-system.md), [enhancement candidates](../../hardware/generation-3-enhancement-candidates.md), decision evidence | Decision Log, affected Systems, Open Issues |
| Components and inventory | [Hardware](../../hardware/README.md), existing inventory and [target BOM](../../hardware/generation-3-target-bom.md) | Parts, affected Systems, Current State when progress changes |
| Photos | Existing archive index, manifests and dated batch records | Photos, relevant Build notes, Current State and stale source summaries |
| Illustrations | Actual editable source/export and provenance/licence record | Illustrations, relevant Systems or Build, Documentation |
| Procedures and tests | Existing manual, measurement and test records | Build, Systems, Open Issues and status properties |

Edit the owning record first. Summaries link to it; do not copy its full procedure, BOM or per-image inventory into this folder. Preserve historical snapshots and distinguish later additions. Resolve conflicting current summaries using the dated evidence; keep uncertainty visible when the evidence is insufficient.

## Properties

Use YAML frontmatter on knowledge-base notes. Scalar text properties are intentionally simple so native Properties and Bases work without community plugins.

| Property | Meaning / values |
| --- | --- |
| `type` | `dashboard`, `project`, `index`, `system`, `build-phase`, `decision-log`, `guide`; use `component` or `decision` only if a dedicated note adds useful context |
| `area` | Primary topic, such as `project`, `build`, `systems`, `mechanics`, `electronics`, `firmware`, `extrusion`, `filament`, `heated-bed`, `user-interface`, `safety`, `hardware`, `evidence`, `documentation` |
| `status` | State of this note's subject; use the definitions below |
| `phase` | Roadmap identifier such as `stage-02`; omit if no single roadmap stage applies |
| `manual_stage` | Optional quoted letter `"A"`–`"J"` for the original reassembly sequence; does not replace `phase` |
| `generation` | Optional configuration context: `original`, `generation-2`, `generation-3`; omit on notes spanning generations |
| `priority` | `high`, `normal` or `low` when sequencing work is useful; not a claim from the historical source |
| `updated` | Date the note was substantively reviewed or changed, in `YYYY-MM-DD` form; not a physical inspection or decision date |

Current navigation statuses are `active` (maintained index, guide or requirements), `documented` (identified/catalogued with no implied passed test), `in-progress` (work evidenced but not closed) and `planned` (future work or completion not established).

When dedicated decision/component notes are needed, `proposed`, `under-study`, `frozen`, `implemented`, `tested`, `discarded` and `legacy` may describe their subjects. **Frozen** means a decision is constrained; **implemented** needs build evidence; **tested** needs a linked test and result. Use `complete` for a work phase only when its completion gate is recorded. Keep confidence (`CONFIRMED`/`PROBABLE`/`PENDING`) and component disposition (`REUSE`/`RESTORE`/`REPLACE`/`REDESIGN`/`ARCHIVE`) in the owning source, distinct from note workflow status.

## Update checklist

1. Update source facts, evidence/provenance and the applicable test or decision record.
2. Follow the change through the table above. Review Current State, Roadmap, Open Issues, Decision Log and affected Systems/Build/indices in the same change.
3. Update dates and properties only where the state has changed. Preserve permanent evidence IDs and decision history.
4. Check new relative links and heading anchors. Use `[Title](relative/path.md)` with forward slashes; avoid wikilinks and absolute machine paths.
5. Reconcile affected counts/ranges in the root README, roadmap and stage summaries. Do not rewrite an old closure snapshot as if later findings had been known then.
6. Review Git changes, including new files, before committing. Mention the knowledge-base updates, or state why the change has no knowledge-base impact.

Renaming a file **inside Obsidian** updates internal links with this vault's settings. Git or external-editor renames still require explicit link checks. This rule is a contributor workflow, not a background watcher.

## Shared and local Obsidian configuration

Only `.obsidian/app.json` is intended for version control. Its shared values are:

```json
{
  "useMarkdownLinks": true,
  "newLinkFormat": "relative",
  "alwaysUpdateLinks": true
}
```

These correspond to **Files and links → Use Wikilinks: off**, **New link format: Relative path to file**, and **Automatically update internal links: on**. See the [official settings reference](https://help.obsidian.md/settings) and [internal links guide](https://help.obsidian.md/links).

The root `.gitignore` ignores all other `.obsidian` content and `.trash/`: window/workspace layouts, appearance, hotkeys, bookmarks, graph preferences, property-type preferences, caches, plugin data and personal core-feature selections. If Obsidian adds personal settings to the shared `app.json`, review them individually and keep its repository policy focused. No existing repository `.gitignore` was present during setup.

Core Backlinks, Graph, Properties, Search, Bookmarks and Bases are available natively. Bases was already enabled in the local vault; its local `core-plugins.json` is not shared. In another clone, enable **Settings → Core plugins → Bases** to open [Knowledge-Base.base](Knowledge-Base.base). Its All notes, Systems and Build phases views read note properties without duplicating records. The syntax follows the [official Bases reference](https://help.obsidian.md/bases/syntax).

No community plugins are required or installed. Opening Home, bookmarking it or keeping its tab pinned is a personal preference and stays local. Use the normal Git workflow to synchronize the repository after review; do not add a second Obsidian synchronization system for this setup.
