import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/competitive-intelligence-solutions-llc-competitive-intelligence-solutions-llc-default/api/cis-vin-decoder'

mcp = FastMCP('cis-vin-decoder')

@mcp.tool()
def vin_decode(vin: Annotated[str, Field(description='')],
               passEmpty: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''Decodes the provided North American vin and provides recall information if available. We require at least the first 12 out of 17 characters in the vin to attempt a decode. The vin is not case sensitive. If passEmpty (default False) is True we will also include the empty fields in the response json.'''
    url = 'https://cis-vin-decoder.p.rapidapi.com/vinDecode'
    headers = {'x-rapidapi-host': 'cis-vin-decoder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
        'passEmpty': passEmpty,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
