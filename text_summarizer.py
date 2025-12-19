from openai import OpenAI

client = OpenAI()

story = """At dawn, the city woke with pockets full of birdsong and a rumor of rain.
Mira found a key in her pocket that hummed like it remembered a door.
She followed the sound through alleys painted with yesterday’s posters and tomorrow’s hope.
The key led her to a library that breathed dust and patience.
Inside, books whispered not to be read but to be returned.
Mira chose one with a cracked spine and a brave title.
When she opened it, the room tilted and the rain arrived early.
She stepped into the story and felt the city settle into her bones.
Outside, the key fell silent, satisfied at last.
Inside, Mira kept walking, carrying the door wherever she went."""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role":"system","content":"You are a copyrighting assistent."},
        {"role":"user","content":"Summurize following story in 2 sentences: "+story}
    ]
)

print(response.output_text)