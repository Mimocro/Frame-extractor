import glob
import os
import argparse
import cv2
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("--path", default="./", type=str) #how many fileeo
parser.add_argument("--num_v", default=None, type=int) #how many fileeo
parser.add_argument("--s_frame", default="5", type=int) #start frame
parser.add_argument("--num_f", default="5", type=int) #total number of frames
parser.add_argument("--every", default="600", type=int) #extract frames every n frames
parser.add_argument("--f_type", default="mp4", type=str)
parser.add_argument("--folders", action='store_true') #each fileeo in different folders
args = parser.parse_args()




files = glob.glob(f"{args.path}\*.{args.f_type}")



for file in files[:args.num_v]:
    pth =  f'{args.path}\\comparsion'
    Path(pth).mkdir(exist_ok=True) 
    if args.folders: Path(f'{pth}\{Path(file).stem.strip()}').mkdir(exist_ok=True); pth = f'{pth}\{Path(file).stem.strip()}'
    n_frame = args.s_frame
    cap = cv2.VideoCapture(file)
    for i in range(args.num_f):
        n_frame+= i*args.every
        cap.set(cv2.CAP_PROP_POS_FRAMES, n_frame)
        res, frame = cap.read()
        frame = frame[:,:,::-1]
        frame = Image.fromarray(frame)
        
        frame.save(f'{pth}\{i}.png')
