from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="I am from Freiburg"
)

embedding = response.data[0].embedding

print(len(embedding))
print(embedding[:10])