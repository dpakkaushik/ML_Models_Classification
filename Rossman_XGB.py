import joblib
import streamlit as st
import pickle as pkl

loaded_model_pkl = pkl.load(open("final_XGBoost_pickle_model.pkl",'rb'))


def predict_note_authentication(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u):

    prediction = loaded_model_pkl.predict([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]])
    print(prediction)
    return prediction


def main():

    st.title("Rossmann Store")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Store Sales Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    state_holiday_regular_day = st.number_input("state_holiday_regular_day",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    day_of_week_cos = st.number_input("day_of_week_cos",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    competition_open_since_year = st.number_input("competition_open_since_year",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    competition_distance = st.number_input("competition_distance",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    store = st.number_input("store",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    competition_open_since_month = st.number_input("competition_open_since_month",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    store_type_d = st.number_input("store_type_d",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    day_cos = st.number_input("day_cos",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    state_holiday_public_holiday = st.number_input("state_holiday_public_holiday",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    promo2 = st.number_input("promo2",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    store_type_b = st.number_input("store_type_b",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    is_promo = st.number_input("is_promo",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    month_cos = st.number_input("month_cos",min_value=0.,max_value=1.0,step=1e-6,format="%.5f")
    promo2_since_year = st.number_input("promo2_since_year", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    competition_time_month = st.number_input("competition_time_month", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    promo2_since_week = st.number_input("promo2_since_week", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    assortment = st.number_input("assortment", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    promo = st.number_input("promo", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    promo_time_week = st.number_input("promo_time_week", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    school_holiday = st.number_input("school_holiday", min_value=0., max_value=1.0, step=1e-6, format="%.5f")
    year = st.number_input("year", min_value=0., max_value=1.0, step=1e-6, format="%.5f")


    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(a, b, c, d, e, f, g, h, i, j, k, l, m)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
