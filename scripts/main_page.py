import streamlit as st


def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":house:",
        layout="wide",
    )

    st.title("Welcome to the Home Page")
    st.write("This is the main page of your Streamlit application.")
    st.write("Use the sidebar to navigate through different sections.")
    user_id = st.query_params.get("user_id", "Guest")
    st.write("User ID:", user_id)
    if user_id == None:
        st.write("You are currently not logged in.")
    else:
        st.write(f"Hello, {user_id}! You are logged in.")













if __name__ == "__main__":
    main()

