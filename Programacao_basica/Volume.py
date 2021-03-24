immport numpy as np

def Vol(x):
  Volume =[]
  for d in x:
    Volume.append(np.pi*d**3/4)
  return Volume
