# This will collect items in the list created upon first call, not creating new list between calls
def appender(item, collection=[]):
    collection.append(item)
    return collection
