import json
import uuid
from pathlib import Path


class FileDB:
    def __init__(self, filepath: str = "db.json"):
        self.path = Path(filepath)
        if not self.path.exists():
            self._write({})

    def _read(self) -> dict:
        with open(self.path, "r") as f:
            return json.load(f)

    def _write(self, data: dict):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def insert(self, record: dict) -> str:
        data = self._read()
        record_id = str(uuid.uuid4())[:8]
        data[record_id] = record
        self._write(data)
        return record_id

    def get(self, record_id: str) -> dict | None:
        return self._read().get(record_id)

    def all(self) -> dict:
        return self._read()

    def update(self, record_id: str, new_data: dict) -> bool:
        data = self._read()
        if record_id not in data:
            return False
        data[record_id].update(new_data)
        self._write(data)
        return True

    def delete(self, record_id: str) -> bool:
        data = self._read()
        if record_id not in data:
            return False
        del data[record_id]
        self._write(data)
        return True
