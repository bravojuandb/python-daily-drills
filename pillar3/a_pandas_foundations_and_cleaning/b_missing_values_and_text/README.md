# b — Missing Values & Text

Start after DataFrame basics. Follow the [chapter rules](../README.md).
Use `pd.Series(values, dtype="string")` for the text examples.

| Drill | New idea |
| --- | --- |
| [01 — Trim and normalize blanks](drill_01_trim_and_normalize_blanks.py) | Empty text and missing values |
| [02 — Replace column placeholders](drill_02_replace_column_placeholders.py) | The same token can mean different things by column |
| [03 — Normalize text by rule](drill_03_normalize_text_by_rule.py) | Canonical labels and explicit aliases |
| [04 — Validate mixed text](drill_04_validate_mixed_text_values.py) | Validation reports validity without changing values |
| [05 — Preserve free text](drill_05_preserve_free_text.py) | Apply a known rule while protecting another field |

<details>
<summary>Optional references and hints — after proposing an approach</summary>

- 01–03: pandas' [text tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html) and [text guide](https://pandas.pydata.org/docs/user_guide/text.html); explore string operations and value replacement.
- 01–02: McKinney, [chapter 7](https://wesmckinney.com/book/data-cleaning), sections 7.1–7.2, for missingness and replacement policies.
- 04: the text guide's full-string matching operations; a partial match is insufficient. Regex is allowed, not required.
- 05: reuse the status rule from 03 and select its target column explicitly.

</details>
