""" 
python3 ./globt.py -p ./ -e txt
"""
from glob import glob
import argparse


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', type=str,
                        required=True, help='dir path of file.')
    parser.add_argument('-e', '--ext', dest='ext', type=str,
                        required=True, help='ext name of  file.')
    args = parser.parse_args()
    

    
    txts = glob(f'{args.path}/*.{args.ext}')
    print(txts)