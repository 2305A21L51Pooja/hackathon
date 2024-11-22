import streamlit as st

def Gen_Efficiency(V,CL,K,IL,Rse,Ra):
    CUL = (K*IL)**2*(Rse+Ra)
    Eff = (K*V*IL)/(K*V*IL+CL+CUL)*100
    return CUL,Eff

st.title("2305A21L51-PS10")
st.subheader("Calculate the Efficency of DC Sereies Generator at Various Load")




col1, col2 = st.columns(2)
with col1:
 st.subheader("Input Parameters:")
 with st.container(border=True):
    V = st.number_input("V:in Volts)", value=100)
    IL =st.number_input("IL:in Amps", value=10.00)
    Rse=st.number_input("Rse:Ohms", value=10.00)
    Ra= st.number_input("Ra:Ohms", value=10.00)
    CL= st.number_input("CL:Watts", value=100)
    K=  st.number_input("K:Load constant",value=1)
    st.button("Compute")
           
            


with col2:
 st.subheader("Results:")
 with st.container(border=True):
    CUL,Eff = Gen_Efficiency(V,CL,IL,K,Rse,Ra)
    st.write(f"Copper losses = {CUL} W")
    st.write(f"Efficiency = {Eff} %")

