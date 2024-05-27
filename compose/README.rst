=======
Compose
=======

Variants
========

Current compose configuration uses `merge <https://github.com/compose-spec/compose-spec/blob/master/13-merge.md#merge-and-override>`_ capability to provide pluggable functionality:

#. `compose.yaml` contains the core functionality: the *planetary-crs-registry* app, based on an in-memory SQLite database.
#. `postgres.yaml` is an overlay that replaces SQLite database with a PostgreSQL database.
#. `observability.yaml` add a *Grafana* based stack to collect and display telemetry.
