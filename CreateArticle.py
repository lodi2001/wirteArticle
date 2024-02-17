import streamlit as st
from docx import Document

st.set_page_config(page_title='Document Editor App', layout = 'wide')
st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', ['Home', 'Upload Article', 'Write Literature Review', 'Structure Paper'])
document = Document()
if selection == 'Home':
    st.title('Home')
elif selection == 'Upload Article':
    st.title('Upload Article')
elif selection == 'Write Literature Review':
    st.title('Write Literature Review')
    text_input = st.text_input('Write your literature review here:')
    if st.button('Convert to Word Document'):
        document.add_paragraph(text_input)
        document.save('Literature_Review.docx')
        st.success('The text has been successfully saved to a Word document!')
elif selection == 'Structure Paper':
    st.title('Structure Paper')
