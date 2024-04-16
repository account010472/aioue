import streamlit as st
import random

def play_janken(user_choice):
    choices = ['グー', 'チョキ', 'パー']
    computer_choice = random.choice(choices)
    
    st.write(f"あなたの選択: {user_choice}")
    st.write(f"コンピュータの選択: {computer_choice}")
    
    if user_choice == computer_choice:
        st.write("引き分けです！")
    elif (user_choice == 'グー' and computer_choice == 'チョキ') or \
         (user_choice == 'チョキ' and computer_choice == 'パー') or \
         (user_choice == 'パー' and computer_choice == 'グー'):
        st.write("あなたの勝ちです！")
    else:
        st.write("コンピュータの勝ちです！")

def main():
    st.title('じゃんけんアプリ')
    st.write('じゃんけんの手を選択してください')

    user_choice = st.radio('あなたの選択', ('グー', 'チョキ', 'パー'))

    if st.button('じゃんけんをする'):
        play_janken(user_choice)

if __name__ == '__main__':
    main()
