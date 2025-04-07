# Guardrails.ai with Azure OpenAI Integration

This project showcases how to integrate Guardrails.ai with Azure OpenAI services to ensure safe, secure, and compliant AI-generated content. Using FastAPI and Streamlit, it offers developers an engaging, hands-on experience testing three key Guardrails directly from the Guardrails Hub:

1. Ban List
2. Competitor Check
3. Gibberish Text

## Overview

Guardrails AI is a framework for adding safety, reliability, and observability to LLM-powered applications. It allows developers to define "guardrails" that validate and control model inputs and outputs, helping mitigate issues like hallucinations, sensitive data leaks, and formatting errors. With both open-source and enterprise options, Guardrails AI supports structured output generation, integrates easily with Python apps, and includes a hub of reusable, production-ready validation components.

## Project Structure

```
.
├── app                 # FastAPI backend
│   └── main.py
├── app.py              # Streamlit frontend
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
└── .env
```

## Prerequisites

- Docker and Docker Compose
- Poetry (version 1.8.3 recommended)
- Azure OpenAI service subscription
- Guardrails.ai token

## Docker Compose Installation and Setup

Populate your `.env` file with the following details:

```bash
GUARDRAILS_TOKEN=your_guardrails_token
API_URL=http://fastapi:8000
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
```

Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

After the build, your services are accessible at:
- FastAPI: `http://localhost:8000`
- Streamlit: `http://localhost:8501`

## Guardrails Configuration

Guardrails.ai is already pre-configured within the Dockerfile.fastapi. The necessary setup commands are executed during the container build process, including token-based authentication and installation of guardrails modules from the Guardrails Hub:

1. [Ban List](https://hub.guardrailsai.com/validator/guardrails/ban_list)
1. [Competitor Check](https://hub.guardrailsai.com/validator/guardrails/competitor_check)
2. [Gibberish Text](https://hub.guardrailsai.com/validator/guardrails/gibberish_text)

No manual setup is required post-deployment.

## Contributing

Contributions are welcome. Submit issues or pull requests for improvements. Or even reach out!
