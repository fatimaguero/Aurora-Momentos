import streamlit as st
from datetime import date

st.set_page_config(page_title="Aurora Momentos", layout="wide")

# ---------------- ESTILO FINAL ESTÁVEL ----------------
st.markdown("""
<style>

/* fundo geral */
.stApp {
    background-color: #FAF7F8 !important;
    font-family: 'Poppins', sans-serif;
}

/* texto seguro (não quebra Início no celular) */
h1, h2, h3, h4, h5 {
    color: #222 !important;
}

p, li, label {
    color: #222 !important;
    line-height: 1.6;
}

/* protege Markdown Streamlit */
.stMarkdown {
    color: #222 !important;
}

/* ---------------- HEADER ---------------- */
.app-header {
    text-align:center;
    padding:15px;
    border-bottom:1px solid #eee;
    background: transparent !important;
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

/* ---------------- MENU (CORREÇÃO DEFINITIVA MOBILE) ---------------- */
div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 10px !important;
}

/* texto do select sempre visível */
div[data-baseweb="select"] * {
    color: #222 !important;
}

/* 🔥 FIX PRINCIPAL: dropdown aparece no topo do app */
div[data-baseweb="popover"] {
    z-index: 999999 !important;
}

/* lista de opções */
div[role="listbox"] {
    background-color: white !important;
    border: 1px solid #eee !important;
    z-index: 999999 !important;
}

/* opções visíveis */
div[role="option"] {
    color: #222 !important;
    background-color: white !important;
}

/* hover */
div[role="option"]:hover {
    background-color: #f2f2f2 !important;
}

/* ---------------- BOTÃO ---------------- */
.stButton > button {
    background-color: #BFA181 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 8px 16px !important;
    border: none !important;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #a88f6d !important;
}

/* ---------------- CARDS ---------------- */
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

/* inputs */
input, textarea, select {
    color:#222 !important;
    background-color:white !important;
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
### 💖 Tudo o que você pode fazer na Aurora Momentos

💍 Casamentos  
- Site completo do casal com história e fotos  
- Lista de convidados e confirmação de presença  
- Compartilhamento fácil pelo WhatsApp  

👑 Festa de 15 anos  
- Página personalizada da debutante  
- Contagem regressiva até o grande dia  
- Informações organizadas do evento  

🎈 Eventos infantis  
- Tema personalizado do aniversário  
- Local, horário e lembretes automáticos  
- Experiência simples para os convidados  

📸 Profissionais do evento  
- Encontre fotógrafos e filmmakers  
- Compare preços e portfólios  
- Contratação direta simplificada  

🚀 Recursos extras  
- Site pronto em minutos  
- Totalmente gratuito para criar evento  
- Acesso pelo celular ou computador  
- Design elegante e profissional
""")

# ---------------- BUSCAR FOTÓGRAFO ----------------
elif menu == "Buscar fotógrafo":

    st.markdown("### 📸 Encontre o fotógrafo ideal")

    cidade = st.text_input("Cidade")
    preco = st.slider("Preço máximo", 0, 5000, 1000)

    if st.button("Buscar fotógrafo"):

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

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço")
    instagram = st.text_input("Instagram")
    portfolio = st.text_input("Portfólio")

    plano = st.radio("Plano", ["Básico", "Premium 🌟"])

    if st.button("Cadastrar fotógrafo"):
        st.session_state.fotografos.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "portfolio": portfolio,
            "destaque": "Premium" in plano
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
        st.session_state.filmmakers.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "instagram": instagram,
            "portfolio": portfolio,
            "destaque": "Premium" in plano
        })

        st.success("Cadastrado!")