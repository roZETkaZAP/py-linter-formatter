def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"], "source": "flake8"}

pass

def format_single_linter_file(file_path: str, errors: list) -> dict:

    #return {"errors": [{"line": error["line_number"], "column": error["column_number"],
    #              "message": error["text"], "name": error["code"], "source": "flake8"} for error in errors],
    #  "path": file_path, "status": "failed"}
    return {"errors": [] if not errors else [
        {"line": e["line_number"], "column": e["column_number"], "message": e["text"], "name": e["code"],
         "source": "flake8"} for e in errors], "path": file_path, "status": "passed" if not errors else "failed"}


pass


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [] if len(linter_report[part]) == 0 else [{"line": error["line_number"],
    "column": error["column_number"],
    "message": error["text"],
    "name": error["code"], "source": "flake8"} for error in
    linter_report[part]], "path": part,
    "status": "passed" if len(linter_report[part]) == 0 else "failed"} for part in linter_report]
    pass
