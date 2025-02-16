import streamlit as st
import random
# Add Custom CSS for Styling
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #fde2e4, #fad2e1, #e2ece9);
        color: #2C3E50;
    }

    /* Title */
    h1 {
        color: #C70039;
        text-align: center;
        text-shadow: 2px 2px #ffffff;
    }

    /* Subheaders */
    .stMarkdown h2 {
        color: #800080;
    }

    /* Custom Buttons */
    div.stButton > button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
    }

    /* Input fields */
    input[type="text"] {
        border-radius: 10px;
        border: 1px solid #FF69B4;
        padding: 5px;
    }

    /* Chat History */
    .stMarkdown h3 {
        color: #E75480;
        text-decoration: underline;
    }

    </style>
    """, unsafe_allow_html=True)

# Valentine's Day Chatbot
st.title("💌 Valentine's Day Gift & Love Calculator Chatbot 💘")
st.write("Hello! I'm CupidBot, here to help you find the perfect Valentine's Day gift and calculate your love compatibility! 🎯")

# Personality options
personalities = [
    "Romantic 💞", "Adventurous 🌄", "Funny 😂", "Thoughtful 🤔", "Creative 🎨", "Foodie 🍕"
]
budget_ranges = ["💸 Low (Under ₹500)", "💲 Medium (₹500-₹2000)", "💎 High (₹2000+)"]

# Gift suggestions
gift_suggestions = {
    "Romantic 💞": [
        "Personalized photo book 📖", "Love letter jar 💌", "Couple's spa day 🧖‍♀️🧖‍♂️",
        "Candle light dinner🕯️", "Breakfast in bed 🍳☕"
    ],
    "Adventurous 🌄": [
        "Hot air balloon ride 🎈", "Hiking adventure 🏔️", "Adventure park tickets 🎢",
        "Scuba diving experience 🤿", "Surprise road trip 🚗"
    ],
    "Funny 😂": [
        "Customized meme calendar 📆", "Joke book 😂", "Funny caricature 🖼️",
        "Prank gift box 🎁", "Laughing Buddha figurine 😆"
    ],
    "Thoughtful 🤔": [
        "Personalized puzzle 🧩", "Memory jar 🎀", "Handwritten poem 📜",
        "Donation to a cause in their name 🌿", "Custom engraved keychain 🔑"
    ],
    "Creative 🎨": [
        "DIY craft kit 🎨", "Pottery class voucher 🏺", "Sketch portrait 🖌️",
        "Customized music playlist 🎶", "Paint-and-sip experience 🍷"
    ],
    "Foodie 🍕": [
        "Gourmet chocolate box 🍫", "Cooking class for two 🍽️", "🌮 Food Tour Experience",
        "Food subscription box 📦", "Breakfast date ☕🥐"
    ]
}

# Chat loop
chat_history = []

personality = st.selectbox("What kind of personality best describes your Valentine?", personalities)
budget = st.selectbox("What's your budget?", budget_ranges)

if st.button("💝 Get Gift Ideas!"):
    if personality and budget:
        gift = random.choice(gift_suggestions[personality])
        response = (
            f"For a {personality.lower()} person, how about: **{gift}**? 💝\n"
            f"Budget: {budget}\n"
            f"Need more ideas? Just ask! 😉"
        )
        chat_history.append(response)
        st.success(response)
        st.balloons()

# Interactive chatbot with FLAMES-based love compatibility
st.subheader("💬 Let's Calculate Your Love Compatibility!")

# Simulating chatbot-like conversation
if 'name_stage' not in st.session_state:
    st.session_state.name_stage = 'ask_user_name'

if st.session_state.name_stage == 'ask_user_name':
    user_name = st.text_input("Hi there! What's your name? 😊")
    if user_name:
        st.session_state.user_name = user_name
        st.session_state.name_stage = 'ask_partner_name'
        st.rerun()

elif st.session_state.name_stage == 'ask_partner_name':
    partner_name = st.text_input(f"Nice to meet you, {st.session_state.user_name}! What's your partner's name? 💕")
    if partner_name:
        st.session_state.partner_name = partner_name
        st.session_state.name_stage = 'calculate_love'
        st.rerun()

elif st.session_state.name_stage == 'calculate_love':
    user_name = st.session_state.user_name
    partner_name = st.session_state.partner_name
    combined_names = user_name.lower().replace(" ", "") + partner_name.lower().replace(" ", "")
    count = 0
    for char in set(combined_names):
        count += combined_names.count(char) % 2
    compatibility_score = count % 6

    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Soulmates"]
    result = flames[compatibility_score - 1] if compatibility_score != 0 else flames[-1]

    st.success(f"💞 {user_name} & {partner_name}'s Love Compatibility: {result}! 💘")
    st.session_state.name_stage = 'ask_user_name'

# Display chat history
st.subheader("📝 Chat History")
for msg in chat_history:
    st.write(msg)

st.caption("💘 CupidBot: Bringing smiles, laughs, and perfect gifts! 💝")
