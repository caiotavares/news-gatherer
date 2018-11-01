# News Gatherer

## Installation

```bash
git clone https://github.com/caiotavares/news-gatherer
cd news-gatherer
pip3 install .
```

## Usage

`python3 src/app.py <CMD> <ARGUMENT>`

## Commands Available

### `from-date`

Gather articles that were published on a given date. YYYY-MM-DD format.

Example

```bash
python3 src/app.py from-date 2018-11-01
```

### `q`

Build a search query

Example

```bash
python3 src/app.py q 'brazil elections'
```
