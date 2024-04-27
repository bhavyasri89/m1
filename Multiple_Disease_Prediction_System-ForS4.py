import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


Breast_Cancer=pickle.load(open("Breast_Cancer.sav","rb"))
Diabetes=pickle.load(open("Diabetes.sav","rb"))
Heart_Disease=pickle.load(open("Heart_Disease.sav","rb"))
Kidney_Disease=pickle.load(open("Kidney_Disease.sav","rb"))
Liver_Disease=pickle.load(open("Liver_Disease.sav","rb"))
Parkinsons_Disease=pickle.load(open("Parkinsons_Disease.sav","rb"))
Scaler1=pickle.load(open("Scaler1.sav","rb"))
Scaler2=pickle.load(open("Scaler2.sav","rb"))
Scaler3=pickle.load(open("Scaler3.sav","rb"))
Scaler4=pickle.load(open("Scaler4.sav","rb"))
Scaler5=pickle.load(open("Scaler5.sav","rb"))
Scaler6=pickle.load(open("Scaler6.sav","rb"))



with st.sidebar:
    selected=option_menu("Multiple Disease Prediction System ",["Breast Cancer Prediction","Diabetes Prediction","Heart Disease Prediction","Kidney Disease Prediction","Liver Disease Prediction","Parkinsons Disease Prediction"],default_index=0)

if (selected=="Breast Cancer Prediction"):
    st.title("Breast Cancer Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        a1=st.text_input("Radius Mean")
    with col2:
        a2=st.text_input("Texture Mean")
    with col1:
        a3=st.text_input("Perimeter Mean")
    with col2:
        a4=st.text_input("Area Mean")
    with col1:
        a5=st.text_input("Smoothness Mean")
    with col2:
        a6=st.text_input("Compactness Mean")
    with col1:
        a7=st.text_input("Concavity Mean")
    with col2:
        a8=st.text_input("Concave Points Mean")
    with col1:
        a9=st.text_input("Symmetry Mean")
    with col2:
        a10=st.text_input("Fractal Dimension Mean")
    with col1:
        a11=st.text_input("Radius SE")
    with col2:
        a12=st.text_input("Texture SE")
    with col1:
        a13=st.text_input("Perimeter SE")
    with col2:
        a14=st.text_input("Area SE")
    with col1:
        a15=st.text_input("Smoothness SE")
    with col2:
        a16=st.text_input("Compactness SE")
    with col1:
        a17=st.text_input("Concavity SE")
    with col2:
        a18=st.text_input("Concave Points SE")
    with col1:
        a19=st.text_input("Symmetry SE")
    with col2:
        a20=st.text_input("Fractal Dimension SE")
    with col1:
        a21=st.text_input("Radius Worst")
    with col2:
        a22=st.text_input("Texture Worst")
    with col1:
        a23=st.text_input("Perimeter Worst")
    with col2:
        a24=st.text_input("Area Worst")
    with col1:
        a25=st.text_input("Smoothness Worst")
    with col2:
        a26=st.text_input("Compactness Worst")
    with col1:
        a27=st.text_input("Concavity Worst")
    with col2:
        a28=st.text_input("Concave Points Worst")
    with col1:
        a29=st.text_input("Symmetry Worst")
    with col2:
        a30=st.text_input("Fractal Dimension Worst")
       
    Diagnosis=' '
    
    if st.button("Breast Cancer Test Result"):
    
     list1=np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30])
     list2=Scaler1.transform(list1.reshape(1,-1))
     
     Breast_Cancer_Prediction=Breast_Cancer.predict(list2)
     
     if(Breast_Cancer_Prediction==1):
            Diagnosis="The tumour is Malignant"
     else:
            Diagnosis="The tumour is Benign"   
            
    st.success(Diagnosis)
    
if (selected=="Diabetes Prediction"):
    st.title("Diabetes Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        b1=st.text_input("Pregnancies")
    with col2:
        b2=st.text_input("Glucose Level")
    with col1:
        b3=st.text_input("Blood Pressure")
    with col2:
        b4=st.text_input("Skin Thickness")
    with col1:
        b5=st.text_input("Insulin Level")
    with col2:
        b6=st.text_input("BMI")
    with col1:
        b7=st.text_input("Diabetes Pedigree Function")
    with col2:
        b8=st.text_input("Age")
        
    Diagnosis = ''
    
    if st.button("Diabetes Test Result"):
          
       list3=np.array([b1,b2,b3,b4,b5,b6,b7,b8])
       list4=Scaler2.transform(list3.reshape(1,-1))
     
       Diabetes_Prediction=Diabetes.predict(list4)
        
       if(Diabetes_Prediction==1):
           Diagnosis = "The person is Diabetic"
       else:
           Diagnosis = "The person is Non-Diabetic"      
            
    st.success(Diagnosis)

    
if (selected=="Heart Disease Prediction"):
    st.title("Heart Disease Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        c1=st.text_input("Age")
    with col2:
        c2=st.text_input("Sex")
    with col1:
        c3=st.text_input("Chest Pain")
    with col2:
        c4=st.text_input("Rest BP")
    with col1:
        c5=st.text_input("Cholestrol")
    with col2:
        c6=st.text_input("Fasting Blood Sugar")
    with col1:
        c7=st.text_input("Rest ECG")
    with col2:
        c8=st.text_input("Max HR")
    with col1:
        c9=st.text_input("Exercise Induced Angina")
    with col2:
        c10=st.text_input("Oldpeak")
    with col1:
        c11=st.text_input("Slope")
    with col2:
        c12=st.text_input("Number Of Major Vessels")
    with col1:
        c13=st.text_input("Thalassemia Value")
        
    Diagnosis=' '
    
    if st.button("Heart Disease Test Result"):

     list5=np.array([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13])
     list6=Scaler3.transform(list5.reshape(1,-1))
     
     Heart_Disease_Prediction=Heart_Disease.predict(list6)
     
     if(Heart_Disease_Prediction==0):
            Diagnosis="The person does'nt have Heart Disease"
     else:
            Diagnosis="The person has Heart Disease"      
            
    st.success(Diagnosis)    

if (selected=="Kidney Disease Prediction"):
    st.title("Kidney Disease Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        d1=st.text_input("Age")
    with col2:
        d2=st.text_input("BP")
    with col1:
        d3=st.text_input("Specific Gravity")
    with col2:
        d4=st.text_input("Albumin")
    with col1:
        d5=st.text_input("Sugar")
    with col2:
        d6=st.text_input("Red Blood Cells")
    with col1:
        d7=st.text_input("Pus Cell")
    with col2:
        d8=st.text_input("Pus Cell Clumps")
    with col1:
        d9=st.text_input("Bacteria")
    with col2:
        d10=st.text_input("Random Blood Glucose Level")
    with col1:
        d11=st.text_input("Blood Urea")
    with col2:
        d12=st.text_input("Serum Creatinine")
    with col1:
        d13=st.text_input("Sodium")
    with col2:
        d14=st.text_input("Potassium")
    with col1:
        d15=st.text_input("Hemoglobin")
    with col2:
        d16=st.text_input("Packed Cell Volume")
    with col1:
        d17=st.text_input("White Blood Cell Count")
    with col2:
        d18=st.text_input("Red Blood Cell Count")
    with col1:
        d19=st.text_input("Hypertension")
    with col2:
        d20=st.text_input("Diabetes Mellitus")
    with col1:
        d21=st.text_input("Coronary Artery Disease")
    with col2:
        d22=st.text_input("Appetite")
    with col1:
        d23=st.text_input("Pedal Edema")
    with col2:
        d24=st.text_input("Anemia")
        
    Diagnosis=' '
    
    if st.button("Kidney Disease Test Result"):
    
      list7=np.array([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24])
      list8=Scaler4.transform(list7.reshape(1,-1))
      
      Kidney_Disease_Prediction=Kidney_Disease.predict(list8)
     
      if(Kidney_Disease_Prediction==0):
            Diagnosis="The person does'nt have Chronic Kidney Disease"
      else:
            Diagnosis="The person has Chronic Kidney Disease"      
            
    st.success(Diagnosis)  
    
if (selected=="Liver Disease Prediction"):
    st.title("Liver Disease Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        e1=st.text_input("Age")
    with col2:
        e2=st.text_input("Gender")
    with col1:
        e3=st.text_input("Total Bilirubin")
    with col2:
        e4=st.text_input("Direct Bilirubin")
    with col1:
        e5=st.text_input("Alkaline Phosphotase")
    with col2:
        e6=st.text_input("Alamine Aminotransferase")
    with col1:
        e7=st.text_input("Aspartate Aminotransferase")
    with col2:
        e8=st.text_input("Total Proteins")
    with col1:
        e9=st.text_input("Albumin")
    with col2:
        e10=st.text_input("Albumin and Globulin Ratio")
        
    Diagnosis=' '
    
    if st.button("Liver Disease Test Result"):
     
      list9=np.array([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10])
      list10=Scaler5.transform(list9.reshape(1,-1))
      
      Liver_Disease_Prediction=Liver_Disease.predict(list10)
     
      if(Liver_Disease_Prediction==1):
           Diagnosis="The person has Liver Disease"
      else:
           Diagnosis="The person does'nt have Liver Disease"
           
    st.success(Diagnosis)
    
if (selected=="Parkinsons Disease Prediction"):
    st.title("Parkinsons Disease Prediction Using ML")
    col1,col2=st.columns(2)
    
    with col1:
        f1=st.text_input("MDVP:Fo(Hz)")
    with col2:
        f2=st.text_input("MDVP:Fhi(Hz)")
    with col1:
        f3=st.text_input("MDVP:Flo(Hz)")
    with col2:
        f4=st.text_input("MDVP:Jitter(%)")
    with col1:
        f5=st.text_input("MDVP:Jitter(Abs)")
    with col2:
        f6=st.text_input("MDVP:RAP")
    with col1:
        f7=st.text_input("MDVP:PPQ")
    with col2:
        f8=st.text_input("Jitter:DDP")
    with col1:
        f9=st.text_input("MDVP:Shimmer")
    with col2:
        f10=st.text_input("MDVP:Shimmer(dB)")
    with col1:
        f11=st.text_input("Shimmer:APQ3")
    with col2:
        f12=st.text_input("Shimmer:APQ5")
    with col1:
        f13=st.text_input("MDVP:APQ")
    with col2:
        f14=st.text_input("Shimmer:DDA")
    with col1:
        f15=st.text_input("NHR")
    with col2:
        f16=st.text_input("HNR")
    with col1:
        f17=st.text_input("RPDE")
    with col2:
        f18=st.text_input("DFA")
    with col1:
        f19=st.text_input("Spread1")
    with col2:
        f20=st.text_input("Spread2")
    with col1:
        f21=st.text_input("D2")
    with col2:
        f22=st.text_input("PPE")
    
    Diagnosis=' '
    
    if st.button("Parkinson's Disease Test Result"):
    
      list11=np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22])
      list12=Scaler6.transform(list11.reshape(1,-1))
      
      Parkinsons_Disease_Prediction=Parkinsons_Disease.predict(list12)
     
      if(Parkinsons_Disease_Prediction==0):
            Diagnosis="The person does'nt have Parkinson's Disease"
      else:
            Diagnosis="The person has Parkinson's Disease"      
            
    st.success(Diagnosis)
    


    

    

              
    
