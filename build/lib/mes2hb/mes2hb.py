__version__ = '1.0.0'

import sys
import numpy as np
import math
from .absorption_coefficients import AbsorptionCoefficients

class Mes2Hb:
    def __init__(self):
        self.coefficients = AbsorptionCoefficients()

    def convert(self, mes_data, baseline = [0, 100], wavelength = [690, 830]):
        """
            Cnverts optical density (OD) to oxy, de-oxy an total
            HB concentrations.
            The arrays returned will have baseline measurements
            zeroed out making the resulting in fewer rows than
            mes_data.

            params:
                mes_data(np.ndarray): a Nx2 dimensional array with
                1st column containing red wavelength values and
                2nd column containing infra-red wavelength values.

                baseline(list): first and last indices of rows to
                be accounted for baseline correction

                wavelength(list): precise wavelengths of red and infra-red
                channels obtained from the sensor.
            returns:
                hbo, hb, hbt(np.ndarray): 3 (N-baseline[1]-baseline[0], 1) arrays
                containing oxy, de-oxy and total haemoglobin concentrations.
        """
        red_mes_data = np.reshape(
            mes_data[0], (mes_data[0].shape[0], 1)
            )
        ir_mes_data = np.reshape(
            mes_data[1], (mes_data[1].shape[0], 1)
            )

        mes_data_shape = ir_mes_data.shape

        wlen_red = wavelength[0]
        wlen_ir = wavelength[1]

        oxy_red = self.coefficients.get_coefficient(
            wlen_red, "oxy"
            )
        oxy_ir = self.coefficients.get_coefficient(
            wlen_ir, "oxy"
            )
        dxy_red = self.coefficients.get_coefficient(
            wlen_red, "dxy"
            )
        dxy_ir = self.coefficients.get_coefficient(
            wlen_ir, "dxy"
            )

        mean_baseline_red = np.mean(red_mes_data[baseline[0]:baseline[1]])
        mean_baseline_ir = np.mean(ir_mes_data[baseline[0]:baseline[1]])

        pos = np.where(
            red_mes_data*mean_baseline_red > 0
            )
        a_red = np.array([
                math.log(mean_baseline_red/i[0]) if idx in pos[0] else 0 \
                for idx, i in enumerate(red_mes_data)
            ])

        pos = np.where(
            ir_mes_data*mean_baseline_ir > 0
            )
        a_ir = np.array([
                math.log(mean_baseline_ir/i[0]) if idx in pos[0] else 0 \
                for idx, i in enumerate(ir_mes_data)
            ])

        hb = np.zeros(mes_data_shape)
        hbo = np.zeros(mes_data_shape)
        hbt = np.zeros(mes_data_shape)

        ####### Oxy Hb #######
        if ((oxy_red*dxy_ir - oxy_ir*dxy_red)!=0):
            hbo = (a_red*dxy_ir - a_ir*dxy_red)/(oxy_red*dxy_ir - oxy_ir*dxy_red)

        ####### DeOxy Hb #######
        if ((dxy_red*oxy_ir - dxy_ir*oxy_red)!=0):
        	hb = (a_red*oxy_ir - a_ir*oxy_red)/(dxy_red*oxy_ir - dxy_ir*oxy_red)

        hbt = hbo + hb
        return hbo[baseline[1]:], hb[baseline[1]:], hbt[baseline[1]:]
