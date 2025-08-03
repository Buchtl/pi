#!/bin/bash
sudo systemctl stop temp-monitor.service
sudo systemctl disable temp-monitor.service
sudo systemctl daemon-reload
systemctl status temp-monitor.service

