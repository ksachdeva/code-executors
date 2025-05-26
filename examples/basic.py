# ruff: noqa: T201

import asyncio

from docker_code_executor import CancellationToken, CodeBlock, CommandLineCodeResult, DockerCommandLineCodeExecutor


async def main() -> None:
    executor = DockerCommandLineCodeExecutor()
    await executor.start()

    code_blocks = [
        CodeBlock(
            code="""
import os
for k, v in os.environ.items():
    print(f"{k}={v}")
""",
            language="python",
        )
    ]

    cancel_token = CancellationToken()

    result: CommandLineCodeResult = await executor.execute_code_blocks(code_blocks, cancel_token)
    print(result.output)

    await executor.stop()


if __name__ == "__main__":
    asyncio.run(main())
