import streamlit as st
st.title('Your Buddy')
st.text("Hello, how're you holding up? Don't forget that I'm always here to help you no matter what!")
name = st.text_input('Your name', key='name')
age = st.slider('Your age', 10, 100, key='age')
st.write('How are you feeling today? Please choose only one, so I can suggest you best!')
mood1 = st.checkbox('Extremely good', key='mood1')
mood2 = st.checkbox('Very good', key='mood2')
mood3 = st.checkbox('Good', key='mood3')
mood4 = st.checkbox('Bad', key='mood4')
mood5 = st.checkbox('Very bad', key='mood5')
mood6 = st.checkbox('Extremely bad', key='mood6')
if 10 <= age <= 100 and mood1:
    st.write(f"Dear {name}, you are on clound nine, aren't you? Keep up your mood and do what makes you happy. Live as if it's your last!")
if 10 <= age <= 100 and mood2:
    st.write(f"Dear {name}, since you are in a very good mood, you must be doing things which put you in a good mood. You're doing great, keep it up!")
if 10 <= age <= 100 and mood3:
    st.write(f"Dear {name}, I believe you are having an average good day. Don't worry too much about things that are not happening yet. Live at the moment!")
if 10 <= age <= 100 and mood4:
    st.write(f"Dear {name}, you look great when you put a smile on you. You do know that, don't you? So, go on and smile more! ")
if 10 <= age <= 100 and mood5:
    st.write(f"Dear {name}, as you are struggling and having a very bad day. Remember that you're not the only one in this whloe world. There's a rainbow after rain. Never give up and do what you think is right!")
if 10 <= age <= 100 and mood6:
    st.write(f"Dear {name}, be strong! You can cry it all out if you want to, but don't even think about giving up. You can cry and let it all out as much as you want. After a storm, there's a calm. You just have to be patient and wait for it!")