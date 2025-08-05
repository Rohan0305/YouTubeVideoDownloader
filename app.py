import streamlit as st
from utils import download_video, get_downloads_path, validate_url

st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    
    .stApp {
        background-color: #0e1117;
    }
    
    .youtube-title {
        background: linear-gradient(45deg, #FF0000, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
        border: 2px solid #FF0000;
        border-radius: 10px;
        padding: 10px;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #FF0000, #FF6B6B);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 30px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 0, 0, 0.3);
    }
    
    .success-message {
        background-color: #1f2937;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .error-message {
        background-color: #1f2937;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="youtube-title">🎥 YouTube Video Downloader</h1>', unsafe_allow_html=True)
    
    with st.container():
        url = st.text_input(
            "Enter YouTube URL:",
            placeholder="https://www.youtube.com/watch?v=...",
            key="url_input"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            download_button = st.button("📥 Download Video", use_container_width=True)
        
        if download_button and url:
            is_valid, error_msg = validate_url(url)
            
            if not is_valid:
                st.markdown(f'<div class="error-message">❌ {error_msg}</div>', unsafe_allow_html=True)
            else:
                with st.spinner("🔄 Downloading video..."):
                    downloads_path = get_downloads_path()
                    
                    success, result, duration = download_video(url, downloads_path)
                    
                    if success:
                        st.markdown(f'''
                        <div class="success-message">
                            ✅ <strong>Download Successful!</strong><br>
                            📁 Saved to: Downloads folder<br>
                            🎬 Title: {result}<br>
                            ⏱️ Duration: {duration // 60}m {duration % 60}s
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        st.markdown(f'''
                        <div class="info-box">
                            📂 File location: <code>{downloads_path}</code>
                        </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.markdown(f'''
                        <div class="error-message">
                            ❌ <strong>Download Failed</strong><br>
                            Error: {result}
                        </div>
                        ''', unsafe_allow_html=True)
        
        elif download_button and not url:
            st.markdown('<div class="error-message">❌ Please enter a YouTube URL first</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 