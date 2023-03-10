"""
We use two classes for atomic and compound propositions respectively, each subclasses of an unused Proposition class.
Each proposition has a name, which will be its display name unless the sentence using it has been assigned a different
(more elaborate) name. The proposition's name will be its bare-bones structure, whereas the user may give a sentence 
whatever label he likes.
The term 'name' we reserve for a proposition's name, i.e. structure; 'label' refers to the name the user gives a sentence
We set it as a convention that atomic propositions must have single-character names. Compound propositions' names are the
logical structure of their composition, e.g. the proposition which is the conjunction of p and q has name 'p & q'.
"""

class Proposition:
    name = "empty"
    atomic = True

    # Wrap the name in brackets if it needs them (for combining the prop into compounds)
    def bracket(self):
        if (not self.atomic) and len(self.places) == 2:
            return "(" + self.name + ")"
        
        return self.name

    # Check whether another proposition is a deep replica of this one
    def same_as(self, prop):
        pass

class AtomicProposition(Proposition):
    def __init__(self, name):
        if len(name) > 1:
            # This should never be reached, but just in case
            raise ValueError("Non-atomic name for atomic proposition")
        
        self.name = name
    
    def same_as(self, prop):
        return self.name == prop.name
    
# A compound proposition is always one or two propositions (called the two places), combined with one operator
class CompoundProposition(Proposition):
    places = []
    op = None
    name = ""

    def __init__(self, place1, op, place2 = None):
        # Assign values
        self.atomic = False
        self.places = [place1]
        if place2:
            self.places.append(place2)
        self.op = op

        # PLACEHOLDER: check the operation matches the number of places supplied

        # Assemble the name
        if place2 == None:
            self.name = op.name + place1.bracket()
        else:
            self.name = place1.bracket() + " " + op.name + " " + place2.bracket()
    
    def same_as(self, prop):
        if prop.atomic:
            return False
        
        if not self.places[0].same_as(prop.places[0]):
            return False
        if self.op.name != prop.op.name:
            return False
        
        if len(self.places) > 1:
            if len(prop.places) == 1:
                return False
            if not self.places[1].same_as(prop.places[1]):
                return False
        
        return True