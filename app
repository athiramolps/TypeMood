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

# Show fonts for matched moods
def show_fonts(fonts):
    for font in fonts:
        font_name = font['name']
        google_font = font['google_font']
        font_link = f"https://fonts.googleapis.com/css2?family={google_font}&display=swap"
        st.markdown(f"""
            <link href="{font_link}" rel="stylesheet">
            <div style="font-family: '{font_name}', sans-serif; font-size: 36px; margin: 16px 0;">
                {font_name}
            </div>
        """, unsafe_allow_html=True)

if user_input:
    found = False
    for mood, fonts in mood_fonts.items():
        if user_input.lower() in mood.lower():
            st.subheader(f"🖋️ Fonts for: *{mood}*")
            show_fonts(fonts)
            found = True
    if not found:
        st.warning("😕 No matching mood found. Try keywords like 'romantic', 'luxury', or 'playful'.")
else:
    st.info("👈 Start typing a mood or vibe to explore matching fonts.")

st.markdown("---")
st.markdown("<small>Built with ❤️ using Streamlit • © 2025 TypeMood</small>", unsafe_allow_html=True)
