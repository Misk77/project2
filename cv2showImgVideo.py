from time import time
from numpy import uint8
from numpy.random import rand
import cv2
from tkinter import *
from PIL import Image


#
def fpsShow():
    xy = (512, 512)
    Nf = 500

    def fpsopencv(dat):
        tic = time()
        for i in dat:
            cv2.imshow('Fps test', i)
            cv2.waitKey(2)  # integer milliseconds, 0 makes wait forever
        cv2.destroyAllWindows()
        return Nf / (time() - tic)

    imgs = (rand(Nf, xy[0], xy[1]) * 255).astype(uint8)
    fps = fpsopencv(imgs)
    print(fps, 'fps')
    # label = Label(fps, 'fps')
    # label = Label(root, fps, text='fps')
    # label.pack()


# Not complete, not showing with pack, my app are in grid
def showimagePIL():
    try:
        img = Image.open(r"C:\Users\miche\PycharmProjects\project2gui\trex.png")
        img.show()

    except IOError:
        print('Error')


def showimageOsStartfile():
    try:
        import os
        os.startfile((r"C:\Users\miche\PycharmProjects\project2gui\trex.png"))

    except IOError:
        print('Error')


# show video

def showvideo():
    cap = cv2.VideoCapture(r'C:\Users\miche\PycharmProjects\project2gui\test.mp4')

    while (cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def showimageombyggnad():
    root = Tk()
    root.title("showimageombyggnad")
    root.geometry("400x100")
    frame1 = Frame(root)
    frame1.config()
    try:
        import os
        os.startfile((r"C:\Users\miche\PycharmProjects\project2gui\ombyggnad.gif"))

    except IOError:
        print('Error')
    root.mainloop()
# (r"C:\Users\miche\PycharmProjects\project2gui\trex.png")


def showaboutplayground():
    root = Tk()
    root.title("showaboutplayground")
    root.geometry("400x100")
    frame1 = Frame(root)
    frame1.config()
    try:
        import os
        os.startfile((r"C:\Users\miche\PycharmProjects\project2gui\aboutplayground.txt"))

    except IOError:
        print('Error')
    root.mainloop()
# (r"C:\Users\miche\PycharmProjects\project2gui\trex.png")
