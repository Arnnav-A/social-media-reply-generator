# Social Media Reply Generator

A FastAPI-based backend service that generates human-like replies to social media posts using an LLM (via Groq API). Replies are tailored for platforms like Twitter, LinkedIn, and Instagram, and are stored in MongoDB for future reference.

## Setup & Installation

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd social-media-reply-generator
   ```

2. Create and activate a virtual environment

3. Install dependencies
    ```
    pip install -r requirements.txt
    ```

4. Configure environment variables. Create a .env using the .env.example and fill in your credentials.

5. Run the FastAPI server
    ```
    uvicorn app.main:app --reload
    ```

## API Usage

Use the ```POST /reply``` endpoint with ```platform``` and ```post_text```.

See sample usage in [request.py](request.py)

## Approach to Human-like Replies

 - Tone Detection: The system first analyzes the post to determine its tone using the LLM.
 - Platform Awareness: Prompts are customized for each platform (Twitter, LinkedIn, Instagram) to match typical user interaction styles.
 - Prompt Engineering: The LLM is prompted to generate replies that are contextually relevant and human-like, with explicit instructions to match the detected tone.
 - Diversity: Multiple replies are generated using different temperature settings to ensure variety and naturalness.

## Architecture Decisions & Trade-offs
 - FastAPI: Chosen for its speed, async support, and ease of integration with Pydantic models.
 - LLM via Groq API: Offloads the complexity of language generation, but introduces dependency on an external service and potential latency.
 - MongoDB: Used for storing generated replies for analytics or future use. No complex relational data, so a document store is sufficient.
 - Stateless API: The backend is stateless except for reply storage, making it easy to scale horizontally.
 - Prompt-based Tone Detection: Relies on the LLM for tone detection, which is flexible but may be less consistent than a dedicated classifier.