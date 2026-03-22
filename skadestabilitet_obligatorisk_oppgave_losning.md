# Losning: Obligatorisk oppgave (avdeling 2 skadet)

## 1. Initialt deplasement

$$
\nabla = LBT = 80\cdot 18\cdot 3.20 = 4608\ \mathrm{m^3}
$$

$$
\Delta = \rho\nabla = 1.025\cdot 4608 = 4723.2\ \mathrm{t}
$$

## 2. Symmetrisk skadet dypgang

En avdeling er skadet:

$$
l_d = 16.0\ \mathrm{m},\qquad L_S = L-l_d = 64.0\ \mathrm{m}
$$

$$
LBT = (L-l_d)BT_S \Rightarrow T_S = \frac{L}{L-l_d}T = \frac{80}{64}\cdot 3.20 = 4.0\ \mathrm{m}
$$

Bevart deplasement i denne metoden:

$$
\nabla_S = \nabla = 4608\ \mathrm{m^3},\qquad \Delta_S = \Delta = 4723.2\ \mathrm{t}
$$

## 3. Skadede hydrostatiske geometristorrelser

Skadet intervall er $[34,51]$ m, sa oppdriftsgivende intervaller blir $[0,34]$ og $[51,85]$ m.

Langskips tyngdepunkter:

$$
LCB_S = LCF_S = \frac{34\cdot 17 + 34\cdot 68}{34+34} = 42.5\ \mathrm{m}\ \text{fra AP}
$$

Skadet tverrskips vannlinjetreghetsmoment:

$$
I_{WL_S} = \frac{1}{12}(68)B^3 = \frac{1}{12}(68)(18^3)=33{,}048\ \mathrm{m^4}
$$

Skadet langskips treghetsmoment om $LCF_S$:

$$
I_{F_S}=\left[\frac{B\,34^3}{12}+A_1(17-42.5)^2\right]+\left[\frac{B\,34^3}{12}+A_2(68-42.5)^2\right]
$$

med $A_1=34\cdot 18=612\ \mathrm{m^2}$ og $A_2=34\cdot 18=612\ \mathrm{m^2}$:

$$
I_{F_S}=1{,}897{,}234\ \mathrm{m^4}
$$

## 4. Oppdaterte stabilitetsstorrelser

Bruk $KB_S \approx T_S/2 = 2.0\ \mathrm{m}$.

$$
BM_{T_S}=\frac{I_{WL_S}}{\nabla}=\frac{31{,}104}{4608}=6.75\ \mathrm{m}
$$

$$
BM_{L_S}=\frac{I_{F_S}}{\nabla}=\frac{669{,}696}{4608}=145.375\ \mathrm{m}
$$

$$
GM_S=KB_S+BM_{T_S}-KG=2.0+6.75-3.80=4.95\ \mathrm{m}
$$

## 5. Trimmoment og total trim

$$
M_T=\Delta(LCG-LCB_S)=4723.2(40.0-44.0)=-18{,}892.8\ \mathrm{t\,m}
$$

Negativt fortegn betyr mot-klokka trim i denne fortegnskonvensjonen.

$$
MCT_{1cm_S}=\frac{\Delta BM_{L_S}}{100L}=\frac{4723.2\cdot 145.375}{100\cdot 80}=85.779\ \mathrm{t\,m/cm}
$$

$$
t=\frac{M_T}{MCT_{1cm_S}}=\frac{-18{,}892.8}{85.779}=-220.2\ \mathrm{cm}
$$

## 6. Trimkomponenter og endelige dypganger

AP-baserte andeler med $LCF_S=40.0$ m (midskips):

$$
a_{aft}=\frac{LCF_S}{L}=0.5,\qquad a_{forward}=\frac{L-LCF_S}{L}=0.5
$$

Signerte komponenter (i cm):

$$
t_a=t\,a_{aft}=-220.2\cdot 0.5=-110.1\ \mathrm{cm}
$$

$$
t_f=t\,a_{forward}=-220.2\cdot 0.5=-110.1\ \mathrm{cm}
$$

Endelige dypganger:

$$
T_A=T_S-\frac{t_a}{100}=4.0-\frac{(-110.1)}{100}=5.101\ \mathrm{m}
$$

$$
T_F=T_S+\frac{t_f}{100}=4.0+\frac{(-110.1)}{100}=2.899\ \mathrm{m}
$$

Dermed blir $T_A > T_F$, som forventet.

## 7. Akseptkontroller

$$
GM_S=4.95\ \mathrm{m}>0\ \mathrm{m}\ \checkmark
$$

$$
T_{crit}=\max(T_A,T_F)=5.101\ \mathrm{m}<D=10.0\ \mathrm{m}\ \checkmark
$$

PASS.
