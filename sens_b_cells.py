from unnamed_sensitivity_package import *
import numpy as np
import scipy
P = np.zeros(24)
P[0] = 6
P[1] = 2e-3
P[2] = 430
P[3] = 30
P[4] = 6
P[5] = 2e-3
P[6] = 190
P[7] = 19.8e-3
P[8] = 1.5e-3
P[9] = 1.4e5
P[10] = 14.4e-3
P[11] = 2.1e-4
P[12] = 13
P[13] = 0.6
P[14] = 5500
P[15] = 0.8
P[16] = 1e6
P[17] = 0
P[18] = 324
P[19] = 5
P[20] = 0.001
P[21] = 1.5
P[22] = 1

x0 = np.zeros(4)
x0[3] = 500
from Bcell import Bcell
x_sol, sensitivity_sol = solve_extended_ode(Bcell, P,
                                            t_min = 0, t_max = 40,init = x0,
                                            method = "RK45")