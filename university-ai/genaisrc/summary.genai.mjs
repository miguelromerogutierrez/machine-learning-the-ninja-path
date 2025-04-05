import fs from 'fs';
import { SUMMARY_PROMPT } from './constants.js'

function readLectures() {
  const dir = fs.readdirSync('./genaisrc/lectures');
 return dir.map((file) => {
    return fs.readFileSync(`./genaisrc/lectures/${file}`, 'utf8');
  });
}

script({
  title: 'summary',
  description: 'Generate a summary of a lecture',
  group: 'education',
  model: 'github_copilot_chat:gpt-4o',
});

const lectures = readLectures();

const lecturesPromise = lectures.map((lecture) => {
  return runPrompt(SUMMARY_PROMPT.replace('{CONTENT}', lecture));
});

const results = await Promise.all(lecturesPromise);

results.forEach((result, index) => {
  fs.writeFileSync(`./summaries/summary_${index}.md`, result.text);
});
