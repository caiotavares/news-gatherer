# News Gatherer

## Installation

```bash
git clone https://github.com/caiotavares/news-gatherer
cd news-gatherer
pip3 install .
```

## API-KEY

Before you can use `news-gatherer`, you need to create an api-key at https://open-platform.theguardian.com/access/ and export it as an env-var named `API_KEY`

## Usage

```bash
cd src
./search.py <CMD> <ARGUMENT>
```

## Commands Available

### `from-date`

Gather articles that were published on a given date. YYYY-MM-DD format.

Example

```bash
./search.py from-date 2018-11-01
```

### `q`

Build a search query

Example

```bash
./search.py q 'brazil elections'
```
