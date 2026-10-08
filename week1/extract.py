import anthropic, json, pathlib
client = anthropic.Anthropic()
PROMPT = """Extract these fields from the email in <email> tags.
Return ONLY valid JSON, no other text, in exactly this shape:
{"name": "...", "company": "...", "request": "one short sentence", "urgency": "low|medium|high"}"""
results = []
for f in sorted(pathlib.Path("emails").glob("*.txt")):
    msg = client.messages.create(
        model="claude-sonnet-5-5", max_tokens=300,
        system="You extract structured data from customer emails.",
        messages=[{"role": "user", "content": f"{PROMPT}\n<email>{f.read_text()}</email>"}],
    )
    data = json.loads(msg.content[0].text)
    data["file"] = f.name
    results.append(data)
    print(data)
pathlib.Path("results.json").write_text(json.dumps(results, indent=2))
print("Saved results.json")
