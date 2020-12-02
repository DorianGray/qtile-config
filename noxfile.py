import os
import nox


nox.options.sessions = ['lint']
nox.options.stop_on_first_error = True
nox.options.reuse_existing_virtualenvs = True
nox.options.pythons = ['pypy3']


HOME = os.getenv('HOME', None)
CWD = os.getcwd()


def setup(session):
    session.install('xcffib')  # must be installed before cairocffi


@nox.session()
def test(session):
    setup(session)
    session.install('-r', 'pip/requirements-test.txt')
    session.run('pytest', 'test/')


@nox.session()
def lint(session):
    setup(session)
    session.install('-r', 'pip/requirements-lint.txt')
    session.run('flake8', 'qtile_config', 'noxfile.py', 'conf', 'test')


@nox.session()
def qtile(session):
    setup(session)
    session.install('-r', 'pip/requirements.txt', '-e', '.')


@nox.session()
def hooks(session):
    session.run(
        'ln',
        '-sf',
        f'{CWD}/git/hooks/pre-commit',
        f'{CWD}/.git/hooks/pre-commit',
        external=True,
    )


@nox.session()
def install(session):
    qtile(session)
    session.run(
        'ln',
        '-s',
        f'{CWD}/conf/config.py',
        f'{HOME}/.config/qtile/config.py',
        external=True
    )
