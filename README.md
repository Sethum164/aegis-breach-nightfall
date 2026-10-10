# Aegis Breach: Operation Nightfall — CTF Play Box

IE3132 Penetration Testing — Assignment 02 (Working Box Implementation)
SLIIT, BSc (Hons) in Information Technology, Year 3 Semester 1

Group: Perera K.S.S. (IT24103718) · Ambegoda L.D.S.P. (IT24103839) · Sewmina G.D.D. (IT24103936) · Hettiarachchi T.J. (IT24102509)

---

## 1. What this is

A 6-stage Capture The Flag box simulating a breach investigation at a fictional
fintech company, Aeon Financial Holdings. Stages cover OSINT, steganography,
web security (SQL injection), cryptography, digital forensics, and
networking/Linux privilege escalation. CTFd hosts the scoreboard and flag
validation; each stage runs as an isolated Docker service.

## 2. Prerequisites

- Ubuntu Server 24.04 or 26.04 LTS (tested on 26.04.1), 4 vCPU / 8 GB RAM / 60 GB disk minimum
- A non-root sudo user
- Internet access during setup (to pull Docker images / install packages)

## 3. Setup — from a clean VM to a running box

```bash
# 1. System packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl gnupg git ufw python3-pip \
    ruby ruby-dev exiftool e2fsprogs sleuthkit zip unzip

# 2. Docker Engine + Compose plugin
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# If your Ubuntu codename is very new and this repo 404s, substitute "noble" for the codename above.
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
# log out and back in (or `newgrp docker`) before continuing

# 3. Clone this repo
git clone <this-repo-url> ~/aegis-breach
cd ~/aegis-breach

# 4. Python tooling used by the build/solver scripts
pip3 install pillow fpdf2 pdfplumber --break-system-packages
sudo gem install zsteg

# 5. Docker networks (one bridge per stage — enforces no cross-stage routing)
docker network create --driver bridge aegis-stage1-net
docker network create --driver bridge aegis-stage3-net
docker network create --driver bridge aegis-stage6-net
docker network create --driver bridge aegis-ctfd-net

# 6. Bring up CTFd
cd ctfd && docker compose up -d && cd ..

# 7. Bring up each live stage
cd stage1 && docker compose up -d && cd ..
cd stage3 && docker compose up -d --build && cd ..
cd stage6 && docker compose up -d --build && cd ..

# 8. Firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 8000/tcp   # CTFd
sudo ufw allow 8081/tcp   # Stage 1 (public site + /old-staging-portal/ path)
sudo ufw allow 8083/tcp   # Stage 3
sudo ufw allow 2222/tcp   # Stage 6 SSH
sudo ufw enable
```

Complete CTFd's first-run setup wizard at `http://<host>:8000`, then re-create
the 6 challenges (names, flags, hints, file uploads, Stage 5→6 Requirement
lock) following `docs/ctfd-challenge-config.md` in this repo, OR import the
database dump if one is included (`ctfd/.data` is git-ignored since it
contains the live DB — see note below).

## 4. Access points

| Stage | URL / connection |
|---|---|
| CTFd | `http://<host>:8000` |
| Stage 1 (public + staging) | `http://<host>:8081` — hidden path `/old-staging-portal/` found via `/robots.txt`; also reachable at hostname `staging.aeonfinancial.local` after a hosts-file entry |
| Stage 3 | `http://<host>:8083/login.php` |
| Stage 6 | `ssh ftpuser@<host> -p 2222` (password recovered from the Stage 6 PCAP) |

Stages 2, 4, 5 are file-based (downloaded through CTFd, or in Stage 2's case,
discoverable via a link inside Stage 1's PDF) — no separate port.

## 5. Reset / recovery

```bash
~/aegis-breach/scripts/reset_stage3.sh   # rebuilds the web app + reseeds the DB
~/aegis-breach/scripts/reset_stage6.sh   # rebuilds the SSH target container
~/aegis-breach/scripts/reset_all.sh      # resets every live stage
```

Stages 1, 2, 4, 5 are static files/images and do not need resetting between
players unless you choose to rotate flags (see `scripts/` for the
re-embedding commands used to regenerate Stage 2's PNG, Stage 4's cipher
blob, and Stage 5's disk image).

## 6. Design changes from the Assignment 01 proposal

- **Stage 1 architecture**: consolidated from two separate nginx containers
  on two ports (8081 public / 8082 staging) into a single nginx container on
  one port, with the staging content served via an nginx `location` block at
  `/old-staging-portal/`. This was changed because the original two-port
  split did not actually match the `robots.txt`-based OSINT clue described in
  the design (a disallowed *path*, not a separate port) — the single-port,
  path-routed version is both more realistic and consistent with the written
  clue.
- **Stage 5 forensic recovery method**: the design assumed standard
  "deleted file" / inode-based recovery (e.g. Autopsy's Deleted Files view).
  During build/testing we found EXT4 clears inode block pointers on
  deletion, so inode-based undelete finds nothing. The intended recovery
  method was corrected to raw/string carving of the unallocated image
  (`grep -a -b` / Autopsy's Keyword Search), which is a standard and
  realistic real-world forensic technique; the challenge hint text was
  updated accordingly.
- **CTFd file uploads**: required adding `UPLOAD_FOLDER=/var/uploads` to
  CTFd's environment, since the app code directory is mounted read-only and
  CTFd's default upload path lives inside it.

## 7. Credentials used in the box (sandboxed accounts only)

| Account | Used for | Password |
|---|---|---|
| `ftpuser` (Stage 6 container) | SSH target | recovered from the Stage 6 PCAP |
| `ftpuser2` (build VM, FTP traffic source) | generating the PCAP's plaintext credentials | same password as above |

All credentials exist only inside isolated containers / the build VM and are
intentionally weak/exposed as the point of the challenge.

## 8. Acknowledgements / tools used

CTFd, Docker & Docker Compose, nginx, PHP/MySQL, MariaDB, Redis, zsteg,
exiftool, Pillow, fpdf2, Sleuth Kit, Wireshark/tshark, vsftpd, GCC, OpenSSH.
See Assignment 01 References section for links.
