import streamlit as st
import pickle
import numpy as np
from streamlit_extras.mention import mention
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stateful_button import button
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="CYRENE: Heart Attack Complications Prediction System", page_icon='FAVICON.png', layout="wide", initial_sidebar_state="auto", menu_items=None)

with st.sidebar:
    mention(
        label="Io Diakou @GitHub",
        icon="github",
        url="https://github.com/IoDiakou",
    )
    


#st.markdown("<h1 style='text-align: center; color: black;'>Heart attack complications prediction</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>CYRENE: Σύστημα πρόβλεψης ιατρικών επιπλοκών για ασθενείς με έμφραγμα</h2>", unsafe_allow_html=True)
st.markdown("***")

explain = st.button("Πώς λειτουργεί το CYRENE;", type='primary', use_container_width=True)
if explain:
    switch_page("cyrene")
st.markdown("<h3 style='text-align: center; color: black;'>Παρακαλώ εισαγάγετε τα στοιχεία του ασθενούς</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Please enter the necessary patient information</h4>", unsafe_allow_html=True)
st.markdown("***")
### SEX ###
sex_display = ("Female", "Male")

options = list(range(len(sex_display)))

SEX = st.selectbox("Φύλο | Gender", options, format_func=lambda x: sex_display[x])

### - ###

### AGE ###
AGE = st.slider("Ηλικία | Age", 1, 100, 1)
### - ###

### INF_ANAM ###
inf_anam_options = (0, 1, 2, 3)
INF_ANAM = st.selectbox("Αριθμός προηγούμενων εμφραγμάτων | Number of previous myocardial infarctions", inf_anam_options)

### STENOK_AN ###
exert_angina_display = ("Never", "During the last year", "1 year ago", "2 years ago", "3 years ago", "4-5 years ago", "More than 5 years ago")

exert_angina_options = list(range(len(exert_angina_display)))

STENOK_AN = st.selectbox("Σταθερή στηθάγχη | Incidence of chest pain after exertion", exert_angina_options, format_func=lambda x: exert_angina_display[x])

### - ###

### FK_STENOK ###

FK_STENOK = 2

### - ####

### IBS_POST ###

ibs_post_display = ("None", "Exertional chest pain", "Unstable chest pain")
ibs_post_options = list(range(len(ibs_post_display)))

IBS_POST = st.selectbox("Συμπτώματα καρδιακής νόσου ημέρες ή εβδομάδες πριν την εισαγωγή στο νοσοκομείο | Coronary heart disease symptoms days or weeks before admission to hospital", ibs_post_options, format_func=lambda x: ibs_post_display[x])

### - ###

### GB ###
gb_display = ("None", "Stage 1", "Stage 2", "Stage 3")
gb_options = list(range(len(gb_display)))

GB = st.selectbox("Υπέρταση | Presence of essential hypertension", gb_options, format_func=lambda x: gb_display[x])

### - ###

### SIM_GIPERT ###
SIM_GIPERT = 0

### - ###

### DLIT_AG ###
DLIT_AG = 0

### - ###

### ZSN_A ###
zsn_display = ("None", "Stage 1", "Heart failure due to right ventricular systolic dysfunction", "Heart failure due to left ventricular systolic dysfunction", "Heart failure due to both left and right dysfunction")
zsn_options = list(range(len(zsn_display)))

ZSN_A = st.selectbox("Ιστορικό χρόνιας καρδιοπάθειας | History of chronic heart failure", zsn_options, format_func=lambda x: zsn_display[x])

### - ###

### nr ###
nr_11 = 0
nr_01 = 0
nr_02 = 0
nr_03 = 0
nr_04 = 0
nr_07 = 0
nr_08 = 0

### np ###
np_01 = 0
np_04 = 0
np_05 = 0
np_07 = 0
np_08 = 0
np_09 = 0
np_10 = 0

### endocr ###
endocr_01 = 0   
endocr_02 = 0
endocr_03 = 0

### zab_leg_01 ###
zab_display = ("No", "Yes")
zab_options = list(range(len(zab_display)))

zab_leg_01 = st.radio("Ιστορικό χρόνιας βρογχίτιδας | History of chronic bronchitis", zab_options, format_func=lambda x: zab_display[x])

### other zab_leg ###
zab_leg_02 = 0
zab_leg_03 = 0
zab_leg_04 = 0
zab_leg_06 = 0

### metrics ####
S_AD_KBRIG = st.number_input("Συστολική πίεση κατά την μέτρηση από την καρδιολογική ομάδα στα έκτακτα | Systolic blood pressure measured by the Emergency Cardiology Team", min_value=1, max_value=180, step=10)

D_AD_KBRIG = st.number_input("Διαστολική πίεση κατά την μέτρηση από την καρδιολογική ομάδα στα έκτακτα | Diastolic blood pressure measured by the Emergency Cardiology Team", min_value=1, max_value=100, step=10)

S_AD_ORIT = st.number_input("Συστολική πίεση κατά την μέτρηση στην εντατική | Systolic blood pressure measured at intensive care unit", min_value=1, max_value=180, step=10)

D_AD_ORIT = st.number_input("Διαστολική πίεση κατά την μέτρηση στην εντατική | Diastolic blood pressure measured at intensive care unit", min_value=1, max_value=100, step=10)

### post ###
O_L_POST = 0
K_SH_POST = 0
MP_TP_POST = 0
SVT_POST = 0
GT_POST = 0
FIB_G_POST = 0

### im ###
ant_im = 0
lat_im = 0
inf_im = 0
post_im = 0

### IM_PG_P ###
IM_PG_P = 0

### ecg ###
ritm_ecg_p_01 = 1
ritm_ecg_p_02 = 0
ritm_ecg_p_04 = 0
ritm_ecg_p_06 = 0
ritm_ecg_p_07 = 0
ritm_ecg_p_08 = 0
n_r_ecg_p_01 = 0
n_r_ecg_p_02 = 0
n_r_ecg_p_03 = 0
n_r_ecg_p_04 = 0
n_r_ecg_p_05 = 0
n_r_ecg_p_06 = 0
n_r_ecg_p_08 = 0
n_r_ecg_p_09 = 0
n_r_ecg_p_10 = 0
n_p_ecg_p_01 = 0
n_p_ecg_p_03 = 0
n_p_ecg_p_04 = 0
n_p_ecg_p_05 = 0
n_p_ecg_p_06 = 0
n_p_ecg_p_07 = 0
n_p_ecg_p_08 = 0
n_p_ecg_p_09 = 0
n_p_ecg_p_10 = 0
n_p_ecg_p_11 = 0
n_p_ecg_p_12 = 0

### therapy ###
fibr_ter_01 = 0
fibr_ter_02 = 0
fibr_ter_03 = 0
fibr_ter_05 = 0
fibr_ter_06 = 0
fibr_ter_07 = 0
fibr_ter_08 = 0

### BLOODWORK ###
GIPO_K = 0
K_BLOOD = 4
GIPER_NA = 0
NA_BLOOD = 138
ALT_BLOOD = 1
AST_BLOOD = 1
L_BLOOD = 8
ROE = 15


### TIME_B_S ###
time_bs_display = ("Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "8-12 hours", "12-24 hours", "More than 1 day", "More than 2 days", "More than 3 days")
time_bs_options = list(range(len(time_bs_display)))

TIME_B_S = st.selectbox("Χρόνος από την αρχή του εμφράγματος μέχρι την άφιξη στο νοσοκομείο | Time elapsed from the beginning of the heart attack to the hospital", time_bs_options, format_func=lambda x: time_bs_display[x])
if TIME_B_S == 0:
    TIME_B_S = 1
else:
    pass

### hospital ###
NA_KB = 0
NOT_NA_KB = 0
LID_KB = 0
NITR_S = 0
LID_S_n = 0
B_BLOK_S_n = 0
ANT_CA_S_n = 0
GEPAR_S_n = 0
ASP_S_n = 0
TIKL_S_n = 0
TRENT_S_n = 0


# model load #
loaded_model = pickle.load(open('onevsrest_model.pkl', 'rb'))
st.markdown("***")
### BUTTON ###
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    ok = button("Πρόβλεψη των επιπλοκών", type='primary',use_container_width=True, key='button1')

if ok:
    X_new = [[AGE, SEX, INF_ANAM, STENOK_AN, FK_STENOK, IBS_POST, GB, SIM_GIPERT, DLIT_AG, 
        ZSN_A, nr_11, nr_01, nr_02, nr_03, nr_04, nr_07, nr_08, np_01, np_04, 
        np_05, np_07, np_08, np_09, np_10, endocr_01, endocr_02, endocr_03, 
        zab_leg_01, zab_leg_02, zab_leg_03, zab_leg_04, zab_leg_06, S_AD_KBRIG, 
        D_AD_KBRIG, S_AD_ORIT, D_AD_ORIT, O_L_POST, K_SH_POST, MP_TP_POST, 
        SVT_POST, GT_POST, FIB_G_POST, ant_im, lat_im, inf_im, post_im, IM_PG_P, 
        ritm_ecg_p_01, ritm_ecg_p_02, ritm_ecg_p_04, ritm_ecg_p_06, ritm_ecg_p_07, 
        ritm_ecg_p_08, n_r_ecg_p_01, n_r_ecg_p_02, n_r_ecg_p_03, n_r_ecg_p_04, 
        n_r_ecg_p_05, n_r_ecg_p_06, n_r_ecg_p_08, n_r_ecg_p_09, n_r_ecg_p_10, 
        n_p_ecg_p_01, n_p_ecg_p_03, n_p_ecg_p_04, n_p_ecg_p_05, n_p_ecg_p_06, 
        n_p_ecg_p_07, n_p_ecg_p_08, n_p_ecg_p_09, n_p_ecg_p_10, n_p_ecg_p_11, n_p_ecg_p_12, 
        fibr_ter_01, fibr_ter_02, fibr_ter_03, fibr_ter_05, fibr_ter_06, fibr_ter_07, fibr_ter_08, 
        GIPO_K, K_BLOOD, GIPER_NA, NA_BLOOD, ALT_BLOOD, AST_BLOOD, L_BLOOD, ROE, TIME_B_S, 
        NA_KB, NOT_NA_KB, LID_KB, NITR_S, LID_S_n, B_BLOK_S_n, ANT_CA_S_n, GEPAR_S_n, ASP_S_n, TIKL_S_n, TRENT_S_n]]
    
    user_input = X_new

    prediction = loaded_model.predict_proba(X_new)
    
    prediction_0 = round(prediction[0][0]*100,2)
    prediction_1 = round(prediction[0][1]*100,2)
    prediction_2 = round(prediction[0][2]*100,2)
    prediction_3 = round(prediction[0][3]*100,2)
    prediction_4 = round(prediction[0][4]*100,2)
    prediction_5 = round(prediction[0][5]*100,2)
    prediction_6 = round(prediction[0][6]*100,2)
    prediction_7 = round(prediction[0][7]*100,2)
    prediction_8 = round(prediction[0][8]*100,2)
    prediction_9 = round(prediction[0][9]*100,2)
    prediction_10 = round(prediction[0][10]*100,2)
    prediction_11 = round(prediction[0][11]*100,2)
    prediction_12 = round(prediction[0][12]*100,2)
    prediction_13 = round(prediction[0][13]*100,2)
    prediction_14 = round(prediction[0][14]*100,2)
    prediction_15 = round(prediction[0][15]*100,2)
    prediction_16 = round(prediction[0][16]*100,2)
    prediction_17 = round(prediction[0][17]*100,2)
    prediction_18 = round(prediction[0][18]*100,2)

    font_size = 22
    result_11 = f'Πιθανότητα επιβίωσης ασθενούς δεδομένων των επιπλοκών: {prediction_11} %'
    html_11 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_11}</p>
    """

    st.markdown(html_11, unsafe_allow_html=True)

    result_0 = f'Κολπική μαρμαρυγή: {prediction_0} %'
    font_size = 22
    html_0 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_0}</p>
    """

    st.markdown(html_0, unsafe_allow_html=True)

    result_1 = f'Υπερκοιλιακή ταχυκαρδία: {prediction_1} %'
    html_1 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_1}</p>
    """

    st.markdown(html_1, unsafe_allow_html=True)

    result_2 = f'Κοιλιακή ταχυκαρδία: {prediction_2} %'
    html_2 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_2}</p>
    """

    st.markdown(html_2, unsafe_allow_html=True)

    result_3 = f'Κοιλιακή μαρμαρυγή: {prediction_3} %'
    html_3 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_3}</p>
    """

    st.markdown(html_3, unsafe_allow_html=True)

    result_4 = f'Kοιλιακός αποκλεισμός: {prediction_4} %'
    html_4 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_4}</p>
    """

    st.markdown(html_4, unsafe_allow_html=True)

    result_5 = f'Πνευμονικό οίδημα: {prediction_5} %'
    html_5 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_5}</p>
    """

    st.markdown(html_5, unsafe_allow_html=True)

    result_6 = f'Ρήξη μυοκαρδίου: {prediction_6} %'
    html_6 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_6}</p>
    """

    st.markdown(html_6, unsafe_allow_html=True)

    result_7 = f'Σύνδρομο Dressler: {prediction_7} %'
    html_7 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_7}</p>
    """

    st.markdown(html_7, unsafe_allow_html=True)

    result_8 = f'Καρδιακή ανεπάρκεια: {prediction_8} %'
    html_8 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_8}</p>
    """

    st.markdown(html_8, unsafe_allow_html=True)
    
    result_9 = f'Υποτροπή εμφράγματος: {prediction_9} %'
    html_9 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_9}</p>
    """

    st.markdown(html_9, unsafe_allow_html=True)

    result_10 = f'Μετεμφραγματική στηθάγχη: {prediction_10} %'
    html_10 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_10}</p>
    """

    st.markdown(html_10, unsafe_allow_html=True)

    result_12 = f'Θανατηφόρο καρδιακό σοκ: {prediction_12} %'
    html_12 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_12}</p>
    """

    st.markdown(html_12, unsafe_allow_html=True)
    
    result_13 = f'Θανατηφόρο πνευμονικό οίδημα: {prediction_13} %'
    html_13 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_13}</p>
    """

    st.markdown(html_13, unsafe_allow_html=True)

    result_14 = f'Θανατηφόρα καρδιακή ρήξη: {prediction_14} %'
    html_14 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_14}</p>
    """

    st.markdown(html_14, unsafe_allow_html=True)

    result_15 = f'Θανατηφόρα καρδιακή ανεπάρκεια: {prediction_15} %'
    html_15 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_15}</p>
    """

    st.markdown(html_15, unsafe_allow_html=True)

    result_16 = f'Θανατηφόρα θρομβοεμβολή: {prediction_16} %'
    html_16 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_16}</p>
    """

    st.markdown(html_16, unsafe_allow_html=True)

    result_17 = f'Θανατηφόρα ασυστολή: {prediction_17} %'
    html_17 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_17}</p>
    """

    st.markdown(html_17, unsafe_allow_html=True)

    result_18 = f'Θανατηφόρα κοιλιακή μαρμαρυγή: {prediction_18} %'
    html_18 = f"""
    <style>
    p.a {{
    font: bold {font_size}px segoe ui;
    text-align: center;
    }}
    </style>
    <p class="a">{result_18}</p>
    """

    st.markdown(html_18, unsafe_allow_html=True)
    
    add_vertical_space(4)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        show_me = button("Δείξε μου πώς βλέπει το CYRENE τα δεδομένα που εισήγαγα", type='primary', use_container_width=True, key='button2')

    add_vertical_space(2)

    if show_me:
        font_size_user = 22
        user_input = f'{user_input}'
        html_user = f"""
        <style>
        p.a {{
        font: bold {font_size_user}px segoe ui;
        text-align: center;
        }}
        </style>
        <p class="a">{user_input}</p>
        """

        st.markdown(html_user, unsafe_allow_html=True)