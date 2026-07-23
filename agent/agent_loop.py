import os
import json
from dotenv import load_dotenv
from groq import Groq
from tools.calculator import calculate

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluates a basic math expression, e.g. '25 * 4'",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

available_tools = {
    "calculate": calculate
}


def run_agent(user_message):
    messages = [
        {
            "role": "system",
            "content": "You only have access to the tools explicitly provided to you in this request. Do not attempt to call any tool that isn't listed. If a question doesn't require a tool, answer directly."
        },
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools_schema,
        tool_choice="auto"
    )

    reply = response.choices[0].message

    if reply.tool_calls:
        tool_call = reply.tool_calls[0]
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)

        print(f"[Agent decided to use tool: {tool_name} with args {tool_args}]")

        tool_function = available_tools[tool_name]
        tool_result = tool_function(**tool_args)

        return f"Tool result: {tool_result}"
    else:
        return reply.content