import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError
from fastapi import FastAPI, Request, Response
from slack_sdk.signature import SignatureVerifier

# Created a new FastAPI app
app = FastAPI()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = AsyncWebClient(token=os.environ['SLACK_TOKEN'])
signature_verifier = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])


# @app.middleware("http")
# async def verify_signature(request: Request, call_next):
#     try:
#         await signature_verifier(request)
#         return await call_next(request)
#     except Exception as e:
#         print(e)
        # return Response(status=403)
    

@app.get("/slack_events")
def slack_init(request: Request, response: Response):
    try:
        if not signature_verifier.is_valid_request(request.body, request.headers):
            return {
                "response": "invalid request",
                "status_code": 403
            }
    except Exception as e:
        print("hi guarav")
        print(e)

# async def func():
#     """ 
#         This function uses the Slack API to send a message to a channel.
#         It uses the `chat_postMessage` method of the `AsyncWebClient` object, which
#         is a method provided by the `slack_sdk.web.async_client` module. This method
#         sends a message to the channel named "gaurav".
#     """
#     try:
#         response = await client.chat_postMessage(
#                 channel='#gaurav',
#                 text="Hello world!")
#         return response
#     except SlackApiError as e:
#         print(e)


if __name__ == "__main__":
    app.debug(True)
    # asyncio.run(func())