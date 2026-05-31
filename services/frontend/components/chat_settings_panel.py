import streamlit as st

def render_chat_settings_panel():

    st.subheader("Chat Settings")

    chat_settings = st.session_state.chat_settings

    top_k = st.slider(
        "Top-K Chunks",
        chat_settings.MIN_TOP_K,
        chat_settings.MAX_TOP_K,
        value=chat_settings.top_k,
        key="chat_settings_top_k"
    )

    selected_llm = st.selectbox(
        "LLM",
        chat_settings.LLM_OPTIONS,
        index=chat_settings.LLM_OPTIONS.index(chat_settings.llm),
        key="chat_settings_llm"
    )

    prompting_strategy = st.selectbox(
        "Prompting Strategy",
        chat_settings.PROMPT_STRATEGIES,
        index=chat_settings.PROMPT_STRATEGIES.index(chat_settings.prompting_strategy),
        key="chat_settings_prompting_strategy"
    )

    if st.button(
        "Apply Settings",
        use_container_width=True,
        type="primary"
    ):

        chat_settings.top_k = top_k
        chat_settings.llm = selected_llm
        chat_settings.prompting_strategy = prompting_strategy

        st.success("Settings applied!")