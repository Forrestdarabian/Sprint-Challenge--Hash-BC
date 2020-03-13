#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


# * If we store each weight's list index as its value,
#  we can then check to see if the hash table contains an entry for `limit - weight`.
#  If it does, then we've found the two items whose weights sum up to the `limit`!


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # first, a for loop is created that is checking to see
    # if the hash table contains an entry for `limit - weight`
    for i in range(length):
        y = hash_table_retrieve(ht, limit - weights[i])
        # if it does, were returning the item weights of the two packages...their sum is the weight limit
        if (y is not None):
            return (i, y)
        # if it doesnt, we insert it back into the hashtable and return None
        else:
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
