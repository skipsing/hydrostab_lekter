# Modul i Skadestabilitet (Tapt oppdrift-metoden)

## 1. Læringsmål

Etter denne modulen skal studenten kunne:

- Beskrive forutsetningene i tapt oppdrift-metoden.
- Beregne ny likevekt etter skade ved symmetrisk oppfylling.
- Beregne og evaluere hydrostatiske endringer etter skade.
- Beregne trimvirkninger ved usymmetrisk skade og bestemme likevekt og dypgang forut og akter. 
- Vurdere akseptabel flytetilstand og stabilitet ved skade 

## 2. Forutsetninger, Symboler og Enheter

### 2.1 Forutsetninger

- Geometrien antas prismatisk (rektangulær lekter) dersom ikke annet er oppgitt.
- Det skadede avdelingmet antas helt åpent mot sjøen og bidrar ikke med oppdrift.
- vanninntregningen i skadet avdeling vil ha samme tetthet. 
- Statisk likevekt antas (ingen dynamiske fyllingseffekter).
- Små vinkel-antakelser for trim brukes.
- Fortegnskonvensjon:
  - Positiv dypgangsendring betyr større neddykking.
  - Positiv trim betyr forlig trim; $T_F > T_A$.
  - Alle mål er gitt fra aktreperpendikulær og baseline, med $x=0$ i AP og $x=L$ i FP.

### 2.2 Symboler

| Symbol | Betydning | Enhet |
|---|---|---|
| $L$ | Lengde | m |
| $B$ | Bredde | m |
| $D$ | Dybde | m |
| $T$ | Intakt dypgang | m |
| $T_S$ | Symmetrisk skadet dypgang | m |
| $\nabla$ | Intakt volumdeplasement | m³ |
| $\nabla_S$ | Skadet volumdeplasement | m³ |
| $I_{WL}$ | Annet arealmoment for vannlinjearealet (intakt) | m⁴ |
| $I_{WL_S}$ | Annet arealmoment for vannlinjearealet (skadet) | m⁴ |
| $I_F$ | Annet arealmoment for vannlinjearealet om $LCF$ (intakt) | m⁴ |
| $I_{F_S}$ | Annet arealmoment for vannlinjearealet om $LCF$ (skadet) | m⁴ |
| $KB$ | Baseline til oppdriftssenter | m |
| $BM$ | Metasentrisk radius | m |
| $GM$ | Metasentrisk høyde | m |
| $LCB$ | Langskips oppdriftssenter | m |
| $LCF$ | Langskips flotasjonssenter | m |
| $t_a$ | Akterlig trimendring | m |
| $t_f$ | Forlig trimendring | m |
| $T_A$ | Dypgang ved AP | m |
| $T_F$ | Dypgang ved FP | m |

## 3. Framgangsmåte 

### 3.1 Oppsummering av geometri og hydrostatikk

![BargeGeometryScene animasjon](exports/BargeGeometryScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Oppbygging av lekterens hoveddimensjoner.*

Inndata:


- Hoveddimensjoner: $L$, $B$, $D$
- Intakt tilstand: $T$, $KG$
- Tetthet til vannet: $\rho$




![BargeHydrostaticsScene animasjon](exports/BargeHydrostaticsScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Intakt hydrostatikk - deplasementsvolum og metasentriske radier.*

Likninger:

- Volumdeplasement:

$$
\nabla = L \times B \times T
$$

- Vektdeplasement:

$$
\Delta = \rho \times \nabla
$$

- Vannlinjearealets "treghetsmoment":

$$
BM_T = \frac{I_{WL}}{\nabla},\qquad BM_L = \frac{I_F}{\nabla}
$$

Mini-sjekk:

- Hvis $L=60\ \mathrm{m}$, $B=12\ \mathrm{m}$, $T=3.0\ \mathrm{m}$, er $\nabla=2160\ \mathrm{m^3}$.


### 3.3 Parallell nedsynking

![BargeDamageSubmergenceScene animasjon](exports/BargeDamageSubmergenceScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Parallell nedsynking til symmetrisk skadet dypgang $T_S$.*

Denne fasen fastsetter ny symmetrisk skadet dypgang før trimeffekter legges til.

Nødvendige inndata:

- Intakt dypgang $T$
- Lekterens lengde $L$ og bredde $B$
- Lengde på skadet avdeling $l_d$

For en rektangulær lekter med en skadet avdeling blir effektiv oppdriftsgivende lengde $(L-l_d)$. Volumdeplasementet er uendret:

$$
L \times B \times T = (L-l_d) \times B \times T_S
$$

Ny dypgang i skadet tilstand:

$$
T_S = \frac{L}{L-l_d}T
$$

Kontroller deretter: 

$$
\nabla_S = \nabla
$$

Eksempel: lekter med 3 like store avdelinger (midtre avdeling skadet)

- Gitt: $L=60\ \mathrm{m}$, $B=12\ \mathrm{m}$, $T=3.00\ \mathrm{m}$, 3 like avdelinger
- Lengde på skadet avdeling: $l_d=L/3=20\ \mathrm{m}$

$$
T_S = \frac{L}{L-l_d}T = \frac{60}{60-20}\cdot 3.00 = 4.50\ \mathrm{m}
$$

$$
\nabla_S = \nabla = L \times B \times T = 60\cdot 12\cdot 3.00 = 2160\ \mathrm{m^3}
$$

Kontroll:

- $T_S > T$ (som forventet etter skade).
- Flytekriteriet i dette eksempelet er oppfylt hvis $D > 4.50\ \mathrm{m}$.
    - Hva skjer om $T_S > D$ ? 

### 3.4 Endring av hydrostatikken ved skade 

Vi skal her se på hva som skjer med de hydrostatiske verdiene $KB$, $A_WL$ og $BM_T$ etter skade

#### 3.4.1 Vertikal forskyvning av oppdriftssenter $KB$ 


![BargeDamageKBScene animasjon](exports/BargeDamageKBScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Vertikal forskyvning av oppdriftssenteret - $KB_S$ etter skade.*

Likninger:

For en rektangulær lekter i denne forenklede modellen er oppdriftssenteret i skadet tilstand:

$$
KB_S = \frac{T_S}{2}
$$

#### 3.4.2 Reduksjon av vannlinjearealet, $ A_{WL}$ og dets treghetsmoment $ BM_T $ 
![BargeDamageBMScene animasjon](exports/BargeDamageBMScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Reduksjon av tverrskips metasenterradius $BM_{T_S}$ på grunn av redusert vannlinjeareal.*

Likninger: 

Skadet vannlinjeareal uttrykt ved skadet lengde $l_d$:

$$
A_{WL_S} = (L-l_d)B
$$

For en rektangulær vannlinje blir tilhørende annet arealmoment:

$$
I_{WL_S} = \frac{(L-l_d)B^3}{12}
$$

$$
BM_{T_S} = \frac{I_{WL_S}}{\nabla},\qquad BM_{L_S} = \frac{I_{F_S}}{\nabla}
$$

#### 3.5 Initialstabilitet ved skade $GM_S$

Likninger:

$$
GM_S = KB_S + BM_{T_S} - KG
$$

Mini-sjekk:

- Hvis $KB_S=1.62\ \mathrm{m}$, $I_{WL_S}=7600\ \mathrm{m^4}$, $\nabla=2160\ \mathrm{m^3}$ og $KG=4.20\ \mathrm{m}$, er $GM_S=0.939\ \mathrm{m}$.

### 3.6 Endring av hydrostatikken ved usymmetrisk skade
Vi skal her se på hva som skjer med de hydrostatiske verdiene $LCB$, $LCF$ og $BM_L$ ved usymmetrisk skade. Med usymmetrisk mener vi at avdelingen som fylles ikke ligger i senter. 



![BargeDamageLongitudinalBMScene animasjon](exports/BargeDamageLongitudinalBMScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Hydrostatikk ved usymmetrisk skade - $LCB_S$, $LCF_S$ og $BM_{L_S}$.*

- $LCB_S$ fra resterende intakte volumer i skadet tilstand.
- $LCF_S$ fra vannlinjearealets arealsenter i skadet tilstand. 

Likninger:

- Langskips metasenterradius om flotasjonssenter, $LCF_S$ i skadet tilstand:

$$
BM_{L_S} = \frac{I_{F_S}}{\nabla}
$$


Fremgangsmåte:

1. Bestem $LCB_S$ fra resterende oppdriftsgivende volum i skadet tilstand.
2. Bestem $LCF_S$ fra vannlinjearealets arealsenter i skadet tilstand.
3. Beregn $BM_{L_S}$.
4. Beregn $M_{trim}$ som inndata til Seksjon 3.7.

Mini-sjekk:

- Hvis $\Delta=2160\ \mathrm{t}$, $LCB_S=29.75\ \mathrm{m}$ fra AP, og $LCG=30.00\ \mathrm{m}$ fra AP, blir $M_{trim}=540.0\ \mathrm{t\,m}$.

### 3.7 Trimmoment og Trimfordeling ($t_a$, $t_f$, $T_A$, $T_F$)

![BargeDamageTrimScene animasjon](exports/BargeDamageTrimScene_ManimCE_v0.20.1_mid.gif)

*Animasjon: Beregning av trimmoment og fordeling i trim $t_a$ (akter) og $t_f$ (for).*


- Trimarm:

$$
l_k = LCG-LCB_S
$$

- Trimmoment:

$$
M_{T} = \Delta \times l_k
$$

- Moment for å endre trim 1 cm (box-barge-tilnærming):

$$
MCT_{1cm_S} = \frac{\Delta \times BM_{L_S}}{100 \times L}
$$

Denne fasen omregner trimmomentet til for- og akterdypgang.


Trinnvis fremgangsmåte:

![Trimoppsett](exports/Trimoppsett.png)

*Figur: Trimoppsett og tegnkonvensjon for akter- og fordypgangsendringer.*

1. Beregn arm

$$
l_k= LCG-LCB_S
$$

2. Beregn trimmoment:

$$
M_{T}=\Delta \times l_k
$$

2. Beregn moment for å endre trim med 1 cm:

$$
MCT_{1cm_S}=\frac{\Delta \times BM_{L_S}}{100 \times L}
$$

3. Beregn total trimendring:

$$
t_{cm} = \frac{M_{T}}{MCT_{1cm_S}}
$$

4. Konverter til meter: $t_m=t_{cm}/100$.

5. Fordel $t_m$ rundt $LCF_S$ i trimkomponentene $t_a$ (akter) og $t_f$ (for) ved bruk av AP/FP-vektfaktorer.

Generelle AP-baserte fordelingsfaktorer:

$$
	aft =\frac{LCF_S}{L},
\qquad
	fore =\frac{L-LCF_S}{L}
$$

![Fordeling av trim](exports/Fordeling_av_trim.png)

*Figur: Fordeling av total trim mellom akter- og fordypgang om $LCF_S$.*

Deretter beregnes trimkomponentene $t_a$ og $t_f$:


$$
t_a = t_m\left(\frac{LCF_S}{L}\right),
\qquad
t_f = t_m\left(\frac{L-LCF_S}{L}\right)
$$



Spesialtilfelle (hvis $LCF_S=L/2$, dvs. midskips):

$$
t_a = \frac{t_m}{2},\qquad t_f = \frac{t_m}{2}
$$


6. Anvend trimkomponentene på $T_S$ for å få endelige dypganger:
MERK: Hvis trimmomentet er mot klokken, reverseres fortegnene i likningene under.
$$
T_A= T_S - t_a,\qquad T_F= T_S + t_f
$$

Mini-eksempel:

- Hvis $trim=1.543\ \mathrm{cm}$, er $trim_m=0.01543\ \mathrm{m}$.
- Hvis $LCF_S=L/2$, er trimkomponentene $t_a = t_f = 0.00771\ \mathrm{m}$.

### 3.8 Kontroll av dypgang og inititalstabilitet ved skade

Inndata:

- Endelige dypganger $T_A$, $T_F$
- Rest metasentrisk høyde $GM_S$
- Fartøydybde $D$

Likninger:

$$
GM_S > 0\ \mathrm{m}
$$

- Kritisk dypgangskriterium:

$$
T_{crit}=\max(T_A,T_F) < D
$$

Fremgangsmåte:

1. Samle endelig skadet tilstand ($T_S$, $T_A$, $T_F$, $GM_S$).
2. Sjekk reststabilitet ($GM_S>0$).
3. Sjekk neddykingsgrense ved bruk av $T_{crit}$.
4. Klassifiser tilfellet som bestatt/ikke bestatt.

Mini-sjekk:

- Hvis begge kriteriene er oppfylt, vil fartøyet ikke synke eller kantre.


## 4. Fullstendig Regneeksempel (fra start til slutt)

### 4.1 Gitte Data

- Fartøy (rektangulær lekter):
  - $L = 60.0\ \mathrm{m}$
  - $B = 12.0\ \mathrm{m}$
  - $D = 6.0\ \mathrm{m}$
  - Initial middeldypgang $T = 3.00\ \mathrm{m}$
  - Vertikalt tyngdepunkt $KG = 4.20\ \mathrm{m}$
  - Tilnærmet sjøvannstetthet: $\rho = 1.0\ \mathrm{t/m^3}$
- Skadetilfelle:
  - Lengde på skadet avdeling $l_d = 3.5\ \mathrm{m}$
  - Langskips oppdriftssenter etter skade: $LCB_S = 29.75\ \mathrm{m}$ fra AP
  - Langskips flotasjonssenter etter skade: $LCF_S = 30.00\ \mathrm{m}$ fra AP
- Oppdaterte hydrostatiske inndata fra geometrimodellen etter skade:
  - $KB_S = 1.62\ \mathrm{m}$
  - $I_{WL_S} = 7600\ \mathrm{m^4}$
  - $I_{F_S} = 2.10 \times 10^6\ \mathrm{m^4}$

### 4.2 Løsningssteg

Steg 1: Initialt deplasement og oppsett

$$
\nabla = L \times B \times T = 60 \cdot 12 \cdot 3.00 = 2160\ \mathrm{m^3}
$$

Med $\rho = 1.0\ \mathrm{t/m^3}$ er initialt deplasement $\Delta = 2160\ \mathrm{t}$.

Steg 2: Parallell nedsynking løst fra avdelingslengden

For en rektangulær lekter med en fullt skadet langskips avdeling er oppdriftsgivende lengde $(L-l_d)$. Likevekt gir:

$$
L \times B \times T = (L-l_d) \times B \times T_S
$$

$$
T_S = \frac{L}{L-l_d}T = \frac{60}{60-3.5}\cdot 3.00 = 3.1858\ \mathrm{m}
$$

Anvend bevaring av deplasement for dette oppsettet med tapt oppdrift:

$$
\nabla_S = \nabla = 2160\ \mathrm{m^3}
$$

Dermed forblir deplasementet:

$$
\Delta_S = \Delta = 2160\ \mathrm{t}
$$

Steg 3: Oppdatert hydrostatikk ($BM_{T_S}$, $BM_{L_S}$, $GM_S$)

$$
BM_{T_S} = \frac{I_{WL_S}}{\nabla} = \frac{7600}{2160} = 3.519\ \mathrm{m}
$$

$$
BM_{L_S} = \frac{I_{F_S}}{\nabla} = \frac{2.10 \times 10^6}{2160} = 972.2\ \mathrm{m}
$$

$$
GM_S = KB_S + BM_{T_S} - KG = 1.62 + 3.519 - 4.20 = 0.939\ \mathrm{m}
$$

Steg 4: Trim og endelige dypganger

Bruk AP-baserte koordinater med $LCG = 30.00\ \mathrm{m}$ og $LCB_S = 29.75\ \mathrm{m}$:

$$
M_{trim} = \Delta \times (LCG - LCB_S) = 2160\,(30.00 - 29.75) = 540.0\ \mathrm{t\,m}
$$

Bruk en box-barge-tilnærming for moment til å endre trim 1 cm:

$$
MCT_{1cm_S} = \frac{\Delta \times BM_{L_S}}{100 \times L} = \frac{2160 \cdot 972.2}{100 \cdot 60} = 350.0\ \mathrm{t\,m/cm}
$$

$$
trim = \frac{M_{trim}}{MCT_{1cm_S}} = \frac{540.0}{350.0} = 1.543\ \mathrm{cm} = 0.01543\ \mathrm{m}
$$

Anta trim om $LCF_S = 30.00\ \mathrm{m}$ fra AP (midskips i dette tilfellet), slik at trimkomponentene $t_a$ og $t_f$ hver blir halvparten av total trim:

$$
t_a = \frac{trim_m}{2} = 0.00771\ \mathrm{m},\qquad t_f = \frac{trim_m}{2} = 0.00771\ \mathrm{m}
$$

Endelige dypganger:

$$
T_F = T_S + t_f = 3.1858 + 0.00771 = 3.1935\ \mathrm{m}
$$

$$
T_A = T_S - t_a = 3.1858 - 0.00771 = 3.1781\ \mathrm{m}
$$

Steg 5: Akseptkontroll

- Reststabilitet:

$$
GM_S = 0.939\ \mathrm{m} > 0\ \mathrm{m}\ \checkmark
$$

- Kontroll av dypgang mot dybde (bruk største dypgang i dette enkle tilfellet):

$$
T_{S,\max} \approx T_F = 3.1935\ \mathrm{m} < D = 6.0\ \mathrm{m}\ \checkmark
$$

### 4.3 Endelige Resultater

| Størrelse | Verdi | Enhet |
|---|---:|---|
| Initialt deplasementsvolum $\nabla$ | 2160 | m^3 |
| Lengde på skadet avdeling $l_d$ | 3.5 | m |
| Beregnet symmetrisk dypgang $T_S$ | 3.1858 | m |
| Skadet deplasementsvolum $\nabla_S$ | 2160 | m^3 |
| $BM_{T_S}$ | 3.519 | m |
| $GM_S$ | 0.939 | m |
| Total trim | 0.0154 | m |
| Dypgang ved AP $T_A$ | 3.1781 | m |
| Dypgang ved FP $T_F$ | 3.1935 | m |
| Akseptstatus | PASS | - |

Merk:
- Dette regneeksemplet er bevisst enkelt og bruker box-barge-tilnærminger for å tydeliggjøre framgangsmåten.
- I praktiske beregninger må forenklede uttrykk erstattes med hydrostatiske modellresultater for hver mellomliggende dypgang.

### 4.4 Ekstra Fullstendig Regneeksempel: 5 like store avdelinger, avdeling 4 skadet

Gitt:

- Lekterdimensjoner: $L=100.0\ \mathrm{m}$, $B=20.0\ \mathrm{m}$, $D=12.0\ \mathrm{m}$
- Initial dypgang: $T=3.50\ \mathrm{m}$
- 5 like store langskips avdelinger, slik at hver avdeling har lengde $L/5=20.0\ \mathrm{m}$
- Skadet avdeling: nr. 4 (fra AP), som strekker seg fra $x=60$ til $x=80\ \mathrm{m}$
- I dette regneeksemplet brukes $\rho=1.025\ \mathrm{t/m^3}$ (sjøvann), og vi antar $LCG=50.0\ \mathrm{m}$ (midskips)
- Box-barge-tilnærming vertikalt i skadet likevekt: $KB_S \approx T_S/2$

![Lekteren har 5 vanntette avdelinger](exports/Lekteren_har_5_vanntette_avdelinger.png)

*Figur: Fem like store vanntette langskips avdelinger, der én avdeling er skadet i regneeksemplet.*

Steg 1: Initialt deplasement

$$
\nabla = L \times B \times T = 100 \cdot 20 \cdot 3.50 = 7000\ \mathrm{m^3}
$$

$$
\Delta = \rho \times \nabla = 1.025\times 7000 = 7175\ \mathrm{t}
$$

Steg 2: Symmetrisk skadet dypgang fra tapt oppdriftsgivende lengde

Lengde på skadet avdeling:

$$
l_d = 20.0\ \mathrm{m},\qquad L_S=L-l_d=80.0\ \mathrm{m}
$$

Løs likevekt:

$$
L \times B \times T = (L-l_d) \times B \times T_S
$$

$$
T_S = \frac{L}{L-l_d}T = \frac{100}{80}\cdot 3.50 = 4.375\ \mathrm{m}
$$

Bevaring av deplasement:

$$
\nabla_S = \nabla = 7000\ \mathrm{m^3},\qquad \Delta_S = \Delta = 7175\ \mathrm{t}
$$

Steg 3: Hydrostatiske inndata i skadet tilstand fra avdelingsgeometrien

Gjenværende oppdrifts- og vannplanområder er intervallene $[0,60]$ og $[80,100]$ m fra AP.

Langskips tyngdepunkter:

$$
LCB_S = LCF_S = \frac{60\cdot 30 + 20\cdot 90}{60+20} = 45.0\ \mathrm{m}
$$

Skadet annet arealmoment for vannlinjearealet om tverrakse:

$$
I_{WL_S}=\frac{1}{12}(80)B^3 = \frac{1}{12}(80)(20^3)=53{,}333.3\ \mathrm{m^4}
$$

Skadet annet arealmoment for vannlinjearealet om $LCF_S$:

$$
I_{F_S}=\left[\frac{B\,60^3}{12}+A_1(30-45)^2\right]+\left[\frac{B\,20^3}{12}+A_2(90-45)^2\right]
$$

med $A_1=60\cdot 20=1200\ \mathrm{m^2}$ og $A_2=20\cdot 20=400\ \mathrm{m^2}$, som gir

$$
I_{F_S}=1{,}453{,}333.3\ \mathrm{m^4}
$$

Bruk $KB_S \approx T_S/2 = 2.1875\ \mathrm{m}$.

Steg 4: Oppdaterte stabilitetsstørrelser

$$
BM_{T_S}=\frac{I_{WL_S}}{\nabla}=\frac{53{,}333.3}{7000}=7.619\ \mathrm{m}
$$

$$
BM_{L_S}=\frac{I_{F_S}}{\nabla}=\frac{1{,}453{,}333.3}{7000}=207.619\ \mathrm{m}
$$

$$
GM_S=KB_S+BM_{T_S}-KG=2.1875+7.619-4.20=5.607\ \mathrm{m}
$$

Steg 5: Trim og endelige dypganger

$$
M_{trim}=\Delta \times (LCG-LCB_S)=7175\times(50.0-45.0)=35{,}875\ \mathrm{t\,m}
$$

$$
MCT_{1cm_S}=\frac{\Delta \times BM_{L_S}}{100\times L}=\frac{7175\times 207.619}{100\times 100}=148.967\ \mathrm{t\,m/cm}
$$

$$
trim_{cm}=\frac{M_{trim}}{MCT_{1cm_S}}=240.83\ \mathrm{cm},\qquad trim_m=2.4083\ \mathrm{m}
$$

Beregne trimkomponentene $t_a$ og $t_f$ ved bruk av AP-baserte fordelingsfaktorer ($LCF_S=45.0\ \mathrm{m}$):

$$
  ext{akterandel}=\frac{LCF_S}{L}=0.45,\qquad \text{forandel}=\frac{L-LCF_S}{L}=0.55
$$

$$
t_a=trim_m\left(\frac{LCF_S}{L}\right)=2.4083\times 0.45=1.084\ \mathrm{m}
$$

$$
t_f=trim_m\left(\frac{L-LCF_S}{L}\right)=2.4083\times 0.55=1.3246\ \mathrm{m}
$$

Endelige dypganger:

$$
T_A=T_S-t_a=4.375-1.084=3.291\ \mathrm{m}
$$

$$
T_F=T_S+t_f=4.375+1.3246=5.700\ \mathrm{m}
$$

Steg 6: Akseptkontroll

$$
GM_S=5.607\ \mathrm{m}>0\ \mathrm{m}\ \checkmark
$$

$$
T_{crit}=\max(T_A,T_F)=5.700\ \mathrm{m}<D=12.0\ \mathrm{m}\ \checkmark
$$

### 4.5 Endelige Resultater (ekstra eksempel)

| Størrelse | Verdi | Enhet |
|---|---:|---|
| Initialt deplasementsvolum $\nabla$ | 7000 | m^3 |
| Lengde på skadet avdeling $l_d$ | 20.0 | m |
| Beregnet symmetrisk dypgang $T_S$ | 4.375 | m |
| $LCB_S=LCF_S$ | 45.0 | m fra AP |
| $I_{WL_S}$ | 53,333.3 | m^4 |
| $I_{F_S}$ | 1,453,333.3 | m^4 |
| $BM_{T_S}$ | 7.619 | m |
| $GM_S$ | 5.607 | m |
| Total trim | 2.408 | m |
| Dypgang ved AP $T_A$ | 3.291 | m |
| Dypgang ved FP $T_F$ | 5.700 | m |
| Akseptstatus | PASS | - |

## 5. Vanlige Feil og Rimelighetskontroller

- Enhetsblanding mellom $\mathrm{m}$, $\mathrm{m^2}$, $\mathrm{m^3}$ og tonn.
- Å behandle deplasementet som endret etter oppfylling i denne modellen ($\nabla_S\neq\nabla$).
- Å blande tverrskips og langskips treghetsmomenter ($I_{WL_S}$ versus $I_{F_S}$).
- Å bruke motsatt fortegnskonvensjon for trim underveis i beregningen.
- Å glemme at akseptkontrollen bruker kritisk dypgang $\max(T_A,T_F)$.

Rimelighetskontroller:

- $T_S$ bør normalt være større enn $T$.
- Kontroller at deplasementet bevares i oppsettet: $\nabla_S=\nabla$ og $\Delta_S=\Delta$.
- $GM_S$ bør i de fleste skadetilfeller være lavere enn i intakt tilstand.

## 6. Kort Referansealgoritme

1. Samle inndata: $L$, $B$, $D$, $T$, $KG$, $l_d$, $I_{WL_S}$, $I_{F_S}$, $KB_S$, $LCB_S$, $LCF_S$.
2. Løs symmetrisk skadet dypgang:

$$
T_S = \frac{L}{L-l_d}T
$$

3. Sett deplasementstilstanden i skadet likevekt:

$$
\nabla_S=\nabla,\quad \Delta_S=\Delta
$$

4. Beregn hydrostatikk:

$$
BM_{T_S}=\frac{I_{WL_S}}{\nabla},\quad BM_{L_S}=\frac{I_{F_S}}{\nabla},\quad GM_S=KB_S+BM_{T_S}-KG
$$

5. Beregn trim:

$$
M_{trim}=\Delta \times (LCG-LCB_S),\quad MCT_{1cm_S}=\frac{\Delta \times BM_{L_S}}{100 \times L},\quad trim_{cm}=\frac{M_{trim}}{MCT_{1cm_S}}
$$

6. Fordel trim for å få $T_A$ og $T_F$.
7. Akseptkontroll: $GM_S>0$ og $\max(T_A,T_F)<D$.

## 7. Referanser og Figurplassholdere

Forslag til referanser:

- Forelesningsnotater i hydrostatikk og skadestabilitet.
- Standard lærebøker i skipskonstruksjon om tapt oppdrift og trim.

Figurplassholdere (eksisterende eksporter):

- Figur for symmetrisk skadet likevekt.
- Figur for reduksjon i tverrskips $BM$.
- Figur for langskips $BM$ og forskyvning av $LCF$.
- Figur for trimoppsett og trimfordeling.
