from setuptools import setup
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name="nb-serverproxy-refl1d",
    packages= ['nb_serverproxy_refl1d'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/innovationOUtside/nb_serverproxy_openrefine",
    author="Brian Maranville",
    description="Jupyter server proxy wrapper for Refl1D",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    entry_points={
        'jupyter_serverproxy_servers': [
            'refl1d = nb_serverproxy_refl1d:setup_refl1d',
        ]
    },
    package_data={
        'nb_serverproxy_refl1d': ['icons/*'],
    },
)
