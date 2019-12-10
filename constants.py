import os

CUR = os.path.dirname(__file__)
FEATURES = os.path.join(CUR, 'data/features')
TRAIN = os.path.join(FEATURES, 'train.csv')
TEST = os.path.join(FEATURES, 'test.csv')

K_MEANS_CLUSTERING_FEATURES = ['mean', 'count', 'vert_mass_center', 'vert_symmetry', 'vert_viola']
