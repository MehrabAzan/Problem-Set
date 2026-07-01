def get_last(items):
    if items:
        return items[len(items) - 1]
    else:
        return None

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
print(get_last(items))