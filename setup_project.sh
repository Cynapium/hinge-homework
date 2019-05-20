#!/bin/sh

requirements="flask_restful"

db_path="src/db"
db_file="${db_path}/hinge-homework-barbara.db"
db_schema="${db_path}/schema_database.json"
db_test_data="${db_path}/test_data.sql"
db_setup_script="${db_path}/setup_database.py"

# Install python modules
echo "====> INITIALIZING PYTHON DEPENDENCIES"
pip3 install ${requirements}

# Create database & populate with test data
echo
echo "====> INITIALIZING DATABASE"
if [ ! -f "${db_file}" ] ; then
    python3 ${db_setup_script} ${db_file} ${db_schema} ${db_test_data}
else
    echo "Database ${db_file} already exists"
fi

#
echo
echo "=============================="
echo "Project has been initialized"
echo "Run with:"
echo "  python3 src/app.py"
echo "=============================="
