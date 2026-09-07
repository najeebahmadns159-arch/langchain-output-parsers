# LangChain Output Parsers

Small scripts I wrote while learning how LangChain output parsers work — turning raw, unstructured LLM text into structured, usable data (JSON, Pydantic models, etc).

## What's in here

| File | What it does |
|---|---|
| p_prsr.py | Uses PydanticOutputParser to force the model to return a `person` object (name, age, city) with type + validation rules enforced via Pydantic Field. |
| 8_Json_output_parser.py | Uses JsonOutputParser inside a chain (prompt | model | parser) to get a clean JSON dict back directly, no manual .parse() step needed. |
| 7_Langchain_output_parser.py | Chains two prompts (report generation -> summary) to explore sequential prompting before wiring in a proper parser. |
| p.prsr.py | Work-in-progress example using StructuredOutputParser with ResponseSchema — set up but not finished, kept as a note-to-self. |

## What I learned

- Why raw LLM output (plain text) is unreliable for downstream code, and how parsers fix that.
- PydanticOutputParser — define a schema with Pydantic, get format instructions for the prompt, and parse + validate the model's response into a real Python object.
- JsonOutputParser — simpler option when you just need a JSON dict back, no custom class required.
- StructuredOutputParser + ResponseSchema — a lighter-weight alternative to Pydantic for defining expected output fields.
- Using partial_variables in a PromptTemplate to inject format_instructions automatically.
- Building a simple chain with the | operator (prompt | model | parser) instead of calling .invoke() on each piece manually.

## Setup

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

Create a .env file in the root with your HuggingFace token:

HUGGINGFACEHUB_API_TOKEN=your_token_here

## Usage

python p_prsr.py
python 8_Json_output_parser.py

## Next steps

- Finish the StructuredOutputParser example.
- Add error handling for parser failures (OutputParserException) with RetryOutputParser / OutputFixingParser.
