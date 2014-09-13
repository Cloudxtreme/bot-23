# -*- coding: utf-8 -*-
"Module to get OpenShift Environment settings"

import os

from sqlalchemy import (
    create_engine,
    engine_from_config,
    )

def get_engine(settings):
    "Function to create a valid engine for OpenShift Deployment"
    if settings['sqlalchemy.url'] == 'pg-openshift-environment':
        return create_engine(os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL', \
                                            'Not Set'))
    elif settings['sqlalchemy.url'] == 'my-openshift-environment':
        return create_engine(os.environ.get('OPENSHIFT_MYSQL_DB_URL', \
                                            'Not Set'))
    else:
        return engine_from_config(settings, 'sqlalchemy.')
