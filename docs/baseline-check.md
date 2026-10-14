# CampusFlow Baseline Check

**Date:** 2026-10-14  
**Baseline branch:** `main`  
**Baseline commit:** `c255a0f` (`r`)  
**Working tree:** Clean, according to the local check supplied by Engineer A  
**Verification source:** Local terminal output supplied by Engineer A

## Existing implementation

The current baseline includes:

- Ticket creation, field validation, and priority calculation.
- Ticket lookup and ID allocation.
- Assignment and the `open -> in_progress -> resolved` lifecycle, including explicit reopening.
- Open-only queue sorted by priority and numeric ID.
- Reports containing total ticket count and status/priority breakdowns.
- JSON persistence with validation and clear storage errors.
- A menu-driven CLI in `main.py`.

## Automated test baseline

Command:

```bash
python -m unittest discover -s tests -v
```

Reported result:

```
Ran 38 tests in 0.011s

OK
```

All 38 tests passed in the supplied output. This is a locally reported result; it has not been independently executed by the assistant environment.

## Coverage represented by the reported suite

- Ticket creation, normalization, invalid inputs, and priority boundaries.
- Ticket lookup and increasing IDs.
- JSON round trips, missing files, malformed JSON, invalid records, duplicate IDs, and save failures.
- Assignment validation and resolved-ticket reassignment restrictions.
- Workflow transition rules and explicit reopening.
- Open queue filtering, sorting, and empty behavior.
- Report counts and zero-safe empty reports.

## Branch decision

The local checkout reports `main...origin/main` with HEAD `c255a0f`. The integration branch `feat/3-cli-integration` was previously found to have diverged from `main` (seven commits ahead and one behind at the time of comparison). Since the CLI integration commit is already present on `main`, treat `main` as the canonical starting point for the new work. Do not merge the divergent integration branch into `main` without a fresh comparison and a concrete reason.

## Original extension requirements

The new extension must be built on the existing implementation, not as a replacement project. The original requirements were:

- Structured ticket notes via `add_note(tickets, ticket_id, author, message)`.
- Case-insensitive title substring search.
- Combined category, status, and priority filters using AND semantics.
- Reports with category counts, resolution percentage, and unresolved-ticket counts, while preserving existing status and priority reporting.
- An Engineering Understanding Check.
- Genuine AI learning records for each engineer, including independently verified corrections/rejections; no fabricated prompts or evidence.

## Post-extension integration checkpoint — 2026-10-14

The baseline above is a historical record of the pre-extension starting point. It is intentionally preserved rather than rewritten as though the extension had already existed at baseline.

### Merged Engineer A work

PR [#13](https://github.com/Bront888/campusflow/pull/13) was merged into `main` on 2026-10-14. It adds structured ticket notes, note validation during JSON persistence, legacy compatibility for records without a `notes` field, and regression tests. Merge commit: `a7d31c94bbdacf68958530b8456a2537b5a46dac`.

### Issue #11 implementation and verification

The search, combined filters, extended reports, notes CLI, and six-question Engineering Understanding Check are implemented in [PR #15](https://github.com/Bront888/campusflow/pull/15). GitHub Actions run [#38598070720](https://github.com/Bront888/campusflow/actions/runs/38598070720) ran the full suite on the PR head using:

```bash
python -m unittest discover -s tests -v
```

Actual output:

```
Ran 75 tests in 0.016s

OK
```

This is verified on the PR branch, not yet on integrated `main`. Review/merge and a post-merge full-suite run remain necessary before declaring the integrated sprint complete.

### Repeatable verification after integration

```bash
git switch main
git pull origin main
git diff --check
python -m unittest discover -s tests -v
```

When recording a later verification, include the date, exact command, actual test count/output, branch, and commit. Do not invent missing output.
