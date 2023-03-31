import openai
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_prompt_completion_dataset(output, gpt3_api_key, model, max_tokens, temperature, dataset_dir):
    # Load API key and model
    openai.api_key = gpt3_api_key

    # Load the Markdown files from the output directory and its subdirectories
    files = []
    for root, _, filenames in os.walk(output):
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(os.path.join(root, filename))

    # Create the dataset directory if it doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    # Write the prompt-completion pairs to a file in JSONL format
    dataset_file = os.path.join(dataset_dir, 'prompt_completion_dataset.jsonl')
    with open(dataset_file, 'w', encoding='utf-8') as f:
        # Send each Markdown file to OpenAI's API to generate prompt completions
        for i, file in enumerate(files):
            with open(file, 'r', encoding='utf-8') as md_file:
                # Read the contents of the Markdown file
                text = md_file.read()

                # Generate the prompt from the contents of the Markdown file
                prompt = "Transform the following content to prompt-completion so that we can fine-tune GPT-3 with it. "

                # Send the prompt to OpenAI's API to generate a completion
                try:
                    response = openai.Completion.create(
                        engine=model,
                        prompt=prompt + text[:2000],  # Limit prompt length to 1500 tokens
                        max_tokens=max_tokens,
                        n=1,
                        temperature=temperature,
                        stop=None,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

                    # Extract the completion text from the response
                    if len(response.choices) > 0:
                        completion = response.choices[0].text.strip()
                    else:
                        completion = ""

                    # Write the prompt-completion pair to the output file
                    f.write(f'{{"prompt": "{text.strip()}", "completion": "{completion}"}}\n')

                    # Log progress
                    logging.info(f'Processed file {i+1}/{len(files)}: {file}')

                except openai.error.InvalidRequestError as e:
                    # Log error
                    logging.warning(f'Skipping {file}: {str(e)}')

    # Log completion message
    logging.info(f'Finished processing {len(files)} files. Dataset file saved to {dataset_file}')

    # Return the path to the generated prompt-completion dataset file
    return dataset_file



# test example
output = '../../output'
gpt3_api_key = 'YOUR_API_KEY'
model = 'text-davinci-003'
max_tokens = 2000
temperature = 0.7
dataset_dir = '../../dataset'

# Generate the prompt-completion dataset
prompt_completion_dataset = generate_prompt_completion_dataset(output, gpt3_api_key, model, max_tokens, temperature, dataset_dir)
