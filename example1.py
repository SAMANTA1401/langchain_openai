## Intregrate out code with opoenai api
import os
from constants import openai_key
# from langchain.llms import OpenAi
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key
#streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input('Enter your text here')


##Prompt Template / prompt engineering
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="tell me about {name}"
)

# Memory
person_memory = ConversationBufferMemory(memory_key="chat_history",input_key='name', return_messages=True)
dob_memory = ConversationBufferMemory(memory_key="chat_history", input_key='person' ,return_messages=True)
# descr_memory = ConversationBufferMemory(memory_key="description", input_key='dob', return_messages=True)

##openai llms
llm = ChatOpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person',memory=person_memory)

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="tell me about {person} born"
)

chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob',memory=dob_memory)

# parent_chain = SimpleSequentialChain(chains=[chain,chain2],verbose=True)
parent_chain = SequentialChain(chains=[chain,chain2],input_variables=['name'],output_variables=['person','dob'],verbose=True)




if input_text:
    # st.write(llm.invoke(input_text))
    # st.write(chain.run(input_text))
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer) 
    
    with st.expander('Person DOB'):
        st.info(dob_memory.buffer)   # 34:05
