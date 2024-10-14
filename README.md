# Langchain LinkedIn Agent

Important Steps:
1. Create a `.env` file.
2. Signup for [PROXYCURL](https://nubela.co/proxycurl/) (Used to scrape your LinkedIn Profile).
3. Signup for [TAVILY](https://app.tavily.com/) (Used to search the web).
4. Signup for [LangSmith](https://smith.langchain.com/) (Logging. Uses LANGCHAIN_PROJECT env as project name).
5. Store all your tokens in the file.

Example `.env` file:
```yaml
PROXYCURL_API_KEY='10-XYZ'
TAVILY_API_KEY='tvly-XYZ'
LANGCHAIN_API_KEY='lsv2_pt_XYZ'
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=LinkedIn Agent
```

Tips:
1. You can store the `PROXYCURL` output in a json gist for testing. Check `scrapers/linkedin.py` for `mock` data. e.g [martinoywa.json](https://gist.github.com/martinoywa/8c1043afa2b2d306f0089ac99ec78a4d)

How to run `agent_chain/main.py`:
[WIP]