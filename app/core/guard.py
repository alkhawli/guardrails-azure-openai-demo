# app/core/guard.py

import asyncio
import logging
from typing import AsyncGenerator

from guardrails import Guard

from .settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    OPENAI_API_VERSION,
    guardrails_list
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_guard(with_guardrails: bool) -> Guard:
    """
    Initializes the Guard object with or without guardrails.
    """
    return Guard().use_many(*guardrails_list) if with_guardrails else Guard()

async def guardrail_stream(prompt: str, with_guardrails: bool) -> AsyncGenerator[str, None]:
    """
    Streams validated output from Azure OpenAI through Guardrails.
    """
    try:
        guard = get_guard(with_guardrails)
        
        stream_chunk_generator = guard(
            messages=[{"role": "user", "content": prompt}],
            model="azure/gpt4o-fi",
            stream=True,
            api_base=AZURE_OPENAI_ENDPOINT,
            api_version=OPENAI_API_VERSION,
            api_key=AZURE_OPENAI_API_KEY,
            num_reasks=2,
        )
        
        for chunk in stream_chunk_generator:
            yield chunk.validated_output
            # let the loop yield control
            await asyncio.sleep(0)


    
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        yield (
            "🚨 The response was filtered due to guardrails "
        )
