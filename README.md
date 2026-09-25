# Claude-Partner-Network-Learning-Path

Repo for the certification and course seen here: 
https://anthropic.skilljar.com/page/claude-partner-network-learning-path?utm_medium=email&amp;_hsmi=421528243&amp;utm_content=421528243&amp;utm_source=hs_email

## Claude API Example request
curl https://api.anthropic.com/v1/messages \
  --header "x-api-key: API KEY HERE" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{"model": "claude-opus-5-5", "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello, world"}]}'