from scipy.optimize import fsolve

#CMOS Parameters

kp = 10
kn = 90
vtn = 1
vtp = -1
vdd = 5

def CMOS_VTC_CALC():
    VOH = vdd
    VOL = 0
    V_IH, V_OUT1 = fsolve(NMOS_LIN_PMOS_SAT, (1, 1))
    V_IL, V_OUT1 = fsolve(NMOS_SAT_PMOS_LIN, (1, 1))
    VM = fsolve(BOTH_SAT,1)
    print(VOH,VOL,V_IH,V_IL,VM)

def NMOS_SAT_PMOS_LIN(p):
    v_in , v_out = p
    return (kp*(2*(v_in-vdd-vtp)*(v_out-vdd)-(v_out-vdd)**2)-kn*(v_in-vtn)**2,kp*(4*v_out-2*v_in+2*vtp-2*vdd)-2*kn*(v_in-vtn))

def NMOS_LIN_PMOS_SAT(p):
    v_in, v_out = p
    return (kn*(2*(v_in-vtn)*v_out - (v_out**2)) - kp * (v_in- vdd - vtp) ** 2,
            kn*(4*v_out-2*v_in+2)-kp*(2*v_in+2*(-vdd-vtp)))
def BOTH_SAT(p):
    v_m = p
    return (kn*(v_m-vtn)**2-kp*(v_m-vdd-vtp)**2)

CMOS_VTC_CALC()







