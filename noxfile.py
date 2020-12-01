import nox


nox.options.sessions = ['lint']
nox.options.stop_on_first_error = True
nox.options.reuse_existing_virtualenvs = True
nox.options.pythons = ['pypy3']


def setup(session):
    session.install('xcffib')  # must be installed before cairocffi


@nox.session()
def test(session):
    setup(session)
    session.install('-r', 'pip/requirements-test.txt')
    session.run('pytest')

@nox.session()
def lint(session):
    setup(session)
    session.install('-r', 'pip/requirements-lint.txt')
    session.run('flake8', 'qtile_config')

@nox.session()
def qtile(session):
    setup(session)
    session.install('-r', 'pip/requirements.txt', '-e', '.')
