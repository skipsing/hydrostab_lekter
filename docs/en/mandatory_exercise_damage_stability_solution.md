# Solution: Mandatory Exercise (Compartment 2 Flooded)

## 1. Initial displacement

$$
\nabla = LBT = 80\cdot 18\cdot 3.20 = 4608\ \mathrm{m^3}
$$

$$
\Delta = \rho\nabla = 1.025\cdot 4608 = 4723.2\ \mathrm{t}
$$

## 2. Symmetric damaged draft

One compartment is flooded:

$$
l_d = 16.0\ \mathrm{m},\qquad L_S = L-l_d = 64.0\ \mathrm{m}
$$

$$
LBT = (L-l_d)BT_S \Rightarrow T_S = \frac{L}{L-l_d}T = \frac{80}{64}\cdot 3.20 = 4.0\ \mathrm{m}
$$

Displacement conservation in this method:

$$
\nabla_S = \nabla = 4608\ \mathrm{m^3},\qquad \Delta_S = \Delta = 4723.2\ \mathrm{t}
$$

## 3. Damaged hydrostatic geometry

Flooded interval is $[16,32]$ m, so surviving intervals are $[0,16]$ and $[32,80]$ m.

Longitudinal centroids:

$$
LCB_S = LCF_S = \frac{16\cdot 8 + 48\cdot 56}{16+48} = 44.0\ \mathrm{m}\ \text{from AP}
$$

Transverse waterplane second moment:

$$
I_{WL_S} = \frac{1}{12}(64)B^3 = \frac{1}{12}(64)(18^3)=31{,}104\ \mathrm{m^4}
$$

Longitudinal flotation second moment about $LCF_S$:

$$
I_{F_S}=\left[\frac{B\,16^3}{12}+A_1(8-44)^2\right]+\left[\frac{B\,48^3}{12}+A_2(56-44)^2\right]
$$

with $A_1=16\cdot 18=288\ \mathrm{m^2}$ and $A_2=48\cdot 18=864\ \mathrm{m^2}$:

$$
I_{F_S}=669{,}696\ \mathrm{m^4}
$$

## 4. Updated stability terms

Use $KB_S \approx T_S/2 = 2.0\ \mathrm{m}$.

$$
BM_{T_S}=\frac{I_{WL_S}}{\nabla}=\frac{31{,}104}{4608}=6.75\ \mathrm{m}
$$

$$
BM_{L_S}=\frac{I_{F_S}}{\nabla}=\frac{669{,}696}{4608}=145.375\ \mathrm{m}
$$

$$
GM_S=KB_S+BM_{T_S}-KG=2.0+6.75-3.80=4.95\ \mathrm{m}
$$

## 5. Trimming moment and total trim

$$
M_T=\Delta(LCG-LCB_S)=4723.2(40.0-44.0)=-18{,}892.8\ \mathrm{t\,m}
$$

Negative sign means counterclockwise trim in this convention.

$$
MCT_{1cm_S}=\frac{\Delta BM_{L_S}}{100L}=\frac{4723.2\cdot 145.375}{100\cdot 80}=85.779\ \mathrm{t\,m/cm}
$$

$$
t=\frac{M_T}{MCT_{1cm_S}}=\frac{-18{,}892.8}{85.779}=-220.2\ \mathrm{cm}
$$

## 6. Trim components and final drafts

AP-based factors with $LCF_S=55.0$ m:

$$
a_{aft}=\frac{LCF_S}{L}=0.55,\qquad a_{forward}=\frac{L-LCF_S}{L}=0.45
$$

Signed components (in cm):

AP-based factors with $LCF_S=40.0$ m (midship):

$$
a_{aft}=\frac{LCF_S}{L}=0.5,\qquad a_{forward}=\frac{L-LCF_S}{L}=0.5
$$

$$
t_a=t\,a_{aft}=-220.2\cdot 0.5=-110.1\ \mathrm{cm}
$$

$$
t_f=t\,a_{forward}=-220.2\cdot 0.5=-110.1\ \mathrm{cm}
$$

Final drafts:

$$
T_A=T_S-\frac{t_a}{100}=4.0-\frac{(-110.1)}{100}=5.101\ \mathrm{m}
$$

$$
T_F=T_S+\frac{t_f}{100}=4.0+\frac{(-110.1)}{100}=2.899\ \mathrm{m}
$$

So $T_A > T_F$, as required.

## 7. Acceptance checks

$$
GM_S=4.95\ \mathrm{m}>0\ \mathrm{m}\ \checkmark
$$

$$
T_{crit}=\max(T_A,T_F)=5.101\ \mathrm{m}<D=10.0\ \mathrm{m}\ \checkmark
$$

PASS.

