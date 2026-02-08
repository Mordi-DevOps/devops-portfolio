#!/bin/bash
# Service Management Utility

echo "Enter service name: "
read service

# Check status
status=$(systemctl is-active "$service")
echo "Service '$service' status: $status"

echo "Select action:"
echo "1) Start/Restart"
echo "2) Stop"
echo "3) Exit"
read choice

case $choice in
  1)
    if [ "$status" = "active" ]; then
        echo "Restarting $service..."
        sudo systemctl restart "$service"
    else
        echo "Starting $service..."
        sudo systemctl start "$service"
    fi
    ;;
  2)
    echo "Stopping $service..."
    sudo systemctl stop "$service"
    ;;
  3)
    echo "Exiting..."
    ;;
esac
