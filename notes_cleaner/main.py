from openai import OpenAI
from pathlib import Path

client = OpenAI()

developer_prompt = """
You are a helpfull assistant. Summirize the notes below in the following structure:
1) A clean summary (3–6 bullets) 
2) A list of action items in a structured JSON format:
    owner (if mentioned, otherwise “Unassigned”)
    task
    due date (if mentioned, otherwise null)
    priority (Low/Medium/High)
"""

raw_notes = Path(__file__).with_name("notes.txt").read_text(encoding="utf-8")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role":"developer","content":developer_prompt},
        {"role":"user","content":raw_notes},
    ]
)

print(response.output_text)