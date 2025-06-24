from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
@tool
def calculator(a:float,b:float) -> str:
    """use for performing addition of two numbers"""
    print("TOOL IS CALLED")
    return f"the sum of {a} and {b} is {a+b}"

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    model = ChatOpenAI(temperature=0, api_key=api_key)
    tools=[calculator]
    agent_executor = create_react_agent(model,tools)

    print("Welcome i am your Ai assitant . press Q to quit!")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou : ").strip()

        if user_input=="Q".lower():
            print("Bye lets meet again!!!")
            break

        print("\nAssistant : ",end="")
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
          if "agent" in chunk and "messages" in chunk["agent"]:
              for message in chunk["agent"]["messages"]:
                  print(message.content,end="")
        print()

if __name__=="__main__":
    main()
            

