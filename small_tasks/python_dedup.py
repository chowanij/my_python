from collections import defaultdict

def merge_remove_dup(a:list, b: list) -> list:
    idx = {}
    result = []
    merged = a + b
    for log_item in merged:
        if  log_item["id"] in idx and (idx[log_item["id"]]["updated_at"] < log_item["updated_at"]):
            idx[log_item["id"]] = log_item
        else: 
            idx[log_item["id"]] = log_item
    result = [value for _, value in idx.items()]
    return sorted(result, key= lambda x: int(x["id"].lstrip("u")))




    


if __name__ == "__main__":
    a = [
        {"id": "u15", "updated_at": 8, "payload": {"x": 9}},
        {"id": "u1", "updated_at": 10, "payload": {"x": 1}},
        {"id": "u2", "updated_at": 5, "payload": {"x": 2}},
    ]
    b = [
        {"id": "u15", "updated_at": 125, "payload": {"x": 9}},
        {"id": "u2", "updated_at": 8, "payload": {"x": 9}},
        {"id": "u3", "updated_at": 1, "payload": {"x": 7}},
    ]
    print(merge_remove_dup(a, b))