import argparse
import os
import sys
import openai
import requests
import logging
from typing import List, Tuple
import tiktoken

# Initialize total_tokens_used
total_tokens_used = 0

import re

def remove_markdown_code_blocks(text):
    """
    Entfernt ```markdown am Anfang und ``` am Ende des Textes, falls vorhanden.
    
    Parameters:
        text (str): Der zu bereinigende Text.
    
    Returns:
        str: Der bereinigte Text ohne die spezifischen Markdown-Codeblöcke.
    """
    # Entfernt ```markdown am Anfang
    text = re.sub(r'^```markdown\s*\n?', '', text)
    # Entfernt ``` am Ende
    text = re.sub(r'\n?```$', '', text)
    return text.strip()

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Count tokens in text using tiktoken for the specified model."""
    try:
        encoder = tiktoken.encoding_for_model(model)
        return len(encoder.encode(text))
    except Exception:
        # Fallback to rough estimation
        return len(text.split()) * 1.5

def list_available_models():
    # Set up your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    try:
        response = requests.get("https://api.openai.com/v1/models", headers=headers)
        response.raise_for_status()
        models = response.json()["data"]
        model_ids = [model['id'] for model in models]
        print("Available models:")
        for model_id in model_ids:
            print(f"- {model_id}")
    except Exception as e:
        logging.error(f"Error fetching models: {e}")
        sys.exit(1)

def select_model_for_file(token_count: int, preferred_model: str) -> str:
    """
    Select the appropriate model based on token count.
    Uses gpt-4o-mini for files <= 4096 tokens, gpt-4o for larger files.
    """
    # Token limits for models
    model_limits = {
        'gpt-4o-mini-2024-07-18': 4096,
        'gpt-4o-mini': 4096,
        'gpt-4o': 128000,
        'gpt-4o-2024-08-06': 128000,
        'gpt-4o-2024-05-13': 128000,
        'gpt-4-turbo': 128000,
        'gpt-4-0125-preview': 128000,
        'gpt-4-1106-preview': 128000,
    }
    
    # If preferred model can handle it, use it
    if preferred_model in model_limits:
        if token_count <= model_limits[preferred_model]:
            return preferred_model
    
    # Otherwise, select appropriate model based on size
    if token_count <= 4096:
        return 'gpt-4o-mini-2024-07-18'  # Cost-effective for small files
    else:
        return 'gpt-4o'  # Large context for big files

def split_text_into_chunks(text: str, max_tokens: int, model: str = "gpt-4o") -> List[str]:
    """
    Split text into chunks that fit within the token limit.
    Attempts to split at paragraph boundaries or newlines.
    """
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode(text)
    
    if len(tokens) <= max_tokens:
        return [text]
    
    chunks = []
    current_chunk_tokens = []
    
    # Split by paragraphs first
    paragraphs = text.split('\n\n')
    
    for paragraph in paragraphs:
        para_tokens = encoder.encode(paragraph)
        
        if len(para_tokens) > max_tokens:
            # Paragraph itself is too large, split by newlines
            lines = paragraph.split('\n')
            for line in lines:
                line_tokens = encoder.encode(line)
                if len(line_tokens) > max_tokens:
                    # Line is still too large, split by sentences
                    sentences = re.split(r'(?<=[.!?])\s+', line)
                    for sentence in sentences:
                        sent_tokens = encoder.encode(sentence)
                        if len(current_chunk_tokens) + len(sent_tokens) <= max_tokens:
                            current_chunk_tokens.extend(sent_tokens)
                        else:
                            if current_chunk_tokens:
                                chunks.append(encoder.decode(current_chunk_tokens))
                                current_chunk_tokens = []
                            current_chunk_tokens.extend(sent_tokens)
                else:
                    if len(current_chunk_tokens) + len(line_tokens) <= max_tokens:
                        current_chunk_tokens.extend(line_tokens)
                    else:
                        if current_chunk_tokens:
                            chunks.append(encoder.decode(current_chunk_tokens))
                            current_chunk_tokens = []
                        current_chunk_tokens.extend(line_tokens)
        else:
            if len(current_chunk_tokens) + len(para_tokens) <= max_tokens:
                current_chunk_tokens.extend(para_tokens)
            else:
                if current_chunk_tokens:
                    chunks.append(encoder.decode(current_chunk_tokens))
                    current_chunk_tokens = []
                current_chunk_tokens.extend(para_tokens)
    
    if current_chunk_tokens:
        chunks.append(encoder.decode(current_chunk_tokens))
    
    return chunks

def translate_text(text, target_lang, model):
    # Set up your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    logging.debug(f"Translating text with length {len(text)} characters.")

    # Define the prompt with explicit instructions
    prompt = f"""
You are a professional translator specializing in software documentation.

Translate the following English Markdown text to {target_lang}.

- Preserve all Markdown formatting, including headings, lists, links, code blocks, inline code, HTML tags, and embedded syntax.
- Do not translate or alter code blocks, inline code, HTML tags, URLs, or embedded syntax
- Only translate the human-readable text content.
- Ensure that the translated text aligns with the original formatting and structure.

Text to translate:
```markdown
{text}

"""

    # Prepare messages based on model capabilities
    messages = []
    if model in ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4o', 'gpt-4o-mini', 'gpt-4o-mini-2024-07-18', 'gpt-4o-2024-08-06']:
        messages.append({"role": "system", "content": "You are a helpful assistant that translates English Markdown documents to other languages while preserving formatting and not altering code or special syntax."})
        messages.append({"role": "user", "content": prompt})
    else:
        # For models that do not support 'system' role
        messages.append({"role": "user", "content": prompt})

    try:
        # Set parameters based on model capabilities
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.2
        )
        logging.debug(f"Received response: {response}")
    except openai.error.OpenAIError as e:
        # Catch all OpenAI-related errors
        logging.error(f"OpenAI API error: {e}")
        raise
    except Exception as e:
        logging.error(f"Error during translation: {e}")
        sys.exit(1)

    translated_text = response.choices[0].message.content.strip()

    # Update total tokens used
    global total_tokens_used
    if 'usage' in response:
        total_tokens_used += response['usage']['total_tokens']
    else:
        logging.warning("Token usage information not available in the response.")

    return translated_text

def translate_markdown(markdown_text, target_lang, model):
    """
    Translate markdown text, handling large files by chunking if necessary.
    """
    try:
        # Count tokens to determine if chunking is needed
        token_count = count_tokens(markdown_text, model)
        logging.info(f"Token count: {token_count}")
        
        # Model token limits
        model_limits = {
            'gpt-4o-mini-2024-07-18': 4096,
            'gpt-4o-mini': 4096,
            'gpt-4o': 128000,
            'gpt-4o-2024-08-06': 128000,
            'gpt-4o-2024-05-13': 128000,
            'gpt-4-turbo': 128000,
        }
        
        max_tokens = model_limits.get(model, 4096)
        
        # Reserve some tokens for the prompt and response
        safe_max = int(max_tokens * 0.85)
        
        if token_count <= safe_max:
            # Translate entire text at once
            logging.info(f"Translating entire file in one request (model: {model})")
            translated_markdown = translate_text(markdown_text, target_lang, model)
        else:
            # Split into chunks and translate each
            logging.info(f"File too large ({token_count} tokens), splitting into chunks (max {safe_max} tokens each)")
            chunks = split_text_into_chunks(markdown_text, safe_max, model)
            translated_chunks = []
            
            for i, chunk in enumerate(chunks, 1):
                logging.info(f"Translating chunk {i}/{len(chunks)}")
                translated_chunk = translate_text(chunk, target_lang, model)
                translated_chunks.append(translated_chunk)
            
            # Reassemble translated chunks
            translated_markdown = '\n\n'.join(translated_chunks)
            
    except Exception as e:
        logging.error(f"Error during translation: {e}")
        raise

    return translated_markdown

def main():
    parser = argparse.ArgumentParser(description="Translate a Markdown file from English to a specified language.")
    parser.add_argument('language', nargs='?', help='Target language (e.g., "German")')
    parser.add_argument('input_file', nargs='?', help='Input Markdown file')
    parser.add_argument('output_file', nargs='?', help='Output Markdown file', default=None)
    parser.add_argument('--model', help='OpenAI model to use (default: auto-select based on file size)', default='auto')
    parser.add_argument('--list-models', action='store_true', help='List available OpenAI models and exit')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')

    args = parser.parse_args()

    if args.list_models:
        list_available_models()
        return


    # Set up logging based on '--debug' argument
    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    if not args.language or not args.input_file:
        parser.print_help()
        sys.exit(1)

    if not os.getenv("OPENAI_API_KEY"):
        logging.error("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    logging.info("Starting translation process...")

    with open(args.input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Count tokens accurately using tiktoken
    approx_tokens = count_tokens(markdown_text, "gpt-4o")
    logging.info(f"Approximate token count: {approx_tokens}")

    # Auto-select model if not specified
    if args.model == 'auto':
        selected_model = select_model_for_file(approx_tokens, 'gpt-4o-mini-2024-07-18')
        logging.info(f"Auto-selected model: {selected_model} (file size: {approx_tokens} tokens)")
    else:
        selected_model = args.model
    
    # Check if the content exceeds token limits (only if not using auto mode)
    if args.model != 'auto':
        model_token_limits = {
            'gpt-4o-mini-2024-07-18': 4096,
            'gpt-4o-mini': 4096,
            'gpt-4o': 128000,
            'gpt-4o-2024-08-06': 128000,
            'gpt-4o-2024-05-13': 128000,
            'gpt-4-turbo': 128000,
            'gpt-4': 8192,
            'gpt-4-32k': 32768,
        }
        max_tokens = model_token_limits.get(selected_model, 4096)

        if approx_tokens > max_tokens:
            logging.error(f"The input file is too large for the selected model ({selected_model}).")
            logging.error(f"Approximate tokens: {approx_tokens}, Model limit: {max_tokens}")
            logging.info("Hint: Use --model auto to automatically select gpt-4o for large files")
            sys.exit(1)

    try:
        translated_markdown = translate_markdown(markdown_text, args.language, selected_model)
    except Exception as e:
        logging.error(f"An error occurred during translation:\n\n{e}")
        sys.exit(1)

    logging.info("Translation process completed.")

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            # Entfernen von ```markdown und ``` nur am Anfang und Ende des übersetzten Textes
            translated_markdown = remove_markdown_code_blocks(translated_markdown)  
            f.write(translated_markdown)
        logging.info(f"Translated markdown saved to {args.output_file}")
    else:
        print(translated_markdown)

    # Print total tokens used and estimated cost
    global total_tokens_used
    logging.info(f"Total tokens used: {total_tokens_used}")

    # Estimate cost
    # Define pricing per 1000 tokens for different models (in USD)
    pricing = {
        'gpt-4o-mini-2024-07-18': 0.00015,      # $0.00015 per 1K tokens (input)
        'gpt-4o-mini': 0.00015,
        'gpt-4o': 0.005,                        # $0.005 per 1K tokens (input)
        'gpt-4o-2024-08-06': 0.005,
        'gpt-4o-2024-05-13': 0.005,
        'gpt-4-turbo': 0.01,
        'gpt-3.5-turbo': 0.0015,
        'gpt-3.5-turbo-16k': 0.003,
        'gpt-4': 0.03,
        'gpt-4-32k': 0.06,
    }

    # Determine price per 1K tokens
    model_price_per_1k = pricing.get(selected_model, 0.005)

    # Calculate cost in USD
    cost_usd = (total_tokens_used / 1000) * model_price_per_1k

    # Convert USD to Euro (assuming 1 USD = 0.85 Euro, adjust as needed)
    usd_to_eur = 0.85
    cost_eur = cost_usd * usd_to_eur

    logging.info(f"Estimated cost: ${cost_usd:.4f} USD ({cost_eur:.4f} EUR)")
        

if __name__ == '__main__':
    main()
