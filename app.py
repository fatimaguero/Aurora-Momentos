import streamlit as st
from datetime import date

st.set_page_config(page_title="Aurora Momentos", layout="wide")

# ---------------- ESTILO ----------------
st.markdown("""
<style>
body {
    font-family: 'Poppins', sans-serif;
    background-color: #FAF7F8;
}

.app-header {
    text-align:center;
    padding:10px;
    border-bottom:1px solid #eee;
}

.card {
    background:white;
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

.premium {
    border:2px solid #BFA181;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="app-header">
<h2 style='color:#BFA181;'>Aurora Momentos</h2>
<p style='color:#777;'>Todo amor merece um novo amanhecer</p>
</div>
""", unsafe_allow_html=True)

# ---------------- MENU ----------------
menu = st.selectbox("", [
    "Início",
    "Buscar fotógrafo",
    "Filmmakers",
    "Meu evento",
    "Sou fotógrafo",
    "Sou filmmaker"
])

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
    ### 💖 Ideal para todos os momentos especiais

    💍 **Casamentos**
    - Crie um site romântico com a história do casal
    - Compartilhe com convidados
    - Organize tudo em um só lugar

    👑 **Festa de 15 anos**
    - Página personalizada da debutante
    - Informações do evento
    - Compartilhamento fácil

    🎈 **Eventos infantis**
    - Página divertida para aniversários
    - Local, horário e tema organizados
    - Facilita para pais e convidados

    ---

    ✨ **O que você pode fazer:**
    - Criar seu site personalizado
    - Contagem regressiva para o evento
    - Informar local e detalhes
    - Lista de presentes

    ---

    📸 **Encontre fotógrafos e cinegrafistas**
    Profissionais prontos para registrar seu momento

    🚀 **100% gratuito para quem cria o evento**
    """)

# ---------------- BUSCA ----------------
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

        resultados = sorted(resultados, key=lambda x: x.get("destaque"), reverse=True)

        for f in resultados:
            badge = "🌟 Premium" if f.get("destaque") else ""
            classe = "card premium" if f.get("destaque") else "card"

            st.markdown(f"""
            <div class="{classe}">
            <h3>{f['nome']} {badge}</h3>
            <p>📍 {f['cidade']}</p>
            <p>💰 R${f['preco']}</p>
            <p>📷 {f['instagram']}</p>
            <p>📸 Portfólio: {f['portfolio']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FILMMAKERS ----------------
elif menu == "Filmmakers":

    st.markdown("### 🎬 Cinegrafistas disponíveis")

    for f in st.session_state.filmmakers:
        badge = "🌟 Premium" if f.get("destaque") else ""

        st.markdown(f"""
        <div class="card">
        <h3>{f['nome']} {badge}</h3>
        <p>📍 {f['cidade']}</p>
        <p>💰 R${f['preco']}</p>
        <p>📷 {f['instagram']}</p>
        <p>🎬 Portfólio: {f['portfolio']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- EVENTO ----------------
elif menu == "Meu evento":

    st.markdown("### 💖 Seu evento")

    opcao = st.radio("", ["Criar", "Ver eventos"])

    if opcao == "Criar":

        nome = st.text_input("Nome do evento")
        data_evento = st.date_input("Data")
        descricao = st.text_area("Descrição")
        local = st.text_input("Local")

        if st.button("Criar evento"):
            st.success("Evento criado!")

    else:

        data_exemplo = date(2026, 12, 20)
        dias = (data_exemplo - date.today()).days

        st.image("https://images.unsplash.com/photo-1519741497674-611481863552")

        st.markdown(f"""
        <div class="card">
        <h2 style="text-align:center;">Ana & Lucas 💍</h2>

        <p style="text-align:center;">
        Um dia inesquecível para celebrar o amor
        </p>

        <p>📅 20/12/2026</p>
        <p>⏳ {dias} dias</p>

        <p>📍 Igreja Central</p>
        <p>🎉 Espaço Aurora</p>

        </div>
        """, unsafe_allow_html=True)

# ---------------- FOTÓGRAFO ----------------
elif menu == "Sou fotógrafo":

    st.markdown("### 📸 Cadastre-se como fotógrafo")

    st.markdown("""
    <div class="card">
    <h3>💼 Planos</h3>

    <p><strong>Básico — R$ 79,90</strong></p>
    <p>✔ Perfil no site</p>

    <hr>

    <p><strong>Premium — R$ 129,90 🌟</strong></p>
    <p>✔ Destaque nas buscas<br>
    ✔ Mais visibilidade</p>
    </div>
    """, unsafe_allow_html=True)

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço")
    instagram = st.text_input("Instagram")
    portfolio = st.text_input("Portfólio")

    plano = st.radio("Plano", ["Básico", "Premium 🌟"])

    if st.button("Cadastrar fotógrafo"):
        destaque = True if "Premium" in plano else False

        st.session_state.fotografos.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "portfolio": portfolio,
            "destaque": destaque
        })

        st.success("Cadastrado!")

# ---------------- FILMMAKER ----------------
elif menu == "Sou filmmaker":

    st.markdown("### 🎬 Cadastre-se como filmmaker")

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço")
    instagram = st.text_input("Instagram")
    portfolio = st.text_input("Portfólio")

    plano = st.radio("Plano", ["Básico", "Premium 🌟"])

    if st.button("Cadastrar filmmaker"):
        destaque = True if "Premium" in plano else False

        st.session_state.filmmakers.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "portfolio": portfolio,
            "destaque": destaque
        })

        st.success("Cadastrado!")