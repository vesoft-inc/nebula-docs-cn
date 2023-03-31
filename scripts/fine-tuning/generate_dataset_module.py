import openai
import os

def generate_prompt_completion_dataset(output, gpt3_api_key, model, max_tokens, temperature, dataset_dir):
    # Load API key and model
    openai.api_key = gpt3_api_key

# Load the split Markdown files from the output directory
    if not os.path.exists(output):
        raise ValueError(f"Output directory '{output}' does not exist.")
    files = []
    for root, _, filenames in os.walk(output):
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(os.path.join(root, filename))
    if len(files) == 0:
        raise ValueError(f"No Markdown files found in directory '{output}' or its subdirectories.")
    files = sorted(files)

    # Send each chunk of text to GPT-3.5 to generate prompt completions
    completions = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
        prompt = "Transform the following content to prompt-completion so that we can fine-tune GPT-3 with it. "
        response = openai.Completion.create(
            engine=model,
            prompt=prompt + text,
            max_tokens=max_tokens,
            n=1,
            temperature=temperature,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )
        if len(response.choices) > 0:
            completions.append((text.strip(), response.choices[0].text.strip()))
        else:
            completions.append((text.strip(), ""))

    # Create the dataset directory if it doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    
    # Write the prompt-completion pairs to a file in JSONL format
    dataset_file = os.path.join(dataset_dir, 'prompt_completion_dataset.jsonl')
    with open(dataset_file, 'w', encoding='utf-8') as f:
        for prompt, completion in completions:
            f.write(f'{{"prompt": "{prompt}", "completion": "{completion}"}}\n')
    
    # Return the path to the generated prompt-completion dataset file
    return dataset_file

# test example
output = '../../output'
gpt3_api_key = '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'
model = 'text-davinci-002'
max_tokens = 4096
temperature = 0.7
dataset_dir = '../../dataset'

# Generate the prompt-completion dataset
prompt_completion_dataset = generate_prompt_completion_dataset(output, gpt3_api_key, model, max_tokens, temperature, dataset_dir)
