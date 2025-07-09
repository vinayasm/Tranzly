import streamlit as st
from utils import detect_language, translate_text

# 🌐 Supported Languages
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'ta': 'Tamil',
    'te': 'Telugu',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'gu': 'Gujarati',
    'mr': 'Marathi',
    'pa': 'Punjabi',
    'ur': 'Urdu',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'ko': 'Korean',
    'ja': 'Japanese',
    'zh-CN': 'Chinese (Simplified)',
    'ru': 'Russian',
    'ar': 'Arabic',
    'it': 'Italian'
}

LANGUAGE_NAMES = sorted(LANGUAGES.values())
LANGUAGE_CODES = {v: k for k, v in LANGUAGES.items()}

st.set_page_config(page_title="Tranzly", layout="centered")

# 🌗 Theme toggle state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# 🔘 Toggle Dark Mode
mode = st.toggle("🌗 Toggle Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = mode

# 🎨 Apply Dark or Light Theme
if mode:
    st.markdown("""
        <style>
            .stApp {
                background-color: #0e1117;
                color: white;
            }
            textarea, .stTextArea textarea, .stSelectbox, .stTextInput input {
                background-color: #262730;
                color: white;
            }
            .stButton>button {
                background-color: #444;
                color: white;
                border: none;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                background-color: #ffffff;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)

# 🧠 Header
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

# 📝 Text Input with change detection
new_text_input = st.text_area("✏️ Enter text to detect and translate:", height=150)

if new_text_input != st.session_state.get("last_text", ""):
    st.session_state.detected_code = None
st.session_state["last_text"] = new_text_input
text_input = new_text_input

# 🧠 Session state for language detection
if 'detected_code' not in st.session_state:
    st.session_state.detected_code = None

# 🔍 Detect Language
if st.button("🔍 Detect Language"):
    if text_input.strip():
        code = detect_language(text_input)
        st.session_state.detected_code = code
        lang_name = LANGUAGES.get(code, "Unknown Language")
        st.success(f"Detected Language: **{lang_name}** (`{code}`)")
    else:
        st.warning("Please enter some text.")

# 🌍 Target language dropdown
target_lang_name = st.selectbox("🌍 Translate to:", LANGUAGE_NAMES)
target_lang_code = LANGUAGE_CODES[target_lang_name]

# 🌐 Translate button
if st.button("🌐 Translate"):
    if text_input.strip():
        # Auto-detect if not already done
        if not st.session_state.detected_code:
            st.session_state.detected_code = detect_language(text_input)

        source_code = st.session_state.detected_code
        source_name = LANGUAGES.get(source_code, "Unknown Language")

        st.info(f"Auto Detected Source Language: **{source_name}** (`{source_code}`)")

        # Translate
        result = translate_text(text_input, target_lang_code)
        st.success(f"**Translation:** {result}")

        # 📋 Copy to Clipboard
        st.markdown(f"""
            <script>
            function copyToClipboard(text) {{
                navigator.clipboard.writeText(text).then(function() {{
                    alert('✅ Translation copied to clipboard!');
                }}, function(err) {{
                    alert('❌ Failed to copy text: ' + err);
                }});
            }}
            </script>
            <button onclick="copyToClipboard(`{result}`)" style="
                margin-top: 10px;
                padding: 8px 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            ">📋 Copy Translation</button>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter text to translate.")
