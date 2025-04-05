script({
  title: 'prototype-figma',
  description: 'Generate HTML and CSS code from Figma design',
  group: 'code',
  model: 'openai:gpt-4o-mini',
});

defTool({
  "sequential-thinking": {
      "command": "npx", 
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
  ["figma-connector"]: {
      command: "npx",
      args: ["-y", "figma-developer-mcp", `--figma-api-key=<API_KEY>`, "--stdio"],
  },
})

$`Implement this Figma file for me.
""`