import numpy as np
import cv2 as cv
from glob import glob
import os.path as osp
import json
import argparse


def run_calib(args):
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((args.num_y * args.num_x, 3), np.float32)
    objp[:, :2] = np.mgrid[0:args.num_y, 0:args.num_x].T.reshape(-1, 2)
    objp[:, 0] = args.len_y * objp[:, 0]
    objp[:, 1] = args.len_x * objp[:, 1]
    objpoints = []
    imgpoints = []

    images = glob(f'{args.path}/*.{args.ext}')
    for fname in images:
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, corners = cv.findChessboardCorners(
            gray, (args.num_y, args.num_x), None)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            if args.verbose:
                cv.drawChessboardCorners(
                    img, (args.num_y, args.num_x), corners2, ret)
                cv.imshow('calib_intrinsic', img)
                #cv.waitKey(500)
    if args.verbose:
        cv.destroyAllWindows()

    ret, mtx, dist, _, _ = cv.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], None, None)
    print("MSE of calibration is: ", ret)
    print("Intrinsic of calibration is: \n", mtx)
    print("Distort of calibration is: \n", dist)

    with open(args.save_path, 'w') as fid:
        intrinsic_dict = {'fx': mtx[0, 0], 'fy': mtx[1, 1],
                          'cx': mtx[0, 2], 'cy': mtx[1, 2]}
        fid.write(json.dumps(intrinsic_dict))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', type=str,
                        required=True, help='dir path of calib images.')
    parser.add_argument('-e', '--ext', dest='ext', type=str,
                        required=True, help='ext name of calib images.')
    parser.add_argument('-s', '--save', dest='save_path', type=str,
                        required=True, help='path to save intrinsic json file.')
    parser.add_argument('-x', '--nx', dest='num_x', type=int, required=True,
                        help='horizontal number of corners point in chessboard.')
    parser.add_argument('-y', '--ny', dest='num_y', type=int, required=True,
                        help='vertical number of corners point in chessboard.')
    parser.add_argument('--lx', dest='len_x', type=float, default=1,
                        help='horizontal length of rectangle, can be any length unit.')
    parser.add_argument('--ly', dest='len_y', type=float, default=1,
                        help='vertical length of rectangle, can be any length unit.')
    parser.add_argument('--verbose',
                        action='store_true', help='show calib images.')
    args = parser.parse_args()

    run_calib(args)
