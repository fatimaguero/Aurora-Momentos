import streamlit as st

st.set_page_config(page_title="Aurora Momentos", layout="wide")

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<style>

/* FORÇAR MODO CLARO (resolve iPhone) */
:root {
    color-scheme: light;
}

/* FONTE */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body {
    font-family: 'Poppins', sans-serif;
    background-color: #FAF7F8 !important;
    color: #000000 !important;
}

/* ESCONDER MENU STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ESPAÇAMENTO */
.block-container {
    padding: 1rem;
}

/* BOTÕES */
button {
    font-size: 16px !important;
}

/* CARD */
.card {
    background: white !important;
    color: black !important;
    border-radius: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 15px;
    overflow: hidden;
}

.card h3, .card p {
    color: black !important;
}

/* IMAGEM */
.card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

/* CONTEÚDO */
.card-content {
    padding: 15px;
}

/* DESTAQUE */
.destaque {
    border: 2px solid #BFA181;
}

/* BADGE */
.badge {
    background-color: #BFA181;
    color: white;
    padding: 4px 10px;
    border-radius: 10px;
    font-size: 12px;
}

/* WHATSAPP */
.whatsapp {
    display:block;
    text-align:center;
    background:#25D366;
    color:white;
    padding:12px;
    border-radius:12px;
    text-decoration:none;
    margin-bottom:20px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h2 style='text-align:center; color:#BFA181;'>Aurora Momentos</h2>
<p style='text-align:center; color:#777;'>Fotógrafos incríveis perto de você 📸</p>
""", unsafe_allow_html=True)

menu = st.selectbox("", ["Buscar fotógrafo", "Sou fotógrafo"])

# ---------------- BANCO ----------------
if "fotografos" not in st.session_state:
    st.session_state.fotografos = [
        {"nome": "Ana Luz", "cidade": "Petrópolis", "preco": 800, "contato": "5524999991111", "destaque": True,
         "foto": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"},

        {"nome": "Juliana Rocha", "cidade": "Petrópolis", "preco": 1200, "contato": "5524977773333", "destaque": True,
         "foto": "https://images.unsplash.com/photo-1519741497674-611481863552"},

        {"nome": "Fernanda Alves", "cidade": "Petrópolis", "preco": 950, "contato": "5524955555555", "destaque": True,
         "foto": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91"},

        {"nome": "Carlos Vieira", "cidade": "Rio de Janeiro", "preco": 500, "contato": "5521988882222", "destaque": False,
         "foto": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"},

        {"nome": "Lucas Martins", "cidade": "Rio de Janeiro", "preco": 400, "contato": "5521944446666", "destaque": False,
         "foto": "https://images.unsplash.com/photo-1492724441997-5dc865305da7"}
    ]

# ---------------- BUSCA ----------------
if menu == "Buscar fotógrafo":

    st.subheader("🔎 Buscar")

    cidade = st.text_input("Cidade")
    preco = st.slider("Preço máximo", 0, 5000, 1000)

    if st.button("Buscar"):

        resultados = [
            f for f in st.session_state.fotografos
            if cidade.lower() in f["cidade"].lower()
            and f["preco"] <= preco
        ]

        resultados = sorted(resultados, key=lambda x: x["destaque"], reverse=True)

        for i, f in enumerate(resultados):

            badge = "🌟 Premium" if f["destaque"] else ""
            classe = "card destaque" if f["destaque"] else "card"

            link = f"https://wa.me/{f['contato']}?text=Olá, vi seu perfil no Aurora Momentos!"

            # CARD
            st.markdown(f"""
            <div class='{classe}'>
                <img src="{f['foto']}">
                <div class='card-content'>
                    <h3>{f['nome']} {badge}</h3>
                    <p>📍 {f['cidade']}</p>
                    <p>💰 <strong style='color:#BFA181;'>R${f['preco']}</strong></p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # BOTÃO CONTRATAR
            if st.button(f"✨ Contratar {f['nome']}", key=f"contratar_{i}"):
                st.success(f"Pedido enviado para {f['nome']}!")
                st.info("Em breve você poderá acompanhar e pagar pelo app 💎")

            # BOTÃO WHATSAPP
            st.markdown(f"""
            <a href="{link}" target="_blank" class="whatsapp">
            📲 Falar no WhatsApp
            </a>
            """, unsafe_allow_html=True)

# ---------------- CADASTRO ----------------
elif menu == "Sou fotógrafo":

    st.subheader("📸 Criar perfil")

    nome = st.text_input("Nome")
    cidade = st.text_input("Cidade")
    preco = st.number_input("Preço", 0, 10000)
    contato = st.text_input("WhatsApp (ex: 5524999999999)")
    foto = st.text_input("Rede social")
    foto = st.text_input("Site")
    destaque = st.checkbox("Quero ser Premium 🌟")

    if st.button("Cadastrar"):

        st.session_state.fotografos.append({
            "nome": nome,
            "cidade": cidade,
            "preco": preco,
            "contato": contato,
            "foto": foto,
            "destaque": destaque
        })

        st.success("Perfil criado com sucesso!")