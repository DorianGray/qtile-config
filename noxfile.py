import os
import nox

PYTHONS = [
    'pypy3',
    '3.7',
]

PYTHON = 'pypy3'

HOME = os.getenv('HOME', None)
CWD = os.getcwd()

nox.options.sessions = ['lint']


def setup(session):
    session.install('-e', '../xcffib')  # must be installed before cairocffi


@nox.session(python=PYTHONS)
def test(session):
    setup(session)
    session.install('-r', 'requirements/test')
    session.run('pytest', 'test/')


@nox.session(python=PYTHON)
def lint(session):
    setup(session)
    session.install('-r', 'requirements/lint')
    session.run(
        'flake8',
        'qtile_config',
        'noxfile.py',
        'conf',
        'test',
        'setup.py',
    )


@nox.session(python=PYTHONS)
def qtile(session):
    setup(session)
    session.install(
        '-r', 'requirements/base',
        '-r', 'requirements/optional',
        '-e', '.',
    )


@nox.session(python=False)
def hooks(session):
    session.run(
        'ln',
        '-sf',
        f'{CWD}/git/hooks/pre-commit',
        f'{CWD}/.git/hooks/pre-commit',
        external=True,
    )


@nox.session(python=False)
def install(session):
    session.run(
        'ln',
        '-s',
        f'{CWD}/conf/config.py',
        f'{HOME}/.config/qtile/config.py',
        external=True
    )
