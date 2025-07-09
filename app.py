import streamlit as st
from utils import detect_language, translate_text

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'te': 'Telugu',
    'mr': 'Marathi',
    'ta': 'Tamil',
    'ur': 'Urdu',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'pa': 'Punjabi',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ru': 'Russian',
    'pt': 'Portuguese',
    'it': 'Italian'
}

# Reverse mapping for dropdown
LANGUAGE_NAMES = sorted(LANGUAGES.values())
LANGUAGE_CODES = {v: k for k, v in LANGUAGES.items()}

st.set_page_config(page_title="Tranzly", layout="centered")

# Centered UI header
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='margin-bottom: 0;'>Tranzly</h1>
        <h4 style='margin-top: 0; color: gray;'>From Any Language, to Yours</h4>
        <p style='font-size: 16px; color: #666;'>
            Detect the language of any text and translate it instantly into your preferred language.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input box
text_input = st.text_area("✏️ Enter text to detect and translate:", height=150)

# Track detected language
if 'detected_code' not in st.session_state:
    st.session_state.detected_code = None

# Detect Button
if st.button("🔍 Detect Language"):
    if text_input.strip():
        code = detect_language(text_input)
        st.session_state.detected_code = code
        lang_name = LANGUAGES.get(code, "Unknown Language")
        st.success(f"Detected Language: **{lang_name}** (`{code}`)")
    else:
        st.warning("Please enter some text.")

# Dropdown for target language
target_lang_name = st.selectbox("🌍 Translate to:", LANGUAGE_NAMES)
target_lang_code = LANGUAGE_CODES[target_lang_name]

# Translate Button
if st.button("🌐 Translate"):
    if text_input.strip():
        result = translate_text(text_input, target_lang_code)
        st.success(f"**Translation:** {result}")
    else:
        st.warning("Please enter text to translate.")
