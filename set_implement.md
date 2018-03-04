* The set() in python3 actually implement with dictionary, which owns O(1) time to access to object
* The key in dic and element in set needs to hashable.
* Since set is not immutable, and cannot hash. There is a method frozenset to make set immutable, and can be hash.