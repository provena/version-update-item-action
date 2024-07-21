from typing import Any, Dict, List, Union, cast, Mapping

JSONValue = Union[str, int, float, bool, None, Mapping[str, Any], List[Any]]
JSONObject = Dict[str, JSONValue]

def update_json(existing: JSONObject, updates: JSONObject) -> JSONObject:
    """
    
    Merges an update json object over an existing one

    Args:
        existing (JSONObject): The existing JSON metadata
        updates (JSONObject): The set of updates (which can either add or overwrite fields)

    Returns:
        JSONObject: The updated json object
    """
    def merge(current: JSONValue, update: JSONValue) -> JSONValue:

        def merge_key(key: str, current: dict, update: dict) -> JSONValue:
            if key in current and key in update:
                return merge(current[key], update[key])
            elif key in current and key not in update:
                return current[key]
            else:
                return update[key]

        if isinstance(current, dict) and isinstance(update, dict):
            return {
                key: merge_key(key, current, update)
                for key in set(current) | set(update)
            }
        elif isinstance(current, list) and isinstance(update, list):
            return update
        else:
            return update

    return cast(JSONObject, merge(existing, updates))