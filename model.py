import wikipedia

def fetch_wikipedia_data(query):
    try:
        # Set Wikipedia language to English
        wikipedia.set_lang("en")

        # Get the Wikipedia page object for the given query
        page = wikipedia.page(query)
        
        # --------------------------------------------
        # Extract images from the page
        # Only keep image URLs that end with .jpg/.jpeg/.png 
        # (this filters out icons, SVG logos, etc.)
        # --------------------------------------------
       # images = [img for img in page.images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Pick the first valid image if available, otherwise None
        #first_image = images[0] if images else None
        
        # Return structured data (title, summary, URL, image link)
        return {
            "title": page.title,       # Title of the Wikipedia page
            "summary": page.summary,   # Short summary of the topic
            "url": page.url,           # Full Wikipedia page URL
            #"image": first_image       # First relevant image (if any)
        }

    except Exception:
        # If something goes wrong (e.g., page not found, disambiguation), return None
        return None
