from .block import VSABlock
from .errors import VSASyntaxError


START_MARKER = "::: vsa-notatie"
END_MARKER = ":::"


def parse_markdown_blocks(markdown: str) -> list[VSABlock]:
    lines = markdown.splitlines()
    blocks = []

    index = 0

    while index < len(lines):
        line = lines[index].strip()

        if line != START_MARKER:
            index += 1
            continue

        start_line = index + 1
        index += 1

        metadata = {}
        body_lines = []
        in_body = False

        while index < len(lines):
            current = lines[index]

            if current.strip() == END_MARKER:
                end_line = index + 1
                blocks.append(
                    VSABlock(
                        metadata=metadata,
                        body="\n".join(body_lines).strip(),
                        start_line=start_line,
                        end_line=end_line,
                    )
                )
                break

            if not in_body:
                stripped = current.strip()

                if stripped == "":
                    in_body = True
                    index += 1
                    continue

                if _looks_like_parameter(stripped):
                    key, value = _parse_parameter(stripped, index + 1)
                    metadata[key] = value
                    index += 1
                    continue

                in_body = True

            body_lines.append(current)
            index += 1

        else:
            raise VSASyntaxError("VSA-blok zonder afsluitende :::", start_line)

        index += 1

    return blocks


def _looks_like_parameter(line: str) -> bool:
    return "=" in line and line.endswith('"')


def _parse_parameter(line: str, line_number: int):
    if '="' not in line or not line.endswith('"'):
        raise VSASyntaxError("Ongeldige blokparameter", line_number)

    key, raw_value = line.split('="', 1)
    value = raw_value[:-1]

    if key == "":
        raise VSASyntaxError("Blokparameter zonder naam", line_number)

    return key, value
