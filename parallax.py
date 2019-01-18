import pygame, pygame.sndarray, numpy, scipy.signal, scipy.constants

colors = {"red" : 620, "orange" : 590, "yellow" : 570, "green": 495, "blue" : 450, "violet" : 380}

def find_frequency(wavelength):
 c=scipy.constants.speed_of_light
 LAMBDA = (float(wavelength*10.0e-9))
 return float((c/LAMBDA)/(2**40))


def play(w,l):
    sound = pygame.sndarray.make_sound(w)
    sound.play(-1)
 
def sine(f,height,sr):
 l = sr / float(f)
 p = (numpy.pi * 2 )/l
 domain = numpy.arange(int(l)) *p
 range= height * numpy.sin(domain)
 return numpy.resize(range, (sr,)).astype(numpy.int16)
 
pygame.mixer.pre_init(44100, -16, 1)
pygame.init() 
cl=[]
print("Parralax ready!")
while 1:
 for i in cl:
  print("Ready to play color ",i,".")
 i=input("add <color>, play, clear, colors, stop, or quit")
 sl=i.split()
 if len(sl) == 1:
  if sl[0]=="colors":
   for k,v in colors.items():
    print(k,": ",find_frequency(float(v)))
  elif sl[0] == "stop":
   pygame.mixer.fadeout(1000)
  elif sl[0] == "play":
   if len(cl) == 0:
    print("Empty color list.")
    continue
   w=0
   for cn in cl:
    w += sine(find_frequency(colors[cn]),4096,44100)
   play(w,1000)
  elif sl[0] == "quit":
   break
  elif sl[0] == "clear":
   if len(cl) == 0:
    print("No colors in the list!")
   cl=[]
   continue
  else:
   print("Bad command.");
   continue
 elif len(sl) == 2:
  if sl[0] == "add":
   if sl[1] in cl:
    print("Color already added.")
    continue
   if sl[1] in colors:
    cl.append(sl[1])
    print("Color ", sl[1], " added.")
    continue  
   else:
    print("Color not found.")
    continue




