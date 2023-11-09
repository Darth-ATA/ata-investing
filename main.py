import typer
import subprocess

PROJECT_NAME = "ata-investing"

app = typer.Typer(no_args_is_help=True)

@app.command(short_help="Setup local environment installing both develop and default packages exactly as specified in `pdm.lock`.")
def setup():
    subprocess.run(["pdm", "install"])
    subprocess.run(["pre-commit", "install"])
    subprocess.run(["pre-commit", "install", "--hook-type", "commit-msg"])

@app.command(short_help="Setup local environment installing both develop and default packages with pdm.")
def init():
    subprocess.run(["git", "init"])
    setup()

@app.command(short_help="Locally run tests.")
def test():
    subprocess.run(["pytest", f"--cov={PROJECT_NAME}", "-v", "tests/"])
    subprocess.run(["coverage", "html"])

@app.command(short_help="Build documentation.")
def build_docs():
    subprocess.run(["mkdocs", "build", "--verbose", "--site-dir", "public"])

@app.command(short_help="Serve documentation in local server http://127.0.0.1:8000/.")
def serve_docs():
    subprocess.run(["mkdocs", "serve"])

@app.command(short_help="Execute the precomit hooks.")
def pre_commit():
    subprocess.run(["pre-commit", "run", "--all-files"])

if __name__ == "__main__":
    app()
