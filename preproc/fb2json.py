import json

import click
import toolz as tz
import xmltodict


def parse_body(body, titles):
    if 'title' in body and 'section' in body:
        title = body['title']['p']
        secs = body['section']
        titles = titles + [title]
        if isinstance(secs, list):
            return tz.concat(map(lambda x: parse_body(x, titles), secs))
        else:
            return parse_body(secs, titles)

    elif 'title' in body and 'p' in body:
        title = body['title']['p']
        secs = body['p']
        titles = titles + [title]
        return tz.concat(map(lambda x: parse_body(x, titles), secs))

    elif 'emphasis' in body and '#text' in body:
        emph = body['emphasis']
        text = body['#text']
        return [{
            'titles': titles,
            'emph': emph,
            'text': text,
        }]
    else:
        if isinstance(body, dict):
            raise ValueError(f"Bad body, keys: {body.keys()}")
        else:
            raise ValueError(f"Bad body, value: {body}")


def parse(inp):
    doc = xmltodict.parse(inp)
    body = doc['FictionBook']['body']
    return parse_body(body, [])


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
    for l in parse(input.read()):
        output.write(json.dumps(l, ensure_ascii=False) + "\n")
