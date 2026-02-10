def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"], "source": "flake8"}

pass

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [] if not errors else [ format_linter_error(e) for e in errors],
        "path": file_path, "status": "passed" if not errors else "failed"}


pass


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(part, linter_report[part]) for part in linter_report]


    pass
