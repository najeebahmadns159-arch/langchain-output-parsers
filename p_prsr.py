from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731',
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
class person(BaseModel):
    name : str =Field(description="name of the person ")
    age :int =Field(gt=18,description="age of the person")
    city : str=Field(description="name of the city the person belong to ")

parser=PydanticOutputParser(pydantic_object=person)
template=PromptTemplate(
    template="give the name, age and city of a fictionl {place} /n {format_instruction} ",
    input_variables=["place"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt=template.invoke({'place':'indian'})
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)