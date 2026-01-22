import asyncio
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession

MCP_URL = "http://127.0.0.1:8000/mcp"


async def main():
    print("CLIENT START")

    async with streamable_http_client(MCP_URL) as streams:
        read_stream = streams[0]
        write_stream = streams[1]

        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("INITIALIZED")

            # PDF → Markdown (WORKS)
            res = await session.call_tool(
                "pdf_to_markdown",
                {
                    "pdf_path": r"C:\Users\sowmy\Downloads\sample_resume\sample_resume.pdf"
                },
            )

            print("RESULT:", res)


if __name__ == "__main__":
    asyncio.run(main())
