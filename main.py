

import streamlit as st
import re

st.set_page_config(page_title="Betting AI MultiSport Esteso", layout="centered")
st.title("🎯 Betting AI - MultiSport (Calcio, Tennis, Basket)")

sport = st.selectbox("Scegli lo sport", ["Calcio", "Tennis", "Basket"])

def stima_probabilita(pronostico, media):
    pronostico = pronostico.lower()
    try:
        soglia = float(re.search(r"(over|under)\s*([0-9\.]+)", pronostico).group(2))
    except:
        soglia = media

    if "over" in pronostico:
        base_prob = media / (soglia + 1.5)
    elif "under" in pronostico:
        base_prob = (soglia + 1.5 - media) / (soglia + 1.5)
    elif "gol" in pronostico or "goal" in pronostico:
        base_prob = media / 3.5
    else:
        base_prob = media / (media + 2.5)

    base_prob = min(max(base_prob, 0.01), 0.90)
    margine = 0.1 * base_prob
    return min(max(base_prob, 0.01), 0.90), (round((base_prob - margine) * 100, 1), round((base_prob + margine) * 100, 1))

def calcola_value(prob, quota):
    quota_teo = round(1 / prob, 2)
    value = round(quota - quota_teo, 2)
    return quota_teo, value

if sport == "Calcio":
    st.header("⚽ Calcio – Pronostico Personalizzato")
    squadra1 = st.text_input("Squadra 1")
    squadra2 = st.text_input("Squadra 2")
    pronostico = st.text_input("Pronostico (es. Over 2.5 gol, No Gol, Over 9.5 corner)")
    media_stat = st.number_input("Media totale stimata", min_value=0.0, step=0.1)
    quota = st.number_input("Quota bookmaker", min_value=1.01, step=0.01)

    if st.button("Analizza Calcio"):
        prob, intervallo = stima_probabilita(pronostico, media_stat)
        quota_teo, value = calcola_value(prob, quota)
        st.markdown(f"**Match:** {squadra1} - {squadra2}")
        st.markdown(f"**Pronostico:** {pronostico}")
        st.markdown(f"**Probabilità stimata:** {round(prob * 100, 1)}%")
        st.markdown(f"**Intervallo realistico:** {intervallo[0]}% - {intervallo[1]}%")
        st.markdown(f"**Quota teorica:** {quota_teo}")
        if value > 0.15:
            st.success("✅ Value bet trovata!")
        elif value > 0:
            st.info("🟡 Value borderline")
        else:
            st.error("❌ Nessun value")

elif sport == "Tennis":
    st.header("🎾 Tennis – Pronostico Personalizzato")
    giocatore1 = st.text_input("Giocatore 1")
    giocatore2 = st.text_input("Giocatore 2")
    pronostico = st.text_input("Pronostico (es. Over 9.5 ace, Tiebreak, Vincente)")
    statistica = st.text_input("Quante volte è successo? (es. 6 su 10)")
    quota = st.number_input("Quota bookmaker", min_value=1.01, step=0.01)

    match = re.search(r"(\d+)\s*(su|/|di)\s*(\d+)", statistica)
    prob = None
    if match:
        successi = int(match.group(1))
        totali = int(match.group(3))
        if totali > 0:
            prob = min(successi / totali, 0.90)

    if st.button("Analizza Tennis"):
        if prob:
            margine = 0.1 * prob
            quota_teo, value = calcola_value(prob, quota)
            intervallo = (round((prob - margine) * 100, 1), round((prob + margine) * 100, 1))
            st.markdown(f"**Match:** {giocatore1} vs {giocatore2}")
            st.markdown(f"**Pronostico:** {pronostico}")
            st.markdown(f"**Probabilità stimata:** {round(prob * 100, 1)}%")
            st.markdown(f"**Intervallo realistico:** {intervallo[0]}% - {intervallo[1]}%")
            st.markdown(f"**Quota teorica:** {quota_teo}")
            if value > 0.15:
                st.success("✅ Value bet trovata!")
            elif value > 0:
                st.info("🟡 Value borderline")
            else:
                st.error("❌ Nessun value")
        else:
            st.warning("⚠️ Inserisci una statistica come '6 su 10'")

elif sport == "Basket":
    st.header("🏀 Basket – Pronostico Personalizzato")
    evento = st.text_input("Evento (facoltativo)")
    pronostico = st.text_input("Pronostico (es. Over 17.5 punti Haliburton)")
    statistica = st.text_input("Quante volte è successo? (es. 7 su 10)")
    quota = st.number_input("Quota bookmaker", min_value=1.01, step=0.01)

    match = re.search(r"(\d+)\s*(su|/|di)\s*(\d+)", statistica)
    prob = None
    if match:
        successi = int(match.group(1))
        totali = int(match.group(3))
        if totali > 0:
            prob = min(successi / totali, 0.90)

    if st.button("Analizza Basket"):
        if prob:
            margine = 0.1 * prob
            quota_teo, value = calcola_value(prob, quota)
            intervallo = (round((prob - margine) * 100, 1), round((prob + margine) * 100, 1))
            st.markdown(f"**Evento:** {evento}")
            st.markdown(f"**Pronostico:** {pronostico}")
            st.markdown(f"**Probabilità stimata:** {round(prob * 100, 1)}%")
            st.markdown(f"**Intervallo realistico:** {intervallo[0]}% - {intervallo[1]}%")
            st.markdown(f"**Quota teorica:** {quota_teo}")
            if value > 0.15:
                st.success("✅ Value bet trovata!")
            elif value > 0:
                st.info("🟡 Value borderline")
            else:
                st.error("❌ Nessun value")
        else:
            st.warning("⚠️ Inserisci una statistica come '7 su 10'")
