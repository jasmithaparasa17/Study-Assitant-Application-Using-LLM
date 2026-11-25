# Study-Assitant-Application-Using-LLM

An AI-powered study assistant built with **Python**, **Gradio**, and the
**Google Gemini API**. Ask a question and receive an explanation in one
of two response styles: **Friendly** or **Academic**.

## Live Demo

Try the deployed application here:

[Study Assistant -- Live
App](https://study-assitant-application-using-llm.onrender.com/)

## Features

-   **AI-powered answers:** Generates responses using Google's Gemini
    model.
-   **Two response personalities:**
    -   **Friendly:** Encouraging, beginner-friendly explanations with
        analogies and relatable examples.
    -   **Academic:** More formal and detailed explanations using
        academic terminology.
-   **Simple web interface:** Enter a question, choose a personality,
    and view the generated response.
-   **Follow-up learning:** The configured assistant prompts a follow-up
    question to check understanding.

## Tech Stack

-   **Python** -- application logic
-   **Gradio** -- web interface
-   **Google Gen AI SDK (`google-genai`)** -- Gemini API integration
-   **Gemini model:** `gemini-3.5-flash-lite`

## Project Structure

``` text
.
├── app.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/<your-username>/<your-repository-name>.git
cd <your-repository-name>
```

Replace the repository URL and directory with your own GitHub repository
details.

### 2. Create and activate a virtual environment

``` bash
python -m venv venv
```

Activate it:

**Windows (Command Prompt):**

``` bash
venv\Scripts\activate
```

**macOS / Linux:**

``` bash
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

The application reads the API key from an environment variable named
`AP_KEY`.

Create a Gemini API key through [Google AI
Studio](https://aistudio.google.com/app/apikey), then set the
environment variable.

**Windows (PowerShell):**

``` powershell
$env:AP_KEY="your_gemini_api_key"
```

**Windows (Command Prompt):**

``` cmd
set AP_KEY=your_gemini_api_key
```

**macOS / Linux:**

``` bash
export AP_KEY="your_gemini_api_key"
```

Keep your API key private. Do not hard-code it in the source code or
commit it to GitHub.

### 5. Run the application

``` bash
python app.py
```

Gradio will start the application and display a local URL in the
terminal. Open that URL in your browser.

## How to Use

1.  Open the [live
    application](https://study-assitant-application-using-llm.onrender.com/)
    or run it locally.
2.  Type your study question into the **Question** field.
3.  Select **Friendly** or **Academic** from the **Personality**
    dropdown.
4.  Submit the question.
5.  Read the generated explanation and use the follow-up question to
    check your understanding.

## Dependencies

The project currently lists these dependencies in `requirements.txt`:

-   `google-genai`
-   `gradio`

Install them with:

``` bash
pip install -r requirements.txt
```

## Configuration Notes

-   The API key environment variable must be named `AP_KEY`.
-   The Gemini model is configured in `app.py` as
    `gemini-3.5-flash-lite`.
-   The application uses Gradio's interface and launch functionality.

## Security

-   Never publish your Gemini API key.
-   For deployment platforms, add `AP_KEY` through the platform's
    environment-variable or secrets settings.
-   If an API key has been exposed, revoke it and create a replacement.

## Future Improvements

Possible enhancements for future versions:

-   Conversation history and multi-turn chat
-   Support for uploaded notes and study documents
-   Subject-specific study modes
-   Quiz and flashcard generation
-   Adjustable response length and difficulty

## Author

Add your name and relevant links here:

-   **GitHub:** https://github.com/jasmithaparasa17/
-   **Live Demo:**
    https://study-assitant-application-using-llm.onrender.com/

------------------------------------------------------------------------

If you find this project useful, consider giving the repository a ⭐ on
GitHub.
