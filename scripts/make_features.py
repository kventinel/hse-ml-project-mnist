#!/usr/bin/env python3
import argparse

import ast
import numpy as np
import pandas as pd


MAX = 256


def _parse_args():
    parser = argparse.ArgumentParser('make features from csv with images')
    parser.add_argument('input', help='path to csv with images')
    parser.add_argument('output', help='path to output csv with features')
    return parser.parse_args()


def mean(img):
    return np.mean(img)


def count(img):
    return np.sum(img > 0)


def vert_symmetry(img):
    symline = img.shape[0] // 2
    return np.mean(img[:symline]) - np.mean(img[symline:])


def hor_symmetry(img):
    symline = img.shape[1] // 2
    return np.mean(img[:, :symline]) - np.mean(img[:, symline:])


def vert_mass_center(img):
    mat = np.repeat(np.arange(img.shape[1]).reshape(-1, 1), img.shape[0], axis=1)
    return np.sum(mat * img) / np.sum(img)


def hor_mass_center(img):
    mat = np.repeat(np.arange(img.shape[0]).reshape(1, -1), img.shape[1], axis=0)
    return np.sum(mat * img) / np.sum(img)


def vert_viola(img):
    symline1 = img.shape[0] // 4
    symline2 = symline1 * 3
    return (np.mean(img[:symline1]) + np.mean(img[symline2:])) / 2 - np.mean(img[symline1:symline2])


def hor_viola(img):
    symline1 = img.shape[1] // 4
    symline2 = symline1 * 3
    return (np.mean(img[:, :symline1]) + np.mean(img[:, symline2:])) / 2 - np.mean(img[:, symline1:symline2])


def all_viola(img):
    symline1 = img.shape[0] // 2
    symline2 = img.shape[1] // 2
    return (
        np.mean(img[:symline1, :symline2]) + np.mean(img[symline1:, symline2:]) -
        np.mean(img[:symline1, symline2:]) - np.mean(img[symline1:, :symline2])
    ) / 2


if __name__ == '__main__':
    args = _parse_args()
    data = pd.read_csv(args.input)
    idxs = data['idx'].values
    images = [np.array(ast.literal_eval(image)) for image in data['image'].values]
    labels = data['label'].values
    pd.DataFrame({
        'idx': idxs,
        'mean': [mean(image) for image in images],
        'count': [count(image) for image in images],
        'vert_symmetry': [vert_symmetry(image) for image in images],
        'hor_symmetry': [hor_symmetry(image) for image in images],
        'vert_mass_center': [vert_mass_center(image) for image in images],
        'hor_mass_center': [hor_mass_center(image) for image in images],
        'vert_viola': [vert_viola(image) for image in images],
        'hor_viola': [hor_viola(image) for image in images],
        'all_viola': [all_viola(image) for image in images],
        'label': labels
    }).to_csv(args.output)
