from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731',
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
#first prompt
template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']

)

#2nd prompt
template2=PromptTemplate(
    template="write a 5 line summarry on /n{text} ",
    input_variables=["text"]
)


prompt1=template1.invoke({'topic':'black hole'})
result1=model.invoke(prompt1)
prompt2=template2.invoke({'text':'result.content'})
result2=model.invoke(prompt2)

print(result1)
print(result2)