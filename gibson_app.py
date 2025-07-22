#Gibson App

import streamlit as st

def vcalc(n):
    vinmix = 0
    divisionfactor = 1
    H2O = 0
    while vinmix < 1:
        divisionfactor += 1
        p = n / divisionfactor
        H2O += 17
        vinmix = 50 / p
    return [H2O, round(vinmix, 3), divisionfactor]

def icalc(iconc, vlen, ilen):
    iinmix = 0
    divisionfactor = 1
    H2O = 0
    imass = 3 * 50 * (ilen / vlen)
    while iinmix < 1:
        divisionfactor += 1
        p = iconc / divisionfactor
        H2O += 17
        iinmix = imass / p
    return [H2O, round(iinmix, 3), divisionfactor]

# --- Streamlit UI ---
st.title("🧬 Gibson Assembly Calculator")

st.markdown("Enter the following values to calculate your Gibson cloning mix:")

vconc = st.number_input("Vector concentration (ng/µL)", min_value=0.0, step=0.1)
iconc = st.number_input("Insert concentration (ng/µL)", min_value=0.0, step=0.1)
vlen = st.number_input("Vector length (bp)", min_value=1.0, step=1.0)
ilen = st.number_input("Insert length (bp)", min_value=1.0, step=1.0)

if st.button("Calculate"):
    if any(x == 0 for x in [vconc, iconc, vlen, ilen]):
        st.error("Please fill in all values greater than 0.")
    else:
        v = vcalc(vconc)
        i = icalc(iconc, vlen, ilen)

        st.subheader("🧪 Vector:")
        st.write(f"- Add **{v[0]} µL** of water for a **{v[2]}x dilution**.")
        st.write(f"- Then add **{v[1]} µL** of this solution to the Gibson MasterMix.")

        st.subheader("🧪 Insert:")
        st.write(f"- Add **{i[0]} µL** of water for a **{i[2]}x dilution**.")
        st.write(f"- Then add **{i[1]} µL** of this solution to the Gibson MasterMix.")
