# Data preprocessing

📂 Project Structure

project/
├── sources/
│   └── atis.json              # Original ATIS dataset
├── templates.json             # SQL template mapping
├── default_values.json        # Default variable values
├── tags_vocab.json            # Tag vocabulary for sequence labeling
├── template_sql_to_id.json    # Reverse template mapping (SQL to template ID)
├── classification_train.jsonl # Classification task data (train)
├── classification_dev.jsonl   # Classification task data (dev)
├── classification_test.jsonl  # Classification task data (test)
├── generation_train.jsonl     # Generation task data (train)
├── generation_dev.jsonl       # Generation task data (dev)
├── generation_test.jsonl      # Generation task data (test)
└── modules/
    ├── 1_template_builder.py
    ├── 2_tag_vocab_builder.py
    ├── 3_sentence_processor.py
    ├── 4_dataset_builder.py
    └── 5_data_saver.py

## 🧩 Modules Description

### 1. Template Builder (`1_template_builder.py`)

- **Function**: Loads the raw ATIS JSON data, selects the shortest SQL queries as templates, assigns unique template IDs, and extracts default variable values.
- **Outputs**:
  - `templates.json`
  - `default_values.json`
  - `template_sql_to_id.json`

------

### 2. Tag Vocabulary Builder (`2_tag_vocab_builder.py`)

- **Function**: Generates a sorted set of unique variable tags (including the special 'O' tag) from the training sentences in the dataset.
- **Outputs**:
  - `tags_vocab.json`

------

### 3. Sentence Processor (`3_sentence_processor.py`)

- **Function**: Processes individual sentences by replacing placeholders with actual values, tokenizing texts (spaCy), labeling tokens with variable tags accurately, encoding the sentence for Transformer models (BERT tokenizer), and generating the complete SQL queries.
- **Output**: Structured samples containing text, tokens, tags, template IDs, input IDs, attention masks, and complete SQL queries.

------

### 4. Dataset Builder (`4_dataset_builder.py`)

- **Function**: Separates data into classification and generation datasets, handling splits into training, development, and test sets. Classification datasets use only templates observed in training, while generation datasets include all examples.
- **Outputs**:
  - Classification: `classification_train.jsonl`, `classification_dev.jsonl`, `classification_test.jsonl`
  - Generation: `generation_train.jsonl`, `generation_dev.jsonl`, `generation_test.jsonl`

------

### 5. Data Saver (`5_data_saver.py`)

- **Function**: Provides utility functions to save processed data (classification and generation datasets) and auxiliary data (templates, default values, and tags vocabulary) to files in JSON and JSONL formats.
- **Ensures** data integrity by including careful checks before saving.





