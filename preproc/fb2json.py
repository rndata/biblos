import xmltodict
import json
import click


@click.command()
@click.option(
    "-i",
    "--input",
    type=click.File("rb"),
    default="-",
    show_default=True,
)
@click.option(
    "-o",
    "--output",
    type=click.File("w"),
    default="-",
    show_default=True,
)
def main(input, output):
    return json.dump(xmltodict.parse(input.read()), output)
