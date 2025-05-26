# Code Executors

This monorepo contains various packages for code executors that can be leveraged by agentic applications.

## Docker Code Executor

Borrowed from microsoft/autogen repository and converted to a standalone package.

See the [docker-code-executor README](./packages/docker-code-executor/README.md) for detailed usage and setup instructions.

### Install

```bash
pip install docker-code-executor
```

### Usage

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