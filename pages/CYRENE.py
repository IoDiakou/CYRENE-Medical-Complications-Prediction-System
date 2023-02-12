import streamlit as st
from markdownlit import mdlit
from streamlit_extras.mention import mention
from streamlit_card import card


with st.sidebar:
    mention(
        label="Io Diakou @GitHub",
        icon="github",
        url="https://github.com/IoDiakou",
    )


font_size=22
text = 'Το μοντέλο πρόβλεψης CYRENE λειτουργεί με βάση έναν αλγόριθμο κατηγοριοποίησης (multi-label classification). Οι 18 πιθανές επιπλοκές αντιμετωπίζονται ως 18 κατηγορίες και ο αλγόριθμος προβλέπει την πιθανότητα ένας ασθενής (με έναν συγκεκριμένο συνδυασμό παθοφυσιολογικών χαρακτηριστικών) να ανήκει σε κάθε μια από τις κατηγορίες αυτές. Για να εκπαιδευθεί το μοντέλο στην διεξαγωγή ορθών προβλέψεων, χρησιμοποιήθηκαν δεδομένα 1700 ασθενών εμφράγματος. Για τους ασθενείς αυτούς είχαν συλλεχθεί δεδομένα ιατρικού ιστορικού, καθώς και δεδομένα εξετάσεων στο νοσοκομείο, ενώ είχαν επίσης καταγραφεί και οι επιπλοκές τις οποίες εμφάνισαν.'
html_1 = f"""
<style>
p.a {{
font: normal {font_size}px segoe ui;
text-align: justify;
}}
</style>
<p class="a">{text}</p>
"""

st.markdown(html_1, unsafe_allow_html=True)

font_size=22
text_2 = "Τα δεδομένα διατηρούνται στο αποθετήριο του University of California, Irving (UCI) και αποτελούν την βάση για την ανάπτυξη συστημάτων όπως το CYRENE, τα οποία θα μπορούν να λειτουργούν υποστηρικτικά στο περιβάλλον του νοσοκομείου. Η έγκαιρη πρόβλεψη πιθανών επιπλοκών επιτρέπει την πιο αποτελεσματική παρακολούθηση και διαχείριση του ασθενούς, με την ελπίδα να αυξηθεί η πιθανότητα επιβίωσης μετά από ένα επεισόδιο εμφράγματος."
html_2 = f"""
<style>
p.a {{
font: normal {font_size}px segoe ui;
text-align: justify;
}}
</style>
<p class="a">{text_2}</p>
"""

st.markdown(html_2, unsafe_allow_html=True)

st.markdown("***")


text_3 = "Ο αλγόριθμος που χρησιμοποιείται από το CYRENE είναι ο ευριστικός OneVsRest, ο οποίος αντιμετωπίζει το ζήτημα της κατηγοριοποίησης σε 18 κατηγορίες, ως 18 διαφορετικά προβλήματα δυαδικής κατηγοριοποίησης (binary classification). Εκπαιδεύονται παράλληλα 18 διαφορετικά μοντέλα, ένα για κάθε κατηγορία/επιπλοκή, κάθε ένα από τα οποία προβλέπει την πιθανότητα να ανήκει ο ασθενής στην κατηγορία αυτή. Η δημιουργία των πολλαπλών μοντέλων αυξάνει το υπολογιστικό και χρονικό κόστος, επομένως για το CYRENE, o OneVsRest αλγόριθμος έγινε wrapped στον αλγόριθμο XGBoost, ο οποίος αντισταθμίζει αυτές τις απαιτήσεις."
html_3 = f"""
<style>
p.a {{
font: normal {font_size}px segoe ui;
text-align: justify;
}}
</style>
<p class="a">{text_3}</p>
"""

st.markdown(html_3, unsafe_allow_html=True)

st.markdown("***")

card(
    title="Θέλω να δω τα δεδομένα",
    text="Πάτησε εδώ για να μεταφερθείς στο UCI",
    url="https://archive.ics.uci.edu/ml/datasets/Myocardial+infarction+complications#",
)