
import streamlit as st

st.set_page_config(page_title="Betting AI – MultiSport", layout="centered")

st.title("🎯 Betting AI – MultiSport (Calcio, Tennis, Basket)")

sport = st.selectbox("Scegli lo sport", ["Calcio", "Tennis", "Basket"])

if sport == "Calcio":
    st.header("⚽ Calcio – Pronostico Personalizzato")
    squadra1 = st.text_input("Squadra 1")
    squadra2 = st.text_input("Squadra 2")
    pronostico = st.text_input("Pronostico (es. Over 2.5 gol, No Gol, Over 9.5 corner)")
    media = st.number_input("Media totale stimata", step=0.1)
    quota = st.number_input("Quota bookmaker", step=0.01)
    if st.button("Analizza Calcio"):
        prob = min(0.9, max(0.05, media / 5))
        quota_teorica = round(1 / prob, 2)
        st.markdown(f"**Match:** {squadra1} - {squadra2}")
        st.markdown(f"**Pronostico:** {pronostico}")
        st.markdown(f"**Probabilità stimata:** {round(prob*100, 1)}%")
        st.markdown(f"**Quota teorica:** {quota_teorica}")
        if quota > quota_teorica:
            st.success("✅ Value bet trovata!")
        else:
            st.error("❌ Nessun value, meglio evitare")

if sport == "Tennis":
    st.header("🎾 Tennis – Pronostico Personalizzato")
    g1 = st.text_input("Giocatore 1")
    g2 = st.text_input("Giocatore 2")
    pron = st.text_input("Pronostico (es. Over 9.5 ace, Tiebreak, Vincente)")
    successi = st.text_input("Quante volte è successo? (es. 6 su 10)")
    quota = st.number_input("Quota bookmaker", step=0.01, key="qt_tennis")
    if st.button("Analizza Tennis"):
        try:
            val = int(successi.split("su")[0].strip())
            tot = int(successi.split("su")[1].strip())
            prob = val / tot
            q_teo = round(1 / prob, 2)
            st.markdown(f"**Match:** {g1} vs {g2}")
            st.markdown(f"**Pronostico:** {pron}")
            st.markdown(f"**Probabilità stimata:** {round(prob*100, 1)}%")
            st.markdown(f"**Quota teorica:** {q_teo}")
            if quota > q_teo:
                st.success("✅ Value bet trovata!")
            else:
                st.error("❌ Nessun value, meglio evitare")
        except:
            st.warning("Scrivi correttamente il formato: 6 su 10")

if sport == "Basket":
    st.header("🏀 Basket – Pronostico Personalizzato")
    evento = st.text_input("Evento (facoltativo)")
    pron = st.text_input("Pronostico (es. Over 17.5 punti Haliburton)")
    successi = st.text_input("Quante volte è successo? (es. 7 su 10)")
    quota = st.number_input("Quota bookmaker", step=0.01, key="qt_basket")
    if st.button("Analizza Basket"):
        try:
            val = int(successi.split("su")[0].strip())
            tot = int(successi.split("su")[1].strip())
            prob = val / tot
            q_teo = round(1 / prob, 2)
            st.markdown(f"**Evento:** {evento}")
            st.markdown(f"**Pronostico:** {pron}")
            st.markdown(f"**Probabilità stimata:** {round(prob*100, 1)}%")
            st.markdown(f"**Quota teorica:** {q_teo}")
            if quota > q_teo:
                st.success("✅ Value bet trovata!")
            else:
                st.error("❌ Nessun value, meglio evitare")
        except:
            st.warning("Scrivi correttamente il formato: 7 su 10")
