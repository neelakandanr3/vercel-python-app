from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
import httpx

app = FastAPI()

@app.get("/api")
async def proxy(request: Request, url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            content = response.content
            headers = response.headers
            headers["Access-Control-Allow-Origin"] = "*"
            return Response(content=content, headers=headers, media_type=response.headers.get("content-type"))
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
