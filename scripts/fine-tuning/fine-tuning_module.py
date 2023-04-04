import openai
import pandas as pd
from sklearn.model_selection import train_test_split
from openai.api_resources import FineTune, GPT3TrainingConfig

def fine_tune_gpt3_model(training_data_file, gpt3_api_key, model_name, output_dir):
    # Load API key and model
    openai.api_key = gpt3_api_key
    model = openai.Model.list()[model_name]

    # Load the prompt-completion dataset from the specified file
    dataset = pd.read_json(training_data_file, lines=True)

    # Split the dataset into training and validation sets
    train_data, val_data = train_test_split(dataset, test_size=0.2, random_state=42)

    # Fine-tune the GPT-3 model using the training set
    training_config = GPT3TrainingConfig(
        prompt_column="prompt",
        completion_column="completion",
        finetune_settings={
            "epochs": 1,
            "batch_size": 1,
            "learning_rate": 5e-5,
            "warmup_steps": 100,
            "max_steps": 10000,
            "gradient_accumulation_steps": 1,
            "model": model.id,
        },
        validation_settings={
            "test_size": 0.1,
            "shuffle": True,
            "random_state": 42,
        },
        output_settings={
            "save_every": 1000,
            "save_gdrive": False,
            "save_s3": False,
            "output_dir": output_dir,
        },
    )

    ft = FineTune.create(training_config=training_config, train_data=train_data, val_data=val_data)

    # Save the fine-tuned GPT-3 model to the specified output directory
    ft.model.save(output_dir)
