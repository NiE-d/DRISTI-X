import numpy as np


class CandidateRanker:

    def __init__(self, features):

        self.f = features

    def score(self):

        score = 0

        explanation = []

        # ---------- SNR ----------
        if self.f["snr"] > 6:
            score += 30
            explanation.append("Excellent SNR")

        elif self.f["snr"] > 4:
            score += 20
            explanation.append("Good SNR")

        elif self.f["snr"] > 2:
            score += 10
            explanation.append("Weak but detectable")

        # ---------- Symmetry ----------
        if self.f["symmetry"] < 0.0002:
            score += 20
            explanation.append("Symmetric transit")

        elif self.f["symmetry"] < 0.0005:
            score += 10
            explanation.append("Moderately symmetric")

        # ---------- RMS ----------
        if self.f["rms"] < 0.0002:
            score += 20
            explanation.append("Low stellar noise")

        elif self.f["rms"] < 0.0005:
            score += 10
            explanation.append("Moderate stellar noise")

        # ---------- Depth ----------
        if 0.00005 < self.f["depth"] < 0.02:
            score += 20
            explanation.append("Physically plausible depth")

        # ---------- Duration ----------
        if 10 < self.f["duration"] < 80:
            score += 10
            explanation.append("Reasonable duration")

        return score, explanation