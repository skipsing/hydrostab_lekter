# Bestemmelse av Ny Dypgang ved Skade
## Parallel Submersjon ved Tapt Oppdriftsmetode

---

## Innledning

Når et skip får en skade under vannlinjen, vil vanninntrengning føre til tap av oppdrift i det skadede området. Dette dokumentet forklarer steg-for-steg hvordan vi beregner den nye dypgangen når skipet søker ny likevekt i skadet tilstand ved hjelp av **tapt oppdriftsmetoden** (Lost Buoyancy Method) med parallell submersjon.

---

## Fase 1: Introduksjon til Lekteren

En lekter med lengde **L**, bredde **B**, og dybde **D** flyter i vann med typgang **T**.

### Utgangspunkt:
- **Lengde (L)**: Totalt lengde mellom perpendiklene
- **Bredde (B)**: Maksimal bredde på skipet
- **Dybde (D)**: Vertikal avstand fra kjøl til dekk
- **Typgang (T)**: Dypgang under normale forhold (even-keel)

### Vektkilder:
Skipet flyter i lik vann (even-keel) uten trim eller list.

---

## Fase 2: Volumdeplasement

Lekteren flyter på even-keel, og volumdeplasementet er gitt ved:

$$\nabla = L \times B \times T$$

### Forklaring:
- **∇ (Nabla)**: Volumdeplasement (det volum vann som blir fortrengd)
- Siden skipet flyter på even-keel, er kontaktflaten rechtangulær
- Volumet beregnes som lengde × bredde × typgang

### Likevektsprinsipp:
For et flytende skip i likevekt: *Vekt av skip = Vekt av fortrengd vann*

---

## Fase 3: Kompartmentalisering

Lekteren er inndelt med 2 transverse vanntette skott, og som danner 3 like store vanntette avdelinger.

### Avdelinger:
- **Avdeling 1**: Fra for til første skott (lengde L/3)
- **Avdeling 2**: Fra første til andre skott (lengde L/3)
- **Avdeling 3**: Fra andre skott til akter (lengde L/3)

### Sikkerhet:
- Vanntette skott hindrer at vann sprer seg over hele skipet
- Hver avdeling kan håndtere ukontrollert vanninntrengning uavhengig
- Dette begrenser tapsomfanget ved skade

---

## Fase 4: Skadescenario

Lekteren får så en skade under vannlinjen i avdeling 2.

### Hva skjer:
- En åpning oppstår under vannlinjen
- Vann strømmer inn i avdeling 2
- Avdeling 2 mister sitt oppdriftsgivende volum

### Konsekvens:
- Tap av oppdrift = Tap av løftekraft
- Skipet må søke ny likevekt
- Skipet synker (dypgangen øker)

---

## Fase 5: Ny Likevekt

Lekteren vil søke ny likevekt ved en ny dypgang: **T_S**

### Hva som skjer:
1. Skade i avdeling 2 gir vanninntrengning helt opp til vannlinjen
2. Skipet synker (dypgangen øker fra T til T_S)
3. Vannet som må fortrengdes blir redusert
4. Ny likevekt oppnås når:
   - Kun avdeling 1 og 3 bidrar til oppdrift
   - Avdeling 2 er skadet og står i fri forbindelse med sjøen

---

## Fase 6: Matematisk Løsning

### Prinsipp 1: Bevaringsloven for Volum
I tapt oppdriftsmetoden er volumdeplasementet før og etter skade **uendret**:

$$\nabla \equiv \nabla_S$$

Dette betyr at det samme volumet vann må fortrengdes før og etter skaden (skipets vekt endres ikke).

### Prinsipp 2: Oppdriftgivende Volum
Oppdriftgivende volum består da av avdeling 1 og 3 i skadet dypgang:

$$L \times B \times T = \left(\frac{L}{3} + \frac{L}{3}\right) \times B \times T_S$$

Forenkling:
$$L \times B \times T = \frac{2L}{3} \times B \times T_S$$

### Løsning for ny dypgang:
Skadet dypgang løses videre slik:

$$T_S = \frac{\nabla}{\frac{2L}{3} \times B}$$

Eller enklere:

$$T_S = \frac{L \times B \times T}{\frac{2L}{3} \times B} = \frac{L \times T}{\frac{2L}{3}} = T \times \frac{3}{2} = 1.5 \times T$$

---

## Resultat

### Ny Dypgang ved Skade:
$$T_S = 1.5 \times T$$

**Betydning:**
- Skipet synker fra normaldypgang **T** til ny dypgang **T_S = 1.5T**
- En 50% økning i dypgang
- Hele avdeling 2 er skadet og står i fri forbindelse med sjøen

### Fysisk Tolkning:
- Skipet mister en tredjedel av sitt oppdriftsgivende volum (avdeling 2)
- De gjenværende to avdelingene (1 og 3) må fortrenge det samme volumet
- Siden disse bare utgjør 2/3 av original lengde, må de ha større dypgang for å oppnå samme volum

---

## Sammendrag: Stegene for Beregning

1. **Identifiser volum før skade**: $\nabla = L \times B \times T$
2. **Bestem oppdriftgivende areal etter skade**: $\frac{2L}{3} \times B$ (bare avdeling 1 og 3)
3. **Anvend bevaringsloven**: $\nabla = \nabla_S$
4. **Løs for ny dypgang**: $T_S = \frac{\nabla}{\frac{2L}{3} \times B}$
5. **Resultat**: Sammenlign T_S med T for å vurdere stabilitet

---

## Viktige Forutsetninger

- ✓ **Parallell submersjon**: Skipet synker rett ned uten trim eller list
- ✓ **Fullt fullvunnent rom**: Avdeling 2 er helt fylt med vann
- ✓ **Uforandret vekt**: Skipets vekt endres ikke (bare fordelinga)
- ✓ **Jevn vannlinje**: Vannlinjen er horisontal på begge sider
- ✓ **Ingen tipping**: Skipet forblir oppreist

---

## Praktisk Betydning

Dette beregningsprinsippet er kritisk for:
- **Skadestabilitet**: Vurdere skipets evne til å overleve skade
- **Sikkerhetskrav**: SOLAS-bestemmelser for kompartmentering
- **Operasjoner**: Vite grensene for sikker drift
- **Design**: Bestemme optimal skottplassering og størrelse

