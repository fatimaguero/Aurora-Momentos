import streamlit as st
from datetime import date

st.set_page_config(page_title="Aurora Momentos", layout="wide")

# ---------------- ESTILO LIMPO (SEM CONFLITO MOBILE) ----------------
st.markdown("""
<style>

/* fundo suave e profissional */
.stApp {
    background-color: #F7F5F3 !important;
    font-family: 'Poppins', sans-serif;
}

/* texto sempre legível */
h1, h2, h3, h4, h5, p, label {
    color: #222 !important;
}

/* header */
.app-header {
    text-align:center;
    padding:15px;
    border-bottom:1px solid #e6e6e6;
}

.app-title {
    color: #BFA181 !important;
    font-size: 34px;
    font-weight: 700;
}

.app-subtitle {
    color: #777 !important;
    font-size: 14px;
}

/* cards */
.card {
    background:white !important;
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

.premium {
    border:2px solid #BFA181;
}

/* botões */
.stButton > button {
    background-color: #BFA181 !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="app-header">
    <div class="app-title">Aurora Momentos</div>
    <div class="app-subtitle">Todo amor merece um novo amanhecer</div>
</div>
""", unsafe_allow_html=True)

# ---------------- MENU (🔥 CORREÇÃO DEFINITIVA) ----------------
menu = st.radio("", [
    "Início",
    "Buscar fotógrafo",
    "Filmmakers",
    "Meu evento",
    "Sou fotógrafo",
    "Sou filmmaker"
], horizontal=True)

# ---------------- BANCO ----------------
if "fotografos" not in st.session_state:
    st.session_state.fotografos = [
        {"nome": "Ana Luz", "cidade": "Petrópolis", "preco": 900,
         "instagram": "@analuzfoto", "portfolio": "link", "destaque": True},
        {"nome": "Carlos Vieira", "cidade": "Rio", "preco": 600,
         "instagram": "@carlosfoto", "portfolio": "link", "destaque": False},
    ]

if "filmmakers" not in st.session_state:
    st.session_state.filmmakers = [
        {"nome": "Love Films", "cidade": "RJ", "preco": 2000,
         "instagram": "@lovefilms", "portfolio": "link", "destaque": True}
    ]

# ---------------- INÍCIO ----------------
if menu == "Início":

    st.markdown("## ✨ Crie o site do seu evento gratuitamente")

    st.markdown("""
💍 Casamentos  
- Site completo com história do casal  
- Lista de convidados  
- Compartilhamento fácil  

👑 Festa de 15 anos  
- Página personalizada  
- Contagem regressiva  
- Informações organizadas  

🎈 Eventos infantis  
- Tema do aniversário  
- Local e horário  
- Experiência simples  

📸 Profissionais  
- Fotógrafos e filmmakers  
- Comparação de preços  
- Contratação direta  

🚀 Plataforma completa e gratuita
""")

# ---------------- BUSCAR FOTÓGRAFO ----------------
elif menu == "Buscar fotógrafo":

    st.markdown("### 📸 Encontre o fotógrafo ideal")

    cidade = st.text_input("Cidade")
    preco = st.slider("Preço máximo", 0, 5000, 1000)

    if st.button("Buscar"):

        resultados = [
            f for f in st.session_state.fotografos
            if cidade.lower() in f["cidade"].lower()
            and f["preco"] <= preco
        ]

        for f in resultados:
            badge = "🌟 Premium" if f.get("destaque") else ""
            classe = "card premium" if f.get("destaque") else "card"

            st.markdown(f"""
            <div class="{classe}">
            <h3>{f['nome']} {badge}</h3>
            <p>📍 {f['cidade']}</p>
            <p>💰 R${f['preco']}</p>
            <p>📷 {f['instagram']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FILMMAKERS ----------------
elif menu == "Filmmakers":

    st.markdown("### 🎬 Cinegrafistas")

    for f in st.session_state.filmmakers:
        st.markdown(f"""
        <div class="card">
        <h3>{f['nome']}</h3>
        <p>📍 {f['cidade']}</p>
        <p>💰 R${f['preco']}</p>
        <p>📷 {f['instagram']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- EVENTO ----------------
elif menu == "Meu evento":

    st.markdown("### 💖 Seu evento")

    opcao = st.radio("", ["Criar", "Ver eventos"])

    if opcao == "Criar":

        st.text_input("Nome do evento")
        st.date_input("Data")
        st.text_area("Descrição")
        st.text_input("Local")

        if st.button("Criar evento"):
            st.success("Evento criado!")

    else:

        dias = (date(2026, 12, 20) - date.today()).days

        st.markdown(f"""
        <div class="card">
        <h2 style="text-align:center;">Ana & Lucas 💍</h2>
        <p>📅 20/12/2026</p>
        <p>⏳ {dias} dias</p>
        <p>📍 Igreja Central</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- CADASTROS ----------------
elif menu == "Sou fotógrafo":

    st.markdown("### 📸 Cadastro fotógrafo")

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço")
    instagram = st.text_input("Instagram")

    plano = st.radio("Plano", ["Básico", "Premium 🌟"])

    if st.button("Cadastrar"):
        st.session_state.fotografos.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "destaque": "Premium" in plano
        })

        st.success("Cadastrado!")

elif menu == "Sou filmmaker":

    st.markdown("### 🎬 Cadastro filmmaker")

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço")
    instagram = st.text_input("Instagram")

    plano = st.radio("Plano", ["Básico", "Premium 🌟"])

    if st.button("Cadastrar"):
        st.session_state.filmmakers.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "destaque": "Premium" in plano
        })

        st.success("Cadastrado!")