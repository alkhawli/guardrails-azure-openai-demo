from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.core.guard import guardrail_stream

router = APIRouter()

@router.get("/generate/{prompt}/{with_guardrails}")
async def generate_response(prompt: str, with_guardrails: bool):
    """
    FastAPI endpoint to generate and stream responses.
    """
    print(f"🔥 Prompt received: {prompt} | Guardrails: {with_guardrails}")

    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    return StreamingResponse(
        guardrail_stream(prompt, with_guardrails),
        media_type="text/plain"
    )

