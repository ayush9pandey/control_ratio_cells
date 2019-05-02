import numpy as np
def Bcell(t,x, P):
    f = np.zeros(len(x))
#      x = 0, T1, 1, A1, 2, S1, 3, S2, 4, T2, 5, A2, 6, C1, 7, C2
#      P = 0, beta_S1, 1, l_S1, 2, K_S1, 3, kb, 4, beta_S2, 5, l_S2, 6,
#      K_S2, 7, beta_lac, 8, l_lac, 9, K_lac, 10, beta_tet, 11, l_tet, 12,
#      K_tet, 13, kc, 14, C_max, 15, dc, 16, I, 17, S1, 18, atc, 19,K_tox  
    # 17 -> 16, 18 -> 17, 19 -> 18, 20 -> 19
    #  S2 (scaled with cell count)
    f[0] = P[10]*(P[11] + P[18]**2/(P[12]+P[18]**2))*x[3] - P[22] * x[3]

    # T2 and A2
    f[1] = P[4]*(P[5] + x[0]**2/(P[6]+x[0]**2))-P[3]*x[1]*x[2] - P[21] * x[1]
    f[2] = 5*P[0]*(P[1] + P[17]**2/(P[2]+P[17]**2))- P[21] * x[2]-P[3]*x[1]*x[2]

    # Cell 2
    f[3] = P[13]*(1 - (x[3])/P[14])*x[3] - P[15]*x[3]*(x[1]/(P[19] + x[1])) - P[20] * x[3]
    return f

