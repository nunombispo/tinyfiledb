# tinyfiledb

A lightweight file-based database for Python projects. No server, no migrations, no dependencies — just a local JSON file and a simple API.

If this project was useful to you, consider donating to support the Developer Service Blog: https://buy.stripe.com/bIYdTrggi5lZamkdQW

## Install

```bash
pip install tinyfiledb
```

## Usage

```python
from tinyfiledb import FileDB

db = FileDB("mydata.json")

# Insert a record
user_id = db.insert({"name": "Alice", "role": "admin"})

# Get, update, list, delete
print(db.get(user_id))
db.update(user_id, {"role": "superadmin"})
print(db.all())
db.delete(user_id)
```

## API

- `insert(record)` — add a record, get back an auto-generated ID
- `get(id)` — retrieve one record by ID (returns `None` if not found)
- `all()` — return every record as a dict
- `update(id, data)` — merge data into an existing record; returns `True` if found
- `delete(id)` — remove a record; returns `True` if found

## License

MIT
