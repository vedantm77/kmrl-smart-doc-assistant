import streamlit as st

# ------------------------------
# App Title
# ------------------------------
st.set_page_config(page_title="KMRL Smart Document Assistant", layout="wide")
st.title("🚇 Kochi Metro Smart Document Assistant")

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("📂 Menu")
page = st.sidebar.radio("Go to", ["Upload & Summarize", "Search Documents", "About"])

# ------------------------------
# Page 1: Upload & Summarize
# ------------------------------
if page == "Upload & Summarize":
    st.subheader("📑 Upload a Document")
    uploaded_file = st.file_uploader("Upload PDF / Word / Image", type=["pdf", "docx", "png", "jpg"])

    if uploaded_file:
        st.success(f"File Uploaded: {uploaded_file.name}")

        # Simulated AI response (replace with backend API later)
        summary = """New speed restrictions on Line 2. 
        Mandatory refresher training for drivers before Sept 10."""
        category = "Safety"
        lang = st.radio("Select Language:", ["English", "Malayalam"])

        st.subheader("📌 AI Summary")
        if lang == "English":
            st.info(summary)
        else:
            st.info("ലൈൻ 2-ൽ പുതിയ വേഗ നിയന്ത്രണങ്ങൾ. സെപ്റ്റംബർ 10-നു മുൻപ് ഡ്രൈവർമാർക്ക് നിർബന്ധമായ പരിശീലനം.")

        st.subheader("🏷️ Category")
        st.write(f"**{category}**")

# ------------------------------
# Page 2: Search Documents
# ------------------------------
elif page == "Search Documents":
    st.subheader("🔍 Search Documents")
    query = st.text_input("Enter keyword (e.g. 'safety', 'finance')")

    if query:
        st.write(f"Showing results for: **{query}**")
        # Simulated results (later connect to vector DB)
        st.write("1. Safety Bulletin - Aug 2023: Speed restrictions on Line 2")
        st.write("2. HR Policy Update: Leave guidelines")

# ------------------------------
# Page 3: About
# ------------------------------
else:
    st.subheader("ℹ️ About This Project")
    st.write("""
    Kochi Metro generates thousands of documents daily.  
    This AI-powered assistant:
    - Summarizes documents
    - Routes to correct departments
    - Supports English + Malayalam
    - Provides quick search & traceability
    """)

    st.caption("🚀 Built for Smart India Hackathon")
