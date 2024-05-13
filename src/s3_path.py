import re

s3_pattern: re.Pattern = re.compile(r"^s3://([^/]+)/(.+)$")


def write_to_s3(content: str, s3_path: str):
    match: re.Match[str] | None = s3_pattern.match(s3_path)
    if match is None:
        raise ValueError(f"Invalid S3 path: {s3_path}")
