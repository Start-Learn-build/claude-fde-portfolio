import anthropic
client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=300,
    system="You are a friendly tutor.",
    messages=[{"role": "user", "content": "what does health informatics professional do?"}],
)
print(msg.content[0].text)
