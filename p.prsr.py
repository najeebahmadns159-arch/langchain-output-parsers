from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731',
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)