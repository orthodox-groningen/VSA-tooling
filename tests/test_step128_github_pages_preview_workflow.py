from pathlib import Path

import yaml


WORKFLOW = Path(".github/workflows/pages-preview.yml")
PRODUCTION_WORKFLOW = Path(".github/workflows/pages-demo.yml")
REUSABLE_WORKFLOW = Path(".github/workflows/pages-deploy-reusable.yml")


class GithubActionsLoader(yaml.SafeLoader):
    """Keep the literal `on` key instead of YAML 1.1 bool coercion."""


for first_letter, resolvers in list(GithubActionsLoader.yaml_implicit_resolvers.items()):
    GithubActionsLoader.yaml_implicit_resolvers[first_letter] = [
        (tag, regex)
        for tag, regex in resolvers
        if tag != "tag:yaml.org,2002:bool"
    ]


def load_workflow(path: Path) -> dict:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=GithubActionsLoader)


def run_commands(workflow: dict) -> list[str]:
    commands: list[str] = []
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "run" in step:
                commands.append(step["run"])
    return commands


def test_pages_preview_workflow_exists():
    assert WORKFLOW.exists()


def test_pages_preview_runs_on_every_push():
    workflow = load_workflow(WORKFLOW)

    assert workflow["on"] == {"push": None}


def test_pages_preview_builds_with_preview_baseurl():
    commands = "\n".join(run_commands(load_workflow(WORKFLOW)))

    assert "--baseURL" in commands
    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in commands


def test_pages_preview_deploys_preview_directory_to_gh_pages():
    workflow = load_workflow(WORKFLOW)
    reusable = load_workflow(REUSABLE_WORKFLOW)
    deploy_job = workflow["jobs"]["deploy"]
    gh_pages_steps = [
        step
        for step in reusable["jobs"]["deploy"]["steps"]
        if step.get("uses") == "peaceiris/actions-gh-pages@v3"
    ]

    assert deploy_job["uses"] == "./.github/workflows/pages-deploy-reusable.yml"
    assert deploy_job["with"]["destination_dir"] == "preview"
    assert gh_pages_steps
    assert all("keep_files" in step["with"] for step in gh_pages_steps)


def test_pages_preview_skips_redundant_pytest():
    commands = run_commands(load_workflow(WORKFLOW))

    assert all("pytest" not in command for command in commands)


def test_pages_preview_keeps_manual_production_workflow_separate():
    production = load_workflow(PRODUCTION_WORKFLOW)

    assert production["on"] == {"workflow_dispatch": None}
    assert "destination_dir" not in production["jobs"]["deploy"].get("with", {})
