# chatting 
import pygame
from PIL import Image
import socket
 from tkinter import *

class Client():
    """docstring for Client"""
    
    def __init__(self):
        super(Client, self).__init__()





def swap():
	print("hi")




def show_img(Class_of_image):
    Class_of_image.show()

def get_img(route_path):
    return Image.open(route_path)


def main():
    mouse = get_img("image/m.jpg")
    show_img(mouse)







if __name__=="__main__":
    main()