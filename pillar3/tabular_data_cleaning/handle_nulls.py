"""
Drill 03 — Replace placeholder values with nulls

Make missing data explicit without guessing meaning.

- Identify placeholder tokens (e.g. `"."`, `"--"`, `"0"`)
- Empty strings (missing values) were handled in drill 2
- Replace them with `pd.NA`
- Apply replacements only to columns where the placeholder truly means “missing”
- Do not touch identifiers or free-text fields

NOTE:
Your job in pipelines is to normalize everything to pd.NA before loading, 
so it maps cleanly to SQL NULL.

"""
