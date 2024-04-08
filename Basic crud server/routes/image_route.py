from fastapi import Request, Response, APIRouter, Depends
from starlette.responses import StreamingResponse
import base64
import asyncio
from modules.logger import Logger

router = APIRouter()
# this function will send the base64 encoded image to the client, on the client side we need to merge all the chunks and decode it to get the final image
# i got this idea from this https://stackoverflow.com/questions/33529685/using-sse-to-send-image-data
async def generate_encoded_image(request):
    with open("./images/students_stock_image.jpg", "rb") as f:
        image_data = f.read()
        # encode the image using base64 to send it using sse, sse can only send text
        encoded_image_data = base64.b64encode(image_data)
        chunk_size = 1024
        num_chunks = (len(encoded_image_data) + chunk_size - 1) // chunk_size
        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = min((i + 1) * chunk_size, len(encoded_image_data))
            chunk = encoded_image_data[start_index:end_index]
            # send the encoded image to trhe client
            yield f"data: {chunk}\n\n"
            await asyncio.sleep(1)  




@router.get("/image")
async def image(request: Request, response: Response, log = Depends(Logger.log_request)):
    response.headers["Content-Type"] = "text/event-stream"
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Connection"] = "keep-alive"
    return StreamingResponse(generate_encoded_image(request))


# this is example pseudocode of compining encoded chunks given by server and decoding the image then showing the decoded image
""" 
this code snippet i made with the help of this
https://code.tutsplus.com/base64-encoding-and-decoding-using-python--cms-25588t


image_path = "students_stock_image.jpg"
with open(image_path, "rb") as f:
    image_data = f.read()

# open the image using PIL
image = Image.open(io.BytesIO(image_data))

# here the we need to compine all the chunks we get from server into one variable that has all encoded image
encoded_image_data = get_all_chunks(chunks: list)

# once the encoded data chunks has been meged
# decode the base64 encoded image data
decoded_image_data = base64.b64decode(encoded_image_data)

# show decoded image
decoded_image = Image.open(io.BytesIO(decoded_image_data))
decoded_image.show()

"""