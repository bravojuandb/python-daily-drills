# c — Types & Identifiers

Start after missing values and text. Follow the [chapter rules](../README.md).

| Drill | New idea |
| --- | --- |
| [01 — Parse nullable integers](drill_01_parse_nullable_integers.py) | Numeric values can coexist with missingness |
| [02 — Preserve identifier strings](drill_02_preserve_identifier_strings.py) | Reject lossy assumptions about raw identifiers |
| [03 — Validate identifier format](drill_03_validate_identifier_format.py) | Width and character rules without numeric conversion |
| [04 — Report invalid conversions](drill_04_report_invalid_conversions.py) | Pair converted values with traceable failures |

<details>
<summary>Optional references and hints — after proposing an approach</summary>

- 01: pandas' [nullable integers](https://pandas.pydata.org/docs/user_guide/integer_na.html); distinguish `Int64` from NumPy's `int64`.
- 02–03: pandas' [text guide](https://pandas.pydata.org/docs/user_guide/text.html); explicit string dtype, missingness, and full-string validation.
- 04: combine a validity mask with conversion and row selection. Missing input and rejected text need separate treatment.
- Further explanation: McKinney, [chapter 7](https://wesmckinney.com/book/data-cleaning), sections 7.1, 7.3, and 7.4.

</details>
