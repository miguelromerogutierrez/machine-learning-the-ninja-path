import re
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from constants import SUMMARY_PROMPT

class TrancriptLoader:
  def __init__(self, fileName, participants = []):
    self.fileName = fileName
    self.participants = participants

  def load(self) -> list[str]:
    conversation = {}
    with open(self.fileName, 'r') as file:
      content = file.read()
      splits = re.split(r"\n\n", content)

      for split in splits:
        for pattern in self.participants:
          if re.match(pattern, split):
            if pattern not in conversation:
              conversation[pattern] = []
            split = re.sub(pattern, '', split).strip()
            conversation[pattern].append(split) 
      
      return [conversation[pattern] for pattern in self.participants]

class Summarizer:
  def __init__(self, llm, transcript, chunk_size=3000, chunk_overlap=400):
    self.llm = llm
    text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=chunk_size, chunk_overlap=chunk_overlap, add_start_index=True
    )
    self.chunks = text_splitter.split_text(transcript)

  def summarize(self):
    summaries = []
    for chunk in self.chunks:
      message = self.llm.invoke(SUMMARY_PROMPT.format(CONTENT=chunk))
      summaries.append(message)
    self.summaries = summaries

  def save(self):
    for i, summary in enumerate(self.summaries):
      output_file = f'./Summaries/summary_{i+1}.md'
      
      with open(output_file, 'w') as file:
        file.write(summary.content)

# fileName = 'Transcript+-+Convolutional+Neural+Networks.txt'
# docs = TrancriptLoader(fileName).load()
# summarizer = Summarizer(llm, docs)
# summarizer.summarize()
# summarizer.save()
