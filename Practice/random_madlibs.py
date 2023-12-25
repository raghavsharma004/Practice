# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:32:03 2023

@author: raghav
"""

from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()