import click
from tqdm import tqdm
from mega import Mega
from mega.errors import RequestError

from .parser import Parser
from .user import User

mega = Mega()


@click.command()
@click.option(
    "--file",
    "-f",
    default="mega.txt",
    help="""
              Location of file which contains users and passwords of Mega. Default: mega.txt\n
              File should be formatted in form of [email][spaces/tabs][password].\n
              File may contain multiple accounts separated in ne line.\n
              Supports comment and empty lines (# or //).\n 
              i.e:\n
              bla@secure.com   mypassword\b\n
              mega@secure.com  securedpassword""",
)
@click.option(
    "--skip-fails",
    "-s",
    default=False,
    is_flag=True,
    type=bool,
    help="Don't exit upon failed accounts (wrong credentials, blocked user etc')",
)
def main(file: str, skip_fails: bool) -> None:
    try:
        users = Parser.parse_file(file)
    except Exception as e:
        print(str(e))
        raise click.Abort()

    users_progress_bar = tqdm(users)

    for user in users_progress_bar:
        try:
            users_progress_bar.set_description(f"Processing user {user.email}")
            login_user(user)
        except RuntimeError:
            if not skip_fails:
                raise click.Abort()
    print(f"Done!")


def login_user(user: User) -> None:
    try:
        logged_user = mega.login(user.email, user.password)
        logged_user.get_user()  # some action to do on the account without any side effects
    except RequestError as e:
        if e.code == -9:
            print(f"{user.email}: wrong email or password")
        elif e.code == -16:
            print(f"{user.email} is blocked")
        else:
            print(f"{user.email}: unknown exception in Mega.")
        raise RuntimeError(e)
