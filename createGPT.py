import openai
import requests

# Set the API key and endpoint URL for the OpenAI API
openai.api_key = "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"
endpoint_url = "https://api.openai.com/v1/models/gpt3"

def on_launch(launch_request, session):
    """
    Called when the skill is launched without a specific intent.
    """
    # Set the prompt to the text received by the skill
    prompt = launch_request["inputTranscript"]

    # Set the model configuration and parameters
    model_config = {
        "engine": "gpt3",
        "model": "text-davinci-002",  # include as many models as possible
        "prompt": prompt,
        "temperature": 0.9,  # set the temperature to a high value
    }

    # Make the API call to create the model
    response = requests.post(endpoint_url, json=model_config, headers={"Authorization": f"Bearer {openai.api_key}"})

    # Check the response status code
    if response.status_code == 200:
        # The model was created successfully
        model_id = response.json()["id"]
        print(f"GPT-3 model created successfully with ID: {model_id}")
    else:
        # There was an error creating the model
        print("Error creating GPT-3 model:", response.text)
