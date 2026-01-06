# Summary
This is a Natural Language Processing assignment in which a natural language instruction is matched up to the appropriate SQL query. Classification.ipynb contains all the code for this part of the project, with the rest of the files being artifacts that are utilized in the second branch (which explores raw generation methods). Classification.ipynb contains four separate approaches; a Linear Model, a Feed Forward NN, an LSTM, and a Transformer.

# Results
Results were 12.75% accuracy for the Linear Model, 15.2% accuracy for the Feed Forward NN, 25.5% accuracy for the LSTM, and 44% for the Transformer.

## Ideal blocks and hyper params for the Transformer Model
We tested 3 values for each hyperparameter, small (2 heads and 1 block), medium (4 heads and 3 blocks), and large (8 heads and 6 blocks). We chose the large dimensions from the example given in the lecture. This gave us 9 separate transformer models, which we trained with a maximum epoch count of 20 and a stopping condition when the validation loss hasn’t improved for 3 epochs.
We plotted the results on a graph, where the y axis is accuracy, the x axis is head count, and each line corresponds to a block count. The results were rather surprising. We had expected to find that the accuracy gain of extra attention heads would decrease with increased encoder/decoder blocks. What we found was that the relationship was unclear. For 1 block, the impact of added attention heads was positive over our parameter-space. For 3 blocks, the relationship was instead negative. For 6 blocks, the relationship was unclear, having moderate lower accuracy on 4 heads than 2, but much higher on 8. This shows that the relationship between these two hyper-parameters is more complex than we thought, and may resemble a gradient space rather than a quadratic or linear space. The best performing transformer model was one with 3 encoder/decoder blocks and 2 attention heads.

We trained on an adam optimizer, as the gradient descent was far more stable compared to kmsprop. This allowed us to compare these models against each other more accurately. When we got the final configuration, we tested on rmsprop with the same stopping condition as above. The accuracy it returned was only 25%, though other configurations of kmsprop with set epochs performed much better in our testing, getting above our adam transformer while i was testing by hand. This could be a case of early stop due to the noisy loss, the different parameters we used there but did not test here (using 2 blocks as proof of concept), or it may be that these two optimizers truly do have different ideal parameters.

# Data preprocessing (second branch, artifact)

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





