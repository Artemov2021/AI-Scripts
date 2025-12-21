from openai import OpenAI
client = OpenAI()

system_prompt = "You are a poem writer."

file = client.files.create(
    file=open("data/From_Hands_to_Heaven_Two_Pages.pdf","rb"),
    purpose="assistants"
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input= [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Summarize the poem in 3 sentences.",
                },
            ]
        }
    ]
)

print(response.output_text)