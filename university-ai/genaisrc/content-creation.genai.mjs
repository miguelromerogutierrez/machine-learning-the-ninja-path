import fs from 'fs';
import { CONTENT_CREATION_PROMPT } from "./constants.js";

script({
  title: 'content-creation',
  description: 'Generate content for LinkedIn posts',
  group: 'education',
  model: 'github_copilot_chat:gpt-4o',
});

const result = await runPrompt(`${CONTENT_CREATION_PROMPT.replace('{NOTES}', ``)}`)
fs.writeFileSync(`./content-creation.md`, result.text);
