#!/bin/bash

cp temp-monitor.service /etc/systemd/system/temp-monitor.service

systemctl daemon-reexec
systemctl enable temp-monitor
systemctl start temp-monitor

