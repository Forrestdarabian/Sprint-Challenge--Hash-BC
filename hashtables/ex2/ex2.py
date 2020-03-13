#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)
    # first were inserting the hastable, source, and destination
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    # then set current location to none
    current_location = "NONE"
    # finally create a for loop that retrieves a new current location
    for i in range(length-1):
        route[i] = hash_table_retrieve(hashtable, current_location)
        current_location = route[i]
    # output an array of strings with the entire route of the trip
    return route
