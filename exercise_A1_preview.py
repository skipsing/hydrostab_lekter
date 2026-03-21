# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # A1 forhåndsvisning: Symmetrisk oppfylling
#
# ## Oppgave
# - Beregn ny likevektsdypgang ved symmetrisk oppfylling.
#
# ## Gitt
# - Rektangulær lekter med $L = 50.0\ \mathrm{m}$, $B = 10.0\ \mathrm{m}$, $D = 5.0\ \mathrm{m}$
# - Initial dypgang $T = 2.80\ \mathrm{m}$
# - Lengde på skadet rom $l_d = 2.0\ \mathrm{m}$
# - Antar full tap-av-oppdrift i skadet rom og parallell nedsynking i denne oppgaven
#
# ## Leveranser
# - Endelig dypgang
# - Kort metode
#
# ## Styrende sammenheng
# $LBT = (L - l_d)BT_S$

# %%
# Inndata
L = 50.0      # m
B = 10.0      # m
D = 5.0       # m
T = 2.80      # m
l_d = 2.0     # m

# Leveranser (bevisst tomme for at studenten skal fylle inn)
T_S = None                 # symmetrisk skadet dypgang [m]
method_summary = None      # kort metodebeskrivelse

# %% [markdown]
# ## Løsning
#
# Siste trinn:
#
# $T_S = \frac{50.0}{50.0-2.0}\cdot 2.80 = 2.9167\ \mathrm{m}$
#
# $2.9167\ \mathrm{m} < D = 5.0\ \mathrm{m}$, så dypgangen er fortsatt mindre enn dybden.
