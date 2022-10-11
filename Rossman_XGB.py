import joblib
import streamlit as st
import pickle as pkl

loaded_model_pkl = pkl.load(open("final_XGBoost_pickle_model.pkl",'rb'))


def fun_pred(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20):
  prediction1  = loaded_model_pkl.predict(pd.DataFrame(data = [[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]], columns=['state_holiday_regular_day', 'day_of_week_cos', 'competition_open_since_year', 'competition_distance', 'store', 'competition_open_since_month', 'store_type_d', 'day_cos', 'state_holiday_public_holiday', 'promo2', 'store_type_b', 'is_promo', 'month_cos', 'promo2_since_year', 'competition_time_month', 'promo2_since_week', 'assortment', 'promo', 'promo_time_week', 'school_holiday', 'year']))
  return prediction1


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
        result = fun_pred(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
