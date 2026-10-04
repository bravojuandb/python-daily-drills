# a — DataFrame Basics

Follow the [chapter rules](../README.md). One row represents one inventory record.

| Drill | New idea |
| --- | --- |
| [01 — Create and inspect](drill_01_create_and_inspect.py) | Table shape, columns, and dtypes |
| [02 — Select columns](drill_02_select_columns.py) | Ordered selection that remains a DataFrame |
| [03 — Filter rows](drill_03_filter_rows.py) | A condition selects rows while preserving labels |
| [04 — Read CSV as strings](drill_04_read_csv_as_strings.py) | Control interpretation at the file boundary |

<details>
<summary>Optional references and hints — after proposing an approach</summary>

- 01: pandas' [table introduction](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html); inspect `shape`, `columns`, and `dtypes`.
- 02–03: [selecting subsets](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html); compare a column label, a list of labels, and a Boolean mask.
- 04: [reading tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html) and [CSV options](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html); examine dtype and missing-value settings.
- Further explanation: McKinney, [chapter 5](https://wesmckinney.com/book/pandas-basics), sections 5.1–5.2.

</details>
