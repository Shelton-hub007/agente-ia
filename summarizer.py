from os import getenv
from pathlib import Path

import torch
from dotenv import load_dotenv
from transformers import AutoTokenizer, MT5ForConditionalGeneration

load_dotenv()


def chunk_text(text: str, max_chunk_size: int = 512) -> list[str]:
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    for word in words:
        if current_size + len(word) + 1 > max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_size = len(word)
        else:
            current_chunk.append(word)
            current_size += len(word) + 1
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def summarize_text(model, tokenizer, text: str, max_length: int = 84) -> str:
    input_ids = tokenizer(
        text,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=512,
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids, max_length=max_length, no_repeat_ngram_size=2, num_beams=4
    )[0]

    summary = tokenizer.decode(
        output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    return summary


def summarization(text: str) -> str:
    MODEL_PATH = getenv("MT5_MULTILINGUAL_XLSUM_PATH")
    model = MT5ForConditionalGeneration.from_pretrained(
        MODEL_PATH, local_files_only=True
    )
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH, use_fast=False, legacy=False, local_files_only=True
    )

    # Split the text into chunks
    chunks = chunk_text(text)

    # Summarize each chunk
    chunk_summaries = [summarize_text(model, tokenizer, chunk) for chunk in chunks]

    # Combine the summaries
    combined_summary = " ".join(chunk_summaries)

    # If the combined summary is still too long, summarize it again
    if len(combined_summary.split()) > 512:
        final_summary = summarize_text(model, tokenizer, combined_summary)
    else:
        final_summary = combined_summary

    return final_summary
