#!/bin/bash
for s in stage1 stage3 stage6; do
  (cd ~/aegis-breach/$s && docker compose down && docker compose up -d --build)
done
echo "All live stages reset."
