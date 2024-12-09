import objaverse.xl as oxl
import pandas as pd
import time



if __name__ == '__main__':
    alignment_annotations = pd.read_csv('alignment_annotations.csv')
    objs = oxl.download_objects(objects=alignment_annotations.head(2), download_dir='~/.objaverse', processes=6)
    print(objs)