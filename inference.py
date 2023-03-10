"""
A class for attempted inferences.
An inference is the smallest possible building block of a deduction: elementary, formal, without any redundant premises,
and order-sensitive. I.E. we can infer p from p & q, but not from (p & q) & r; and we can infer p & q from premises p and q,
but not from premises q and p.
We do this so that we can approach deductions by trying every possible iteration of propositions to brute-force them. If an 
inference is valid, the ordering is preserved, which means we can eventually read off labels like "&I 3, 5".
Because inferences are elementary, we only have to look one level up/down from the propositions we are given. Also inferences
have either one or two premises, depending on the kind of step we are attempting to find.
Longer chains of propositions with intermediary steps are deductions, dealt with in a seperate class (via checking 
for inferences).
Bi/conditional and negation introduction aren't captured by inferences, because these require assumption blocks, which 
Diogenes implements structurally.
"""

from operation import *

class Inference:
    prem1 = None
    prem2 = None
    conc = None
    valid = False

    def __init__(self, conc, prem1, prem2 = None):
        self.prem1 = prem1
        self.prem2 = prem2
        self.conc = conc

        self.valid = self.eval()
    
    # Check the validity of the inference as an elimination
    def elim_eval(self):
        return False

    # Try to reach the conclusion by introduction from a non-empty list of components of the conclusion, which we can
    # take to be true because they are whole premises
    def intro_eval(self, components):
        print(f"Components: {[comp.name for comp in components]}")
        # Try each operation
        for op in Operation.__subclasses__():
            print(f"Trying {op.name}")
            truth_makers = op.truth_makers()

        return False

    # Check the (logical, formal) validity of the inference
    def eval(self):
        # If there's only one premise, we must be eliminating
        if not self.prem2:
            if self.elim_eval():
                return True
        
        if self.conc.atomic:
            # If the conclusion is atomic, we're eliminating
            if self.elim_eval():
                return True
        else:
            # If the conclusion is an immediate component of one of the premises, we're eliminating
            prem_places = []
            for prem in [self.prem1, self.prem2]:
                if not prem.atomic:
                    prem_places.append(prem.places[0])
                    if len(prem.places) > 1:
                        prem_places.append(prem.places[1])
            
            for prem in prem_places:
                if self.conc.same_as(prem):
                    if self.elim_eval():
                        return True
            
            # If one of the premises is an immediate component of the conclusion, we're introducing
            components = []
            for prem in [self.prem1, self.prem2]:
                if self.conc.places[0].same_as(prem) or (len(self.conc.places)>1 and self.conc.places[1].same_as(prem)):
                    components.append(prem)
            
            if components and self.intro_eval(components):
                return True
        
        # If none of the above, the conclusion doesn't immediately follow from the premises
        return False

    def print(self):
        print(f"P1. {self.prem1.name}")
        if self.prem2:
            print(f"P2. {self.prem2.name}")
        print(f"C.  {self.conc.name}")

        if self.valid:
            print("Inference valid.")
        else:
            print("Inference invalid.")