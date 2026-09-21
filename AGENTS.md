# Repository instructions

## Scope and source of truth

This repository is the Obsidian vault for Prusa-i3-Revival-2026. The knowledge-base entry point is [Home](docs/knowledge-base/Home.md).

- Use English names, paths, headings and technical documentation. Keep permanent legacy evidence identifiers unchanged.
- Follow the existing [method and provenance](docs/00-archaeology/03-method-and-provenance.md), [roadmap](docs/ROADMAP.md), [reassembly scope](docs/02-reassembly/README.md) and frozen [Generation 3 architecture](docs/final-build-architecture.md).
- Preserve original evidence and distinguish originals, sanitized later batches and derivatives. Do not infer installed hardware or successful tests from possession or photographs alone.
- Keep detailed procedures, inventories, BOMs and media in their canonical locations. Knowledge-base pages should link to them and summarize only what navigation or status requires.
- Preserve the original-design files under `printed-parts/original-designs/upstream/` byte-for-byte. New imports require source/license notes and manifest hashes; adaptations belong outside `upstream/` and must link their parent design and measured fit results. Keep published design sets distinct from confirmed as-built parts.

## Required knowledge-base maintenance

Whenever a change affects decisions, subsystem architecture, component identification/status, build phases, inventories, photographs or illustrations, update the affected files in `docs/knowledge-base/` in the **same change** as the canonical source. This requirement applies to humans and agents working in the repository.

1. Update the authoritative document, inventory, manifest or evidence record first.
2. Review `project/Current-State.md`, `project/Roadmap.md`, `project/Open-Issues.md`, `decisions/Decision-Log.md`, the affected `systems/` and `build/` pages, and the `indexes/Parts.md`, `indexes/Photos.md`, `indexes/Illustrations.md` and `indexes/Documentation.md` entries. Update only those affected, plus `Home.md` when its summary changes.
3. If a source update changes totals or progress, synchronize summaries in the root README and relevant stage READMEs/roadmap. Preserve historical closure snapshots and explain later additions rather than rewriting history.
4. Preserve decision IDs and link superseding decisions; distinguish proposed, frozen, implemented and tested. Keep roadmap stages, manual stages and machine generations separate. A photograph is not a passed acceptance test.
5. Maintain useful YAML properties according to [Maintenance](docs/knowledge-base/Maintenance.md). Update `updated` when the note is substantively reviewed/changed.
6. Use relative Markdown links, including the `.md` extension for notes; do not introduce wikilinks or absolute local paths. After renaming/moving files outside Obsidian, repair links explicitly.
7. Verify local links, new media references, YAML/JSON syntax and the diff. State in the review which knowledge-base pages changed, or why no knowledge-base change was necessary.

## Obsidian and Git

- Use native Obsidian features only; do not install community plugins for this knowledge base.
- Preserve the shared link settings in `.obsidian/app.json`: relative Markdown links and automatic link updates.
- Only `.obsidian/app.json` is intended for version control. Personal layouts, core-plugin choices, appearance, bookmarks, caches and plugin data remain ignored. `.base` views under `docs/knowledge-base/` are shared project files.
- Do not duplicate this repository into a separate vault. Obsidian edits the Git working tree directly and does not perform Git synchronization by itself.
- For the initial setup, leave changes uncommitted and unpushed until the user has reviewed them. Later commit/push actions require the user's authorization for that task.
