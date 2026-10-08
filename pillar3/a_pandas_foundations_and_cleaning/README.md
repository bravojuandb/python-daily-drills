# A — Pandas Foundations & Cleaning

Build small tables, select data, and clean values without losing their meaning.
Start with Python functions, lists, dictionaries, and an environment with pandas.

## Study order

| Subchapter | Drills | Focus |
| --- | --- | --- |
| [a — DataFrame basics](a_dataframe_basics/README.md) | 4 | Create, inspect, select, filter, read CSV |
| [b — Missing values and text](b_missing_values_and_text/README.md) | 5 | Missingness, column rules, normalization, validation |
| [c — Types and identifiers](c_types_and_identifiers/README.md) | 4 | Nullable integers, identifiers, conversion reports |


## Shared rules

- Return new pandas objects without modifying inputs or printing. Only a/04
  reads a file; it must leave the source unchanged. Put demonstrations under
  `if __name__ == "__main__":`.
- Inputs satisfy the stated prerequisites; validate only errors named in the
  prompt. Tables have unique string column names and scalar cells. Row indexes
  have unique integer labels that fit `int64`; labels need not be consecutive.
- Preserve row order, index labels/name, and Series name unless specified.
  Unchanged columns keep their values and dtypes. Empty inputs are valid and
  retain the required columns/dtypes; validation masks are empty too.
- For b and c, text Series use `dtype="string"` and `pd.NA`, except c/02's raw
  input. Lists in examples show Series values; dictionaries of lists show
  DataFrame columns. They are display shorthand, not alternative return types.
- Use pandas operations and standard-library helpers. Earlier solved helpers
  may be reused. Documentation is allowed; no loop-only restrictions apply.

Predict a normal case and an edge case before running your attempt. Check values,
shape, dtypes, index, and input preservation with small synthetic data. Use pandas
testing helpers when useful; add tests as each drill is attempted.

For cost questions, define rows, columns, and total text length as relevant.
Include temporary masks, copies, and returned data; count more than API calls.

## Learning references

These original prompts use the concepts in the [official pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
and Wes McKinney's *Python for Data Analysis*, [chapter 5](https://wesmckinney.com/book/pandas-basics)
and [chapter 7](https://wesmckinney.com/book/data-cleaning). Subchapter guides link
the relevant sections.
