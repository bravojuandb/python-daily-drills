# Pillar 2 — Data Structures & Problem Solving

This pillar is being restructured. Its previous material is preserved in two
local archives, excluded from Git by the `/archive/` rule in `.gitignore`:

- `archive/pillar2/legacy1/`: the contents of the former `pillar2/legacy/`
  directory, grouped by their original chapter names.
- `archive/pillar2/legacy2/`: the six letter-prefixed chapters and
  supporting files that were in `pillar2/` before this restructuring.

Both archives contain historical learning material, including unfinished drills.
The new active chapter structure has not been defined yet.

The existing chapter tests are archived in
`archive/pillar2/legacy2/tests/` and import the archived modules from
`archive.pillar2.legacy2`. Archiving the exercises does not establish
their correctness or completion.

Running `pytest` from the repository root excludes `legacy/` and `archive/`
directories. CI uses the same exclusions and currently allows an empty suite
while the new tests are being developed. The local archives are not included
in new clones of the repository.
