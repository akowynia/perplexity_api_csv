import requests
import json
import configparser
from config import read_config

# Configuration file name
config_file = "config.ini"

def get_perplexity(text, prompt):
    try:

        # Read the API key from the configuration file
        api_key = read_config(config_file)
        

        # URL for the Perplexity AI API endpoint
        url = "https://api.perplexity.ai/chat/completions"

        # Payload for the API request
        
        payload = {
            #model llama are deprecated and not available , please check the available models in the documentation on https://docs.perplexity.ai/guides/model-cards
            #"model": "llama-3.1-sonar-small-128k-chat",  # Model to use
            "model": "sonar",  # Model to use
            
            "messages": [
                {
                    "role": "system",
                    "content": prompt  # System prompt
                },
                {
                    "role": "user",
                    "content": text  # User input text
                }
            ],
            "max_tokens": "15500",  # Maximum number of tokens to generate
            "temperature": 0.2,  # Sampling temperature
            "top_p": 0.9,  # Nucleus sampling parameter
            "return_citations": True,  # Whether to return citations
            "search_domain_filter": ["perplexity.ai"],  # Domain filter for search
            "return_images": False,  # Whether to return images
            "return_related_questions": False,  # Whether to return related questions
            "search_recency_filter": "month",  # Recency filter for search
            "top_k": 0,  # Top-k sampling parameter
            "stream": False,  # Whether to stream the response
            "presence_penalty": 0,  # Presence penalty parameter
            "frequency_penalty": 1  # Frequency penalty parameter
        }

        # Headers for the API request
        headers = {
            "Authorization": "Bearer " + api_key,  # Bearer token for authorization
            "Content-Type": "application/json"  # Content type of the request
        }

        # Make the API request
        response = requests.request("POST", url, json=payload, headers=headers)

        # Print the raw response text
        print(response.text)

        # Parse the response JSON
        response_json = json.loads(response.text)

        # Extract the message content from the response
        message_content = response_json.get('choices', None)

        # Return the content of the first message
        return message_content[0]['message']['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None