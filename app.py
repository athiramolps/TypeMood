import streamlit as st

# ---------- Expanded mood-font dictionary with single moods as keys ----------
mood_fonts = {
    "Passion": [
        {"name": "Impact", "google_font": "Impact"},
        {"name": "Bebas Neue", "google_font": "Bebas+Neue"},
    ],
    "Energy": [
        {"name": "Anton", "google_font": "Anton"},
    ],
    "Urgency": [
        {"name": "Anton", "google_font": "Anton"},
    ],
    "Romance": [
        {"name": "Playfair Display", "google_font": "Playfair+Display"},
        {"name": "Great Vibes", "google_font": "Great+Vibes"},
    ],
    "Intensity": [
        {"name": "Cinzel", "google_font": "Cinzel"},
    ],
    "Luxury": [
        {"name": "Cinzel", "google_font": "Cinzel"},
    ],
    "Youthful": [
        {"name": "Baloo", "google_font": "Baloo+2"},
    ],
    "Playful": [
        {"name": "Comic Neue", "google_font": "Comic+Neue"},
        {"name": "Pacifico", "google_font": "Pacifico"},
    ],
    "Excitement": [
        {"name": "Pacifico", "google_font": "Pacifico"},
    ],
    "Rustic": [
        {"name": "Arvo", "google_font": "Arvo"},
    ],
    "Earthy": [
        {"name": "Bitter", "google_font": "Bitter"},
    ],
    "Warmth": [
        {"name": "Courier Prime", "google_font": "Courier+Prime"},
    ],
    "Vibrant": [
        {"name": "Quicksand", "google_font": "Quicksand"},
    ],
    "Friendly": [
        {"name": "Poppins", "google_font": "Poppins"},
    ],
    "Feminine": [
        {"name": "Dancing Script", "google_font": "Dancing+Script"},
    ],
    "Softness": [
        {"name": "Lato", "google_font": "Lato"},
    ],
    "Innocence": [
        {"name": "EB Garamond", "google_font": "EB+Garamond"},
    ],
    "Calm": [
        {"name": "Comfortaa", "google_font": "Comfortaa"},
    ],
    "Success": [
        {"name": "Didot", "google_font": "Didact+Gothic"},
    ],
    "Wealth": [
        {"name": "Cormorant Garamond", "google_font": "Cormorant+Garamond"},
    ],
    "Radiance": [
        {"name": "Libre Baskerville", "google_font": "Libre+Baskerville"},
    ],
    "Elegant": [
        {"name": "Garamond", "google_font": "EB+Garamond"},
    ],
    "Classic": [
        {"name": "Cormorant", "google_font": "Cormorant+Garamond"},
    ],
    "Depth": [
        {"name": "Baskerville", "google_font": "Libre+Baskerville"},
    ],
    "Power": [
        {"name": "Bodoni Moda", "google_font": "Bodoni+Moda"},
    ],
    "Modernity": [
        {"name": "Didot", "google_font": "Didact+Gothic"},
    ],
    "Digital": [
        {"name": "Orbitron", "google_font": "Orbitron"},
    ],
    "Clean": [
        {"name": "Exo", "google_font": "Exo"},
    ],
    "Futuristic": [
        {"name": "Roboto Mono", "google_font": "Roboto+Mono"},
    ],
}

st.set_page_config(page_title="TypeMood - Single Mood Fonts", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>TypeMood</h1>
    <p style='text-align: center; font-size: 1.1em;'>Enter a mood keyword to find matching fonts.</p>
""", unsafe_allow_html=True)

user_input = st.text_input("Enter a mood keyword (e.g., Passion, Energy, Romance)").strip().capitalize()

if user_input:
    # case insensitive lookup
    matched_moods = [m for m in mood_fonts.keys() if m.lower() == user_input.lower()]
    if matched_moods:
        mood = matched_moods[0]
        fonts = mood_fonts[mood]
        st.markdown(f"### Fonts for mood: {mood}")
        for font in fonts:
            font_name = font['name']
            google_font = font['google_font']
            font_link = f"https://fonts.googleapis.com/css2?family={google_font}&display=swap"
            st.markdown(f'<link href="{font_link}" rel="stylesheet">', unsafe_allow_html=True)
            st.markdown(f'<div style="font-family:\'{font_name}\', sans-serif; font-size: 32px; margin-bottom: 12px;">{font_name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="font-family:\'{font_name}\', sans-serif; font-size: 18px; color: gray; margin-bottom: 32px;">The quick brown fox jumps over the lazy dog.</div>', unsafe_allow_html=True)
    else:
        st.warning(f"No fonts found for mood: '{user_input}'. Try another mood keyword.")
else:
    st.info("Please enter a mood keyword to see matching fonts.")

st.markdown("---")
st.markdown("<small>Built with ❤️ by Athiramol PS — June 25, 2025</small>", unsafe_allow_html=True)
