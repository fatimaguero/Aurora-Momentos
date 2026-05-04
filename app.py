import streamlit as st
from datetime import date

st.set_page_config(page_title="Aurora Momentos", layout="wide")

# ---------------- ESTILO LIMPO (CORREÇÃO SOMENTE VISIBILIDADE INÍCIO) ----------------
st.markdown("""
<style>

.stApp {
    background-color: #F7F5F3 !important;
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3, h4, h5, p, label {
    color: #222 !important;
}

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

/* 🔥 CORREÇÃO DEFINITIVA DO INÍCIO (TEXTOS QUE SUMIAM NO CELULAR) */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown ul, .stMarkdown ol {
    color: #222 !important;
    opacity: 1 !important;
    visibility: visible !important;
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

# ---------------- MENU ----------------
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
- Site completo do casal  
- Lista de convidados  
- Compartilhamento fácil  

👑 Festa de 15 anos  
- Página personalizada  
- Contagem regressiva  
- Informações do evento  

🎈 Eventos infantis  
- Tema personalizado  
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

        for f in st.session_state.fotografos:
            st.markdown(f"""
            <div class="card">
            <h3>{f['nome']}</h3>
            <p>📍 {f['cidade']}</p>
            <p>💰 R${f['preco']}</p>
            <p>📷 {f['instagram']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FILMMAKERS ----------------
elif menu == "Filmmakers":

    st.markdown("### 🎬 Cinegrafistas disponíveis")

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
        <p>⏳ {dias} dias</p>
        <p>📍 Igreja Central</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- CADASTRO FOTÓGRAFO ----------------
elif menu == "Sou fotógrafo":

    st.markdown("### 📸 Cadastre-se como fotógrafo")

    st.markdown("""
### 💼 Planos

<p><b>Básico — R$ 79,90</b></p>
<p>✔ Perfil no site</p>

<hr>

<p><b>Premium — R$ 129,90 🌟</b></p>
<p>✔ Destaque nas buscas<br>✔ Mais visibilidade</p>
""", unsafe_allow_html=True)

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

# ---------------- CADASTRO FILMMAKER ----------------
elif menu == "Sou filmmaker":

    st.markdown("### 🎬 Cadastre-se como filmmaker")

    st.markdown("""
### 💼 Planos

<p><b>Básico — R$ 79,90</b></p>
<p>✔ Perfil no site</p>

<hr>

<p><b>Premium — R$ 129,90 🌟</b></p>
<p>✔ Destaque nas buscas<br>✔ Mais visibilidade</p>
""", unsafe_allow_html=True)

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