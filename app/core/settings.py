import os

from dotenv import load_dotenv
from guardrails.hub import CompetitorCheck, BanList, GibberishText

# Load environment variables
load_dotenv()

# Azure OpenAI API credentials from .env
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

guardrails_list = [
    CompetitorCheck(competitors=["Lidl", "Aldi"], on_fail="filter"),
    BanList(banned_words=['ukraine', 'russia'], on_fail="exception"),
    GibberishText(threshold=0.9, validation_method="full", on_fail="fix")
]