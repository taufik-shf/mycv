import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    with open(ROOT / "cv.yaml") as f:
        data = yaml.safe_load(f)

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=False,
    )
    template = env.get_template("index.html")
    html = template.render(**data)

    with open(ROOT / "index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
