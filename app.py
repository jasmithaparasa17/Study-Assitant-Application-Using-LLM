import os
from google import genai
from google.genai import types
key=os.getenv('AP_KEY')
client=genai.Client(api_key=key)
personalities = {
  "Friendly": """You are a friendly, enthusiastic, and highly encouraging Study Assistant.
      Your goal is to break down complex concepts into simple, beginner-friendly explanations.
      Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding""",
  "Academic": """You are a strictly academic, highly detailed, and professional university Professor.
      Use precise, formal terminology, cite key concepts and structure your response.
      Your goal is to break down complex concepts into simple, beginner-friendly explanations.
      Use analogies and real-world examples that beginners can relate to.
      Always ask a follow-up question to check understanding"""
}
def user_function(user_prompt,personality):
  system_prompt=personalities[personality]
  response=client.models.generate_content(
      model="gemini-3.5-flash-lite",
      config=types.GenerateContentConfig(
          system_instruction=system_prompt,
          temperature=0.7,
          max_output_tokens=1024
      ),
      contents=user_prompt
  )
  return response.text
  
import gradio as gr
demo = gr.Interface(
    fn = user_function,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question...", label="Question"),
        gr.Dropdown(choices=list(personalities.keys()), value="Friendly", label="Personality")
    ],
    outputs = gr.Textbox(lines=10, label="Response"),
    title = "Study Assistant",
    description="Ask a question and get an answer from your AI study assistant with a chosen personality."
)
demo.launch(server_name="0.0.0.0",server_port=int(os.environ.get("PORT",7860)))
