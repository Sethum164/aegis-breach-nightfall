#!/bin/bash
cd ~/aegis-breach/stage3
docker compose down -v
docker compose up -d --build
echo "Stage 3 reset complete."
