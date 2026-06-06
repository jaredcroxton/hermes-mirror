# AgentOS EC2 Client Deployment — Step-by-Step (June 2026)

## Instance Specs

- **Type:** g6.2xlarge (8 vCPU, 32 GB RAM)
- **GPU:** NVIDIA L4, 23 GB VRAM
- **AMI:** Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.11 (Ubuntu 24.04)
- **Region:** us-east-1 (N. Virginia)
- **Storage:** 30 GB root + 419 GB ephemeral NVMe
- **Security group:** SSH (My IP), port 8080 (My IP)
- **Cost:** ~$0.98 USD/hour on-demand

## Complete Deployment Commands

### 1. Mount ephemeral volume

```bash
sudo mkdir -p /data
sudo mount /dev/vg.01/lv_ephemeral /data
df -h /data  # should show ~412GB
```

### 2. Relocate Docker to ephemeral volume

```bash
sudo systemctl stop docker docker.socket containerd
sudo mkdir -p /data/docker /data/containerd
sudo rsync -aP /var/lib/docker/ /data/docker/
sudo rsync -aP /var/lib/containerd/ /data/containerd/
echo '{"data-root":"/data/docker"}' | sudo tee /etc/docker/daemon.json
sudo bash -c 'cat > /etc/containerd/config.toml << EOF
root = "/data/containerd"
EOF'
sudo systemctl start containerd docker
docker info | grep 'Docker Root Dir'  # should show /data/docker
```

### 3. Install Ollama and models

```bash
# Ollama already installed via user data script
ollama --version
ollama list

# Pull minimum viable agent models
ollama pull llama3.1:8b    # 4.9 GB — tool calling support
ollama pull llama3.2:3b    # 2.0 GB — chat only, no tools
```

### 4. Install Open WebUI

```bash
docker run -d --network host --name open-webui \
  -v /data/open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  ghcr.io/open-webui/open-webui:main
```

Verify: `curl -s -o /dev/null -w '%{http_code}' http://localhost:8080`
Health: `docker ps --filter name=open-webui --format '{{.Status}}'`

### 5. Install Hermes

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes --version
```

### 6. Configure Hermes for Ollama

```bash
cd ~/.hermes
cp config.yaml config.yaml.bak
python3 -c "
import yaml
with open('config.yaml') as f:
    c = yaml.safe_load(f)
c['model']['default'] = 'llama3.1:8b'
c['model']['provider'] = 'custom'
c['model']['base_url'] = 'http://localhost:11434/v1'
yaml.dump(c, open('config.yaml','w'), default_flow_style=False, sort_keys=False, width=120)
"
```

Verify: `hermes chat -q 'Reply exactly: AgentOS operational.' --quiet`

### 7. Open security group port

AWS Console → EC2 → Security Groups → launch-wizard-4 → Edit inbound rules → Add rule:
- Type: Custom TCP
- Port: 8080
- Source: My IP (for testing; later switch to client's IP or a known range)

### 8. Add Telegram bot (post-test)

```bash
echo 'TELEGRAM_BOT_TOKEN=<token>' >> ~/.hermes/.env
echo 'TELEGRAM_ALLOWED_USERS=<user_id>' >> ~/.hermes/.env
hermes gateway install
hermes gateway start
```

## Verification Checklist

- [ ] Ollama serving models on localhost:11434
- [ ] llama3.1:8b returns text (curl test)
- [ ] Hermes chat works with llama3.1:8b
- [ ] Open WebUI accessible at public IP:8080
- [ ] Docker root is on /data, not /
- [ ] Ephemeral volume mounted at /data
- [ ] Security group allows port 8080 from correct IP
- [ ] GPU visible: nvidia-smi shows L4 with 23GB
