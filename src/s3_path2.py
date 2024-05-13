import re
from urllib.parse import urlparse
from dataclasses import dataclass, field

s3_pattern: re.Pattern = re.compile(r"^s3://([^/]+)/(.+)$")


@dataclass(frozen=True)
class S3Path:
    s3_path: str
    bucket: str = field(init=False, hash=False, compare=False)
    key: str = field(init=False, hash=False, compare=False)

    def __post_init__(self):
        match: re.Match[str] | None = s3_pattern.match(self.s3_path)
        if match is None:
            raise ValueError(f"Invalid S3 path: {self.s3_path}")
        parsed_url = urlparse(self.s3_path)
        object.__setattr__(self, "bucket", parsed_url.netloc)
        object.__setattr__(self, "key", parsed_url.path.lstrip("/"))


def write_to_s3(content: str, s3_path: S3Path):
    pass
