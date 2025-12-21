from openai import OpenAI

client = OpenAI()

system_prompt = """
You are a email assistent. Change the ton of the following message:
"""

message = "Hi chief! Send me the project plan tomorrow"

tones = ["polite","friendly","formal","casual","assertive"]

response = client.responses.create(
    model="gpt-4.1-mini",
    input = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": message + "\n" + "Tone: " + tones[0]
        }
    ]
)

print(response.output_text)

