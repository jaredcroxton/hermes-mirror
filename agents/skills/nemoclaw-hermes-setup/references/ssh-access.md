# Enabling SSH Password Access on Brev/Cloud Instances

Brev cloud instances default to SSH key-only authentication. To enable password-based SSH:

## From Jupyter terminal (or any shell on the instance)

```bash
# Enable password authentication
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Set a password for the current user
echo -e 'yourpassword\nyourpassword' | sudo passwd $USER

# Restart SSH
sudo systemctl restart sshd
```

## From local Mac

```bash
ssh -o StrictHostKeyChecking=no -L 8642:127.0.0.1:8642 -L 18789:127.0.0.1:18789 user@<INSTANCE_IP>
```

Enter the password set above.

## Multiple port forwards

Chain multiple `-L` flags for each port you need:
```bash
ssh -L 8642:127.0.0.1:8642 -L 18789:127.0.0.1:18789 -L 8888:127.0.0.1:8888 user@<IP>
```

## Troubleshooting

- **"Permission denied (publickey)"**: Password auth not enabled. Run the sed commands above.
- **"Connection refused"**: SSH not running or wrong IP. Verify the instance is active.
- **"Connection timed out"**: Instance may be stopped or IP changed.
