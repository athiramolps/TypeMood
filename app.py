import streamlit as st

# Mood to font mapping
mood_fonts = {
    "Passion": [{"name": "Impact", "google_font": "Impact"}, {"name": "Bebas Neue", "google_font": "Bebas+Neue"}],
    "Energy": [{"name": "Anton", "google_font": "Anton"}],
    "Urgency": [{"name": "Anton", "google_font": "Anton"}],
    "Romance": [{"name": "Playfair Display", "google_font": "Playfair+Display"}, {"name": "Great Vibes", "google_font": "Great+Vibes"}],
    "Intensity": [{"name": "Cinzel", "google_font": "Cinzel"}],
    "Luxury": [{"name": "Cinzel", "google_font": "Cinzel"}],
    "Youthful": [{"name": "Baloo", "google_font": "Baloo+2"}],
    "Playful": [{"name": "Comic Neue", "google_font": "Comic+Neue"}, {"name": "Pacifico", "google_font": "Pacifico"}],
    "Excitement": [{"name": "Pacifico", "google_font": "Pacifico"}],
    "Rustic": [{"name": "Arvo", "google_font": "Arvo"}],
    "Earthy": [{"name": "Bitter", "google_font": "Bitter"}],
    "Warmth": [{"name": "Courier Prime", "google_font": "Courier+Prime"}],
    "Vibrant": [{"name": "Quicksand", "google_font": "Quicksand"}],
    "Friendly": [{"name": "Poppins", "google_font": "Poppins"}],
    "Feminine": [{"name": "Dancing Script", "google_font": "Dancing+Script"}],
    "Softness": [{"name": "Lato", "google_font": "Lato"}],
    "Innocence": [{"name": "EB Garamond", "google_font": "EB+Garamond"}],
    "Calm": [{"name": "Comfortaa", "google_font": "Comfortaa"}],
    "Success": [{"name": "Didot", "google_font": "Didact+Gothic"}],
    "Wealth": [{"name": "Cormorant Garamond", "google_font": "Cormorant+Garamond"}],
    "Radiance": [{"name": "Libre Baskerville", "google_font": "Libre+Baskerville"}],
    "Elegant": [{"name": "Garamond", "google_font": "EB+Garamond"}],
    "Classic": [{"name": "Cormorant", "google_font": "Cormorant+Garamond"}],
    "Depth": [{"name": "Baskerville", "google_font": "Libre+Baskerville"}],
    "Power": [{"name": "Bodoni Moda", "google_font": "Bodoni+Moda"}],
    "Modernity": [{"name": "Didot", "google_font": "Didact+Gothic"}],
    "Digital": [{"name": "Orbitron", "google_font": "Orbitron"}],
    "Clean": [{"name": "Exo", "google_font": "Exo"}],
    "Futuristic": [{"name": "Roboto Mono", "google_font": "Roboto+Mono"}],
    "Minimalist": [{"name": "Work Sans", "google_font": "Work+Sans"}],
    "Mysterious": [{"name": "UnifrakturCook", "google_font": "UnifrakturCook"}],
    "Professional": [{"name": "Open Sans", "google_font": "Open+Sans"}],
    "Bold": [{"name": "Oswald", "google_font": "Oswald"}],
    "Sad": [{"name": "Crimson Text", "google_font": "Crimson+Text"}],
    "Happy": [{"name": "Fredoka", "google_font": "Fredoka"}],
    "Vintage": [{"name": "Special Elite", "google_font": "Special+Elite"}],
    "Retro": [{"name": "Bangers", "google_font": "Bangers"}],
    "Creative": [{"name": "Gloria Hallelujah", "google_font": "Gloria+Hallelujah"}],
    "Techy": [{"name": "Share Tech Mono", "google_font": "Share+Tech+Mono"}],
}

st.set_page_config(page_title="TypeMood", layout="wide")

# Title and description
st.markdown("""
    <h1 style='text-align: center; color: #6A1B9A;'>🎨 TypeMood</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>
        A mood-based font exploration app for UI/UX designers and content creators.<br>
        Type or choose a mood to preview fonts with h1 to h6 heading levels.<br>
        Customize size and font style below.
    </p>
""", unsafe_allow_html=True)

# Inputs: mood typed or selected
col1, col2 = st.columns([2,1])
with col1:
    typed_mood = st.text_input("Type a mood (e.g., Calm, Bold, Luxury)").strip().lower()
with col2:
    selected_mood = st.selectbox("Select a mood from list:", [""] + sorted(mood_fonts.keys())).strip().lower()

# Style controls
col3, col4, col5, col6 = st.columns(4)
with col3:
    font_size = st.selectbox("Font size (px)", ["16", "18", "20", "24", "30", "36", "48"], index=2)
with col4:
    bold = st.checkbox("Bold")
with col5:
    italic = st.checkbox("Italic")
with col6:
    underline = st.checkbox("Underline")

# Decide moods to show
final_moods = []
if typed_mood:
    final_moods = [m for m in mood_fonts if typed_mood in m.lower()]
elif selected_mood:
    final_moods = [m for m in mood_fonts if selected_mood == m.lower()]

# Collect Google Fonts to load once
fonts_to_load = set()
for mood in final_moods:
    for font in mood_fonts[mood]:
        fonts_to_load.add(font['google_font'])

# Load all fonts once
for gf in fonts_to_load:
    font_link = f"https://fonts.googleapis.com/css2?family={gf}&display=swap"
    st.markdown(f'<link href="{font_link}" rel="stylesheet">', unsafe_allow_html=True)

# Prepare CSS styles from user input
style_font_weight = "bold" if bold else "normal"
style_font_style = "italic" if italic else "normal"
style_text_decoration = "underline" if underline else "none"
font_size_px = int(font_size)

# Show results or info
if final_moods:
    for mood in final_moods:
        st.subheader(f"Fonts for Mood: {mood}")
        for font in mood_fonts[mood]:
            font_name = font['name']
            st.markdown(f"<b>Font: {font_name}</b>", unsafe_allow_html=True)

            for tag, base_em in zip(["h1","h2","h3","h4","h5","h6"], [2.5,2,1.75,1.5,1.25,1]):
                computed_size = base_em * font_size_px
                st.markdown(f"""
                    <div style="
                        font-family: '{font_name}', sans-serif;
                        font-size: {computed_size}px;
                        font-weight: {style_font_weight};
                        font-style: {style_font_style};
                        text-decoration: {style_text_decoration};
                        margin-bottom: 10px;
                    ">
                        {tag}. The children play happily in the sunny green park.
                    </div>
                """, unsafe_allow_html=True)
else:
    st.info("🔎 Type or select a mood to preview matching fonts.")

# Footer
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style="text-align: center; font-size: 14px; color: gray;">
        © All rights reserved by <strong>Athiramol PS</strong><br>
        Published on: <strong>June 26, 2025</strong><br>
        This project, <em>“TypeMood: A Visual Guide to Mood-Based Typography”</em>, is an original creation.
    </div>
""", unsafe_allow_html=True)
