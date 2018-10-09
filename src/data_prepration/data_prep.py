import math
import os
import re
import cv2
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import av

def display_image(input_dir) :

    test_images_input = os.listdir(input_dir)

    stopper=0
    for img in test_images_input:
        print(img)
        stopper+=1
        image = mpimg.imread( os.path.join(input_dir,img))
        print('Shape of image: ',image.shape)
        plt.imshow(image)
        plt.show()
        if stopper==1:
            break
    pass

def rgb_2_single(input_dir, output_dir):
    """Applies the Grayscale transform
    This will return an image with only one color channel but
    NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')
    """

    test_images_input = os.listdir(input_dir)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for img in test_images_input:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.imread(os.path.join(input_dir,img), cv2.IMREAD_GRAYSCALE)
        base_filename= os.path.basename(img)
        cv2.imwrite(output_dir+'/'+os.path.basename(img)[:-9]+'gray'+'.png', gray_image)
        counter+=1
    pass


def create_videos(frames_path):

    Path(frames_path).mkdir(parents=True, exist_ok=True)
    parent_path= Path(frames_path)
    seq_folder = parent_path.glob('**')
    print("seq_folder-->",seq_folder)

    for seq in seq_folder:
        for frames in seq:
            frame_read=cv2.imread(frames)
            height , width , layers =  frame_read.shape
            print('captured shape img', height , width , layers)
            video = cv2.VideoWriter(frames.parents[1]+str(seq)[5:]+'.mov',-1,1,(width,height))
            video.write(frame_read)
        cv2.destroyAllWindows()
        video.release()
    pass

def create_semantic_segmentation_mask(image_path):
    #TODO
    pass

def frame_cutter(video_path):

    video_pathlist = os.listdir(video_path)
    print("pathlist-->",len(list(video_pathlist)), type(video_pathlist))

    currentFrame = 0
    stop=0
    # create a folder for each frame.
    for video in reversed('./*.mov'):
        stop+=1
        print('Processing video... ', os.path.basename(video))

        parent_path= Path(video_path).parents[0]
        new_seq_folder= str(parent_path) +'/test_sequences/'+ os.path.basename(video)[:-4]
        print('folder name   : ',new_seq_folder)
        Path(new_seq_folder).mkdir(parents=True, exist_ok=True)

        vidcap = cv2.VideoCapture(video)
        success, image = vidcap.read()
        print("What's it returning", success)
        count = 0
        while success:
            print('reached')
            name = new_seq_folder + "/" + os.path.basename(video)[:4]+'/'+ "frame_%d.png" % count
            print('frame_name  :',name)
            cv2.imwrite(name, image)  # save frame as JPEG file
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            if count==10:
                break
            count += 1

        if stop==1:
            break
  
    pass

def main():
    """
    Starting point of the program.
    """
    # rgb_path= "/home/ubuntu/Documents/anubhav/vid2vid/datasets/Cityscapes/bdd100k_seg_color_labels"
    # single_Channel_conv(rgb_path)
    #
    # create_frames(video_path)
    #
    # frames_path="~/home/anubh/Documents/Anubhav/datasets/customVideos/frames/"
    # create_videos(frames_path)
    # test_random_ssm_input = "/home/ubuntu/Documents/anubhav/vid2vid/datasets/Cityscapes/test_A/stuttgart_00/"
    # test_random_ssm_output=  "/home/ubuntu/Documents/anubhav/vid2vid/datasets/Cityscapes/test_A/stuttgart_00_sChannel"
    #
    # original_ssm_seq = "/home/ubuntu/Documents/anubhav/vid2vid/datasets/Cityscapes/stuttgart_00_original"
    #
    # display_image(original_ssm_seq)
    # display_image(test_random_ssm_input) # three channel SSM
    # rgb_2_single(test_random_ssm_input, test_random_ssm_output)
    # display_image(test_random_ssm_output)

    frames_path= "/home/ubuntu/Documents/anubhav/vid2vid/datasets/BDD/bdd_sample_videos/test_sample_videos/samples-1k/Test"
    frame_cutter(frames_path, video_path='.')

    # frame_path = "/home/ubuntu/Documents/anubhav/vid2vid/datasets/BDD/bdd_sample_videos/test_sample_videos/samples-1k/test_sequences/00b04b30-2e874876/"
    # display_image(frame_path)
    pass
if __name__ == "__main__":

    main()
