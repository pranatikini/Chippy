from pygame import mixer
from threading import Thread
import queue

mixer.init()

def load1():
  mixer.music.load("song.webm")

def premix1():
  t1 = Thread(target=load1)
  t1.start()
  t1.join()

def run1(out_queue):
  ct = int(mixer.music.get_pos() / 1000)
  out_queue.put(ct)
  mixer.music.unload()


def mix1():
  my_queue = queue.Queue()
  t2 = Thread(target=run1,args = (my_queue,))
  t2.start()
  t2.join()
  ct = my_queue.get()
  return ct

def load2():
   mixer.music.load("qsong.webm")

def premix2():
  t4 = Thread(target=load1)
  t4.start()
  t4.join()

def run2(out_queue):
  ct = int(mixer.music.get_pos() / 1000)
  out_queue.put(ct)
  mixer.music.unload()
  


def mix2():
  my_queue = queue.Queue()
  t3 = Thread(target=run2,args = (my_queue,))
  t3.start()
  t3.join()
  ct = my_queue.get()
  return ct

