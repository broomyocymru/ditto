import click

from ditto.core import util


@click.group('env')
def cli():
    """env commands"""
    pass


@cli.command('team-setup')
@click.option('--jenkins/--no-jenkins', default=True)
@click.option('--git/--no-git', default=False)
@click.option('--elk/--no-elk', default=False)
@click.option('--sonarqube/--no-sonarqube', default=False)
def env_team_setup(jenkins, git, elk, sonarqube):
    if jenkins:
        util.makedir('/srv/jenkins')
        util.shell_run("docker run -p 8080:8080 -p 50000:50000 -v /srv/jenkins:/var/jenkins_home jenkins")

    if git:
        cmd = """
            docker run --detach \
            --hostname gitlab \
            --publish 443:443 --publish 80:80 --publish 22:22 \
            --name gitlab \
            --restart always \
            --volume /srv/gitlab/config:/etc/gitlab \
            --volume /srv/gitlab/logs:/var/log/gitlab \
            --volume /srv/gitlab/data:/var/opt/gitlab \
            gitlab/gitlab -ce:latest
        """
        util.shell_run(cmd)

    if elk:
        pass

    if sonarqube:
        "docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube"
