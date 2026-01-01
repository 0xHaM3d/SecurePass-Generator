import random
import string
import streamlit as st
# from typing import List, Optional

# --- LOGIC LAYER (OOP) ---

class PasswordGenerator:
    """A modular class to handle different password generation strategies."""
    
    @staticmethod
    def generate_random(length: int = 12, include_numbers: bool = True, include_symbols: bool = True) -> str:
        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def generate_memorable(no_of_words: int = 4, separator: str = "-", capitalization: bool = True) -> str:
        # Static vocabulary for demonstration; could be expanded or loaded from a file
        vocabulary = [
            'apple', 'cloud', 'ocean', 'river', 'mountain', 'forest', 'bright', 
            'silent', 'golden', 'purple', 'winter', 'summer', 'breeze', 'planet'
        ]
        
        password_words = random.sample(vocabulary, min(no_of_words, len(vocabulary)))
        if capitalization:
            password_words = [word.capitalize() for word in password_words]
        
        return separator.join(password_words)

    @staticmethod
    def generate_pin(length: int = 4) -> str:
        return ''.join(random.choice(string.digits) for _ in range(length))


# --- UI LAYER (Streamlit) ---

def main():
    st.set_page_config(page_title="SecurePass Generator", page_icon="🔐")
    
    st.title("🔐 SecurePass Generator")
    st.write("Generate secure, random, or memorable passwords instantly.")

    # Sidebar for global settings or info
    st.sidebar.header("Settings")
    generator_type = st.sidebar.radio(
        "Select Generator Type",
        ["Standard Random", "Memorable Phrase", "PIN Code"]
    )

    gen = PasswordGenerator()
    result = ""

    # Tab/Interface Logic based on selection
    if generator_type == "Standard Random":
        st.subheader("Random Password Configuration")
        col1, col2 = st.columns(2)
        
        with col1:
            length = st.slider("Length", 6, 64, 16)
            nums = st.checkbox("Include Numbers", value=True)
        with col2:
            syms = st.checkbox("Include Symbols", value=True)
            
        if st.button("Generate Password"):
            result = gen.generate_random(length, nums, syms)

    elif generator_type == "Memorable Phrase":
        st.subheader("Memorable Phrase Configuration")
        col1, col2 = st.columns(2)
        
        with col1:
            word_count = st.slider("Number of Words", 2, 8, 4)
            sep = st.text_input("Separator", value="-")
        with col2:
            caps = st.checkbox("Capitalize Words", value=True)
            
        if st.button("Generate Phrase"):
            result = gen.generate_memorable(word_count, sep, caps)

    elif generator_type == "PIN Code":
        st.subheader("PIN Configuration")
        pin_length = st.number_input("PIN Length", 4, 12, 4)
        
        if st.button("Generate PIN"):
            result = gen.generate_pin(pin_length)

    # Display Result
    if result:
        st.success("Generated!")
        st.code(result, language="text")
        st.info("Click the icon in the top right of the box above to copy.")

if __name__ == "__main__":
    main()