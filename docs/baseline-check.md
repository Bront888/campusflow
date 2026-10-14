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

## Known gaps before the extension

The new extension must be built on the existing implementation, not as a replacement project. Requirements still to implement and verify:

- Structured ticket notes via `add_note(ticket_id, author, message)`.
- Case-insensitive title substring search.
- Combined category, status, and priority filters using AND semantics.
- Reports with category counts, resolution percentage, and unresolved-ticket counts, while preserving existing status and priority reporting.
- An Engineering Understanding Check.
- Genuine AI learning records for each engineer, including independently verified corrections/rejections; no fabricated prompts or evidence.

## Next verification

After the extension is integrated, rerun the full test suite on the integrated `main`, demonstrate the new behavior end to end, and update this record with the actual command output. Do not mark future checks complete before they are performed.
