import pickle

class Dotdict(dict):
    __getattr__ = dict.get
    def __getstate__(self): return self.__dict__
    def __setstate__(self, d): self.__dict__.update(d)

sinusoid = Dotdict(pickle.load(open("sinusoid.pkl", "rb")))

print("time", sinusoid.time[0:4])
print("cos", sinusoid.cos[5:10])
print("sin*cos", sinusoid["sin*cos"][0:5])
