import streamlit as st

# ---------- Full Mood-Font Mapping ----------
mood_fonts = {
    "Passion, Energy, Urgency": [
        {"name": "Impact", "google_font": "Impact"},
        {"name": "Bebas Neue", "google_font": "Bebas+Neue"},
        {"name": "Anton", "google_font": "Anton"}
    ],
    "Romance, Intensity, Luxury": [
        {"name": "Playfair Display", "google_font": "Playfair+Display"},
        {"name": "Great Vibes", "google_font": "Great+Vibes"},
        {"name": "Cinzel", "google_font": "Cinzel"}
    ],
    "Youthful, Playful, Excitement": [
        {"name": "Baloo", "google_font": "Baloo+2"},
        {"name": "Comic Neue", "google_font": "Comic+Neue"},
        {"name": "Pacifico", "google_font": "Pacifico"}
    ],
    "Rustic, Earthy, Warmth": [
        {"name": "Arvo", "google_font": "Arvo"},
        {"name": "Bitter", "google_font": "Bitter"},
        {"name": "Courier Prime", "google_font": "Courier+Prime"}
    ],
    "Vibrant, Friendly, Feminine": [
        {"name": "Quicksand", "google_font": "Quicksand"},
        {"name": "Poppins", "google_font": "Poppins"},
        {"name": "Dancing Script", "google_font": "Dancing+Script"}
    ],
    "Softness, Innocence, Calm": [
        {"name": "Lato", "google_font": "Lato"},
        {"name": "EB Garamond", "google_font": "EB+Garamond"},
        {"name": "Comfortaa", "google_font": "Comfortaa"}
    ],
    "Success, Wealth, Radiance": [
        {"name": "Didot", "google_font": "Didact+Gothic"},
        {"name": "Cormorant Garamond", "google_font": "Cormorant+Garamond"},
        {"name": "Libre Baskerville", "google_font": "Libre+Baskerville"}
    ],
    "Elegant, Classic, Depth": [
        {"name": "Garamond", "google_font": "EB+Garamond"},
        {"name": "Cormorant", "google_font": "Cormorant+Garamond"},
        {"name": "Baskerville", "google_font": "Libre+Baskerville"}
    ],
    "Luxury, Power, Modernity": [
        {"name": "Bodoni Moda", "google_font": "Bodoni+Moda"},
        {"name": "Didot", "google_font": "Didact+Gothic"},
        {"name": "Cormorant Upright", "google_font": "Cormorant+Upright"}
    ],
    "Digital, Clean, Futuristic": [
        {"name": "Orbitron", "google_font": "Orbitron"},
        {"name": "Exo", "google_font": "Exo"},
        {"name": "Roboto Mono", "google_font": "Roboto+Mono"}
    ]
    # Add remaining moods in similar format...
}

# ---------- Streamlit App UI ----------
st.set_page_config(page_title="TypeMood", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>TypeMood</h1>
    <p style='text-align: center; font-size: 1.1em;'>Find the perfect font for every feeling.</p>
""", unsafe_allow_html=True)

user_input = st.text_input("🎯 Enter Mood or Vibe (e.g., Elegant, Bold, Romantic)").strip()

# Show fonts for exact match only
def show_fonts(mood, fonts):
    st.markdown(f"<h3 style='margin-top: 40px;'>{mood}</h3>", unsafe_allow_html=True)
    for font in fonts:
        font_name = font['name']
        google_font = font['google_font']
        font_link = f"https://fonts.googleapis.com/css2?family={google_font}&display=swap"
        st.markdown(f"""
            <link href="{font_link}" rel="stylesheet">
            <div style="font-family: '{font_name}', sans-serif; font-size: 32px; padding-bottom: 12px;">
                {font_name}
            </div>
        """, unsafe_allow_html=True)

if user_input:
    matched_mood = None
    for mood in mood_fonts:
        if user_input.lower() == mood.lower():
            matched_mood = mood
            break
    if matched_mood:
        show_fonts(matched_mood, mood_fonts[matched_mood])
    else:
        st.warning("😕 No exact mood match found. Please check your spelling or try a listed mood.")
else:
    st.info("👈 Start typing a mood or vibe to explore matching fonts.")

st.markdown("---")
st.markdown("<small>Built with ❤️ by Athiramol PS — June 25, 2025</small>", unsafe_allow_html=True)
