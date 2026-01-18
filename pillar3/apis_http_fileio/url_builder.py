"""
Drill 1 (15 min) — URL Builder (pure function)

Goal: Make build_url() bulletproof and testable.

Tasks
	1.	Create a new drill file 
	2.	Implement build_url(base_url, dataset, params) so it:
	•	strips trailing / from base_url
	•	supports list params via doseq=True 
	•	returns a fully formed URL string

Definition of Done
	•	Running the file prints exactly one URL.
	•	The URL contains:
	•	.../ds-059341?
	•	cxt_indicators=QUANTITY_KG&cxt_indicators=VALUE_EUR (two entries, same key)
	•	You can change base_url to end with / and output stays correct.

Mini-test you can do without pytest
	•	Use assert "cxt_indicators=QUANTITY_KG" in url

https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/
ds-059341?
format=JSON&
cxt_free_iso=CN&
cxt_free_iso=JP&
cxt_free_iso=KR&
cxt_free_iso=US&
cxt_nc=8703&
cxt_eu_flux=1&
cxt_indicators=VALUE_EUR&
lang=EN

"""
from pathlib import Path
from urllib.parse import urlencode


def build_url(base_url: str, dataset: str, params: dict) -> str: 
    # doseq=True: expands lists into repeated keys 
    return f"{base_url.rstrip('/')}/{dataset}?{urlencode(params, doseq=True)}"


def main():
    base_url = "https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/"
    dataset = "DS-059332"
    params = {
        "format": "JSON",
        "lang": "EN",
        "cxt_free_iso": ["CN", "JP", "KR", "US"],
        "cxt_nc": "8703",
        "cxt_eu_flux": "1",
        "cxt_indicators": ["QUANTITY_KG", "VALUE_EUR"],
    }

    url = build_url(base_url, dataset, params)

    assert url.count("cxt_indicators=") == 2
    assert "cxt_indicators=QUANTITY_KG" in url
    assert "cxt_indicators=VALUE_EUR" in url

    print(url)


if __name__ == "__main__":
    main()