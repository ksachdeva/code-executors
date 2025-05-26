from dataclasses import dataclass
from typing import List, Optional, Tuple, Union


@dataclass
class CodeBlock:
    """A code block extracted fromm an agent message."""

    code: str
    language: str


@dataclass
class CodeResult:
    """Result of a code execution."""

    exit_code: int
    output: str


@dataclass
class CommandLineCodeResult(CodeResult):
    """A code result class for command line code executor."""

    code_file: Optional[str]


@dataclass(frozen=True)
class Alias:
    name: str
    alias: str


@dataclass(frozen=True)
class ImportFromModule:
    module: str
    imports: Tuple[Union[str, Alias], ...]

    # backward compatibility
    def __init__(
        self,
        module: str,
        imports: Union[Tuple[Union[str, Alias], ...], List[Union[str, Alias]]],
    ):
        object.__setattr__(self, "module", module)
        if isinstance(imports, list):
            object.__setattr__(self, "imports", tuple(imports))
        else:
            object.__setattr__(self, "imports", imports)


Import = Union[str, ImportFromModule, Alias]
