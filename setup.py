from setuptools import setup, find_packages

extra_deps = dict()
extra_deps["all"] = sorted(set(sum(extra_deps.values(), [])))


setup(
    name='biblos',
    version='0.0.1',
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=[
        "toolz ~= 0.9",
        "click ~= 7.0",
        "xmltodict ~= 0.11.0"
    ],
    extras_require=extra_deps,
    entry_points={
        "console_scripts": [
            "fb2json=preproc.fb2json:main",
        ],
    }
)
