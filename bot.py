import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = AsyncWebClient(token=os.environ['SLACK_TOKEN'])

async def func():
    """ 
        This function uses the Slack API to send a message to a channel.
        It uses the `chat_postMessage` method of the `AsyncWebClient` object, which
        is a method provided by the `slack_sdk.web.async_client` module. This method
        sends a message to the channel named "gaurav".
    """
    try:
        response = await client.chat_postMessage(
                channel='#gaurav',
                text="Hello world!")
        return response
    except SlackApiError as e:
        print(e)

asyncio.run(func())