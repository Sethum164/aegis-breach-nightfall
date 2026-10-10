#!/bin/bash
cd ~/aegis-breach/stage6
docker compose down
docker compose up -d --build
echo "Stage 6 reset complete."
