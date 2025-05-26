# ruff: noqa: T201

import asyncio
import os
from pathlib import Path

import pandas
from docker_code_executor import CancellationToken, CodeBlock, DockerCommandLineCodeExecutor, with_requirements


@with_requirements(python_packages=["pandas"], global_imports=["pandas"])
def load_data() -> pandas.DataFrame:
    """Load some sample data.

    Returns:
        pandas.DataFrame: A DataFrame with sample data
    """
    data = {
        "name": ["John", "Anna", "Peter", "Linda"],
        "location": ["New York", "Paris", "Berlin", "London"],
        "age": [24, 13, 53, 33],
    }
    return pandas.DataFrame(data)


async def run_example() -> None:
    os.makedirs("./tmp", exist_ok=True)
    # The decorated function can be used in executed code
    executor = DockerCommandLineCodeExecutor(
        work_dir=Path("./tmp"),
        functions=[load_data],
        delete_tmp_files=False,
    )
    await executor.start()
    code = f"""
from {executor._functions_module} import load_data
# Use the imported function
data = load_data()
print(data['name'][0])
    """

    result = await executor.execute_code_blocks(
        code_blocks=[CodeBlock(language="python", code=code)],
        cancellation_token=CancellationToken(),
    )
    print(result.output)  # Output: John
    await executor.stop()


if __name__ == "__main__":
    # Run the async example
    asyncio.run(run_example())
