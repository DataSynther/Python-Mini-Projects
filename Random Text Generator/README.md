# Random Text Generation with GPT-2

This Python script demonstrates how to generate random text using a pre-trained GPT-2 model from Hugging Face's `transformers` library.

## Features

- Uses the GPT-2 language model for text generation.
- Automatically detects and uses GPU if available for faster inference.
- Generates multiple text sequences based on a given prompt.

## Requirements

- Python 3.x
- [transformers](https://pypi.org/project/transformers/)
- [torch](https://pypi.org/project/torch/)

Install dependencies with:
```
pip install transformers torch
```

## Usage

1. Ensure you have installed the required libraries.
2. Run the script:
    ```
    python text_generation.py
    ```
3. The script will generate and print two random text sequences starting with the prompt:
    ```
    Once upon a time in a land far, far away
    ```

## Example Output

```
Once upon a time in a land far, far away, the king ruled with kindness and wisdom...
Once upon a time in a land far, far away, there lived a dragon who loved to read books...
```

## Notes

- The script uses the default GPT-2 model. You can change the prompt or model as needed.
- If you do not have a GPU, the script will automatically use the CPU.
- For longer or more creative outputs, adjust the parameters such as `max_length`, `temperature`, or `top_k`.

---