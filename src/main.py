import streamlit as st

# Custom CSS to style the buttons and overall layout
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px;
        font-weight: bold;
        color: white;
        background-color: #4A4A4A;
        border: 1px solid #666;
        border-radius: 5px;
    }
    .stTextInput > div > div > input {
        font-size: 24px;
        height: 60px;  /* Same height as buttons */
        text-align: right;
        padding-right: 10px;  /* Optional: Adds padding for better alignment */
    }
    .calculator {
        max-width: 400px;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

def calculate(expression):
    try:
        if '/' in expression and '0' in expression.split('/')[-1]:
            return 'INF'
        return eval(expression)
    except:
        return 'Error'

def button_click(button):
    if button == '=':
        result = calculate(st.session_state.expression)
        st.session_state.display = str(result)
        st.session_state.expression = str(result)
    elif button == 'AC':
        st.session_state.display = '0'
        st.session_state.expression = ''
    else:
        st.session_state.expression += button
        st.session_state.display = st.session_state.expression

st.title('My simple calculator')

if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'expression' not in st.session_state:
    st.session_state.expression = ''

with st.container():
    st.markdown('<div class="calculator">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text_input('', st.session_state.display, key='display_input')
    with col2:
        st.button('AC', on_click=button_click, args=('AC',))

    # Create 4 rows of buttons
    for row in [['7', '8', '9', '&#47;'],    # '/' character as &#47;
                ['4', '5', '6', '&#42;'],    # '*' character as &#42;
                ['1', '2', '3', '&#8722;'],  # '-' character as &#8722;
                ['0', '.', '=', '&#43;']]:   # '+' character as &#43;
        cols = st.columns(4)
        for i, button in enumerate(row):
            with cols[i]:
                st.button(button, key=button, on_click=button_click, args=(button,))

    st.markdown('</div>', unsafe_allow_html=True)
