import numpy as np
def reed_ode(t,x, P):
    f = np.zeros(len(x))
#      x = 0, T1, 1, A1, 2, S1, 3, S2, 4, T2, 5, A2, 6, C1, 7, C2
#      P = 0, beta_S1, 1, l_S1, 2, K_S1, 3, kb, 4, beta_S2, 5, l_S2, 6,
#      K_S2, 7, beta_lac, 8, l_lac, 9, K_lac, 10, beta_tet, 11, l_tet, 12,
#      K_tet, 13, kc, 14, C_max, 15, dc, 16, xx, 17, I, 18, xx, 19, atc, 20,K_tox  
    #  T1 and A1
    f[0] = P[0]*(P[1] + x[2]**2/(P[2]+x[2]**2))-P[3]*x[0]*x[1] - P[22] * x[0]
    f[1] = P[4]*(P[5] + x[3]**2/(P[6]+x[3]**2)) - P[22] * x[1] - P[3]*x[0]*x[1]

    #  S1 and S2 (scaled with cell count)
    f[2] = P[7]*(P[8] + P[17]**2/(P[9]+P[17]**2))*x[6] - P[23] * x[2]
    f[3] = P[10]*(P[11] + P[19]**2/(P[12]+P[19]**2))*x[7] - P[23] * x[3]

    #  T2 and A2
    f[4] = P[4]*(P[5] + x[3]**2/(P[6]+x[3]**2))-P[3]*x[4]*x[5] - P[22] * x[4]
    f[5] = P[0]*(P[1] + x[2]**2/(P[2]+x[2]**2))- P[22] * x[5]-P[3]*x[4]*x[5]

    #  Cell 1 and Cell 2
    f[6] = P[13]*(1 - (x[6] + x[7])/P[14])*x[6] - P[15]*x[6]*(x[0]/(P[20] + x[0])) - P[21] * x[6]
    f[7] = P[13]*(1 - (x[6] + x[7])/P[14])*x[7] - P[15]*x[7]*(x[4]/(P[20] + x[4])) - P[21] * x[7]
    return f

