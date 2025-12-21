from openai import OpenAI

client = OpenAI()

email = """
To: maria38@gmail.com

Subject: Project Update and Upcoming Milestones

Hi Maria,

I hope you’re doing well. I wanted to take a moment to provide a more detailed update on the current project timeline and outline what to expect over the next couple of weeks.

I’m happy to share that we are progressing as planned and remain on track to complete the first phase of the project by April 15. The team has completed the initial development tasks, and we are now moving into testing and refinement. So far, there have been no major blockers, and everything is aligning well with our original schedule.

Later this week, I will send you a more detailed breakdown of the remaining tasks, including key milestones and deliverables for the next phase. This should give you better visibility into our progress and help with any internal planning on your side.

Please feel free to reach out if you have any questions, need clarification on any part of the timeline, or would like to discuss adjustments. I’m always happy to connect.

Thank you for your continued support, and I look forward to your feedback.

Best regards,
Alex Johnson
Project Manager
"""

system = "You are a email assistent. Rewrite the following email, so that the message is not longer than 400 character.\n\n"
    
response = client.responses.create(
    model="gpt-4.1-mini",
    input= [
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
                    "text": email
                }
            ]
        }
    ]
)

print(response.output_text)

