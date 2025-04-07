import streamlit as st
import httpx
import asyncio
import urllib.parse

FASTAPI_URL = "http://fastapi:8000/generate/"

async def fetch_response(prompt: str, use_guardrails: bool, container: st.delta_generator.DeltaGenerator):
    # URL encode the prompt to prevent path errors
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{FASTAPI_URL}{encoded_prompt}/{str(use_guardrails).lower()}"

    async with httpx.AsyncClient(timeout=60.0) as client:
        async with client.stream("GET", url) as response:
            response_text = ""
            async for chunk in response.aiter_text():
                if chunk:
                    response_text += chunk
                    container.markdown(response_text)
                    await asyncio.sleep(0)


async def fetch_both_responses(prompt: str):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("AI Response (With Guardrails)")
        response_container1 = st.empty()

    with col2:
        st.subheader("AI Response (No Guardrails)")
        response_container2 = st.empty()

    tasks = [
        asyncio.create_task(fetch_response(prompt, True, response_container1)),
        asyncio.create_task(fetch_response(prompt, False, response_container2))
    ]
    await asyncio.gather(*tasks)

# ------------------- STREAMLIT UI ------------------- #

st.set_page_config(
    layout="wide", 
    page_title="Chatbot - Guardrails vs No Guardrails"
)

st.title("💬 QnA - Guardrails vs No Guardrails")
st.write("Ask a question and see responses **with and without guardrails** side by side.")

prompt = st.text_input("Your Question:", placeholder="Type here...")

if st.button("Get Answers"):
    if prompt.strip():
        asyncio.run(fetch_both_responses(prompt))
    else:
        st.warning("Please enter a question!")
