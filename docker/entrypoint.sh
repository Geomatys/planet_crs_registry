#!/usr/bin/env sh

COMMAND="planet_crs_registry --conf_file /conf/planet_crs_registry.conf"


if [ -z "$OTEL_EXPORTER_OTLP_ENDPOINT" ]; then
  echo 'Open telemetry deactivated. Reason: no OLTP endpoint defined (via environment variable $OTEL_EXPORTER_OTLP_ENDPOINT)'
elif [ -z $(which opentelemetry-instrument 2> /dev/null || echo "") ]; then
  echo 'Open telemetry deactivated. Reason: not installed'
else
  COMMAND="opentelemetry-instrument $COMMAND"
fi;

$COMMAND
