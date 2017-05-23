#!/usr/bin/env python

import numpy as np
from math import acos
import json


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))


def problem_5():
    with open("homework4/cnn_dataset.json", "rb") as f:
    	json_data = json.load(f)

    imgs = ['mj1', 'mj2', 'cat']
    for rep in ['pixel_rep', 'vgg_rep']:
        for i, img in enumerate(imgs):
            print rep, "cosine similarity between", img, "and", imgs[(i+1)%len(imgs)], "is:",
            print cosine_similarity(json_data[rep][img], json_data[rep][imgs[(i+1)%len(imgs)]])

    return


def problem_7():
    with open("homework4/cnn_dataset.json", "rb") as f:
    	json_data = json.load(f)

    imgs = ['mj1', 'mj2', 'cat']
    for rep in ['pixel_rep', 'vgg_rep']:
        for i, img in enumerate(imgs):
            print rep, "cosine similarity between", img, "and", imgs[(i+1)%len(imgs)], "is:",
            print cosine_similarity(json_data[rep][img], json_data[rep][imgs[(i+1)%len(imgs)]])

    return


def main():
    a = np.array([0.1,0.56,0.0])
    b = np.array([1.0,1.0,1.0])
    print cosine_similarity(a, b)

    problem_5()

    problem_7()

if __name__=='__main__':
    main()
