import streamlit as st


def main():
    st.write("Hello World!")
    a = 5
    b = 7
    a = a + b
    if a != 13:
        raise Exception("Erreur de calcul, a vaut %s et pas %s" % (a, 13))


if __name__ == '__main__':
    main()
