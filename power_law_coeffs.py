#!/usr/bin/env python
# coding: utf-8


import numpy as np


def get_maherndl_mean_coeffs(m):
    """get the coeffs for the Maherndl parametrization for a given M
    
    Returns:
        coeffA, Coeffm
    
    """

    M = np.array([0.0, 0.013, 0.021, 0.033, 0.052, 0.082, 0.129, 0.205, 0.325, 0.515, 0.816])

    aA = np.array([0.0611, 0.0699, 0.0843, 0.120, 0.158, 0.183, 0.234, 0.293, 0.356, 0.421, 0.480])
    bA = np.array([1.81, 1.81, 1.83, 1.88, 1.91, 1.92, 1.94, 1.96, 1.97, 1.98, 1.99])

    am = np.array([0.0324, 0.224, 0.537, 1.54, 4.27, 10.1, 22.2, 43.3, 79.0, 157, 173])
    bm = np.array([2.10, 2.35, 2.45, 2.57, 2.69, 2.77, 2.85, 2.89, 2.93, 2.97, 2.93])
    
    coeffA = np.interp(m, M, aA), np.interp(m, M, bA)
    coeffm = np.interp(m, M, am), np.interp(m, M, bm)
    return coeffA, coeffm


def get_maherndl_rimed(D, M, ptype='mean'):
    """
    """
    if ptype == 'mean':
        coeffA, coeffm = get_maherndl_mean_coeffs(M)
    mass = np.zeros_like(D)
    mass = coeffm[0]*D**coeffm[1]
    area = np.zeros_like(D)
    area = coeffA[0]*D**coeffA[1]

    return area, mass
    

Dmean = np.array([3.88592306e-06, 5.86216800e-06, 6.77951000e-06, 7.93205340e-06,
       9.28069691e-06, 1.07100048e-05, 1.24447745e-05, 1.43748377e-05,
       1.65944675e-05, 1.91652704e-05, 2.20864473e-05, 2.53591807e-05,
       2.90504781e-05, 3.32070942e-05, 3.78899845e-05, 4.32051865e-05,
       4.91755140e-05, 5.59504587e-05, 6.36371833e-05, 7.23027870e-05,
       8.20892226e-05, 9.31698268e-05, 1.05707773e-04, 1.19916116e-04,
       1.36012591e-04, 1.54242723e-04, 1.77478306e-04, 2.06819258e-04,
       2.41010897e-04, 2.80855143e-04, 3.27286493e-04, 3.81393937e-04,
       4.44446497e-04, 5.17922991e-04, 6.03546717e-04, 7.03325873e-04,
       8.19600654e-04, 9.55098139e-04, 1.11299625e-03, 1.29699829e-03,
       1.51141979e-03, 1.76128975e-03, 2.05246854e-03, 2.39178541e-03,
       2.78719859e-03])

def get_hexagonal_plates(D):
    """
    """
    mass = np.zeros_like(D)
    mass[D < 100e-6] = 0.00739*(D[D < 100e-6]*1e2)**2.45*1e-3
    mass[D > 100e-6] = 0.00739*(D[D < 100e-6]*1e2)**2.45*1e-3
    area = np.zeros_like(D)
    area[D < 100e-6] = 0.24*(D[D < 100e-6]*1e2)**1.85*1e-4
    area[D < 100e-6] = 0.65*(D[D < 100e-6]*1e2)**2.00*1e-4
    return area, mass

def get_hexagonal_column(D):
    """
    """
    mass = np.zeros_like(D)
    mass[D < 100e-6] = 0.1677*(D[D < 100e-6]*1e2)**2.91*1e-3
    mass[D > 100e-6] = 0.00166*(D[D > 100e-6]*1e2)**1.91*1e-3
    mass[D > 300e-6] = 0.000907*(D[D > 300e-6]*1e2)**1.74*1e-3
    area = np.zeros_like(D)
    area[D < 100e-6] = 0.684*(D[D < 100e-6]*1e2)**2.00*1e-4
    area[D > 100e-6] = 0.0696*(D[D > 100e-6]*1e2)**1.50*1e-4
    area[D > 300e-6] = 0.0512*(D[D > 300e-6]*1e2)**1.414*1e-4
    return area, mass

def get_rimed_long_columns(D):
    """
    """
    mass = 0.00145*(D*1e2)**1.80*1e-3
    area = 0.0512*(D*1e2)**1.141*1e-4
    return area, mass





if __name__ == '__main__':
    print("Area")
    for D in [10e-6, 100e-6, 1e-3, 3e-3]:
        print(f"{D:.1e} {(np.pi/4.) * D** 2:.2e} m2")
        
        
    print("Volume")
    for D in [10e-6, 100e-6, 1e-3, 3e-3]:
        print(f"{D:.1e} {(4/3 * np.pi * (D/2)**3) :.2e} m3")
        
        
    print("Mass (1000 kg m-3)")
    for D in [10e-6, 100e-6, 1e-3, 3e-3]:
        print(f"{D:.1e} {(4/3 * np.pi * (D/2)**3 * 1000) :.2e} kg")
        
        
    print("Mass  (700 kg m-3)")
    for D in [10e-6, 100e-6, 1e-3, 3e-3]:
        print(f"{D:.1e} {(4/3 * np.pi * (D/2)**3 * 700) :.2e} kg")
        #print(f"{D:.1e} {(np.pi/6. * 700 *  D ** 3) :.2e} kg")
    



