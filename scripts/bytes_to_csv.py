#!/usr/bin/env python3
import argparse

import numpy as np
import pandas as pd


N_COLS = 28
N_ROWS = 28
SEED = 42


def _parse_args():
    parser = argparse.ArgumentParser('Make csv from bytes files (images and labels)')
    parser.add_argument('img', help='path to images bytes')
    parser.add_argument('labels', help='path to labels')
    parser.add_argument('csv', help='path to save csv')
    parser.add_argument('--nimages', type=int, default=1000, help='save only nimages (default: %(default)s)')
    return parser.parse_args()


def bytes_to_int(byte_data):
    return int.from_bytes(byte_data, byteorder='big')


if __name__ == '__main__':
    # Read data part
    args = _parse_args()
    with open(args.img, 'rb') as fin:
        img_data = fin.read()
    with open(args.labels, 'rb') as fin:
        labels_data = fin.read()
    n_images = bytes_to_int(img_data[4:8])
    if n_images != bytes_to_int(labels_data[4:8]):
        print('Differenc count of images in images {} and labels {}'.format(n_images, bytes_to_int(labels_data[4:8])))
        exit(1)
    print('Parse {} images'.format(n_images))

    # Random choise part
    np.random.seed(SEED)
    idxs = np.arange(n_images)
    np.random.shuffle(idxs)
    idxs = idxs[:args.nimages]

    # Parse data part
    images = []
    labels = []
    for i in idxs:
        start_img_byte = 16 + i * N_COLS * N_ROWS
        start_label_byte = 8 + i
        img = [
            [
                bytes_to_int([img_data[start_img_byte + j * N_COLS + k]]) for k in range(N_COLS)
            ] for j in range(N_ROWS)
        ]
        label = bytes_to_int([labels_data[start_label_byte]])
        images.append(img)
        labels.append(label)

    # Save csv part
    df = pd.DataFrame({
        'idx': idxs,
        'image': images,
        'label': labels
    })
    df.to_csv(args.csv)
