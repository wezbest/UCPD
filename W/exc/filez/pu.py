# imports here
import aiohttp
import asyncio

# Define the asynchronous function to fetch and print content
# filez/pu.py

async def fetch_snips_pussy():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://snips.sh/f/CRm5avdsZP?r=1') as response:
            text = await response.text()
            print(text)

def run_fetch_snips_pussy():
    asyncio.run(fetch_snips_pussy())
