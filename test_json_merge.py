from util import update_json, JSONObject

def test_simple_update() -> None:
    existing: JSONObject = {"name": "John", "age": 30}
    updates: JSONObject = {"age": 31}
    expected = {"name": "John", "age": 31}
    assert update_json(existing, updates) == expected


def test_nested_update() -> None:
    existing: JSONObject = {"user": {"name": "John", "age": 30}}
    updates: JSONObject = {"user": {"age": 31}}
    expected = {"user": {"name": "John", "age": 31}}
    assert update_json(existing, updates) == expected


def test_new_field() -> None:
    existing: JSONObject = {"name": "John"}
    updates: JSONObject = {"age": 30}
    expected = {"name": "John", "age": 30}
    assert update_json(existing, updates) == expected


def test_deep_new_field() -> None:
    existing: JSONObject = {"user": {"name": "John"}}
    updates: JSONObject = {"user": {"age": 30}}
    expected = {"user": {"name": "John", "age": 30}}
    assert update_json(existing, updates) == expected


def test_list_update() -> None:
    existing: JSONObject = {"scores": [1, 2, 3]}
    updates: JSONObject = {"scores": [4, 5, 6]}
    expected = {"scores": [4, 5, 6]}
    assert update_json(existing, updates) == expected


def test_mixed_types() -> None:
    existing: JSONObject = {"data": {"value": 10}}
    updates: JSONObject = {"data": "new value"}
    expected = {"data": "new value"}
    assert update_json(existing, updates) == expected


def test_null_values() -> None:
    existing: JSONObject = {"name": "John", "age": 30}
    updates: JSONObject = {"age": None}
    expected = {"name": "John", "age": None}
    assert update_json(existing, updates) == expected
