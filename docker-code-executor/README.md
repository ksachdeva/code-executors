# Docker Code Executor

This is borrowed from
https://github.com/microsoft/autogen/blob/main/python/packages/autogen-ext/src/autogen_ext/code_executors/docker/_docker_code_executor.py

and converted into an independent package with some minor modifications and adjustments.

## Install

```bash
pip install docker-code-executor
```

## Usage

```python
import asyncio

from docker_code_executor import CancellationToken, CodeBlock, CommandLineCodeResult, DockerCommandLineCodeExecutor

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
```