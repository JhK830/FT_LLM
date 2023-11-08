import os
import openai


openai.api_key = "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"
openai.File.create(
  file=open("test_data.jsonl", "rb"),
  purpose='fine-tune'
)

# openai.FineTuningJob.create(training_file="file-4vznn3HQX5Ax5TNaZHeMUvAB", model="gpt-3.5-turbo")