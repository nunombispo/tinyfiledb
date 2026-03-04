"""Quick demo of tinyfiledb: insert, get, update, all, delete."""

from tinyfiledb import FileDB

db = FileDB("demo_db.json")

print("=== Insert ===")
id1 = db.insert({"title": "Write blog post", "done": False})
id2 = db.insert({"title": "Publish to PyPI", "done": True})
print(f"Inserted: {id1}, {id2}")

print("\n=== Get one ===")
print(db.get(id1))

print("\n=== All records ===")
print(db.all())

print("\n=== Update ===")
db.update(id1, {"done": True})
print(db.get(id1))

print("\n=== Delete ===")
db.delete(id2)
print(f"Remaining: {db.all()}")
