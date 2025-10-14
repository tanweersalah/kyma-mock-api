# main.py

from fastapi import FastAPI, Body
import httpx
import constants

app = FastAPI(title="FastAPI with Remote Text Data")

async def fetch_text(url: str) -> str:
    """Fetch text data from a remote URL."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.text

@app.post("/query-tool")
async def query_tool(payload: dict = Body(...)):
    """
    Accepts a JSON body and returns mock text from a remote URL.
    Example body: { "query": "some input" }
    """
    text_data = await fetch_text(constants.QUERY_TOOL_URL)
    return {
        "input": payload,
        "message": text_data
    }

@app.post("/rag-tool")
async def rag_tool(payload: dict = Body(...)):
    """
    Accepts a JSON body and returns mock text from a remote URL.
    Example body: { "query": "some input" }
    """
    text_data = await fetch_text(constants.RAG_TOOL_URL)
    return {
        "input": payload,
        "message": text_data
    }
