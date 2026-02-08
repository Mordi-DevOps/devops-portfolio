#!/bin/bash

# A simple system health logger
# Purpose: Check disk usage and log status to syslog

THRESHOLD=80
CURRENT_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//')

if [ "$CURRENT_USAGE" -gt "$THRESHOLD" ]; then
    logger -t "SYS_MONITOR" -p user.warn "CRITICAL: Disk usage is at ${CURRENT_USAGE}% on $(hostname)"
else
    logger -t "SYS_MONITOR" -p user.info "HEALTH_CHECK: Disk usage is normal (${CURRENT_USAGE}%)"
fi
