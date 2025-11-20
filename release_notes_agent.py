import json
from pathlib import Path
from datetime import datetime


# ------------------------------
# 1. Load JSON
# ------------------------------

def load_json(path: Path) -> dict:
    """Load the JSON source of truth file (updates.json)."""
    if not path.exists():
        raise FileNotFoundError(f"❌ JSON file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


# ------------------------------
# 2. Section formatting
# ------------------------------

def format_list(title: str, items: list) -> str:
    """
    Convert a list of items into a Markdown section.
    Supports:
    - pure strings
    - objects with {title: "", description: ""}
    """
    if not items:
        return ""

    lines = [f"## {title}", ""]

    for item in items:
        if isinstance(item, str):
            lines.append(f"- {item}")

        elif isinstance(item, dict):
            t = item.get("title", "")
            d = item.get("description", "")
            if t and d:
                lines.append(f"- **{t}** — {d}")
            elif t:
                lines.append(f"- **{t}**")
            elif d:
                lines.append(f"- {d}")

        else:
            lines.append(f"- {str(item)}")

    lines.append("")  # blank line at end
    return "\n".join(lines)


# ------------------------------
# 3. Build Markdown release notes
# ------------------------------

def build_markdown(data: dict) -> str:
    """
    Build final release notes according to your README structure.
    """
    version = data.get("release_version", "Unversioned")
    date = data.get("release_date", datetime.utcnow().strftime("%Y-%m-%d"))

    md = []

    md.append(f"# Release Notes — v{version}")
    md.append(f"_Date: {date}_")
    md.append("")

    # Mapping as defined in README
    md.append(format_list("New Features", data.get("new_features", [])))
    md.append(format_list("Fixed Issues", data.get("fixed_issues", [])))
    md.append(format_list("Known Issues", data.get("known_issues", [])))

    return "\n".join(line for line in md if line).strip() + "\n"


# ------------------------------
# 4. Save to review folder
# ------------------------------

def save_markdown(content: str, version: str):
    review_folder = Path("review_folder")
    review_folder.mkdir(exist_ok=True)

    filename = f"release_notes_v{version}.md"
    path = review_folder / filename

    path.write_text(content, encoding="utf-8")
    print(f"✅ Release notes saved: {path}")
    return path


# ------------------------------
# 5. Placeholder for Pull Request logic
# ------------------------------

def create_pull_request(path: Path):
    """
    Placeholder:
    You would integrate with GitHub API (PyGithub) or GitLab API here.
    """
    print(f"🔧 (Simulated) PR created for: {path}")
    print("👉 In real implementation: push to branch, open PR automatically.\n")


# ------------------------------
# 6. Main Agent Workflow
# ------------------------------

def run_agent():
    print("🤖 Running Release Notes Agent...")

    json_path = Path("updates.json")
    data = load_json(json_path)

    version = data.get("release_version", "0.0.0")

    markdown = build_markdown(data)
    output_path = save_markdown(markdown, version)

    create_pull_request(output_path)

    print("🎉 Agent task completed.")


if __name__ == "__main__":
    run_agent()
