# streamlit_frontend.py
#too much ui haha
import streamlit as st
from langchain_core.messages import HumanMessage
import time
import uuid

# Import your backend chatbot
from langgraph_backend import chatbot

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Dhruv AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, #312e81 0%, transparent 25%),
        radial-gradient(circle at bottom right, #7c3aed 0%, transparent 25%),
        linear-gradient(135deg, #020617 0%, #0f172a 50%, #111827 100%);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.9);
    border-right: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
}

/* Header */
.main-title {
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(90deg,#60a5fa,#a78bfa,#f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}

.subtitle {
    color: #cbd5e1;
    font-size: 1rem;
    margin-bottom: 30px;
}

/* User bubble */
.user-bubble {
    background: linear-gradient(135deg,#2563eb,#4f46e5);
    padding: 16px;
    border-radius: 18px 18px 4px 18px;
    margin-bottom: 15px;
    margin-left: 20%;
    box-shadow: 0px 4px 20px rgba(59,130,246,0.25);
    animation: fadeIn 0.3s ease-in-out;
}

/* AI bubble */
.ai-bubble {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(16px);
    padding: 16px;
    border-radius: 18px 18px 18px 4px;
    margin-bottom: 15px;
    margin-right: 20%;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    animation: fadeIn 0.3s ease-in-out;
}

/* Cards */
.glass {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(14px);
}

/* Buttons */
.stButton button {
    width: 100%;
    border: none;
    border-radius: 14px;
    background: linear-gradient(90deg,#3b82f6,#8b5cf6);
    color: white;
    font-weight: 600;
    padding: 12px;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
    opacity: 0.95;
}

/* Chat Input */
.stChatInputContainer {
    background: rgba(15,23,42,0.9) !important;
    border-top: 1px solid rgba(255,255,255,0.08);
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #6366f1;
    border-radius: 10px;
}

/* Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(8px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div class="glass">
        <h2>🤖 Dhruv AI</h2>
        <p style="color:#cbd5e1;">
        Futuristic AI assistant powered by LangGraph + Groq.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### ⚡ Features")

    st.markdown("""
    - 🧠 Memory Persistence
    - ⚡ Ultra Fast Responses
    - 🎨 Premium Glassmorphism UI
    - 💬 Conversational AI
    - 🔥 LangGraph Powered
    """)

    st.write("")

    if st.button("🗑 Clear Conversation"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()

    st.write("")

    st.markdown("""
    <div class="glass">
        <h4>🛠 Stack</h4>
        <p>
        Streamlit<br>
        LangGraph<br>
        LangChain<br>
        Groq API
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MAIN HEADER
# ==========================================

st.markdown(
    '<div class="main-title">Dhruv AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Next generation conversational AI experience</div>',
    unsafe_allow_html=True
)

# ==========================================
# DISPLAY CHAT
# ==========================================

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="user-bubble">
                <b>👤 You</b><br><br>
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div class="ai-bubble">
                <b>🤖 AI</b><br><br>
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# CHAT INPUT
# ==========================================

prompt = st.chat_input("Type your message...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message instantly
    st.markdown(
        f"""
        <div class="user-bubble">
            <b>👤 You</b><br><br>
            {prompt}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Thinking animation
    thinking = st.empty()

    thinking.markdown("""
    <div class="ai-bubble">
        <b>🤖 AI</b><br><br>
        Thinking...
    </div>
    """, unsafe_allow_html=True)

    # LangGraph config
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    # Backend call
    response = chatbot.invoke(
        {
            "messages": [HumanMessage(content=prompt)]
        },
        config=config
    )

    ai_response = response["messages"][-1].content

    # Remove thinking bubble
    thinking.empty()

    # Streaming effect
    streamed_text = ""
    response_container = st.empty()

    for char in ai_response:
        streamed_text += char
        time.sleep(0.003)

        response_container.markdown(
            f"""
            <div class="ai-bubble">
                <b>🤖 AI</b><br><br>
                {streamed_text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })