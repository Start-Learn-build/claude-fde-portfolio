# Week 1: Email-to-JSON extractor
A Python script that sends customer emails to Claude via the API and
returns name, company, request and urgency as structured JSON.

## What I learned
- How the Claude API works: my code + API key → Claude → answer
- Prompting for reliable JSON output (exact format, XML tags, "only JSON")
- System prompts vs user messages

## Run it
pip3 install anthropic
export ANTHROPIC_API_KEY=your-key
python3 extract.py
