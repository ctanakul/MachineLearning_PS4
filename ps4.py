#!/usr/bin/env python
import numpy as np
from math import acos

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))

def main():
    a = np.array([0.1,0.56,0])
    b = np.array([1,1,1])
    print cosine_similarity(a, b)

if __name__=='__main__':
    main()
