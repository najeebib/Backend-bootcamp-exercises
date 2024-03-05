import asyncio
import requests

async def get_data(url):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await  future
    
    return response.content


def count_genres(genres):
    genres_count = {}
    for genre in genres:
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
    return genres_count
