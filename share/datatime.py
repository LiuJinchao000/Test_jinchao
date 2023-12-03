from datetime import datetime
import cv2 as cv

if __name__ == "__main__":
    dt=datetime(2023,11,13,10,25).timestamp()
    print(dt)
    print(cv.__version__)