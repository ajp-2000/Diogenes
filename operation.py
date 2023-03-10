"""
The purpose of having objects for each operation is to have the truth-functional properties of that operation written
into the object, rather than relying on externally defined rules.
We don't want to create a new instance every time an operation is used in building up a proposition, but every operation
has different truth-functional properties. So we create an informal interface, by writing these properties into class 
methods in subclasses of Operation.
"""

class Operation:
    name = ""
    place_count = 1

    # The placeholder method returning the truth value of [op][place1] or [place1][op][place2]
    @classmethod
    def eval(cls, places):
        pass

    # Return the combinations of boolean values of length n: used by truth_table() and truth_makers()
    @classmethod
    def bool_combs(cls, n):
        combs = []
        for i in range(2 ** n):
            comb = []
            for j in range(n):
                comb.append(not bool((i>>j) & 1))
            
            combs.append(comb)
        
        return combs

    # Return the operation's truth table as a dict mapping either bool or [bool][bool] to bool
    @classmethod
    def truth_table(cls):
        table = {}
        keys = cls.bool_combs(cls.place_count)
        for key in keys:
            table[tuple(key)] = cls.eval(key)
        
        return table

    # Return the list of (lists of) truth-value/s which spit out True when combined with the operation
    @classmethod
    def truth_makers(cls):
        return [vals for vals in cls.bool_combs(cls.place_count) if cls.eval(vals)]
    
    @classmethod
    def print_truth_table(cls):
        table = cls.truth_table()
        print(f"Truth table for {cls.name}:")
        for row in table:
            print(f"{row}\t{table[row]}")
            
        print("")


# Define the operations of TFL
class Conjunction(Operation):
    name = "&"
    place_count = 2

    @classmethod
    def eval(cls, places):
        return places[0] and places[1]

class Disjunction(Operation):
    name = "∨"
    place_count = 2

    @classmethod
    def eval(cls, places):
        return places[0] or places[1]

class Conditional(Operation):
    name = "→"
    place_count = 2

    @classmethod
    def eval(cls, places):
        if places[0] and not places[1]:
            return False
        
        return True

class Biconditional(Operation):
    name = "↔"
    place_count = 2

    @classmethod
    def eval(cls, places):
        return places[0] == places[1]

class Negation(Operation):
    name = "~"
    place_count = 1

    @classmethod
    def eval(cls, places):
        return not places[0]