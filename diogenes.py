#!/usr/bin/env python3

"""
Diogenes - a logic-based notemaking application for the command line.
"""

from proposition import *
from operation import *
from inference import Inference

def main():
    p = AtomicProposition("p")
    q = AtomicProposition("q")

    a = CompoundProposition(p, Conjunction, q)
    b = CompoundProposition(a, Conjunction, q)
    c = CompoundProposition(b, Conjunction, a)

    #inf = Inference(b, q, a)
    infb = Inference(b, a, q)
    #inf2 = Inference(p, a)

    d = CompoundProposition(p, Conjunction, q)
    e = CompoundProposition(d, Conjunction, q)
    #infb.print()

    for op in Operation.__subclasses__():
        print(f"{op.name}:\t{op.truth_makers()}")

if __name__ == "__main__":
    main()