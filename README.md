# translate-english-to-kannada

Simple English → Kannada translator (CLI).

Installation
-----------

1. Create a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Usage
-----

Translate a phrase on the command line:

```bash
python translate.py "hello"
# prints: ಹಲೋ
```

Translate from a file:

```bash
python translate.py -f input.txt
```

Notes
-----
- The script uses `googletrans` for online translation when available.
- If the online translator is unavailable, a small offline fallback dictionary is used.

Testing
-------

Run the included tests with `pytest`:

```bash
pip install pytest
pytest -q
```

If you want additional languages, modify `translate.py` and change the `dest` code.