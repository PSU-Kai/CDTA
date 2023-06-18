# merger script
import argparse
import glob
import pandas as pd
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, metavar='', nargs='+', help = 'name of the files to be merged')
ap.add_argument('-o', '--output', required=True, help = 'name of the files to be merged')
args = ap.parse_args()

file_num = 0
li = []
print(args.file)
if len(set(args.file)) == len(args.file):
    for filename in args.file:
        print(filename)
        df = pd.read_csv(filename, index_col = None, header=0, skiprows=[0])
        print(df)
        df['Actor']+= '_' + str(file_num)
        file_num += 1
        li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    frame = frame.sort_values(by=["time stamp"], ascending=True)
    frame.to_csv(args.output, index = True)
    print(frame)
else:
    print("Error! list of file names contains duplicates")
    quit()
