import wikipedia
from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask application
app = Flask(__name__)

# Load a free AI model (Flan-T5) from HuggingFace for fact generation
fact_generator = pipeline("text2text-generation", model="google/flan-t5-small")

# -------------------------------
# Function: Generate "Did you know?" fun facts from the Wikipedia summary
# -------------------------------
def generate_did_you_know(summary):
    # Create a prompt for the model
    prompt = f"From this text, write 2 short and interesting facts in a fun way:\n\n{summary}"
    try:
        # Generate text using the AI model
        result = fact_generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']
    except Exception as e:
        # If something goes wrong, return the error message
        return f"Error generating facts: {e}"

# -------------------------------
# Route: Home page (with search form)
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None     # Stores Wikipedia title, summary, and URL
    images = []       # Stores related images
    facts = None      # Stores AI-generated facts

    # If user submits a query through the search bar
    if request.method == "POST":
        query = request.form["query"]   # Get the user’s input
        try:
            # Fetch Wikipedia page for the query
            page = wikipedia.page(query)

            # Get a short summary (5 sentences)
            summary = wikipedia.summary(query, sentences=5)

            # Save page details to send to template
            result = {
                "title": page.title,
                "summary": summary,
                "url": page.url
            }

            # Collect up to 5 usable images (jpg/png only)
            images = [img for img in page.images if img.lower().endswith((".jpg", ".jpeg", ".png"))][:5]

            # Generate "Did you know?" fun facts
            facts = generate_did_you_know(summary)

        except Exception as e:
            # If error occurs (e.g., no page found), show error message
            result = {"error": str(e)}

    # Render the HTML template and pass data (results, images, facts) to it
    return render_template("index.html", result=result, images=images, facts=facts)

# -------------------------------
# Run the app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode = auto reload + error messages
