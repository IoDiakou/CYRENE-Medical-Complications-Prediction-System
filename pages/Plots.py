import streamlit as st
from streamlit_extras.mention import mention


with st.sidebar:
    mention(
        label="Io Diakou @GitHub",
        icon="github",
        url="https://github.com/IoDiakou",
    )

st.markdown("<h2 style='text-align: center; color: black;'>Ανάλυση των σχέσεων που παρατηρούνται ανάμεσα στις επιπλοκές</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Κάθε επιπλοκή παρουσιάζεται ως κόμβος, ο οποίος συνδέεται με τους υπόλοιπους με νήματα. Το πάχος των νημάτων αντιστοιχεί σε μεγαλύτερη συχνότητα συνεμφάνισης.</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Για παράδειγμα, η κολπική μαρμαρυγή επέδειξε υψηλή συχνότητα συνεμφάνισης με θανατηφόρα καρδιακή ανεπάρκεια, πνευμονικό οίδημα και υποτροπή εμφράγματος.</h3>", unsafe_allow_html=True)


st.markdown("***")
st.image('Graph.png', caption="Πατήστε πάνω στην εικόνα για μεγέθυνση", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")