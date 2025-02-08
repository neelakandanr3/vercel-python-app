from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

   # Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Allow all origins
       allow_methods=["GET"],  # Allow only GET requests
       allow_headers=["*"],
   )

@app.get("/api/outline")
async def get_country_outline(country: str = Query(..., description="Name of the country")):
       # Construct the Wikipedia URL for the country
       wikipedia_url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"

       # Fetch the Wikipedia page
       response = requests.get(wikipedia_url)
       if response.status_code != 200:
           raise HTTPException(status_code=404, detail="Country page not found on Wikipedia")

       # Parse the HTML content
       soup = BeautifulSoup(response.content, "html.parser")

       # Extract all headings (H1 to H6)
       headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

       # Generate the Markdown outline
       markdown_outline = "## Contents\n\n"
       for heading in headings:
           level = int(heading.name[1])  # Extract the heading level (1 for H1, 2 for H2, etc.)
           text = heading.get_text().strip()
           markdown_outline += f"{'#' * level} {text}\n\n"

       return {"outline": markdown_outline.strip()}
