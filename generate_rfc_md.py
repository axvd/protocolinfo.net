import os
import re

RFC_DIR = "static/rfc"
OUTPUT_DIR = "content/rfc"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in sorted(os.listdir(RFC_DIR)):

    if not filename.lower().endswith(".txt"):
        continue

    match = re.match(r"rfc(\d+)\.txt", filename.lower())

    if not match:
        continue

    rfc_num = match.group(1)

    filepath = os.path.join(RFC_DIR, filename)

    title = f"RFC {rfc_num}"

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        # RFC 첫 부분에서 제목 추출
        for line in lines[:100]:

            line = line.strip()

            if len(line) < 5:
                continue

            if line.startswith("RFC"):
                continue

            if "Request for Comments" in line:
                continue

            title = line
            break

    except Exception:
        pass

    md = f"""---
title: "RFC {rfc_num}"
rfc: "RFC{rfc_num}"
draft: false
tags:
  - RFC
---

# RFC {rfc_num}

## Title

{title}

## Summary

> Summary 작성 예정

## Original RFC

[View TXT](/rfc/rfc{rfc_num}.txt)

## Related Protocols

- TBD

"""

    output_file = os.path.join(
        OUTPUT_DIR,
        f"rfc{rfc_num}.md"
    )

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(md)

    print(f"Generated: {output_file}")
