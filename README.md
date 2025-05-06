# ATIS Preprocessing Script

This script processes the [ATIS dataset](./sources/atis.json) into multiple formats suitable for training and evaluating various SQL generation models, including:

- **Classification models** (template prediction and tagging)
- **Sequence-to-sequence models** (e.g., LSTM, Transformer)
- **LLM prompting**

## 🔧 Functionality

The script performs the following:

1. **Loads the raw `atis.json` dataset**.
2. **Selects the shortest SQL template** for each group of questions.
3. **Replaces placeholders in natural language questions** with their actual values.
4. **Generates token-level tags** indicating variable spans (e.g., `airport_code0`, `O`).
5. **Fills SQL templates with actual values** to create gold-standard SQL queries.
6. **Builds tag vocabulary** across the dataset.
7. **Computes default variable values** per SQL template from the training split.
8. **Generates and saves multiple output files** for different task settings:
   - `question_{train,dev,test}.jsonl`: classification/tagging/generation inputs
   - `query_{train,dev,test}.jsonl`: for query-split evaluation
   - `generation_{train,dev,test}.jsonl`: input-output pairs for seq2seq and prompting
   - `templates.json`: mapping from template_id to SQL templates
   - `tags_vocab.json`: all tag types used
   - `default_values.json`: default values for each SQL template

## 📁 Output Directory Structure (`datasets/`)

## 📄 Dependencies

Only standard Python libraries are used:

- `json`
- `os`
- `re`
- `collections`

No external installation is required.