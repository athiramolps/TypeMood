import streamlit as st

# Font data for each mood
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
}

# Streamlit config
st.set_page_config(page_title="TypeMood - Font Heading Levels", layout="centered")

# Title
st.markdown("""
    <h1 style='text-align: center;'>TypeMood</h1>
    <p style='text-align: center; font-size: 1.1em;'>Choose or type a mood keyword to see fonts with h1-h6 preview.</p>
""", unsafe_allow_html=True)

# Dropdown and text input
mood_options = sorted(mood_fonts.keys())
selected_mood = st.selectbox("🎨 Select a mood from the list:", [""] + mood_options)
user_input = st.text_input("🔍 Or type a mood keyword (e.g., Passion, Calm, Luxury)").strip().lower()

# Combine dropdown and input
active_moods = []
if selected_mood:
    active_moods.append(selected_mood)
if user_input:
    matched_moods = [m for m in mood_fonts if user_input in m.lower()]
    active_moods.extend(m for m in matched_moods if m not in active_moods)

# Display fonts for selected/typed moods
if active_moods:
    for mood in active_moods:
        fonts = mood_fonts[mood]
        st.markdown(f"### Fonts for mood: {mood}")
        for font in fonts:
            font_name = font['name']
            google_font = font['google_font']
            font_link = f"https://fonts.googleapis.com/css2?family={google_font}&display=swap"
            st.markdown(f'<link href="{font_link}" rel="stylesheet">', unsafe_allow_html=True)
            st.markdown(f"<b>Font: {font_name}</b>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="font-family:'{font_name}', sans-serif; font-size: 2.5em; margin-bottom: 0;">h1. The children play happily in the sunny green park.</div>
                <div style="font-family:'{font_name}', sans-serif; font-size: 2em; margin-bottom: 0;">h2. The children play happily in the sunny green park.</div>
                <div style="font-family:'{font_name}', sans-serif; font-size: 1.75em; margin-bottom: 0;">h3. The children play happily in the sunny green park.</div>
                <div style="font-family:'{font_name}', sans-serif; font-size: 1.5em; margin-bottom: 0;">h4. The children play happily in the sunny green park.</div>
                <div style="font-family:'{font_name}', sans-serif; font-size: 1.25em; margin-bottom: 0;">h5. The children play happily in the sunny green park.</div>
                <div style="font-family:'{font_name}', sans-serif; font-size: 1em; margin-bottom: 24px;">h6. The children play happily in the sunny green park.</div>
            """, unsafe_allow_html=True)
else:
    st.info("Please select or enter a mood keyword to see fonts with h1-h6 preview.")

# Footer
st.markdown("---")
st.markdown("<small>Built with ❤️ by Athiramol PS — June 25, 2025</small>", unsafe_allow_html=True)
