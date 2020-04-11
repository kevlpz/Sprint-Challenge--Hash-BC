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
    route = [None] * length

    index = 1
    for i in range(length):
        print(tickets[i].source)
        if tickets[i].source == "NONE":
            
            route[0] = tickets[i].destination
        else:
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
   
    while index < length:
        route[index] = hash_table_retrieve(hashtable, route[index - 1])
        index += 1
    route = route[:len(route) - 1]
    
    return route