from openai import OpenAI
import json

client = OpenAI()

system = """"
    You are a message classification engine.

    Respond ONLY in valid JSON using this structure:

    {
    "category": "billing" | "technical" | "general",
    "urgency": "low" | "medium" | "high",
    "action": "reply" | "escalate" | "ignore"
    }

    Rules:
    - urgency is "high" if time-sensitive or service-stopping
    - action is "escalate" if urgency is "high"
    - Do not include any text outside the JSON object
    """
message = "hi, do you have Ausbildungsplätze? I am right no on search, I like your company and i have coding experience"

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "system",
            "content": [
                {
                    "type": "input_text",
                    "text": system
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": message
                }
            ]
        }
    ]
)

raw_output = response.output_text
data = json.loads(raw_output)

category = data["category"]
urgency = data["urgency"]
action = data["action"]

print(f"Category: {category}")
print(f"Urgency: {urgency}")
print(f"Action: {action}")

