import numpy as np


class FeatureExtractor:

    def __init__(self, sample):

        self.sample = sample

    def rms(self, y):

        return np.std(y)

    def depth(self):

        y = self.sample["local_y"]

        return 1 - np.min(y)

    def duration(self):

        y = self.sample["local_y"]

        threshold = np.min(y) + 0.5 * (np.max(y)-np.min(y))

        inside = y < threshold

        return np.sum(inside)

    def snr(self):

        y = self.sample["local_y"]

        depth = 1 - np.min(y)

        noise = np.std(y)

        return depth / noise

    def symmetry(self):

        y = self.sample["local_y"]

        n = len(y)

        left = y[:n//2]

        right = y[n//2:]

        right = right[::-1]

        m = min(len(left), len(right))

        return np.mean(np.abs(left[:m]-right[:m]))

    def extract(self):

        return {

            "depth": self.depth(),

            "duration": self.duration(),

            "snr": self.snr(),

            "symmetry": self.symmetry(),

            "rms": self.rms(self.sample["local_y"])

        }