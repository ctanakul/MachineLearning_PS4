#!/usr/bin/env python

import numpy as np
from math import acos
import json
import matplotlib.pyplot as plt


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))


def nearest_neighbor(train_set, test_set, image_list, data):
    neighbors = {}
    for test_img in test_set:
        i = image_list.index(test_img)
        nearest = -1.0
        nearest_index = -1
        for train_img in train_set:
            j = image_list.index(train_img)
            dist = cosine_similarity(data[i], data[j])
            if dist > nearest:
                nearest = dist
                nearest_img = train_img
        neighbors[test_img] = nearest_img
    # print "neighbors:\n", neighbors
    return neighbors


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
    with open("homework4/dataset.json", "rb") as f:
    	json_data = json.load(f)

    train_images = json_data['train']
    test_images = json_data['test']
    all_images = json_data['images']
    captions = json_data['captions']

    vgg_data = np.load("homework4/vgg_rep.npy")
    pixel_data = np.load("homework4/pixel_rep.npy")

    vgg_NN = nearest_neighbor(train_images, test_images, all_images, vgg_data)
    # print "VGG REP:"
    f = open('vgg.txt', 'w')
    for key in test_images:
        # print vgg_NN[key], all_images.index(vgg_NN[key]), cap
        cap = captions[vgg_NN[key]]
        f.write(cap + '\n')
    f.close()

    pix_NN = nearest_neighbor(train_images, test_images, all_images, pixel_data)
    # print "PIXEL REP:"
    f = open('pixel.txt', 'w')
    for key in test_images:
        cap = captions[pix_NN[key]]
        # print pix_NN[key], all_images.index(pix_NN[key]), cap
        f.write(cap + '\n')
    f.close()

    # for key in test_images:
    #     plt.subplot(131)
    #     plt.imshow(plt.imread("homework4/images/" + key))
    #     plt.subplot(132)
    #     plt.imshow(plt.imread("homework4/images/" + vgg_NN[key]))
    #     plt.subplot(133)
    #     plt.imshow(plt.imread("homework4/images/" + pix_NN[key]))
    #     plt.show()

    return


def main():
    # a = np.array([0.1,0.56,0.0])
    # b = np.array([1.0,1.0,1.0])
    # print cosine_similarity(a, b)

    # problem_5()

    problem_7()

if __name__=='__main__':
    main()
