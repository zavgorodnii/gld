from clldutils.path import Path
from clld.web.assets import environment

import gld


environment.append_path(
    Path(gld.__file__).parent.joinpath('static').as_posix(),
    url='/gld:static/')
environment.load_path = list(reversed(environment.load_path))
