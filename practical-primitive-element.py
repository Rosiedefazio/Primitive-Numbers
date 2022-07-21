from enum import unique
from operator import eq
from xml.dom.minidom import Element
import numpy

def prim_elem(elem,mod): 
    powerlist = []
    equivlist=[]
    for i in range(1,mod): 
        power = elem ** i
        powerlist = powerlist + [power]
        equiv = power % mod
        equivlist = equivlist + [equiv]
    
#check is the element is a primitive element 
    equivlist = numpy.unique(equivlist)
    return equivlist

def Find_all_prim_elements(mod): 
    modlist = list(range(1,mod))
    primitive = []
    for x in  modlist: 
        y = prim_elem(x, mod)
        if len(y) == (mod-1): primitive = primitive +[x]
    if primitive != []: 
        print(f"The primitive elements of Modulo {mod} are {primitive}")
    else: print(f"There are no primitve elements in Modulo {mod}.")


