#!/usr/bin/env python
from migrate.versioning.shell import main
from self_quant.config import SQLALCHEMY_DATABASE_URI as URL
from self_quant.config import  MIGRATE_REPO, DEBUG

if __name__ == '__main__':
    main(url=URL, debug=str(DEBUG), repository=MIGRATE_REPO)
