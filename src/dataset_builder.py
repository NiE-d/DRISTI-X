import numpy as np


class DatasetBuilder:

    def __init__(self, phase, flux):
        self.phase = np.asarray(phase)
        self.flux = np.asarray(flux)

    def extract_window(self,
                       center=0.0,
                       half_width=0.05,
                       points=200):

        mask = (
            (self.phase >= center-half_width) &
            (self.phase <= center+half_width)
        )

        x = self.phase[mask]
        y = self.flux[mask]

        if len(x) < 5:
            return None, None

        order = np.argsort(x)
        x = x[order]
        y = y[order]

        x_new = np.linspace(
            center-half_width,
            center+half_width,
            points
        )

        y_new = np.interp(
            x_new,
            x,
            y
        )

        return x_new, y_new

    def local_view(self):
        return self.extract_window(
            center=0.0,
            half_width=0.05,
            points=200
        )

    def secondary_view(self):
        return self.extract_window(
            center=0.5,
            half_width=0.05,
            points=200
        )

    def global_view(self, points=400):

        order = np.argsort(self.phase)

        x = self.phase[order]
        y = self.flux[order]

        x_new = np.linspace(
            -0.5,
            0.5,
            points
        )

        y_new = np.interp(
            x_new,
            x,
            y
        )

        return x_new, y_new

    def build_sample(self):

        lx, ly = self.local_view()
        gx, gy = self.global_view()
        sx, sy = self.secondary_view()

        return {
            "local_x": lx,
            "local_y": ly,
            "global_x": gx,
            "global_y": gy,
            "secondary_x": sx,
            "secondary_y": sy
        }