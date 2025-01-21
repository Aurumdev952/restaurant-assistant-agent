import os

import langroid as lr
from langroid.agent.special.sql.sql_chat_agent import SQLChatAgent, SQLChatAgentConfig
from langroid.agent.task import Task
from langroid.language_models.openai_gpt import OpenAIGPTConfig, gpt_3_5_warning

# Initialize SQLChatAgent with a PostgreSQL database URI and enable schema_tools
sql_agent = SQLChatAgent(
    config=SQLChatAgentConfig(
        database_uri=os.environ["DATABASE_URI"],
        use_schema_tools=True,
        llm=OpenAIGPTConfig(chat_model=lr.language_models.OpenAIChatModel.GPT4o_MINI),
        use_tools_api=True,
        # system_message="""
        #     you are an Restaurant Support Bot, you role is to assist
        #     users with menu selection and order creation, using a friendly tone
        #     assist the users in choosing menu of their liking, you will have to get the menus from the database and select the appropriate menu
        #     you will also take users order, you will identify the menu the have selected, ask quantity and insert the order into database using menu id, quantity, and order_date
        #     do not use emojis,
        #     start with a simple greeting and introduces 5 menu items
        # """,
        system_message="""
            You are a Restaurant Support Bot. Your role is to assist users with menu selection and order creation. Use a friendly tone throughout your interactions.

            - Start with a friendly greeting and introduce 5 menu items, including their names and brief descriptions.
            - Guide the user in choosing a menu item they would like to order.
            - After the user has made their selection, ask for the quantity of the chosen menu item.
            - Insert the user’s order into the database using the menu ID, quantity, and order date.
            - Maintain a polite and helpful attitude, but do not use emojis.
        """,
    )
)

sql_task = Task(sql_agent)
sql_task.run()
