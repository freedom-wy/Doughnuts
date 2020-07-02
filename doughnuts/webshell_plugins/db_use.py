from libs.config import alias, color, gget, gset
from libs.myapp import send
from webshell_plugins.db_init import get_connect_code


def get_php(database):
    return """%s
if (!$con){die("Connect error: ".mysqli_connect_error());}
""" % get_connect_code(gget("db_host", "webshell"), gget("db_user", "webshell"), gget("db_password", "webshell"), database, gget("db_port", "webshell"))


@alias(True, db="database")
def run(database: str):
    """
    db_use

    Change current database.
    
    eg: db_use {database}
    """
    if (not gget("db_connected", "webshell")):
        print(color.red("Please run db_init command first"))
        return
    res = send(get_php(database))
    if ("Connect error" in res.r_text):
        print("\n" + color.red(res.r_text.strip()) + "\n")
    else:
        print("\n" + color.green(f"Change current database: {database}") + "\n")
        gset("db_dbname", database, True, "webshell")
