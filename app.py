import streamlit as st

st.title("🔐 Password Strength Checker")

# Password input field
password = st.text_input("Apna password likhiye:", type="password")

# Strength checking logic
if password:
    score = 0
    special_characters = "!@#$%^&*"

    st.write("## 🔍 Password Analysis")

    # 1. Length check
    if len(password) >= 8:
        st.success("✅ Password ki length theek hai!")
        score += 1
    else:
        st.error("❌ Password bohot chhota hai! Kam az kam 8 characters ka rakhein.")

    # 2. Uppercase check
    if any(char.isupper() for char in password):
        st.success("✅ Uppercase letter mojood hai!")
        score += 1
    else:
        st.error("❌ Kam az kam ek uppercase letter zaroori hai!")

    # 3. Lowercase check
    if any(char.islower() for char in password):
        st.success("✅ Lowercase letter mojood hai!")
        score += 1
    else:
        st.error("❌ Kam az kam ek lowercase letter zaroori hai!")

    # 4. Special character check
    if any(char in special_characters for char in password):
        st.success("✅ Special character mojood hai!")
        score += 1
    else:
        st.error("❌ Kam az kam ek special character (!@#$%^&*) zaroori hai!")

    # 5. Number check
    if any(char.isdigit() for char in password):
        st.success("✅ Number (0-9) mojood hai!")
        score += 1
    else:
        st.error("❌ Kam az kam ek number (0-9) zaroori hai!")

    # Final Score and Strength
    st.write("## 📊 Password Score:", score, "/ 5")

    if score == 5:
        st.success("🚀 Password bohot strong hai!")
    elif score >= 3:
        st.warning("🔄 Password theek hai, lekin behtar banaya ja sakta hai.")
    else:
        st.error("⚠️ Password bohot weak hai! Mazeed behtar karein.")
